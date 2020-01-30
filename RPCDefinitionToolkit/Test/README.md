## Test for definition-driven, Session Nuance

Ensure RPC and App definitions support sufficient __Session Object Nuance__, with sessions having authentication-method, user and other key information identified ("fully defined").

Nuance ...

Property | Source | Description
--- | --- | ---
auth method | not in 3.081 | ala DUZ("AUTHENTICATION")
userIEN | user info RPC | file 200 user
source IP | TCP Connection or  _TCP Connect_ | 
job | N/A | 
duration | time TCP Connect to Bye/Close | will just have start and end times
remote IEN | SIGNON SETUP
remote station no | SIGNON SETUP |
(remote) app | SIGNON SETUP (BSE) |  
workstation | _TCP Connect_ | may just be part of IP again (JLV=10) and is made lowercase in SO create
contexts set (counted/ordered) | SET CONTEXT | for traffic reproduction + enforcement
contexts added to user | DB call to add secondary options | needed for full 200
... | ... | ...

