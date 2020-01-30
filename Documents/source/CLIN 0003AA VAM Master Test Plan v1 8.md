<h1 align="center">
VistA Adaptive Maintenance VAEC Security (VAM)<br><br>
Master Test Plan<br><br>
<img src="media/DVA.png"><br>
</h1>
<h2 align="center">
<br>
Department of Veterans Affairs <br>
Office of Information and Technology<br>
Contract No: VA118-16-D-1009<br>
Task Order: 36C10B19F10090015<br>
January 2020<br>
Version 1.8
</h2>

---

## Revision History

| Date       | Version | Description                | Author   |
| ---------- | ------- | -------------------------- | -------- |
| 01/28/2020 | 1.8     | Final Master Test Plan     | AbleVets |
| 01/03/2020 | 1.7     | Updated Master Test Plan   | AbleVets |
| 09/03/2019 | 1.6     | Updated Master Test Plan   | AbleVets |
| 08/02/2019 | 1.5     | Updated Master Test Plan   | AbleVets |
| 07/03/2019 | 1.4     | Updated Master Test Plan   | AbleVets |
| 06/03/2019 | 1.3     | Updated Master Test Plan   | AbleVets |
| 05/03/2019 | 1.2     | Updated Master Test Plan   | AbleVets |
| 04/03/2019 | 1.1     | Updated Master Test Plan   | AbleVets |
| 02/26/2019 | 1.0     | Baselined Master Test Plan | AbleVets |

## CLIN Satisfaction Statement

This document is submitted in satisfaction of CLIN 0003AA.

## Table of Contents

