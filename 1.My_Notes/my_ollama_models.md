
# 🧠 Local Ollama Models Roster & Developer Reference



| Model | Creator | Role |
| :--- | :--- | :--- |
| **1. deepseek-r1:8b** | DeepSeek AI | Reasoning Agent |
| **2. nomic-embed-text** | Nomic AI | Vector Embedding |
| **3. llama3.2:3b** | Meta AI | Fast General |
| **4. qwen2.5-coder:7b** | Alibaba Qwen | Code Specialist |

---

### 1. `deepseek-r1:8b` (Size: 5.2 GB) 

* **Created By:** **DeepSeek AI** (China-based AI research lab). *(Note: The `8b` version is distilled using Meta's Llama 3.1 8B architecture and fine-tuned on DeepSeek-R1's reasoning data).*
* **What it’s good for:**
* Complex logic, step-by-step math, algorithm design, and structured problem-solving.
* It emits internal `<think> ... </think>` chains before returning an answer, giving it self-reflection and self-correction capabilities.


* **When to use it:**
* **Ed Donner's Agentic Track:** Perfect for building AI agents that need to plan multi-step workflows, perform tool routing decisions, or critique their own outputs.



---

### 2. `nomic-embed-text:latest` (Size: 274 MB) 

* **Created By:** **Nomic AI** (An open-source AI lab known for data visualization and reproducible embeddings).
* **What it’s good for:**
* Converting raw text chunks into high-dimensional numerical vectors (dense embeddings).
* It supports long context windows (up to 8,192 tokens).


* **When to use it:**
* **Ed Donner's Core Track (RAG Modules):** Used strictly inside vector databases (e.g., ChromaDB, FAISS) for indexing PDF documents, codebase documentation, or knowledge bases.
* *Note:* You do **not** run this model like a chat model (`ollama run`). Python calls its API directly to turn text strings into arrays of floating-point numbers.



---

### 3. `llama3.2:3b` (Size: 2.0 GB) 

* **Created By:** **Meta AI** (Facebook/Instagram parent company).
* **What it’s good for:**
* Ultra-fast text completion, classification, summary generation, and simple function calling.
* Extremely low memory footprint and negligible latency.


* **When to use it:**
* Everyday quick prototyping, rapid unit testing of your Python LLM wrappers, or light text transformation tasks where you need high throughput and instantaneous responses.



---

### 4. `qwen2.5-coder:7b` (Size: 4.7 GB) 

* **Created By:** **Alibaba Cloud / Qwen Team** (Alibaba's open-source AI unit).
* **What it’s good for:**
* Dedicated Python/JavaScript/SQL code generation, code refactoring, inline comments, bug fixing, and unit test generation.


* **When to use it:**
* Local pair-programming assistant, running code-generation benchmark scripts, or feeding code-review prompts without sending private code to external cloud APIs.



---

### 🎓 AI Engineer Interview-Style Reflection

> **Interview Question:** Suppose you are building a local **Retrieval-Augmented Generation (RAG)** pipeline in Python using `uv`. A user asks a question about a company policy contained within a 100-page PDF document. Which models from your stack handle each stage of the pipeline?

1. **Ingestion & Indexing Phase:** Use **`nomic-embed-text`** .
* The PDF is split into text chunks. `nomic-embed-text` converts each chunk into a vector embedding and saves them into ChromaDB.


2. **Retrieval Phase:** Use **`nomic-embed-text`** again .
* Converts the user's incoming query into a query vector (`search_query` mode) to perform cosine similarity search against ChromaDB.


3. **Reasoning / Generation Phase:** Pass the retrieved context + prompt to **`deepseek-r1:8b`** or **`llama3.2:3b`** .
* `deepseek-r1:8b` analyzes the retrieved context, verifies whether the answer is present, and streams back the synthesized response.



---