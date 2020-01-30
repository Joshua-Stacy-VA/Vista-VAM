<h1 align="center">
VistA Adaptive Maintenance VAEC Security (VAM)<br><br>
Monthly Progress Report<br><br>
<img src="media/DVA.png"><br>
</h1>
<h2 align="center">
<br>
Department of Veterans Affairs <br>
Office of Information and Technology (OIT)<br>
Contract No: VA118-16-D-1009<br>
Task Order: 36C10B19F10090015<br>
January 2020<br>
Version 1.11
</h2>

---

## Deliverable (Product) Version History

| Date       | Version | Description                     | Author   |
| ---------- | ------- | ------------------------------- | -------- |
| 01/31/2020 | 1.11    | Final Monthly Progress Report   | AbleVets |
| 01/03/2020 | 1.10    | Updates for December 2019       | AbleVets |
| 12/03/2019 | 1.9     | Updates for November 2019       | AbleVets |
| 11/04/2019 | 1.8     | Updates for October 2019        | AbleVets |
| 10/03/2019 | 1.7     | Updates for September 2019      | AbleVets |
| 09/03/2019 | 1.6     | Updates for August 2019         | AbleVets |
| 08/02/2019 | 1.5     | Updates for July 2019           | AbleVets |
| 07/03/2019 | 1.4     | Updates for June 2019           | AbleVets |
| 06/03/2019 | 1.3     | Updates for May 2019            | AbleVets |
| 05/03/2019 | 1.2     | Updates for April 2019          | AbleVets |
| 04/03/2019 | 1.1     | Updates for March 2019          | AbleVets |
| 03/04/2019 | 1.0     | Initial version of the document | AbleVets |

## CLIN Satisfaction Statement

This document is submitted in satisfaction of CLIN 0001AB.

## Table of Contents

