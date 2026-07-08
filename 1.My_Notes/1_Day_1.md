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

---

## Ollama Models for course

Hello! It's fantastic to have you on board. As your **Windows-to-Mac AI Bridge** for Ed Donner's courses, I'm here to ensure that every terminal command, package path, and environmental variable translates perfectly onto your Windows 11 setup.

Looking closely at your device specifications and your current Ollama configuration, we have a very specific hardware reality to optimize for. Let's break down your specs first to see what we're working with.

### 🔍 Analysis of Your Hardware Specs

* **System RAM:** **8.00 GB**
* **GPU:** **NVIDIA GeForce MX350 (2 GB VRAM)**
* **Current Ollama Models:** You already have `mxbai-embed-large:latest` (669 MB), `llama3.2:1b` (1.3 GB), and a large ~7.2 GB model (`gemma2:9b` or similar).

> ⚠️ **The Critical Constraint:** Ed Donner’s courses (especially the *Agentic* and *Production* tracks) rely heavily on complex tasks like **Structured Output (JSON mode)** and **Tool/Function Calling**.
> While you have a 7.2 GB model downloaded, running a model that size on a machine with **8GB of total system RAM** and a **2GB VRAM GPU** will cause severe bottlenecking, extreme slowdowns, or crashes. Ollama will be forced to split the layers across your system RAM and swap memory, competing directly with Windows 11 and VS Code.

---

## 🚀 The Best Ollama Models for Your Setup

To get smooth performance without freezing your PC, we need ultra-optimized, state-of-the-art **Small Language Models (SLMs)** that natively support tool calling and fit comfortably within your available memory footprint.

### 1. The Ideal Sweet Spot: `qwen3:1.7b` or `qwen2.5:1.5b`

* **Why it works:** The Qwen series punches way above its weight class. The small parameter variants (`1.5B` / `1.7B`) have incredible instruction-following and surprisingly robust native tool-calling capabilities.
* **Memory Footprint:** ~1.2 GB to 1.6 GB. It will load completely into your system RAM without starving your OS, allowing your Python scripts to execute quickly.

### 2. The Native Agent: `gemma3:1b`

* **Why it works:** Google's lightweight model is optimized for rapid local inference, excellent reasoning capabilities, and handles system prompt instructions perfectly.
* **Memory Footprint:** ~1.4 GB.

### 3. The Specialized Tool Caller: `functiongemma:latest` (270M)

* **Why it works:** Google explicitly fine-tuned this ultra-lightweight `270M` parameter model solely for text-only function calling. It is custom-built to be deployed on resource-constrained environments like laptops.
* **Memory Footprint:** < 500 MB. It runs blazing fast and is exceptional for testing Ed's agentic loop scripts locally.

---

## 🛠️ Step-by-Step PowerShell Setup Guide

Let’s pull these lightweight models and set up your environment inside VS Code. Open your integrated **PowerShell** terminal (`Ctrl + ~`) and follow these steps:

1. **Pull a high-performing SLM:** Downloads the 1.5B parameter model weights.
Let's fetch the highly capable Qwen model that fits beautifully inside your memory specs:

```powershell
ollama pull qwen2.5:1.5b

```


2. **Check your updated list:** Verify the local registry changes.
Run the command from your screenshot to verify it registered successfully alongside your other models:

```powershell
ollama list

```


3. **Set up your environmental variables:** Replaces Mac's 'export' command on Windows.
Ed will frequently tell you to use `export OLLAMA_HOST=...`. In PowerShell, map it like this:

```powershell
$env:OLLAMA_HOST="http://127.0.0.1:11434"

```


4. **Engage your UV Virtual Environment:** Activates script isolation using Windows paths.
Ed uses `uv` for package management. Instead of the Mac command (`source .venv/bin/activate`), activate your virtual environment using the Windows layout:

```powershell
.\.venv\Scripts\activate

```

*(You will see your prompt change to confirm it is active, exactly like your `(llm-engineering)` prompt in your screenshot!)*


---

## 💡 Pro-Tips for Ed's Courses on Your Machine

### 💻 Mixing Local + Cloud (The Hybrid Approach)

Because your machine's hardware is tightly bounded, I highly recommend using a hybrid approach across the three tracks:

1. **For Embedding & RAG modules:** Keep using your local `mxbai-embed-large:latest`! Generating text embeddings is lightweight and will run beautifully on your computer.
2. **For Complex Agentic Architectures:** When Ed is teaching multi-agent frameworks or heavy LangGraph pipelines where small local models get confused by massive prompts, remember that you can always use your **Gemini API key** to do the heavy lifting while doing the basic setup validation locally using `qwen2.5:1.5b`.

### 🚨 Quick Check: "ModuleNotFoundError"

If you ever run a file via `python main.py` and get a `ModuleNotFoundError` despite installing packages with `uv`, your VS Code is likely tracking a different global python executable.

* **The Fix:** Press `Ctrl + Shift + P`, search for **"Python: Select Interpreter"**, and explicitly select the executable inside your local workspace folder path: `D:\Github\Udemy-AI-Courses\...\llm_engineering\.venv\Scripts\python.exe`.

Give `ollama pull qwen2.5:1.5b` a run! Let me know if you hit any roadblocks spinning up your first agent script on Windows.

---

## Ollama Models Usage