[1. Introduction](#introduction)

- [1.1. Purpose](#purpose)

[2. Test Objectives](#test-objectives)

[3. Levels of Testing](#levels-of-testing)

- [3.1. Smoke Testing](#smoke-testing)

- [3.2. System Testing](#system-testing)

- [3.2.1. Functional Testing](#functional-testing)

- [3.2.2. Regression Testing](#regression-testing)

- [3.3. Product Component Testing](#product-component-testing)

- [3.4. Component Integration Testing](#component-integration-testing)

- [3.5. User Acceptance Testing](#user-acceptance-testing)

- [3.6. Security Testing](#security-testing)

[4. Test and Test Data Management](#test-and-test-data-management)

[5. Test Dependencies](#test-dependencies)

[6. Developer-Level Tests](#developer-level-tests)

- [6.1. Traffic Mirror Monitor](#traffic-mirror-monitor)

- [6.1.1. Traffic Mirror Monitor Risks](#traffic-mirror-monitor-risks)

- [6.1.2. Traffic Mirror Monitor Risk Mitigation](#traffic-mirror-monitor-risk-mitigation)

- [6.1.3. Static Code Quality](#static-code-quality)

- [6.2. RPC Definition Model](#rpc-definition-model)

- [6.2.1. RPC Definition Model Risks](#rpc-definition-model-risks)

- [6.2.2. RPC Definition Model Risk Mitigation](#rpc-definition-model-risk-mitigation)

[7. Code Delivery Pipeline](#code-delivery-pipeline)

[8. Test Deliverables](#test-deliverables)

[A. Appendix: Acronyms and Abbreviations](#appendix-a)

## Table of Tables

[Table 1: Project VAM Test Deliverables](#table1)

[Table 2: Acronyms and Abbreviations](#table2)

# <a id="introduction"></a>1. Introduction

The Veterans Health Information Systems and Technology Architecture (VistA) Adaptive Maintenance (VAM) System is a cloud-native Platform as a Service (PaaS), deployed entirely and exclusively within the Federal Risk and Authorization Management Program (FedRAMP), Health Insurance Portability and Accountability Act of 1996 (HIPAA)-compliant VA Enterprise Cloud (VAEC), leveraging the Amazon Web Services (AWS) commercial cloud infrastructure and services.

VAM provides comprehensive, commercial cloud-based monitoring and security for all clients, applications, and users of the VistA Remote Procedure Call (RPC) interface. VAM is operationalized and scaled for Enterprise Production use for all VistA systems migrated to the VAEC, leveraging FedRAMP High, VAEC-approved AWS Kinesis and AWS CloudWatch Logs.

VAM is a passive monitoring PaaS that mirrors VistA RPC traffic via AWS Kinesis to the AWS CloudWatch Logs, which is then interpreted by the RPC Monitor. AWS CloudWatch Logs are FedRAMP High certified and store all data in an encrypted form.

VAM is a 100% cloud-native, legacy-free, and non-invasive PaaS. VAM requires no change to any VistA system, nor to any end user client or application, allowing VAM to be safely and reliably deployed and scaled Enterprise-wide with minimal to no risk. Should VAM (RPC Mirror or Monitor) be disabled or deactivated, all RPC traffic flows between VistA and all its clients as usual, only without monitoring.

All of VAM's functionality is contained exclusively and entirely as a PaaS within the VAEC, thus inheriting all security and compliance controls of the Federal Information Security Management Act of 2002 (FISMA) High VAEC. VAM has neither a connection with, nor does it share any information with, any organization, application, or system outside of the VAEC.

## <a id="purpose"></a>1.1. Purpose

This Master Test Plan summarizes the testing approach, key objectives, test tools, and test data output for Project VAM. The document introduces:

- Test Strategy: The rules upon which testing will be based, and the process for establishing valid tests to output sound test data. The project's test strategy will address the scheduling of test events, entry and exit criteria, and test data management.

- Execution Strategy: Describes how tests will be performed.

- Test Management Plan: Details test design, execution, and the process for test event issue resolution.

# <a id="test-objectives"></a>2. Test Objectives

Testing will validate and quantify all RPC volumes and coverage to generate the necessary data for resource planning, and the optimization and scaling of RPC Interface monitoring for all VAEC-hosted VistA systems as required in Section 5.6 (Release and Deployment Support) of the Performance Work Statement (PWS).

The overarching test objectives are:

- Communicate the test methods that will be employed to achieve expected results

- Leverage both manual and automated test techniques

- Perform robust testing across all solution components using VA-approved methods, tools, and reporting formats

- Conduct testing on a continuous basis (at a minimum, weekly)

- Illustrate how the test results will be validated

- Associate the deliverable test artifacts to each test performed

Specific test goals are:

- Craft an RPC Interface test suite for all 5500 VistA RPCs and their attributes

  - Establish a set of reusable test cases for subsequent system and User Acceptance Testing (UAT)

  - Validate the thoroughness of testing, based upon the number and percentage of the RPCs audited

  - Validate the accuracy of testing, based upon RPC type, attributes, users, clients, and sensitivity

  - Provide audit and test results in a machine-processable format, to align with the use of the automated monitoring tool CloudWatch

# <a id="levels-of-testing"></a>3. Levels of Testing

The following subsections describe the levels of testing Team AbleVets will conduct during the lifecycle of the project.

## <a id="smoke-testing"></a>3.1. Smoke Testing

Smoke testing is the first test performed to ensure the core functionality is working and the test environment is stable enough to continue testing. Team AbleVets will perform smoke testing after each build is installed.

## <a id="system-testing"></a>3.2. System Testing

System tests are performed on the integrated system to evaluate compliance with the requirements. Compliance is established by executing both functional and regression testing.

### <a id="functional-testing"></a>3.2.1. Functional Testing

Functional testing is executed as part of system testing to validate the front-end components and ensure the functionality of the application is operating as designed.

### <a id="regression-testing"></a>3.2.2. Regression Testing

The AbleVets Development and Test teams will perform a full regression test after defects are remediated and/or new functionality is implemented to ensure that existing functionality continues to perform as expected.

## <a id="product-component-testing"></a>3.3. Product Component Testing

The AbleVets Development team will perform component testing, also referred to as unit testing, in local development Environments, using a tool similar to Jasmine.

## <a id="component-integration-testing"></a>3.4. Component Integration Testing

The AbleVets Development team will perform component integration testing during Sprint testing cycles to ensure that the installation and user interface are operating as designed, and to validate the interaction between integrated components.

## <a id="user-acceptance-testing"></a>3.5. User Acceptance Testing

UAT is performed by the client during Initial Operating Capacity (IOC) to certify that the system is functioning per the requirements, prior to moving into Production. End users will develop and execute test scripts, per their testing approach, with assistance from Team AbleVets.

## <a id="security-testing"></a>3.6. Security Testing

Security testing identifies and resolves vulnerabilities within the system to prevent unauthorized access. The AbleVets Security Assessment team will perform all security tests per the Assessment and Authorization (A&A) process.

# <a id="test-and-test-data-management"></a>4. Test and Test Data Management

Team AbleVets is responsible for managing test activities throughout the project lifecycle. The activities for each phase are detailed below.

**Planning Phase:** Create the test schedule, review and analyze requirements, determine the functionality to be tested, create the test plan, allocate resources, and assist in standing up the test environment.

**Design Phase:** Create the test data, the manual test cases, and the automated test scripts.

**Execution Phase:** Execute the test cases, document any defects identified through testing, report defects to the Development team, and perform regression testing once the defects have been remediated.

**Closure Phase:** Create post-test reports and communicate the results.

Team AbleVets is not required to create test data; however, test data will be obtained from a VistA within the VA environment. When the IOC test cases are defined, Team AbleVets will determine the method for securing sensitive test data.

# <a id="test-dependencies"></a>5. Test Dependencies

Successful testing is dependent upon the setup of the AbleVets delivery pipeline with the latest VistA and Computerized Patient Record System (CPRS) instance; coordinating with the Development team to identify web client testing requirements; identification of IOC test instances of VistA and CPRS; and open communication with IOC Test team.

# <a id="developer-level-tests"></a>6. Developer-Level Tests

Team AbleVets has created Developer-level tests and execution schemes for the RPC Monitor, RPC Mirror, and RPC Definition Models. After the initial testing and meeting with AWS team, architecture was changed, and RPC Mirror and RPC Monitor are being replaced with new Traffic Mirror Monitor.

## <a id="traffic-mirror-monitor"></a>6.1. Traffic Mirror Monitor

The RPC Monitor represents the software pipeline that facilitates RPC parsing, classification, and alert notification functions of VAM.

### <a id="traffic-mirror-monitor-risks"></a>6.1.1. Traffic Mirror Monitor Risks

The risks associated with the Traffic Mirror Monitor software are downtime due to runtime errors and crashes, and degraded quality of the static code.

### <a id="traffic-mirror-monitor-risk-mitigation"></a>6.1.2. Traffic Mirror Monitor Risk Mitigation

Mitigation of downtime caused by runtime errors is achieved using the Jest framework when creating unit and integration-level tests. Unit tests will ensure runtime coverage of at least 95%. Integration-level regression test scripts are created using Batch mode to test RPC inputs.

Each published commit to the master branch in the Traffic Mirror Monitor code repository triggers the automated execution of Jest unit and regression tests. If the test code coverage drops below 95%, and/or if there are any errors identified during testing, they will be reported within the results. Any errors logged will be fixed immediately.

Running these tests may facilitate the need for a continuous integration system in VAEC, to provide access to the Kinesis mechanisms.

### <a id="static-code-quality"></a>6.1.3. Static Code Quality

Static code quality issues are addressed with the use of the ESLint inspection tool and a pre-defined code formatting standard. The formatting standard is based upon the Airbnb JavaScript (JS) standard.

Each published commit to the master branch in the RPC Monitor code repository triggers the automated execution of the code inspection tool. If the results indicate broken code formatting, it will be fixed immediately.

## <a id="rpc-definition-model"></a>6.2. RPC Definition Model

The RPC Definition Model is the static RPC definition model file collection and the classifier pipeline. The files are generated by the RPC definition toolkit that, with the classifier pipeline, are resident in the Traffic Mirror Monitor. The generated model files are applied against the RPC traffic to generate classifications and alerts.

### <a id="rpc-definition-model-risks"></a>6.2.1. RPC Definition Model Risks

The risk associated with RPC Definition Models are inconsistent classifications generated by known RPC sequences.

### <a id="rpc-definition-model-risk-management"></a>6.2.2. RPC Definition Model Risk Mitigation

Mitigation of inconsistent classifications is realized through the creation of RPC sequences that validate the classifier's response and running multiple sets of RPC sequences into a test VistA system, to validate that the VistA FileMan state matches the classifier's response.

Team AbleVets will ensure that the RPC Definition Models and the RPC Monitor software consistently produces known results. A test harness is created to validate the notifications and alerts generated by the RPC Monitor, and that allows testers to run multiple, known sequences of RPCs into the RPC Monitor software with a known RPC Definition Model.

The test harness runs regression tests whenever new code is committed to the RPC Mirror repository. Deviation from the known classifications set by the definition models are marked as errors and fixed immediately.

# <a id="code-delivery-pipeline"></a>7. Code Delivery Pipeline

Code is initially stored and tested in GitHub, a version control system. The code is then integrated into the AbleVets build pipeline and installed in the AbleVets test environment. Once the code testing in the AbleVets environment is complete, the code is moved to the VA environment.

Jenkins on Demand is deployed to the test environments and GitHub via the continuous integration of code. Jenkins deploys the updated artifacts to GitHub, which are then deployed to the Production environment.

VA User Acceptance (UA) testers will develop all manual UAT test scripts. If necessary, the test cases used during manual testing are delivered to UA testers. Automated testing is not conducted during UAT.

# <a id="test-deliverables"></a>8. Test Deliverables

Team AbleVets delivers the test artifacts listed in [Table 1](#table1), in accordance with the PWS.

### <a id="table1"></a>Table 1: Project VAM Test Deliverables

| CLIN   | Title                    | Frequency                                                       |
| ------ | ------------------------ | --------------------------------------------------------------- |
| 0003AA | Master Test Plan (MTP)   | The 3rd day of every month throughout the life of the project   |
| 0003AB | RPC Interface Test Suite | The 2nd day of every quarter throughout the life of the project |

# <a id="appendix-a"></a>A. Appendix: Acronyms and Abbreviations

[Table 2](#table2) details the acronyms and abbreviations used
throughout this document.

### <a id="table2"></a>Table 2: Acronyms and Abbreviations

| Term    | Definition                                                  |
| ------- | ----------------------------------------------------------- |
| A&A     | Assessment and Authorization                                |
| AWS     | Amazon Web Services                                         |
| CPRS    | Computerized Patient Record System                          |
| FedRAMP | Federal Risk and Authorization Management Program           |
| FISMA   | Federal Information Security Management Act of 2002         |
| HIPAA   | Health Insurance Portability and Accountability Act of 1996 |
| IOC     | Initial Operating Capability                                |
| JS      | JavaScript                                                  |
| MTP     | Master Test Plan                                            |
| OIT     | Office of Information and Technology                        |
| PaaS    | Platform as a Service                                       |
| PoP     | Period of Performance                                       |
| PWS     | Performance Work Statement                                  |
| RPC     | Remote Procedure Call                                       |
| UA      | User Acceptance                                             |
| UAT     | User Acceptance Testing                                     |
| VA      | Veteran Affairs                                             |
| VAEC    | VA Enterprise Cloud                                         |
| VAM     | Vista Adaptive Maintenance VAEC Security                    |
| VistA   | Veteran Information System Technology Architecture          |
