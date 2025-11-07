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
Explain how each system part functions (frontend, backend, model, storage, authentication)


---

## 3. Security and Data Protection Plan
Outline measures for authentication, access control, encryption, and restricted data handling


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

---

## 5. Refined Requirements List
> _Anything in **bold italics** was added or edited from the list provided in Milestone 1._

- Natural language processing for policy-related queries **_with at least 90% accuracy in intent recognition based on internal testing_**
- Access and retrieve relevant sections from HR documents (PDFs, SharePoint) **_within 3 seconds for typical queries_**
- Track unanswered questions and route them to HR for review **_within 24 business hours_**
- **_Responses related to HR policies, pay, or benefits must be accompanied by a citation or link to the exact policy section used to generate the answer_**