![](images/3.png)

![](images/4.png)

Welcome back! It looks like you successfully downloaded those lightweight models—excellent work! Your terminal looks pristine, and having your `(llm-engineering)` virtual environment active means you're completely set up for success on Windows.

Let's break down how an LLM interacts with your hardware like we are sitting down for a 1-on-1 tutoring session. No confusing jargon—just practical logic to help you ace Ed Donner’s courses.

---

## 🧠 Part 1: Your Specs vs. How LLMs Use Your Computer

Think of an AI model like a giant book of knowledge. To read it quickly, your computer needs to open this book and hold it entirely inside its ultra-fast short-term memory (**RAM**).

* **VRAM (Video RAM):** This is the lightning-fast memory on your graphics card (NVIDIA MX350). Your GPU has **2 GB** of this. This is the absolute best place to put an AI model because it processes text at blinding speeds.
* **System RAM:** This is your regular computer memory. You have **8 GB** total, but Windows 11 and VS Code use about 4–5 GB just to stay turned on. That leaves you with roughly **3 GB to 3.5 GB** of free space.

If a model fits completely inside your VRAM or free System RAM, it runs smoothly. If it's too big, things break.

---

## 🛠️ Part 2: Which Models to Use for Which Tasks (With Examples)

Based on your list, here is exactly how to distribute your models across Ed's tracks for the best learning experience.

### 🗺️ Task A: Vector Embeddings & RAG (Retrieval-Augmented Generation)

**Best Model:** `mxbai-embed-large:latest` (669 MB)

* **Why:** This isn't a conversational chatbot. It is a highly specialized model designed to turn text into math numbers (vectors) so your computer can look up information inside documents (Ed's Core Track). Because it's under 1 GB, it fits perfectly into your 2 GB GPU VRAM.
* **Example 1 (Document Search):** Giving the model a 50-page PDF manual and asking it to find the exact paragraph about "How to reset the machine."
* **Example 2 (Memory Preservation):** Storing a user's past chat history in a database so the AI remember who you are when you say hello again tomorrow.

### 🤖 Task B: Agentic Loops, Tool/Function Calling

**Best Model:** `qwen2.5:1.5b` (986 MB) or `functiongemma:latest` (300 MB)

* **Why:** In the *Agentic Track*, Ed teaches models how to "think" and execute Python code. `qwen2.5:1.5b` is brilliant at formatting outputs in precise JSON structures without messing up. `functiongemma` is a specialized micro-model that strictly outputs code structures. Both fit inside your GPU VRAM completely.
* **Example 1 (Calculations):** An AI agent detects that a user asked a math problem, halts its chat, formats a structured command to call your local `calculator()` Python function, gets the result, and replies to the user.
* **Example 2 (API Fetching):** An agent deciding it needs real-time data, correctly generating a JSON block to trigger a `get_weather(city="Chennai")` routine.

### 💬 Task C: Quick Chat & Simple Instructions

**Best Model:** `gemma3:1b` (815 MB) or `llama3.2:1b` (1.3 GB)

* **Why:** These are amazing, ultra-lightweight conversationalists. They are perfect for basic text generation, summarization, or checking if your code logic flows correctly.
* **Example 1 (Summarization):** Pasting a long email thread into your Python terminal and asking the model to summarize it in 3 bullet points.
* **Example 2 (Classification):** Asking the model to look at customer feedback and tag it as either "POSITIVE" or "NEGATIVE".

---

## 🚨 Part 3: The Model That Exceeds Your System Limits

Look closely at your list: **`gemma4:e2b`** (which is roughly a 7B to 9B parameter model compressed down) takes up **7.2 GB** of space.

### Why will it fail?

Your graphics card only has **2 GB** of VRAM. Your free system RAM is only about **3 GB**.
When you type `ollama run gemma4:e2b`, Ollama tries to open a 7.2 GB book inside a room that only has 5 GB of total combined shelf space left.

### 💥 Example of How It Fails (The Nightmare Scenario)

If you try to run Ed's code using this model, you will experience what we call **System Bottlenecking & Memory Swapping**. Here is exactly what happens step-by-step:

1. **The Freeze:** Ollama takes 1.5 GB and shoves it into your GPU. It takes another 3 GB and jams it into your System RAM. Your System RAM hits **100% capacity**.
2. **The "Page File" Crawl:** Windows panics because it has no memory left to run VS Code or your Python script. It starts using your hard drive storage as pretend RAM (called a Page File/Swap). Hard drives are hundreds of times slower than RAM.
3. **The Token Trickle:** Instead of the AI generating text smoothly, you will watch your terminal print out **one single word every 10 to 15 seconds** while your laptop cooling fans scream at full blast.
4. **The Crash (OOM):** Eventually, your Python script will time out, or Windows will forcefully terminate Ollama with an **Out Of Memory (OOM)** exception error to save your system from crashing completely.

### 💡 The AI Engineer's Solution

When Ed's course demands a heavy reasoning model that your laptop simply cannot load, don't force `gemma4:e2b`. Instead, leverage your **Claude API Key**!
Use your local small models (`qwen2.5:1.5b`) to test that your loops, loops syntax, and variables work without errors. When you need complex logical execution, swap the model engine over to Claude in your code. It keeps your laptop cool, fast, and highly productive!

---
