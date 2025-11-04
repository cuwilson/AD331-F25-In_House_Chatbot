**1\. Company Overview**

**Company Name**: _Muffin Maniacs_  
**Industry**: Smaller baking kitchens with small storefront for pickup and in person ordering. Majority of orders are placed online through the website or email.

**Overview**: The Muffin Maniacs is a modern-day bakery with a focus on consistent yet wild flavored muffins that are an easy catering choice for all levels of events from company outings all the way to weddings.

**Industry Context**: Muffin Maniacs is a small chain on the west coast known for its muffins and always a pleasure to see at all levels of events. With that there is only a certain number of muffins that can be sold daily and have a limit of same day orders that can be handled and will go over ordering capacity. With more kitchen only based locations opening and in the works the goal is to have store front only filling order locations and the ghost styled bakeries will be for larger preset orders and filling shelves of local stores. The largest threat of Maniac Muffins is the Cupcakes Holics trying to take business away.

**2\. Problem Statement**

_Muffin Maniacs_ HR team is not always available during the hours all employees work, leaving many, especially overnight workers, without access to immediate answers. This creates several compounding issues:

- **Delayed Information:** Employees have simple but urgent questions about topics like PTO balances, parental leave qualifications, and benefits of enrollment. Waiting for an HR response delays their decision-making.
- **HR Backlog:** The HR team is inundated with high-volume, repetitive questions. This consumes valuable time that could be dedicated to more complex, strategic issues like talent acquisition, employee relations, and compliance reporting.
- **Lost Productivity:** Employees waste significant time trying to find (and verify) up-to-date policy documents, which are often scattered across internal drives and wikis.
- **Critical Security Risk:** Frustrated by the delays, employees are increasingly turning to public AI tools to ask sensitive questions. They might paste in excerpts from a benefits document or describe a specific personal scenario, leading to the inadvertent leakage of confidential company policy and employee data, creating a massive compliance and privacy risk.

**The proposed solution**: An internal secure, in-house HR chatbot - **Muffin Mate -** that enables employees to easily ask questions and get real-time, accurate answers based on the latest company policies. This system will be available 24/7 and will be directly and securely connected to the company's internal, canonical HR knowledge base (employee handbooks, policy documents, benefits guides). This ensures that no sensitive HR data ever leaves the company's network, providing all employees with instant, trustworthy answers and freeing the HR team to focus on high-impact work.

**3\. Stakeholders and Intended Users**

**Stakeholders:**

- **Company Owners/Execs** - want efficient operations and consistent HR practices across locations
- **HR Department** - Primary owners of the policy content and beneficiaries of reduced workload. Ensures policies are communicated clearly and consistently and responses align with labor laws and privacy regulations
- **IT Department** - Responsible for chatbot implementation, integration with internal systems, and maintaining security
- **Store Managers/Site Supervisors** - Need access to HR policies for team management, scheduling and compliance
- **Employees** - End-users who interact with the chatbot daily.
- **Training Team** - provides up-to-date HR resources and onboarding materials (if separate team from HR)

**Intended Users and Use Case Examples:**

- **Employees** for quick HR answers and self-service
  - "How many vacation days do I get in my first year?"
  - "When will I get my next paycheck?"
- **Managers** for staff oversight
  - "How do I report an employee's absence?"
  - "How do I submit a promotion request for my team member?"
- **HR Staff/Training Team** for policy updates and analytics
  - "Show me the most common employee questions this month"

**4\. Functional and Non-Functional Requirements**

**Functional Requirements**

- Natural language processing for policy-related queries
- Access to and retrieval of relevant sections from HR documents (PDFs, SharePoint)
- Track unanswered questions and route them to HR for further review
- Support file downloads (e.g., benefits guides, forms, paystubs)
- Push reminders for policy changes or payroll updates

**Non-Functional Requirements**

