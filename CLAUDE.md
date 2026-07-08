# Project Rules & Windows-to-Mac Environment Bridge

## Context & Environment
- **Course:** Ed Donner's AI Engineer Tracks (Core, Agentic, Production)
- **User OS:** Windows 11
- **Terminal:** PowerShell (VS Code default)
- **Package Manager:** `uv` (preferred tool)
- **Local Models:** Ollama open models
- **Cloud Models:** Google Geimini models

## Available Local Hardware & Ollama Models

> ⚠️ **Hardware Constraints:** Host machine runs Windows 11 with **8.00 GB System RAM** and a **2 GB VRAM GPU (NVIDIA MX350)**.

| Model Name | Size | Operational Task Category | System Compatibility Note |
| :--- | :--- | :--- | :--- |
| `qwen2.5:1.5b` | 986 MB | **Agentic Track / Tool Calling / JSON** | **Optimal Sweet Spot.** Fits completely in VRAM. Use for function loops. |
| `gemma3:1b` | 815 MB | **Core Track / Simple Text Chat & Prompting** | **Safe.** Light memory footprint. Fast local text execution. |
| `functiongemma:latest` | 300 MB | **Agentic Track / Strict Code formatting** | **Safe.** Ultra-lightweight micro-model custom-tuned for code generation. |
| `mxbai-embed-large:latest`| 669 MB | **Core Track / Vector Search & RAG** | **Optimal.** Specialized embedder. Fits inside VRAM completely. |
| `llama3.2:1b` | 1.3 GB | **General Text Instruction Follower** | **Safe.** Runs well on CPU/RAM allocation without choking the OS. |
| `gemma4:e2b` | 7.2 GB | **DO NOT RUN LOCALLY** | 🚨 **Exceeds System Limits.** Will trigger heavy swapping and system freeze. Use Claude Pro/Gemini API instead for heavy tasks. |


## Core Translation Rules (Strictly Enforce)
1. **Shell Commands:** Never use Unix syntax. Always replace `export VAR=val` with `$env:VAR="val"` and `ls` with `dir` or `Get-ChildItem`.
2. **Execution:** Run scripts using `python script.py` instead of `python3`.
3. **UV Environments:** Remind the user that activation on Windows PowerShell requires `.\.venv\Scripts\activate` (instead of `source .venv/bin/activate`). Always use `uv run` for executing isolated tasks.
4. **File Paths:** Use Windows backslashes `\` for local system path interactions, but remember that Python handles forward slashes `/` internally.
5. **Hidden Files:** Be aware that `.env` config files are sometimes hidden in Windows File Explorer but fully accessible/visible inside the VS Code tree.

## Debugging Workflow & Commands
- **Build / Run:** Use `uv run python <filename>.py`
- **ModuleNotFoundError:** Check the selected VS Code Python Interpreter first and ensure the `uv` environment is active.
- **Permission Denied:** Instruct the user to restart VS Code or run PowerShell as an Administrator.
- **Encoding Errors:** Intercept potential Windows-specific encoding conflicts by preferring UTF-8 explicitly (`encoding='utf-8'`) in file I/O operations.