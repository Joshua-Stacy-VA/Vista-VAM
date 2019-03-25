DRAFT Notes

## Technical Deep Dive Meeting Minutes  - VistA Adaptive Maintenance
U.S. Department of Veterans Affairs, Veteran Health Administration


### Meeting Information
| -- | -- |
|:---|:---|
| Meeting Purpose: | Technical Deep Dive to discuss AWS track of the VAM project  |
| Date & Time: |	March 21, 2019; 9:00 am – 3:30 pm, Eastern Standard Time |
| Location:	| AWS, Herndon, VA | 
| Facilitator:	| Nilesh Lal |
| Scribe: |	Piyush Thesia |


### Attendance
|  | Attendees |  | Attendees	|  | Attendees |
|:---:|:---:|:---:|:---:|:---:|:---:|
| x | Richards, Rafael M – VA Business Owner |  | Owsley, Cheryl – VA PM |  | Goode, Robert – VA COR  |
|  | Weckessser, Michael – VA CS |  | Fourcade, Joseph – VAEC ISO | x | Lal, Nilesh V. - AbleVets PM |
| x | Wilcox, Tom - AbleVets CIO | x | Lentile, Christy – AbleVets Portfolio Director | x | Dowling, Conor – Caregraf Technical Architect | 
|  | Hill, Kristen A. – Cognosante | x | Furoyama, Michael – Technical Lead HRG |  | Akamine, Adam - HRG Developer |
| x | Faulkner, David – AbleVets System Security Engineer |  | Lucas, Michael – Cognosante  |  | Teeple, James – Congnosante |
|  | Rindle, Christie – HRG Developer |  |  -  | x | Thesia, Piyush – AbleVets Associate Business Analyst |

x = in attendance


### Agenda and Meeting Notes
| ID | Topic: |  |
|:---:|:---|:---|
| 1. | Roll Call | ?? Total |
| 2. | Introductions |  | 
| 3. | Key Points </br> 1.	high level summaries will be presented for: </br> a.	Management </br> b.	Technical </br> 2.	Agenda for AWS track: </br> i.	Overview of new architechture | **Dr. Richards:** 1) Explained the purpose of the meeting is to get the VAM2 team techinacally updated on the AWS track. </br> 2) He also revealed that the Omaha and Valley Coastal, Texas VistA have been identified as the VAM2 VistAs. </br> 3) He mentioned that the Texas and Omaha VistA will be available by June 22nd for VAM2 use. </br> 4) Internal VA MOUs for these two VistAs are done. </br> 5) They will be production deployable copies as per the MOU. </br> </br> **Connor:** 1) Updated the group on the technical necessaity of the VAM2. </br> 2) Traffic coming in all of the VistA’s from over 400,000 windows users.  </br> 3) Currently there is no monitoring or log in the VistA. </br> 4) VAM2 is meant to be Data-Driven, non-invasive intelligent audting and alerting classifier system of these inquires in to the VistA. </br> 5) He covered the various options available technically to deliver VAM2. </br> 6) In particular he talked using about physical Router(s) vs. software shield to ensure only the recognized RPC’s are allowed in the VistA. </br> </br> **Mike Furoyama:** Presented the new architechture. </br> </br> **Tom:** Explained the VA processes and procedures that need to be followed and or adhered to in delivering the VAM2 project. </br> </br> During the course of the discussions, AWS team highlighted that their product Dynamo which is expected to be available later this year will suit the needs of VAM2 far better than the AWS CloudWatch that has currently been identified as a key part of the VAM2 solution.</br>  </br> **Dr. Richards** acknowledged the probable capacity of Dynamo but stated that we will continue with CloudWatch for the current VAM2 project as Dynomo is still not available and we can’t base our solution based on a not-yet-availble software. </br> </br> **Nilesh:** highlighted that the AbleVets team is doing the project management and how the current timelines and lead times required for permissions etc. are managed. |
| 4. |	Next Steps | - |
| 5. | Adjourned: | 3:30 pm |



### Action Items
| ID | Action Item (AI) | AI POC | AI Date | Due Date | Completed Date | Comments |
|:---:|:---|:---|:---|:---|:---|:---:|
| 1. | AI 1:  Look at Kinesis | Mike Furoyama | 03-21-2015 | - | - | - |
| 2. | AI 2:  Update SDD based on new architecture | Conor Dowling | 03-21-2015 | - | - | - |
| 3. | AI 3:  Lambda research | Mike Furoyama | 03-21-2015 | - | - | - |
| 4. | AI 4:  Provide Orchestration  for Security Documents ( mostly covered in SDD but might have extra questions for ATO specific needs) | Conor Dowling | 03-21-2015 | - | - | - |
| 5. | AI 5:  Need Cloud cost  | Cheryl Owesly | 03-21-2015 | - | - | - |
| 6. | AI 6:  Get AWS Sizing </br> a)	Pre-Prod </br> b)	Prod | Nilesh Lal | 03-21-2015 | - | - | - |
| 7. | AI 7:  VPC Peering process scope where we can connect to Pre-Prod </br> a)	EECCB Process | Nilesh Lal | 03-21-2015 | - | - | - |
| 8. | AI 8:  S3 Traffic Analysis | Tom Wilcox | 03-21-2015 | - | - | - |
| 9. | AI 9:  Bay Pine refreshes </br> a)	Cheyenne </br> b)	Palo Alto </br> c)	Omaha </br> d)	Valley Coastal | Dr. Richards/Nilesh Lal | 03-21-2015 | - | - | - |
| 10. | AI 10:  EECCB tickets for two new VistA - Omaha and Valley Coastal | Nilesh Lal | 03-21-2015 | - | - | - |
| 11. | AI 11:  Get access to Pre-Prod and Prod VistA from Pre-Prod and Prod VAEC environments for all team members | Nilesh Lal | 03-21-2015 | - | - | - |
| 12. | AI 12:  Admin issues with AWS account commssrequest@va.gov for activating the accounts; keep Jim Jonson in the loop | Nilesh Lal | 03-21-2015 | - | - | - |
			

**NOTE:** There was a bad Technical glitch with Skype. Connections kept dropping during the call.  Most of the remote attendees attended the meeting via dial in.




