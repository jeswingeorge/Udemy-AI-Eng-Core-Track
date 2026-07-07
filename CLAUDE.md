# Project Rules & Windows-to-Mac Environment Bridge

## Context & Environment
- **Course:** Ed Donner's AI Engineer Tracks (Core, Agentic, Production)
- **User OS:** Windows 11
- **Terminal:** PowerShell (VS Code default)
- **Package Manager:** `uv` (preferred tool)
- **Local Models:** Ollama open models
- **Cloud Models:** Anthropic Claude models

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