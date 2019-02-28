## VistA Adaptive Maintenance II - Master Test Plan

Version 1.0

February 2019

### Table of Contents
* Introduction
  * Purpose of the Test Plan Document
* Test Objectives
* Test Requirements
* Data Management
* Test Approach
  * Levels of Testing
  * Product Component (Unit) Testing
  * Component Integration Testing
  * Regression Testing
  * Smoke Testing
  * System Testing
  * Security Testing
* Test Management
* AbleVets Delivery Pipeline:
* Test Deliverables
* Testing Dependencies
* List of Tables
  * Table 2: Test Deliverables
* List of Figures


## Introduction
Purpose of the Test Plan Document

This Master Test Plan summarizes the testing approach, key objectives, test tools, and test data output for the VistA Adaptive Maintenance VAEC Security (VAM2) project. The document introduces:

__Test Strategy:__  The rules upon which testing will be based, and the process for establishing valid tests to output sound test data. The project’s test strategy will address the scheduling of test events, entry and exit criteria, and test data management.

__Execution Strategy:__  Describes how tests will be performed.

__Test Management Plan:__  Details test design, execution, and the process for test event issue resolution.

## Test Objectives
Testing will validate and quantify all Remote Procedure Call (RP)C volumes and coverage to generate the necessary data for resource planning, and the optimization and scaling of RPC Interface monitoring for all VA Enterprise Cloud (VAEC)-hosted VistA systems as required in Section 5.6 (Release and Deployment Support) of the Project Work Statement (PWS).

The overarching test objectives are:

* Communicate the test methods that will be employed to achieve expected results
* Leverage both manual and automated test techniques
* Perform robust testing across all solution components using VA-approved methods, tools, and reporting formats
* Conduct testing on a continuous basis (at a minimum, weekly)
* Illustrate how the test results will be validated
* Associate the deliverable test artifacts to each test performed

Specific test goals are:
* Craft an RPC Interface test suite for all 5500 VistA RPCs and their attributes
* Establish a set of reusable test cases for subsequent system and User Acceptance Testing (UAT)
* Validate the thoroughness of testing, based upon the number and percentage of the RPCs audited
* Validate the accuracy of testing, based upon RPC type, attributes, users, clients, and sensitivity
* Provide audit and test results in a machine-processable format, to align with the use of the automated monitoring tool, CloudWatch



## Test Requirements

__Data Management__
The VAM2 test team is not required to create test data, however, it will be obtained from a VistA instance in the VA environment.  Once the Initial Operating Capability (IOC) test cases are defined, the VAM2 test team will determine the method for securing sensitive test data.

## Test Approach
__Levels of Testing__:
VAM2 will execute the following types of testing:

__Product Component (Unit) Testing__:
 	The development team will perform component testing in the local development 
 	environments; the developer will also execute unit testing via Jasmine.

__Component Integration Testing__:
The development team will perform component integration testing during Sprint testing cycles.  Testing is executed to ensure that the installation and user interface is operating as designed; in addition, the interaction between the integrated components will be verified.

__Regression Testing__:
After one or changes/fixes have been implemented, the application is re-tested to ensure that existing functionality still performs as expected. The development and test team will perform a full regression test after defects are fixed and/or new functionalities are implemented.

__Smoke Testing__:
Smoke testing is the first test performed to ensure the core functionality is working and the test environment is stable enough to continue testing.  The VAM2 team will perform this testing after each build is installed.

__System Testing__:
System testing is performed on the integrated system to evaluate compliance with the requirements; this is established by executing functional and regression testing.  

__Security Testing__:
Security testing identifies and resolves vulnerabilities within the information system to prevent unauthorized users from accessing the system.  The AbleVets Security Assessment Team will perform this test, per the A&A Process.


## Test Management
The VAM2 test team is responsible for managing the testing activities throughout the testing lifecycle to include:

__Planning Phase__: Creating the test plan, review and analyze requirements, allocating resources to ensure proper coverage for execution and completion of testing tasks throughout all phases, assisting in setting up the test environment, creating and updating the test schedule, and determining the functionality that will be tested

__Design Phase__: Creating test data, test cases (for manual testing), and test scripts (for automated testing)

__Execution Phase__: Executing test cases, documenting defects, reporting issues to developers, performing regression testing

__Closure Phase__: Creating the test report and communicating results to management 


### Delivery Pipeline:
All VAM code will be interfaced and integrated into the AbleVets Build Pipeline such that as new code is published on the Project Repository, it will automatically trigger the build and test sequence on the Build Pipleline.  

Jenkins on-demand will be deployed to the test environments as well as Nexus via continuous integration of code. Based on the results, Jenkins will deploy the updated artifacts to Nexus, which will then be deployed to the Production environment.


## Test Deliverables
AbleVets will deliver the following test artifacts at the end of each release:

Table 2: Test Deliverables
 
| CLIN #	| Test Deliverables	|
|---|---|
|0002AA	| Security Vulnerability Report	|
|0003AA	| Master Test Plan	|
|0003AB	| RPC Interface Test Suite	|

### Testing Dependencies
Testing is dependent on the following:
* Connection of Delivery Pipeline with the appropriate artifacts in the VAM Github Repository
* Identify IOC test instance of VistA and CPRS 
* Communication with IOC test team

## Appendix A: Key Terms
The following table provides definitions for terms relevant to this document.
 
| Term	| Definition |
|---|---|
|A&A	|Assessment & Authorization| 	   
|CPRS |	Computerized Patient Record System	   
|Dev/INT | Development/Integration 	   
|GIT	|Global Information Technology	   
|HRG	|Hawaii Resources Group	   
|IOC	|Initial Operating Capability	   
|UAT	|User Acceptance Testing	   
|UFT	|User Functionality Testing	   
|UI	|User Interface	   
|VA	|Veteran Affairs	   
|VAM2	|Vista Adaptive Maintenance VAEC Security	   
|VIP	|Veteran-Focused Integration Process	   
|VistA	|Veteran Information System Technology Architecture	 

