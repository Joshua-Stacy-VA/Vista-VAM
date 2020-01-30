## VA VistA RPC Interface Definition 
    
There are __6,385__ RPCs, __4,829 (75.63%)__ of which are active. The first RPCs were distributed on _1996-04-14_, the last on _2019-02-13_. The last installation happened on _2019-04-15_.
    
RPCs are marked inactive in stages ...

\# | Stage | \# At/After
--- | --- | ---
1 | Total | 6,385
2 | 8994 Full Entry | 6,069
3 | Installed Build | 5,882
4 | Has currently used Active Option | 4,829


### RPC Distribution by Year
    
214 RPCs have no 'first distributed' date as their first builds lacked a date - the other 6,171 all have dates. Here is RPC distribution year by year, along with the small amount of deletion too. Note that only __287 (4.49%)__ RPCs are formally deleted though __1,556 (24.37%)__ should be.

\# | Year | Added \# | Deleted \# | Inactive \#
--- | --- | --- | --- | ---
1 | 2019 | 8 (0.13%) | &nbsp; | 2 (25.0%)
2 | 2018 | 173 (2.8%) | &nbsp; | 6 (3.47%)
3 | 2017 | 188 (3.05%) | 1 | 13 (6.91%)
4 | 2016 | 872 (14.13%) | 27 | 142 (16.28%)
5 | 2015 | 197 (3.19%) | 12 | 56 (28.43%)
6 | 2014 | 78 (1.26%) | 3 | 5 (6.41%)
7 | 2013 | 268 (4.34%) | 3 | 13 (4.85%)
8 | 2012 | 163 (2.64%) | 1 | 36 (22.09%)
9 | 2011 | 141 (2.28%) | &nbsp; | 10 (7.09%)
10 | 2010 | 361 (5.85%) | 66 | 178 (49.31%)
11 | 2009 | 248 (4.02%) | 1 | 20 (8.06%)
12 | 2008 | 205 (3.32%) | 4 | 71 (34.63%)
13 | 2007 | 219 (3.55%) | 2 | 36 (16.44%)
14 | 2006 | 191 (3.1%) | 2 | 68 (35.6%)
15 | 2005 | 375 (6.08%) | 21 | 70 (18.67%)
16 | 2004 | 362 (5.87%) | 34 | 78 (21.55%)
17 | 2003 | 373 (6.04%) | 5 | 115 (30.83%)
18 | 2002 | 365 (5.91%) | 48 | 131 (35.89%)
19 | 2001 | 306 (4.96%) | 12 | 33 (10.78%)
20 | 2000 | 439 (7.11%) | 22 | 57 (12.98%)
21 | 1999 | 158 (2.56%) | 16 | 36 (22.78%)
22 | 1998 | 66 (1.07%) | &nbsp; | 11 (16.67%)
23 | 1997 | 339 (5.49%) | &nbsp; | 90 (26.55%)
24 | 1996 | 76 (1.23%) | 7 | 65 (85.53%)


### MUMPS Routine Implementation
    
__6069__ RPCs are implemented in __1928__ separate MUMPS routines, while __316__ identified RPCs lack an implementation. The highest number of RPCs per routine is __129__ (_SDEC_), the median is __2.0__, the lowest is __1__. __1,432 (74.27%)__ routines implement only active RPCs, __394__ only inactive RPCs (candidates for deletion?), while __102__ implement a mix of active and inactive RPCs.

The (outliers) that implement the most RPCs are ...

\# | \# RPCs | Routine(s)
--- | --- | ---
1 | 129 | SDEC
2 | 43 | ORWTPP
3 | 39 | OREVNTX1
4 | 34 | __VEJDTPR__ [INACTIVE]
5 | 28 | __ORWPCE2__ [INACTIVE]
6 | 27 | ORQQPXRM, ORWGRPC, __ORWPT__ [INACTIVE]
7 | 24 | ORWPCE
8 | 23 | __DSIPRPC0__ [INACTIVE], ORWU
9 | 22 | ORQQCN2, __ORWTIU__ [INACTIVE], VEJDATL, VIABRPC
10 | 21 | ORWDX
11 | 20 | ORWLRR
12 | 19 | DSIUTL1, __SDOERPC__ [INACTIVE]
13 | 18 | DSIFCNS1
14 | 17 | DSIROI6
15 | 16 | DSIROI1, ORWDXA, RMIMRP
16 | 15 | __APUFYID2__ [INACTIVE], AXARDGUI, __DSIQUTL9__ [INACTIVE], __NUPABCL2__ [INACTIVE], __ORQQCN1__ [INACTIVE], ORWDPS1
17 | 14 | DSIYGNI, DVBAB1, __MAGDRPC1__ [INACTIVE], ORWDFH, __ORWPT16__ [INACTIVE]
18 | 13 | __APUFYAP1__ [INACTIVE], __ARKCPTSK__ [INACTIVE], __ARKCVAPH__ [INACTIVE], DSICXPR, DSIVXPR, ORAM1, ORQQPX, __ORWD__ [INACTIVE], ORWDPS33, __ORWOR__ [INACTIVE], TIUSRVA, VANOD04


