# Day 1

[Ollama](https://ollama.com) is an open-source framework designed to run Large Language Models (LLMs) locally on your own hardware (macOS, Windows, or Linux) with minimal setup. In the context of Ed Donner’s AI Engineer Core Track, Ollama serves as the bridge between theoretical "Frontier" models (like GPT-4) and practical, cost-effective engineering using open-source models like Llama 3, Mistral, and Phi-3

![](images/1.png)

Now to download model from computer: `ollama run model_name`. 

![](images/2.png)

Its a small model and can kepp expectations low.

`ctrl + d` to exit gemma3.

Running: `ollama run gemma:e2b`.  

Gemma 4 models are designed to deliver frontier-level performance at each size. They are well-suited for reasoning, agentic workflows, coding, and multimodal understanding.


## 🚀 AI Engineer Core Track: 8-Week Syllabus

* **Week 1: Foundations & First Projects**
    * Transformer fundamentals and the "Attention" mechanism.
    * Setting up your environment with **uv** and **VS Code**.
    * **Project:** A business GenAI product that scrapes the web and generates sales brochures.
* **Week 2: Frontier APIs & Multimodal Bots**
    * Deep dive into OpenAI, Claude, and Gemini APIs.
    * Function calling and tool-use basics.
    * **Project:** A multimodal customer support agent (Text, Audio, Images) with a Gradio UI.
* **Week 3: Open-Source Models & Hugging Face**
    * Moving beyond closed APIs to local models using **Ollama** and **Hugging Face**.
    * Using Google Colab for free GPU access.
    * **Project:** An automated "Meeting Minutes" generator from audio recordings.
* **Week 4: LLM Selection & Code Generation**
    * Evaluating model performance and tokenization costs.
    * **Project:** An AI Programmer that translates Python to high-performance C++.
* **Week 5: Retrieval-Augmented Generation (RAG)**
    * Mastering Vector Embeddings and Vector Databases (**ChromaDB/FAISS**).
    * Chunking strategies and semantic search.
    * **Project:** An "AI Knowledge Worker" that chats with your private company documents.
* **Week 6: Transitioning to Training**
    * Moving from inference (using models) to training (improving models).
    * Fine-tuning a Frontier model (like GPT-4o-mini) for specific business logic.
* **Week 7: Advanced Training (QLoRA)**
    * Deep dive into PEFT (Parameter-Efficient Fine-Tuning) and **QLoRA**.
    * Training open-source models (like Llama 3) on specialized datasets.
* **Week 8: Deployment & Autonomous Agents**
    * The "Grand Finale": Combining everything into a production-ready app.
    * **Project:** An autonomous Agentic system that collaborates to solve complex commercial problems.

---

### ⚠️ Windows-Specific Heads Up
As you start Week 1, keep these PowerShell translations handy for the setup:

* **Environment Setup:** When Ed says `source .venv/bin/activate`, you type:
    `.\.venv\Scripts\activate`
* **Running the Code:** Always use `python` instead of `python3`.
* **Local Models:** If you use **Ollama** locally, remember that Windows might require you to run PowerShell as **Administrator** the first time you serve a model.

---


## Why are we using `uv`?

In Ed’s courses, **`uv`** is the backbone of the workflow. Developed by Astral, it is an extremely fast Python package installer and resolver, written in Rust. It is designed to replace `pip`, `pip-tools`, and `virtualenv`.

Here is the breakdown of why it’s being used:

1.  **Speed:** It is often 10–100x faster than `pip`. When you're installing heavy AI libraries like `torch` or `anthropic`, this saves a massive amount of time.
2.  **Project Isolation:** It manages virtual environments automatically. Instead of manually creating and managing folders, `uv` ensures that the dependencies for one project don't break another.
3.  **Reproducibility:** It uses a `uv.lock` file. This ensures that the exact versions of the libraries Ed uses on his Mac are the ones installed on your Windows machine, preventing the dreaded "It worked on his machine but not mine" syndrome.
4.  **Single Tool:** It handles Python version management. If a project needs Python 3.12 but you only have 3.10, `uv` can fetch the correct version for you without you needing to go to python.org.

---

### Step-by-Step: Installing and Using `uv` on Windows

Since you are on Windows 11 using PowerShell, follow these steps to get aligned with the course:

#### 1. Installation
Open your PowerShell terminal (Shift + Right Click in your project folder > "Open PowerShell window here") and run:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 2. Initializing a Project
When Ed starts a new project, he might run `uv init`. On Windows, this creates the same structure:
```powershell
uv init
```

#### 3. Managing the Environment (The "Windows Translation")
This is where the Mac and Windows paths diverge. Pay close attention to these differences:

* **To create/sync the environment:**
    ```powershell
    uv sync
    ```
* **To activate the environment:**
    Ed will say: `source .venv/bin/activate`
    **You must type:**
    ```powershell
    .\.venv\Scripts\activate
    ```
    *(Note: If you get a "Scripts cannot be executed" error, run PowerShell as Administrator and type `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*.

#### 4. Setting Environment Variables
If Ed tells you to set an API key in the terminal:
Ed's Mac command: `export ANTHROPIC_API_KEY="your-key"`
**Your Windows command:**
```powershell
$env:ANTHROPIC_API_KEY="your-key"
```

---

### Pro Tip for VS Code Users
Once you run `uv sync`, a `.venv` folder will appear in your file explorer. To make sure VS Code uses the correct "Brain":
1.  Press `Ctrl + Shift + P`.
2.  Type **"Python: Select Interpreter"**.
3.  Choose the one that points to your project folder: `.\.venv\Scripts\python.exe`.

If you run into any "ModuleNotFound" errors, it’s almost always because VS Code is looking at your global Python instead of the `uv` environment!


---

Nice work on getting your API key ready! Since Ed's course typically uses OpenAI, switching to Gemini on Windows requires a few adjustments to the environment setup and the library code.

Here is your step-by-step guide to getting Gemini running in your Windows/VS Code environment.

---

### 1. Install the Google Generative AI Library
In your VS Code terminal (PowerShell), use `uv` to install the official Google SDK.

```powershell
uv add google-generativeai
```

---

### 2. Set Your API Key (The Windows Way)
Instead of Ed's `export` command, you need to use the PowerShell syntax.

**For the current session (Quick Test):**
Run this in your terminal (replace `your_key_here` with your actual key):
```powershell
$env:GOOGLE_API_KEY="your_key_here"
```

**For long-term use (Persistent):**
Ed often uses a `.env` file. Create a file named `.env` in your project root and add:
```text
GOOGLE_API_KEY=your_key_here
```
> **Windows Tip:** In File Explorer, files starting with a dot might be hidden. VS Code will always show them in the sidebar.

---

### 3. The Code Translation (OpenAI vs. Gemini)
Here is how you "translate" Ed's standard OpenAI boilerplate into Gemini code.

**Ed's typical OpenAI code:**
```python
# Don't use this for Gemini
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(...)
```

**Your new Gemini code (`test_gemini.py`):**
```python
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the environment variable from your .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Configure the library
genai.configure(api_key=api_key)

# 3. Initialize the model (Gemini 2.5 Flash is great for testing)
model = genai.GenerativeModel('gemini-2.5-flash')

# 4. Generate a response
response = model.generate_content("Give me a quick 'Hello World' from Gemini!")

print(response.text)
```

---

### 4. How to Test If It's Working
To verify everything is wired up correctly:

1.  **Check Environment:** Type `$env:GOOGLE_API_KEY` in your PowerShell. It should print your key.
2.  **Select Interpreter:** In VS Code, press `Ctrl+Shift+P`, type **"Python: Select Interpreter"**, and ensure it points to your `.venv` created by `uv`.
3.  **Run the Script:**
    ```powershell
    uv run python test_gemini.py
    ```

### Troubleshooting Windows-Specific Hurdles
* **ModuleNotFoundError:** If Python says it can't find `google.generativeai`, run `uv sync` to ensure your virtual environment is up to date.
* **Permission Errors:** If you get a "Scripts cannot be loaded" error when activating a virtual environment, run this once as Administrator: 
    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

If you want to see exactly which models your API key has access to (to avoid 404s error in the future), you can run this quick snippet in a new file called `list_models.py`:

```
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available models that support text generation:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
```

