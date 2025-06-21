# 🤖 Ollama Agent Chat Setup Guide

## 1. Prerequisites

- **Python:** Install the latest version from [python.org](https://www.python.org/downloads/).
- **Ollama:** Download and install from [ollama.com/download](https://ollama.com/download).

## 2. Verify Installation

Open a terminal and run:
```sh
ollama --version
python --version
```

## 3. Choose and Download a Qwen 3 Model

Available Qwen 3 models:
- `qwen3:0.6b`
- `qwen3:4b` (recommended for this project)
- `qwen3:8b`
- `qwen3:14b`
- `qwen3:32b`

**Pull your chosen model:**
```sh
ollama pull qwen3:4b
```

## 4. Test Ollama (Optional)

Chat directly with the model from the command line:
```sh
ollama run qwen3:4b
```

## 5. Run Ollama as a Server

```sh
ollama serve
```

## 6. Set Up Your Python Environment

```sh
python -m venv venv
.\venv\Scripts\activate
```

## 7. Install Python Dependencies

```sh
pip install -r requirements.txt
```

## 8. Run the Streamlit Chat App

```sh
streamlit run agent_chat_ui.py
```

---

## 🖥️ Deploying on Another Machine

1. **Copy the entire project folder** (including `requirements.txt`, `chat_style.html`, and all code files) to the new machine.
2. **Repeat steps 1–8 above** on the new machine.

---

## 💡 Appendix

### Controlling Qwen 3's Thinking Mode

- **Step-by-step reasoning:** Append `/think` to your prompt.
- **Direct, fast response:** Append `/no_think` to your prompt.

This works via the Ollama CLI and in prompts sent via the API or LangChain.

---

## 📚 Reference

- [Build a Local AI Chatbot with Ollama and Streamlit (freeCodeCamp)](https://www.freecodecamp.org/news/build-a-local-ai/)

---

**Enjoy chatting with your local Ollama-powered AI!**