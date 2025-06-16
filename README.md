
# 💻 Insta Code Gen

**Insta Code Gen** is a multilingual, AI-powered code assistant that helps you generate, debug, and explain code using natural language prompts. It supports multiple programming languages, skill levels.

> 🧠 Powered by: Groq + LangChain + Streamlit + FAISS

---

## 🌟 Features

- ✅ Natural Language to Code (prompt → code)
- ✅ Multilingual support (e.g., Telugu → English → Python)
- ✅ Beginner / Intermediate / Expert explanation modes
- ✅ Supports Python, JavaScript, C#, Java, Go, Rust
- ✅ Retrieval Augmented Generation (RAG) using FAISS
- ✅ Modular code structure (LangChain-friendly)
- ✅ GitHub Repo Analyzer and Flow Visualizer (coming soon!)

---

## 📸 Demo

Paste a prompt like:

```text
Generate a registration page with a multi-step form in Python using Flask
```

And get the complete working code instantly ✨

---

## 🔧 Tech Stack

| Layer | Tool |
|-------|------|
| UI | Streamlit |
| LLM Backend | Groq API (OpenAI-compatible) |
| Prompt Engine | LangChain |
| Translation | Google Translate (googletrans) |
| Embedding & Retrieval | FAISS + OpenAI Embeddings |
| Language Detection | langdetect |
| Context Builder | Custom Model Context Protocol (MCP) |
| GitHub Flow Parsing | Python AST (coming soon) |

---

## 📁 Project Structure

```
insta-code-gen/
├── app/
│   ├── ui.py                  ← Streamlit layout
│   ├── llm_chain.py           ← LangChain + Groq integration
│   ├── rag_retriever.py       ← FAISS retrieval logic
│   ├── mcp.py                 ← Task-aware system prompt builder
│   ├── translator.py          ← googletrans utils
│   ├── utils.py               ← Shared formatting helpers
│   └── github_cloner.py       ← (upcoming)
├── data/
│   └── source_docs/           ← Knowledge docs (for RAG)
├── main.py                    ← Streamlit entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/insta-code-gen.git
cd insta-code-gen
```

2. Create virtual environment:
```bash
python3.11 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set your API Key (Groq):
```bash
export GROQ_API_KEY=your-groq-api-key
```

5. Run the app:
```bash
streamlit run main.py
```

---

## 🔭 Upcoming Features

- 🧠 GitHub Repo Analyzer (enter URL → summary + flow)
- 🧾 Auto README/documentation generator
- 🐞 Code bug spotter + fix suggester
- 🧱 LLM agent boilerplate generator

---

## 🤝 Contributing

PRs and suggestions welcome! Just open an issue or ping me on LinkedIn.

---

## 📬 Contact

Built by [Your Name](https://www.linkedin.com/in/yourprofile)

---

## 🏷️ Tags

`#AI` `#Groq` `#LangChain` `#Python` `#DevTools` `#Streamlit` `#RAG` `#LLM` `#CodeGeneration`
