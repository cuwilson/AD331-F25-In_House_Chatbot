# Milestone 2 – Deliverables Breakdown

## 1. Detailed System Architecture Diagram
Show the data flow between components: **input → model → response → storage**.

---

## 2. Component Descriptions
The employee will begin at a computer and loggin to the device which will take it into the authentication process if the loggin is bad it will send the user back to the login screen. If the loggin is succcessful the user will arrive on the input/question screen. After the question is entered it will go into the LLM Ollama RAG Model going through the process. This process includes going through the model, going through the document retrival, and finally through the verifier to send out going out the server storage of the question and answer for later usage and dirrectly to the user displaying the anser and links to the documentation whjere it came from. If the user is happy from the response and all needs satisfied then teh user closes the screen and logs out. If the user is not satisfied additional information is sent to storage, HR is notified of the information disconnect, and the user is taken back to the question screen to repeat the cycle.


---

## 3. Security and Data Protection Plan
One of the security measures being taken is an enforced passowrd policy that will keep unwanted access out of the devices and accounts. All data and LLM's are being hosted in internal company servers so all the data and movement will be secured. The AI model will have no access to external information outside of the data given to it so it can not pull data from any internet sources just approved ones. Periodic access reviews will be taken to make sure all devices and accounts are secured.


---

## 4. Technology and Tool Justification
Using an internal LLM on our hosting machines will allow for minimal external issues and outside corruption. Ollama is being chosen for its simple and low integration costs with effective results for this case scenario. We are utulizing Azure loggin for verification of sign in to minimize the need for extra usernames and passwords and each user will be able to loggin to the system with there assigned microsoft email loggin. This will also allow for easier tracking and audits in the future within Azure. Azure will also be what we use for the alerting system if there is an issue with an answer that the LLM is giving for alerting HR.

---

## 5. Refined Requirements List
> _Anything in **bold italics** was added or edited from the list provided in Milestone 1._

- Natural language processing for policy-related queries **_with at least 90% accuracy in intent recognition based on internal testing_**
- Access and retrieve relevant sections from HR documents (PDFs, SharePoint) **_within 3 seconds for typical queries_**
- Track unanswered questions and route them to HR for review **_within 24 business hours_**
- **_Responses related to HR policies, pay, or benefits must be accompanied by a citation or link to the exact policy section used to generate the answer_**
