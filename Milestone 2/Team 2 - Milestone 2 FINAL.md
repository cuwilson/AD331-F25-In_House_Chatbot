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
Explain the rationale for each chosen technology.

---

## 5. Refined Requirements List
> _Anything in **bold italics** was added or edited from the list provided in Milestone 1._

- Natural language processing for policy-related queries **_with at least 90% accuracy in intent recognition based on internal testing_**
- Access and retrieve relevant sections from HR documents (PDFs, SharePoint) **_within 3 seconds for typical queries_**
- Track unanswered questions and route them to HR for review **_within 24 business hours_**
- **_Responses related to HR policies, pay, or benefits must be accompanied by a citation or link to the exact policy section used to generate the answer_**
