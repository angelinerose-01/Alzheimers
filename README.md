# Alzheimers Disease Detection
Detecting if a patient has the risk of being affected with alzheimers is quite a tedious job. It takes multiple doctor visits and taking a lot of scans which could cost a lot of money and time to go to waste . The tool aims to be used as pre diagnostic step which could help the possibly affected patients to check out if they are at the risk of having alzheimers disease at the comfort of their own homes . The tool helps with a pre diagnosis or a consultation which provides the users an insight whether if they're at the risk of having alzheimers or not  . The model takes the cognitive test scores such as MMSE , SES and CDR and some more features as the input and uses random forest algorithm to classify if the patient is affected with alzheimers or not 
## Data and Features
The model was trained based on different cognitive test scores which was obtained from the OASIS website .The dataset has around  374 bservations. Each subject is above the age of 65, every one is right handed  and has had atleast one clinical visit.
The features used in the model are 
- EDUC
- SES
- MMSE
- CDR
- eTIV
- nWBV
- ASF
- MR Delay
- Gender     
These tests are available online and can be taken by anyone .