- **Performance:** responses should appear within a few seconds for typical queries
- **Accessibility/****Usability:** complies with accessibility standards for employees with disabilities while having an easy-to-use interface that supports text-based interaction
- **Maintainability:** HR and IT should be able to update policies and FAQs without full redeployment
- **Scalability**: Able to serve concurrent users across multiple locations without performance issues.
- **Language Support**: Optional multilingual support for ESL employees.
- **Logging**: Maintain interaction logs for review and auditing purposes while respecting employee privacy.

**Data Privacy and Compliance Requirements**

- **Data Protection & Compliance**: All employee data must be encrypted and must comply with applicable local labor data laws
- **Access Control**: Role-based access ensures employees only see their own data, unless they are in a position that must have the appropriate permissions to view other employees' data, like HR staff or Managers
- **Data Retention and Transparency**: users should be informed that interactions are logged for HR support, policy compliance, and that they follow the company's data retention schedule

**5\. Research Summary: Self-Hosted/Open-Source LLMs**

**5.1. Ollama: Self-Hosting Platform - Deployment Tool**

It's important to first distinguish the model (the "brain") from the tool that runs it. Ollama is not an LLM itself; rather, it is an essential open-source platform that makes it incredibly simple to download, set up, and run open-source LLMs like Llama 3 and Mistral on a company's own hardware. It bundles the model weights, configuration, and server into a single, easy-to-manage package. For Muffin Maniacs' IT team, using Ollama would dramatically reduce the engineering effort required to get the internal chatbot system up and running.

**Key Technology:** Retrieval-Augmented Generation (RAG)

The technical approach described in the solution, connecting a chatbot to a "canonical HR knowledge base", is known as Retrieval-Augmented Generation (RAG). This method is critical for our project and directly addresses the problems of accuracy and security.

**How it Works:** Instead of relying on its general pre-trained knowledge, the chatbot first retrieves relevant, up-to-date documents (like the "PTO policy" or "benefits guides") from our internal knowledge base. Then, it augments the user's question with this information and passes it to the language model. The model's job is simply to generate an answer based only on the specific documents provided.

**Why it's the Solution:**

- **Stops Hallucinations:** The bot answers using Muffin Maniacs' actual data, not generic internet knowledge. This directly solves Problem #3 by providing trustworthy, verifiable answers.
- **Always Up to Date:** When HR updates a policy, the RAG system has access to it immediately. The LLM itself does not need to be retrained.
- **Secure:** All sensitive documents and employee queries remain within the company's network, solving Problem #4.

Both Llama 3 and Mistral are excellent choices to be the "brain" (the generator) for a RAG system.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAMAAAAAenpMAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAGUExURQAAAAAAAKVnuc8AAAACdFJOU/8A5bcwSgAAAAlwSFlzAAAOwwAADsMBx2+oZAAAABJJREFUOE9jYBgFo2AUjILhCwAE5AABUbILhAAAAABJRU5ErkJggg==)

**5.2. Llama 3: Open-Source LLM "Brain"**

Just as Ollama serves as the "engine" that runs the chatbot, Llama 3 is the "brain" that powers it. Developed by Meta, Llama 3 represents the latest generation of open-source large language models (LLMs) and delivers top-tier performance for a fraction of the cost of proprietary alternatives. It's designed to be efficient, flexible, and ideal for companies that want advanced AI capabilities without relying on external cloud providers.

**Key Technology: Llama 3 8B Model**  
It strikes the perfect balance between speed, accuracy, and hardware efficiency-making it powerful enough for HR question-answering while still feasible to host on in-house infrastructure.

**How It Works:**  
When paired with Ollama, Llama 3 takes the relevant documents retrieved by the RAG system and generates answers directly from that information. The model doesn't need to "know" everything in advance; it simply interprets the provided context and produces clear, accurate responses in real time.

**Why It's the Solution:**

- **High Performance:** Llama 3 delivers state-of-the-art results across reasoning, summarization, and question-answering tasks. Despite its relatively small size, the 8B model outperforms older models many times larger.
- **Efficient and Scalable:** Its 128K-token context window allows it to handle longer documents and complex prompts efficiently, making it perfect for HR content.
- **Hardware Friendly:** The 8B model runs smoothly on consumer- or prosumer-grade GPUs. This means Muffin Maniacs' IT team can deploy it on existing hardware or a single new server-no need for expensive cloud resources.
- **Cost-Effective:** The model provides the best ratio of performance to cost, ensuring a fast, reliable chatbot without overspending on compute power.

**Summary:**  
Llama 3 provides the intelligence that drives Muffin Mate's responses, while Ollama ensures it's secure and easy to deploy. Together, they form a modern, self-contained AI stack.

**6\. Rationale for a Secure, In-House Chatbot**

- **Confidentiality**: Employees may ask sensitive questions (e.g., related to medical leave, harassment policies). Keeping data in-house ensures confidentiality. Learning what are the most common questions asked to see what are the most relevant information that may need to be focused on during onboarding.
- **Customization**: Public models lack awareness of company-specific policies and lingo. We can keep the information delivery simple and give more document-based answers so there is less likely to be room for errors based on perception.
- **Control**: Internal deployment enables updates to the policy database as soon as documents change.
- **Compliance**: Avoid risks tied to sending data to external APIs or public clouds. No data can then be used and manipulated by competitors to use against us. All sensitive data then could stay contained avoiding lawsuits and leaks.