
# 💻 Insta Code Gen

**Insta Code Gen** is a multilingual, AI-powered code assistant that helps you generate, debug, and explain code using natural language prompts. It supports multiple programming languages, skill levels.

> 🧠 Powered by: Groq + LangChain + Streamlit

---

## 🌟 Features

- ✅ Natural Language to Code (prompt → code)
- ✅ Multilingual support (e.g., Telugu → English → Python)
- ✅ Beginner / Intermediate / Expert explanation modes
- ✅ Supports Python, JavaScript, C#, Java, Go, Rust
- ✅ Modular code structure (LangChain-friendly)

---

## 📸 Demo
![Insta Code Gen in Action](Insta-Code-Gen-1.png)  
![Insta Code Gen in Action](Insta-Code-Gen-2.png)  
![Insta Code Gen in Action](Insta-Code-Gen-3.png)  
![Insta Code Gen in Action](Insta-Code-Gen-4.png)  

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
| Embedding & Retrieval | FAISS + OpenAI Embeddings |
| Language Detection | langdetect |

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
git clone https://github.com/SrikanthP126/Insta-Code-Gen.git
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

Built by [Srikanth Penta](https://www.linkedin.com/in/penta-srikanth/)

---

## 🏷️ Tags

`#AI` `#Groq` `#LangChain` `#Python` `#DevTools` `#Streamlit` `#RAG` `#LLM` `#CodeGeneration`