[1. Introduction](#introduction)

[2. Work Completed](#work-completed)

[3. Work Planned](#work-planned)

[4. Risks and Issues](#risks-and-issues)

[5. Appendix: Acronyms and Abbreviations](#acronyms-and-abbreviations)

# <a id="introduction"></a>1. Introduction

The Veterans Health Information Systems and Technology Architecture (VistA) Adaptive Maintenance (VAM) System is a cloud-native Platform as a Service (PaaS), deployed entirely and exclusively within the Federal Risk and Authorization Management Program (FedRAMP), Health Insurance Portability and Accountability Act of 1996 (HIPAA)-compliant VA Enterprise Cloud (VAEC), leveraging the Amazon Web Services (AWS) commercial cloud infrastructure and services.

VAM provides comprehensive, commercial cloud-based monitoring and security for all clients, applications, and users of the VistA Remote Procedure Call (RPC) interface. VAM is operationalized and scaled for Enterprise Production use for all VistA systems migrated to the VAEC, leveraging FedRAMP High, VAEC-approved AWS Kinesis and AWS CloudWatch Logs.

VAM is a passive monitoring PaaS that mirrors VistA RPC traffic via AWS Kinesis to the AWS CloudWatch Logs, which is then interpreted by the RPC Monitor. AWS CloudWatch Logs are FedRAMP High certified and store all data in an encrypted form.

VAM is a 100% cloud-native, legacy-free, and non-invasive PaaS. VAM requires no change to any VistA system, nor to any end user client or application, allowing VAM to be safely and reliably deployed and scaled Enterprise-wide with minimal to no risk. Should VAM (RPC Mirror or Monitor) be disabled or deactivated, all RPC traffic flows between VistA and all its clients as usual, only without monitoring.

All of VAM's functionality is contained exclusively and entirely as a PaaS within the VAEC, thus inheriting all security and compliance controls of the Federal Information Security Management Act of 2002 (FISMA) High VAEC. VAM has neither a connection to, nor does it share any information with, any organization, application, or system outside of the VAEC.

# <a id="work-completed"></a>2. Work Completed

The work detailed below was completed during the January 1 through January 31, 2020 Period of Performance (PoP).

- Concluded IOC Production at Valley Costal Band (VCB). Received concurrence from the VA.
- Delivered the Draft Capacity, Performance and Scalability Assessment for National Deployment on January 17, 2020.
- Facilitated weekly status meetings to discuss Team AbleVets’ progress. Meeting minutes can be found on the [Project VAM workspace](https://github.com/vistadataproject/VAM2ProjectManagement/tree/master/Documents/source) of GitHub.
- Transitioned the Project Manager from Nilesh Lal to Savio Mendonsa.
- Delivered the Weekly Onboarding Status Reports on January 02, 08, 15, 22, 29, and 31, 2020.
- Reviewed the Project Closeout plan with the COR and the VA IT PM.
- Reviewed the GFE transition at end of PoP with the COR and VA IT PM.
- Updated and delivered the following PWS artifacts on January 3 and 31, 2020.

| CLIN   | Artifact                                  |
| ------ | ----------------------------------------- |
| 0001AA | Contractor Project Management Plan (CPMP) |
| 0001AB | Monthly Progress Report                   |
| 0003AA | Master Test Plan                          |

- Updated and delivered the following PWS artifacts on January 31, 2020.

| CLIN   | Artifact                                                                                                                               |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| 0002AA | Comprehensive RPC Interface Audit Report                                                                                               |
| 0002AB | Massachusetts General Hospital Utility Multi-Programming System (MUMPS) RPC to JavaScript Object Notation (JSON) Model Data Definition |
| 0002AC | Version Description Document (VDD)                                                                                                     |
| 0002AD | Automated CloudWatch Configuration                                                                                                     |
| 0002AE | Security Vulnerability Report                                                                                                          |
| 0003AB | RPC Interface Test Suite                                                                                                               |
| 0005AA | Production Operations Manual (POM)                                                                                                     |
| 0005AB | Deployment and Installation Guide                                                                                                      |
| 0005AC | User Guide                                                                                                                             |
| 0006AA | Final Capacity, Performance, and Scalability Assessment for National Deployment                                                        |

0006AA

# <a id="work-planned"></a>3. Work Planned

None. This is the final monthly report for the project. Project ends on 1/31/2020.

# <a id="risks-and-issues"></a>4. Risks and Issues

There are no open risks and issues. After successful ATO approval and access to IOC sites all the risks and issues were resolved.

# <a id="acronyms-and-abbreviations"></a>5: Appendix: Acronyms and Abbreviations

| Acronym     | Description                                                                      |
| ----------- | -------------------------------------------------------------------------------- |
| **ATO**     | Authority to Operate                                                             |
| **AWS**     | Amazon Web Services                                                              |
| **BIA**     | Business Impact Analysis                                                         |
| **CM**      | Configuration Management                                                         |
| **COMS**    | Cloud Operations and Management Services/Cloud Operations and Migration Services |
| **CPMP**    | Contractor Project Management Plan                                               |
| **CSOC**    | Cybersecurity Operations Center                                                  |
| **DRP**     | Disaster Recovery Plan                                                           |
| **eMASS**   | Enterprise Mission Assurance Support Service                                     |
| **FedRAMP** | Federal Risk and Authorization Management Program                                |
| **FISMA**   | Federal Information Security Management Act of 2002                              |
| **HIPAA**   | Health Insurance Portability and Accountability Act of 1996                      |
| **IOC**     | Initial Operating Capability                                                     |
| **IRP**     | Incident Response Plan                                                           |
| **ISA**     | Independent Safety Assessment                                                    |
| **ISCP**    | Information Security Contingency Plan                                            |
| **ISSO**    | Information System Security Officer                                              |
| **JSON**    | JavaScript Object Notation                                                       |
| **MOU**     | Memorandum of Understanding                                                      |
| **MTP**     | Master Test Plan                                                                 |
| **MUMPS**   | Massachusetts General Hospital Utility Multi-Programming System                  |
| **PaaS**    | Platform as a Service                                                            |
| **PIA**     | Privacy Impact Assessment                                                        |
| **PM**      | Project Manager                                                                  |
| **POAM**    | Plan of Action and Milestones                                                    |
| **POM**     | Production Operations Manual                                                     |
| **PoP**     | Period of Performance                                                            |
| **PTA**     | Privacy Threshold Analysis                                                       |
| **PWS**     | Performance Work Statement                                                       |
| **RMF**     | Risk Management Framework                                                        |
| **RPC**     | Remote Procedure Call                                                            |
| **SIA**     | Security Impact Analysis                                                         |
| **SDD**     | System Design Document                                                           |
| **SSC**     | System Security Categorization Report                                            |
| **SSP**     | System Security Plan                                                             |
| **VA**      | Department of Veterans Affairs                                                   |
| **VAEC**    | VA Enterprise Cloud                                                              |
| **VAM**     | VistA Adaptive Maintenance                                                       |
| **VDD**     | Version Description Document                                                     |
| **VistA**   | Veterans Health Information Systems and Technology Architecture                  |
| **WASA**    | Web Application Security Assessment                                              |
