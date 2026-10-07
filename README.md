# 🤖 AI Agent Demo

A minimal Python project with a web UI to test and integrate your own AI agent.
Built with [Streamlit](https://streamlit.io/) for the UI and the
[OpenAI](https://platform.openai.com/) API as the default backend.

## ✨ Features

- Clean chat UI to interact with the agent
- Configurable system prompt from the sidebar
- Clear-chat button to reset the conversation
- Swappable agent backend — the UI only needs `run(messages) -> str`

## 📁 Project structure

```
.
├── app.py              # Streamlit UI
├── agent.py            # AI agent logic (swap in your own here)
├── requirements.txt    # Python dependencies
├── .env.example        # Template for environment variables
└── README.md
```

## 🚀 Getting started

> Commands below use **Git Bash** on Windows.

### 1. (Optional) Create a virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Copy the example env file and add your OpenAI API key:

```bash
cp .env.example .env
```

Then edit `.env`:

```text
OPENAI_API_KEY=sk-your-real-key-here
```

### 4. Run the app

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`).

To stop the app press `Ctrl+C`, and run `deactivate` to exit the virtual environment.

## 🔌 Plugging in your own agent

The UI only depends on the `AIAgent.run(messages) -> str` interface, so you can
replace the internals of `agent.py` with anything:

- Your own REST API
- A local model (e.g. Ollama)
- A framework like LangChain, CrewAI, LlamaIndex

Keep the `messages` format as a list of
`{"role": "user" | "assistant", "content": "..."}` and the UI keeps working.

## 🔐 Security

- `.env` is git-ignored — never commit your API keys.
- Share `.env.example` (with placeholder values) instead.

## 📄 License

[MIT License](https://gh.io/mit)
