# 🍎 Apple RAG Assistant

A simple **Retrieval-Augmented Generation (RAG)** project that uses a local knowledge base and Google's Gemini API to answer questions about Apple products.

This project is designed as a beginner-friendly introduction to understanding how a basic RAG system works **without using embeddings, vector databases, or NLP libraries**.

---

## 📌 Project Overview

The Apple RAG Assistant allows users to ask questions about Apple products and retailer-related information.

Instead of sending the user's question directly to an AI model, the application first searches a local knowledge base (`data.txt`) for relevant information.

The retrieved information is then provided to Gemini as context.

### Basic Architecture

```text
                 User Question
                       │
                       ▼
              Simple Retrieval
                       │
                       ▼
             Search Knowledge Base
                       │
                       ▼
              Rank Matching Lines
                       │
                       ▼
              Relevant Information
                       │
                       ▼
                Build RAG Prompt
                       │
                       ▼
              Google Gemini API
                       │
                       ▼
             Streaming AI Response
                       │
                       ▼
                     User
```

---

# ✨ Features

* 🍎 Apple product-focused AI assistant
* 📄 Uses a local `.txt` knowledge base
* 🔎 Keyword-based information retrieval
* 🧠 Context-aware prompting
* 🚫 No embeddings
* 🚫 No vector database
* 🚫 No NLP libraries
* ⚡ Streaming Gemini responses
* 🔐 API key stored securely using `.env`
* 🔄 Automatic retry for temporary Gemini server errors
* 💬 Interactive command-line chat
* 🛑 `exit` command to close the application

---

# 🛠️ Technologies Used

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Core programming language |
| Google Gemini API | AI response generation    |
| `google-genai`    | Gemini Python SDK         |
| `python-dotenv`   | Load API key from `.env`  |
| TXT file          | Knowledge base            |
| Keyword Matching  | Basic retrieval mechanism |

---

# 📂 Project Structure

```text
RAG_P1/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── Complete_knowlade_base/
│   └── data.txt
│
└── PyCode/
    └── main.py
```

---

# ⚙️ How the System Works

The project follows a simple RAG pipeline:

```text
Question
   ↓
Retrieve
   ↓
Augment
   ↓
Generate
```

## 1. User asks a question

For example:

```text
You: What is the return policy for iPhone?
```

---

## 2. Retrieve relevant information

The program reads:

```text
Complete_knowlade_base/data.txt
```

It compares words from the user's question with each line in the knowledge base.

For example:

```text
Question:
What is the return policy for iPhone?

Knowledge Base:
iPhone products can be returned within 14 days.
```

Matching words such as:

```text
return
iPhone
```

increase the relevance score of that line.

---

## 3. Select relevant information

The system ranks matching lines according to the number of matching words.

Example:

```text
Line 1 → Score: 3
Line 2 → Score: 1
Line 3 → Score: 2
Line 4 → Score: 0
```

The highest-ranking lines are selected as context.

---

## 4. Augment the prompt

The retrieved information is inserted into the Gemini prompt:

```text
KNOWLEDGE BASE:

iPhone products can be returned within 14 days.

USER QUESTION:

What is the return policy for iPhone?
```

The prompt also instructs Gemini not to invent information.

---

## 5. Generate the answer

Gemini receives the question and retrieved context.

The response is streamed to the terminal as it is generated.

Example:

```text
AI: iPhone products can be returned within 14 days according
to the provided retailer policy.
```

---

# 🧠 Why This Is RAG

RAG stands for:

> **Retrieval-Augmented Generation**

The project performs both major parts:

### Retrieval

```text
data.txt
   ↓
Search
   ↓
Relevant information
```

### Generation

```text
Relevant information
       +
User question
       ↓
Gemini
       ↓
Answer
```

Therefore:

```text
Retrieval + Generation = RAG
```

---

# 🔎 Retrieval Method

This project intentionally uses a simple retrieval mechanism.

It does **not** use:

* ❌ Embeddings
* ❌ Vector databases
* ❌ Semantic search
* ❌ Transformers for retrieval
* ❌ NLP libraries

Instead, it uses Python string processing.

Conceptually:

```python
question_words
       ↓
compare with knowledge-base lines
       ↓
count matching words
       ↓
calculate score
       ↓
sort by score
       ↓
select top results
```

This makes the project easier to understand before moving to advanced RAG techniques.

---

# 🤖 Gemini Integration

The application uses Google's Gemini API.

The Gemini client is initialized using the API key stored in `.env`.

```python
client = genai.Client(
    api_key=API_KEY
)
```

The application uses streaming generation:

```python
response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=prompt
)
```

The response is then displayed chunk by chunk:

```python
for chunk in response:

    if chunk.text:

        print(
            chunk.text,
            end="",
            flush=True
        )
```

This makes the application feel more like a real-time AI assistant.

---

# 🔐 Environment Variables

Create a `.env` file in the root project directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The application loads it using:

```python
from dotenv import load_dotenv

load_dotenv()
```

Then:

```python
API_KEY = os.getenv("GEMINI_API_KEY")
```

### ⚠️ Important

Never upload your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/y-ash2103/Simple_RAG_Without_NLP
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

You should see:

```text
(.venv)
```

in your terminal.

---

## 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

## 4. Configure the API key

Create:

```text
.env
```

and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

