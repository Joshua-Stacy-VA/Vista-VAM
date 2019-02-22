# VAEC ATO: Securing Veteran Data in the Cloud

Reference: 
https://vaww.portal.va.gov/sites/ECS/Pages/Cybersecurity-in-the-VAEC.aspx


Ensuring that sensitive Veteran data is secure, available, and safe from cyber threats is among the highest priorities of VA OIT and the Enterprise Cloud Solutions Office (ECSO).  For that reason, VAEC applications must meet the same rigorous cybersecurity requirements as any other VA IT system.  These requirements are defined by the VA Handbook 6500 and the National Institutes of Standards and Technology (NIST) cybersecurity standards. 

In a typical on-premises application (i.e., an app hosted in a VA-owned data center), the IT and Operations Services (ITOPS) team is typically responsible for security from the networking components through application-level security.  Cloud-leveraged systems use a shared responsibility model where the accountability for security is split among the Cloud Service Provider (CSP), the VA enterprise, the VAEC team, and the project team.  This has two benefits.  First, VA can take advantage of the billions of dollars of investments in security made by CSPs to build secure applications faster.  Second, VA project teams can obtain an Authority-to-Operate or ATO more quickly since their applications are only reviewed for the security controls that they are responsible for.  The remaining security controls are "inherited" from the lower layer components which have already by tested by the Federal Risk and Authorization Management Program (FedRAMP) or VA OIT.

Typical Shared Responsibility Model

ATO-Typical Shared Responsibility Model.jpg 

## Getting Thru the Cloud ATO Process Quickly

The ECSO team, working with VA cybersecurity groups such as the Office of Information Security (OIS), has developed three documents to help your project team go through the ATO process quickly:

__VAEC Application On-Boarding Form__ - Provides a quick description of your new or to-be-migrated application. Filled out by the project manager, it is designed to help VA and ECSO cybersecurity staff quickly understand your cloud-leveraged systems and its requirements.  When complete, this form should be sent to ecsoinfo@va.gov.

https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/ATO/VAEC_Guide/source/VAEC_Application_Onboarding_Form.pdf

__Cloud ATO Process__ - Explains how to get a VA ATO for a cloud-leveraged system. *This document doesn't replace existing VA ATO process documentation* but is meant to supplement it by explaining how the ATO process works with a cloud-leveraged system. 

https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/ATO/VAEC_Guide/source/Cloud_ATO_Process_2018-11-09.pdf


* Pre-Submission Checklist
https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/ATO/VAEC_Guide/source/Cloud_ATO_Checklist-FULL.pdf

* Cloud Authority to Operate (ATO) Checklist - Cloud authorization checklist for deployments within the VAEC
https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/ATO/VAEC_Guide/source/Cloud_ATO_Checklist.pdf



__Customer Responsibility Matrix (CRM)__ - Building on the concept of the shared responsibility model, the CRM identifies who is responsible for which NIST security control.  This responsibility will shift based on the service model used: SaaS, PaaS or IaaS.

https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/ATO/VAEC_Guide/source/VAEC_CRM_2019-02-06.xlsx

The following templates include the VAEC information and can be used as a basis for your documents:

AWS Incident Response Plan (IRP) Template
https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/ATO/VAEC_Guide/source/VAEC_AWS_IRP_Template_2018-11-30.docx

AWS Disaster Recovery Plan (DRP) Template  
Link: https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/A%26A/VAEC/vaec-documents/VAEC%20AWS%20-%20DRP%2011252018%20Associate%20Template.docx

AWS Configuration Management Plan (CMP) Template


AWS Information System Contingency Plan Associate Template
Link: https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/A%26A/VAEC/vaec-documents/VAEC_AWS_ISCP_1125018%20Associate%20template.docx


Azure Incident Response Plan Associate Template  
Azure Disaster Recovery Plan Associate Template   
Azure Configuration Management Plan Associate Template  
Azure Information System Contingency Plan Associate Template  


The VAEC Security team can run UNOFFICIAL pre-ATO Nessus scans for your environment to aid in assessing your security posture. Download the following documents:

Instructions for submitting a scan request
Link: https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/A%26A/VAEC/vaec-documents/APPLICATION%20information%20for%20Nessus%20scan%20-%20template.xlsx

Template for Nessus scan
Link: https://github.com/vistadataproject/VAM2ProjectManagement/blob/master/A%26A/VAEC/vaec-documents/Information%20required%20to%20run%20Nessus%20scan%20on%20applications%20in%20the%20VAEC%20V2.docx

