#!/usr/bin/env python

#
# LICENSE:
# This program is free software; you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License version 3 (AGPL) 
# as published by the Free Software Foundation.
#

import re
import time
import socket
import json
import getopt 
import sys
import re

"""
The Broker protocol is simple and its details have been in the public domain for years. The following connects to a remote VISTA and sends a series of RPCs
given in a 'dialog'

> ./runSessions.py OSEHRA sessions/unidentifiedGetAnyGlobalOrCode.json

TODO:
- simple constant application to params ... %(IPADDRESS)s etc
"""
def connectAndRun(host, port, dialog, terminalHighlight=True):

    def makeRequest(name, params, isCommand=False, constants={}):

        protocoltoken = "[XWB]" # "new" style broker

        if isCommand:   # Are we executing a command?
            protocoltoken += "1030"
            commandtoken = "4"
        else:
            protocoltoken += "1130"
            # ... chr for length is because XWBPRS uses $A(.) to get length and then parses that number of chars
            # ... version doesn't matter to VISTA per se ie/ chr(1)0 works (as CPRS vs JLV seems to use)
            commandtoken = "2" + chr(5) + "1.108" # length of version and version though version seems to be hard coded and this is ignored

        namespec = chr(len(name)) + name    # format name S-PACK

        paramsspecs = "" # blank if no argument command

        if not len(params):  # if no paramters do this and done
            if not isCommand:
                paramsspecs += "5" + "4" + "f" # 5 == params coming then just end. 
        else: # if there are paramters
            paramsspecs += "5" # means that what follows is Params to RPC
            for param in params:
                if type(param) is not dict:
                    paramsspecs += "0" # Type of RPC: Literal
                    paramsspecs += str(len(param)).zfill(3) + str(param) # L-PACK
                    paramsspecs += "f"  # End
                elif "type" in param and param["type"] == "REFERENCE":
                    paramsspecs += "1" # Type of RPC: Reference
                    paramsspecs += str(len(param["value"])).zfill(3) + str(param["value"]) # L-PACK
                    paramsspecs += "f"  # End
                else: # we are in a dictionary
                    paramsspecs += "2" # Type of RPC: List
                    paramIndex = 1 # keep track of where to put the t's
                    for key,val in param.items():
                        if paramIndex > 1: paramsspecs += "t" # t is the delimiter b/n each key,val pair
                        paramsspecs += str(len(str(key))).zfill(3) + str(key) # L-PACK
                        paramsspecs += str(len(str(val))).zfill(3) + str(val) # L-PACK
                        paramIndex += 1
                    paramsspecs += "f" # close list

        endtoken = chr(4) # EOT
        return protocoltoken + commandtoken + namespec + paramsspecs + endtoken

    def readToEndMarker(sock):
        msgChunks = []
        noChunks = 0
        msg = ""
        ENDMARK = chr(4)
        while True:
            msgChunk = sock.recv(256)
            # Connection closed
            # Note: don't differentiate connection closed and no chunks sent from connection just dropped
            # ... could use select.select((sock,), (), (), 0)
            if not msgChunk:
                break
            if not len(msgChunks):
                # \x00\x00 in VistA. CIA uses ID\x00
                # but some connect handshake lack this
                if msgChunk[0] == "\x00": # smh fix
                    msgChunk = msgChunk[2:]
            noChunks += 1
            if msgChunk[-1] == ENDMARK:
                msgChunks.append(msgChunk[:-1])
                break
            msgChunks.append(msgChunk)
        if len(msgChunks):
            msg = "".join(msgChunks)
        # a/c for accents in characters - go from latin-1 to unicode for printing
        # ... otherwise print etc leads to exception that ends in 'return encode_basestring_ascii(o)'
        return msg.decode("ISO-8859-1").encode("utf-8")
 
    def connect(host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return sock

    # See: http://ascii-table.com/ansi-escape-sequences.php (Linux only)
    def bold(s):
        if not terminalHighlight:
            return s
        return '\033[1m' + s + '\033[0m'

    # TODO: need to allow application in scripts
    CONSTANTS = {"IPADDRESS": socket.gethostbyname(socket.gethostname())} 

    print
    print "Invoking RPCs to VISTA at " + host + ":" + str(port)
    print
    print bold(dialog["description"])
    print

    sock = None
  
    for i, requestResponse in enumerate(dialog["rpcs"], 1):
        if i == 1:
            print "\t\t\t\t....................................................\n\n"
        if "skip" in requestResponse:
            continue
        request = requestResponse["request"]
        if sock == None:
            if request["name"] != "TCPConnect":
                raise Exception("No connection - first request must be TCPConnect")
            sock = connect(host, port)
            print
            print "... connected"
            print
        print bold(str(i) + ". " + request["name"]), "- " + requestResponse["description"] if "description" in requestResponse else ""
        requestMessage = makeRequest(request["name"], request["params"] if "params" in request else [], request["isCommand"] if "isCommand" in request else False)
        print
        print "\tContents:", request["name"], request["params"] if "params" in request else "", "\n"
        lenSent = sock.send(requestMessage)
        print "\t\tRaw (" + str(lenSent) + "):", json.dumps(requestMessage), "\n"
        response = readToEndMarker(sock)
        if "stopIfResponse" in requestResponse and eval(requestResponse["stopIfResponse"]): # look at exec for flexibility
            print "\t", bold("DEAD STOP RESPONSE"), "(unexpected so no going on):", bold(json.dumps(response)), "\n\n"
            print
            break
        if "response" in requestResponse:
            if (callable(requestResponse["response"]) and requestResponse["response"](response)) or (response == requestResponse["response"]):
                print "\tExpected response:", bold(json.dumps(response)), "\n"
            else:
                print "\tUNEXPECTED RESPONSE:", len(response), bold(json.dumps(response)), "\n"
                print "\t... ending my try"
                break
            if "assign" in requestResponse:
                assigned[requestResponse["assign"]] = response
                print "assigned", assigned
        else: #  
            print "\tResponse:", bold(json.dumps(response)), "\n"
        if request["name"] == "#BYE#":
            print
            print "... disconnected"
            print
            sock = None
        print
        print "\t\t\t\t....................................................\n\n"

SYSTEMS = {
    "NODEVISTA": { "host": "localhost", "port": 9330 }
}

def main():
    opts, args = getopt.getopt(sys.argv[1:], "")
    if len(args) < 2:
        raise Exception("Specify {SYSTEM} {DIALOGFILE}")
    if args[0] not in SYSTEMS:
        raise Exception("Unknown System: " + str(args[0]))
    if len(args) > 2:
        terminalHighlight = False
    else:
        terminalHighlight = True 
    dialog = json.load(open(args[1]))
    connectAndRun(SYSTEMS[args[0]]["host"], SYSTEMS[args[0]]["port"], dialog, terminalHighlight)

if __name__ == "__main__":
    main()