### Packages
    
_Package_ is a sometimes inconsistently used breakdown of VistA into a set of cooperating applications. All but __633 (9.91%)__ RPCs are assigned to __86__ different packages, __26__ of which only have _inactive_ RPCs and __41__ more have a mix of active and inactive RPCs. 

Those with at least one active RPC are - note ORDER ENTRY has a huge proportion which MAY be due to redundant/overlapping purposes of individual RPCs ...

\# | Package | First Distributed RPC | Active RPCs | Inactive RPCs
--- | --- | --- | --- | ---
1 | ORDER ENTRY/RESULTS REPORTING | 1997-07-27 | 972 | 63
2 | IMAGING | 1996-04-14 | 463 | 52
3 | VENDOR - DOCUMENT STORAGE SYS | 2000-02-14 | 297 | 118
4 | ABOVE PAR | 2016-08-17 | 330 | 14
5 | SCHEDULING | 1996-05-30 | 198 | 124
6 | ENCODER PRODUCT SUITE (EPS) | 2005-11-04 | 239 | 7
7 | ADVANCED PROSTHETICS ACQUISITION TOOL (APAT) | 2016-08-30 | 215 | 1
8 | FEE BASIS CLAIMS SYSTEM | 2007-11-20 | 148 | 10
9 | RELEASE OF INFORMATION - DSSI | 2003-01-28 | 133 | 23
10 | TEXT INTEGRATION UTILITIES | 1997-04-14 | 120 | 4
11 | DENTAL | 1999-05-21 | 91 | 31
12 | CORI | 2000-08-14 | 76 | 33
13 | MENTAL HEALTH | 2000-01-13 | 80 | 16
14 | DSIT TELECARE RECORD MANAGER | 2004-03-16 | 69 | 24
15 | AUTOMATED MED INFO EXCHANGE | 2001-06-21 | 90 | 1
16 | VA CERTIFIED COMPONENTS - DSSI | 2003-03-04 | 78 | 11
17 | VISTA INTEGRATION ADAPTER | 1997-07-27 | 87 | 1
18 | INSURANCE CAPTURE BUFFER | 2004-11-04 | 75 | 6
19 | CLINICAL CASE REGISTRIES | 2002-05-15 | 58 | 23
20 | DSIB CARIBOU CLC SUITE | 2017-03-15 | 77 | &nbsp;
21 | ASISTS | 2002-07-09 | 64 | 1
22 | KERNEL | 1996-05-24 | 25 | 39
23 | PROSTHETICS | 2002-12-18 | 54 | 4
24 | SHIFT CHANGE HANDOFF TOOL | 2008-05-13 | 57 | &nbsp;
25 | MENTAL HEALTH SUITE, DSS INC. | 2010-11-15 | 54 | &nbsp;
26 | BAR CODE MED ADMIN | 1999-04-19 | 43 | 5
27 | EVENT CAPTURE | 2001-07-05 | 44 | &nbsp;
28 | REGISTRATION | 2000-02-01 | 16 | 25
29 | VA NURSING OUTCOMES DATABASE PROJECT | 2005-03-23 | 38 | &nbsp;
30 | PATIENT ASSESSMENT DOCUM | 2012-02-24 | 34 | 2
31 | DSIQ - VCM | 2011-07-13 | 30 | 5
32 | RPC BROKER | 1996-05-24 | 20 | 13
33 | GEN. MED. REC. - VITALS | 2002-10-28 | 17 | 15
34 | DSIG | 2015-03-27 | 25 | 7
35 | CARE MANAGEMENT | 2004-01-16 | 1 | 30
36 | VPS KIOSK | 2012-08-16 | 29 | &nbsp;
37 | CLINICAL PROCEDURES | 2004-05-21 | 14 | 10
38 | DATA BRIDGE | 2011-04-19 | 22 | 1
39 | VISTALINK | 2003-09-30 | 12 | 11
40 | FUNCTIONAL INDEPENDENCE | 2000-02-01 | 20 | &nbsp;
41 | CLINICAL REMINDERS | 2001-05-17 | 3 | 16
42 | VISUAL AID FOR CLINIC APPOINTMENTS (VISN 20) | 2005-09-29 | 18 | &nbsp;
43 | VISUAL IMPAIRMENT SERVICE TEAM | 2003-02-18 | 4 | 13
44 | HEALTHEVET DESKTOP | 2004-01-16 | 12 | 4
45 | VBECS | 2009-04-23 | 14 | &nbsp;
46 | R5 VBA IMPORT TOOL | 2012-07-31 | 11 | &nbsp;
47 | R1 SURGERY SCHEDULE VIEWER | 2012-07-13 | 11 | &nbsp;
48 | VA FILEMAN | 1998-02-28 | 10 | &nbsp;
49 | PATIENT REPRESENTATIVE | 2007-01-24 | 6 | &nbsp;
50 | QUASAR | 2003-10-27 | 4 | 1
51 | ELECTRONIC SIGNATURE | 2006-07-14 | 5 | &nbsp;
52 | DSS CORE RPCS | 1999-06-18 | 1 | 4
53 | VIRTUAL PATIENT RECORD | 2011-08-04 | 2 | 2
54 | IFCAP | 2007-04-27 | 3 | &nbsp;
55 | MASH UTILITIES | 2015-12-16 | 3 | &nbsp;
56 | EMERGENCY DEPARTMENT | 2010-09-02 | 3 | &nbsp;
57 | CONSULT/REQUEST TRACKING | 1997-10-28 | 1 | 2
58 | REMOTE ORDER/ENTRY SYSTEM | 2003-09-26 | 1 | 2
59 | ANU HS DOWNLOAD | 2000-11-08 | 1 | &nbsp;
60 | CW GUIMAIL | 1998-05-21 | 1 | &nbsp;