# ▶️ Running the Project

Move into the Python directory:

```powershell
cd PyCode
```

Run:

```powershell
python main.py
```

You should see:

```text
============================================================
              APPLE AI ASSISTANT
============================================================

Ask questions about Apple products.
Type 'exit' to close the program.

You:
```

Now enter a question:

```text
You: What is the return policy for iPhone?
```

The AI will retrieve relevant information and generate an answer.

To stop the application:

```text
You: exit
```

---

# 📄 Knowledge Base

The knowledge base is stored in:

```text
Complete_knowlade_base/data.txt
```

You can add information such as:

```text
Product information

iPhone 17 is available with different storage options.

Return policy

Eligible iPhone products can be returned within 14 days.

Warranty

Eligible Apple products are covered according to the
retailer's warranty policy.

Pricing

Product prices are listed in the retailer's current
knowledge base.
```

The AI can only answer based on the information retrieved from this file.

---

# 🛡️ Hallucination Control

The prompt explicitly instructs Gemini:

```text
Answer ONLY using information from the knowledge base.

Do not make assumptions or invent information.
```

If the retrieved information doesn't contain the answer, the application instructs the model to say that the information isn't available.

This provides a basic grounding mechanism.

> Note: Prompt instructions cannot guarantee that an LLM will never hallucinate. The system is designed to reduce unsupported answers by restricting the model's context.

---

# 🔄 Error Handling

The application handles temporary Gemini server errors.

For example:

```text
503 UNAVAILABLE
```

If Gemini is temporarily overloaded, the application retries the request.

The retry pattern is approximately:

```text
Request
   ↓
503
   ↓
Wait 1 second
   ↓
Retry
   ↓
503
   ↓
Wait 2 seconds
   ↓
Retry
```

If the service remains unavailable, the program displays a friendly error instead of crashing.

---

# 📋 Requirements

The project currently requires:

```text
google-genai
python-dotenv
```

Install them using:

```powershell
python -m pip install -r requirements.txt
```

---

# 🚧 Current Limitations

This is a beginner-level RAG implementation.

### 1. Keyword-based retrieval

The system relies on word matching.

For example:

```text
"What is the return policy?"
```

may not retrieve:

```text
"Customers may receive their money back within 14 days."
```

if the important words don't overlap.

---

### 2. No semantic search

The system does not understand that:

```text
return
```

and:

```text
refund
```

may have related meanings.

---

### 3. No embeddings

The project does not convert text into numerical vectors.

---

### 4. No vector database

There is currently no:

* FAISS
* Chroma
* Pinecone
* Weaviate
* Qdrant

---

### 5. Small knowledge base

The current approach is better suited for a small text file.

Large knowledge bases would require a more scalable retrieval method.

---

# 🚀 Future Improvements

This project can be developed step by step.

## Version 1 — Current

```text
TXT
 ↓
Keyword Matching
 ↓
Gemini
```

## Version 2

Add better text preprocessing:

```text
TXT
 ↓
TF-IDF
 ↓
Similarity Search
 ↓
Gemini
```

## Version 3

Add embeddings:

```text
Documents
 ↓
Chunks
 ↓
Embeddings
 ↓
Vector Search
 ↓
Relevant Context
 ↓
Gemini
```

## Version 4

Add a vector database:

```text
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
Gemini
```

## Version 5 — Advanced RAG

```text
          Documents
              ↓
           Chunking
              ↓
          Embeddings
              ↓
        Vector Database
              ↓
        Semantic Search
              ↓
       Re-ranking / Filter
              ↓
        Context Selection
              ↓
          LLM / Gemini
              ↓
       Streaming Response
```

---

# 🎯 Learning Objectives

This project helps understand:

* What RAG is
* Retrieval vs generation
* Knowledge-base retrieval
* Prompt augmentation
* Grounded generation
* LLM API integration
* Streaming responses
* Environment variables
* API key security
* Basic ranking/relevance
* Error handling
* Virtual environments
* Project structure

---

# 📚 RAG Concepts Demonstrated

| Concept              | Implemented |
| -------------------- | ----------- |
| Knowledge Base       | ✅           |
| Retrieval            | ✅           |
| Context Augmentation | ✅           |
| LLM Generation       | ✅           |
| Streaming            | ✅           |
| Prompt Grounding     | ✅           |
| Embeddings           | ❌           |
| Vector Database      | ❌           |
| Semantic Search      | ❌           |
| NLP                  | ❌           |
| Reranking            | ❌           |

---

# 💡 Example Questions

You can ask questions such as:

```text
What is the return policy?

Which iPhone has the largest storage?

What is the warranty period?

What products are available?

How much does the iPhone cost?

What are the available iPhone models?
```

The exact answers depend on the information available in:

```text
Complete_knowlade_base/data.txt
```

---

# 👨‍💻 Author

**Yash**

This project was created as a learning project to understand the fundamentals of **RAG, LLM integration, information retrieval, and Generative AI** using Python.

---

# ⭐ Future Goal

The ultimate goal of this project is to evolve from a simple keyword-based RAG system into a production-style semantic RAG application using:

```text
NLP
   ↓
TF-IDF
   ↓
Embeddings
   ↓
Vector Database
   ↓
Semantic Retrieval
   ↓
Reranking
   ↓
Gemini
   ↓
Production RAG Application
```

---


