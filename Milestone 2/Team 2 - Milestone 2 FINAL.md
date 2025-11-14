# Milestone 2 – Deliverables Breakdown

## 1. Detailed System Architecture Diagram
Show the data flow between components: **input → model → response → storage**.

Data Flow
Frontend Chat Interface → 
Backend/API Gateway →
RAG System →
Backend/API Gateway →
    Frontend Chat Interface
    AND
    Encrypted Log Storage/Analytics DB
- Input: Empoloyee or Manger login
- Backend/API Gateway (Processing): receives user query and verifies access level. Passes query to RAG pipeline
- RAG System: has three subcomponents
    1. Document Retriever/Vector Database
    - searches internal HR knowledge base
    - returns top matching text blocks
    2. LLM Model Server
    - Takes retrieve passages and user query to generate a verified answer
    - provides a reference or citation to the document source
    3. Response Verifier
    - checks generated response is based on the document snippet
    - rejects or flags answers without a valid source
- Backend/API Gateway (Output and Logging): logs the interation for auditing and analytics and sends verified resonse back to the user interface
- Response display (Output): what the user sees
---

## 2. Component Descriptions
The employee will begin at a computer and loggin to the device which will take it into the authentication process if the loggin is bad it will send the user back to the login screen. If the loggin is succcessful the user will arrive on the input/question screen. After the question is entered it will go into the LLM Ollama RAG Model going through the process. This process includes going through the model, going through the document retrival, and finally through the verifier to send out going out the server storage of the question and answer for later usage and dirrectly to the user displaying the anser and links to the documentation whjere it came from. If the user is happy from the response and all needs satisfied then teh user closes the screen and logs out. If the user is not satisfied additional information is sent to storage, HR is notified of the information disconnect, and the user is taken back to the question screen to repeat the cycle.


---

## 3. Security and Data Protection Plan
One of the security measures being taken is an enforced passowrd policy that will keep unwanted access out of the devices and accounts. All data and LLM's are being hosted in internal company servers so all the data and movement will be secured. The AI model will have no access to external information outside of the data given to it so it can not pull data from any internet sources just approved ones. Periodic access reviews will be taken to make sure all devices and accounts are secured.


---

## 4. Technology and Tool Justification
# If you see this, please edit this section for accuracy
Each tool and technology in the Muffin Mate system was selected to balance security, scalability, and accuracy while maintaining ease of use for HR and employees. The flowchart demonstrates how the system integrates these technologies through a secure and efficient data flow --- from employee login to verified response output.

**- Ollama (Model Hosting Platform)**\
Ollama serves as the local model deployment tool that allows the LLM (Llama 3) to run entirely on Muffin Maniacs' in-house servers. This ensures data never leaves the internal network, aligning with our data protection and compliance requirements. It simplifies model updates, reduces cloud costs, and provides full control over uptime and resource allocation.

**- Llama 3 (LLM Model Server)**\
Llama 3, hosted within Ollama, is the "brain" of the chatbot. It interprets employee questions and produces clear, context-based responses using HR policy data retrieved by the RAG system. Its 8B parameter model provides a mix of accuracy, efficiency, and performance which is capable of handling real-time HR queries without requiring high-end cloud infrastructure.

**- Retrieval-Augmented Generation (RAG) Pipeline**\
The RAG system ensures that answers are based on company-verified HR documents. The pipeline includes:

-   **Document Retriever / Vector Database:** Searches internal HR databases for relevant text.

-   **Response Verifier:** Confirms that each generated response is grounded in an authorized policy source before returning it to the user.\
    This design minimizes hallucinations and provides traceable, cited responses for compliance and trust.

**- API Gateway**\
The API Gateway acts as the central controller for user authentication, query routing, and access control. It verifies employee or manager credentials before passing requests to the RAG system. It also handles logging and analytics, ensuring that each query is securely stored and reviewable for HR insights.

**- Authentication Service**\
Integrated with existing employee credentials, the authentication service ensures only authorized users can access the system. Failed logins or unauthorized access attempts are handled at this stage, keeping sensitive HR data protected.

**- Encrypted Log Storage / Analytics Database**\
All interactions are encrypted and stored for auditing and continuous improvement. Analytics derived from these logs help HR identify common questions or unclear policy areas, which can inform updates to the employee handbook.

**- Frontend Chat Interface**\
The user-facing interface allows employees to interact naturally with the HR system. It displays verified responses, including policy references, and supports follow-up questions. 

**This is the addition that was put on main, needs to be combined with above info**
Using an internal LLM on our hosting machines will allow for minimal external issues and outside corruption. Ollama is being chosen for its simple and low integration costs with effective results for this case scenario. We are utulizing Azure loggin for verification of sign in to minimize the need for extra usernames and passwords and each user will be able to loggin to the system with there assigned microsoft email loggin. This will also allow for easier tracking and audits in the future within Azure. Azure will also be what we use for the alerting system if there is an issue with an answer that the LLM is giving for alerting HR.

---

## 5. Refined Requirements List
> _Anything in **bold italics** was added or edited from the list provided in Milestone 1._

- Natural language processing for policy-related queries **_with at least 90% accuracy in intent recognition based on internal testing_**
- Access and retrieve relevant sections from HR documents (PDFs, SharePoint) **_within 3 seconds for typical queries_**
- Track unanswered questions and route them to HR for review **_within 24 business hours_**
- **_Responses related to HR policies, pay, or benefits must be accompanied by a citation or link to the exact policy section used to generate the answer_**