The 'inactive-only' Packages are ...

\# | Package | First Distributed RPC | RPCs (Inactive)
--- | --- | --- | ---
1 | SPINAL CORD DYSFUNCTION | 2010-03-24 | 66
2 | HEALTH MANAGEMENT PLATFORM | 2016-02-23 | 56
3 | NATIONAL VISTA SUPPORT | 2001-02-08 | 49
4 | CAPACITY MANAGEMENT TOOLS | 2004-03-22 | 28
5 | MASTER PATIENT INDEX VISTA | 2002-07-12 | 22
6 | PCE PATIENT CARE ENCOUNTER | 2014-04-24 | 19
7 | AUTOMATED INFO COLLECTION SYS | 1997-02-12 | 16
8 | TOOLKIT | 2008-11-21 | 15
9 | REAL TIME LOCATION SYSTEM | 2016-05-26 | 13
10 | PRECISION G AUTO INSTRUMENT | 1998-06-29 | 10
11 | CLINICAL EVENT MONITOR | 1999-07-13 | 10
12 | INTEGRATED BILLING | 2001-05-31 | 9
13 | MY HEALTHEVET | 2006-07-18 | 8
14 | RADIOLOGY/NUCLEAR MEDICINE | 2010-06-03 | 7
15 | CLINICAL INFO RESOURCE NETWORK | 2002-06-07 | 6
16 | OUTPATIENT PHARMACY | 2017-10-24 | 3
17 | PAID | 2012-02-17 | 2
18 | INTEGRATED PATIENT FUNDS | 2007-02-06 | 2
19 | ONCOLOGY | 2011-08-09 | 1
20 | MAGJ RADIOLOGY | 1999-05-21 | 1
21 | ENROLLMENT APPLICATION SYSTEM | 2007-11-27 | 1
22 | WOUNDED INJURED ILL WARRIORS | 2008-12-30 | 1
23 | NATIONAL HEALTH INFO NETWORK | 2010-10-15 | 1
24 | GUI NOIS | 1998-09-06 | 1
25 | BENEFICIARY TRAVEL | 2013-02-03 | 1
26 | NATIONAL DRUG FILE | 2010-02-12 | 1


### Source Information for Integrated Definition
    
The integrated interface definition combines RPC definitions from multiple real VistA and FOIA. Overall __2,635 (41.27%)__ RPCs are not in FOIA.

\# | Station | RPCs | Definition Contribution
--- | --- | --- | ---
1 | 442 | 5,376 | 20
2 | 640 | 5,520 | 199
3 | 663 | 6,097 | 6,097
4 | 668 | 5,509 | 62
5 | 999 | 3,750 | 7


