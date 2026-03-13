<div align="center">

# 🤖 EngineeringTeam Crew

### Multi-Agent AI Software Engineering Workflow

![Python](https://img.shields.io/badge/Python-3.10--3.12-3776AB?style=for-the-badge&logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF6B6B?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Gradio](https://img.shields.io/badge/Gradio-Frontend-F97316?style=for-the-badge)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

**EngineeringTeam Crew** simulates a real software engineering team using AI agents. Multiple agents collaborate autonomously to design, develop, test, and generate complete application modules — end to end.

🚀 **[Live Demo →](https://engineering-team.onrender.com)**

</div>

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Agent Workflow](#-agent-workflow)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Running the Crew](#-running-the-crew-locally)
- [Running the API Server](#-running-the-api-server)
- [Running the Frontend](#-running-the-generated-frontend)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Customization](#-customization)
- [Output Files](#-output-files)
- [Future Improvements](#-future-improvements)
- [Support](#-support)

---

## 🔷 Project Overview

> EngineeringTeam Crew is designed to simulate a real software engineering team using AI agents. Each agent performs a dedicated responsibility — design, backend development, frontend generation, and testing.

| Agent | Role | Output |
|---|---|---|
| 🧑‍💼 Engineering Lead | Technical design planning | Design document (Markdown) |
| 🐍 Backend Agent | Python module implementation | Backend `.py` module |
| 🎨 Frontend Agent | UI generation using Gradio | Frontend `app.py` |
| 🧪 QA Agent | Test case generation | `pytest` test file |

All generated files are automatically saved inside the `output/` directory.

---

## 🔁 Agent Workflow

```
Step 1 → Engineering Lead Agent creates technical design document
            │
            ▼
Step 2 → Backend Agent implements Python module
            │
            ▼
Step 3 → Frontend Agent builds Gradio UI interface
            │
            ▼
Step 4 → QA Agent generates pytest test cases
```

> Each agent uses the output of the previous agent — simulating real team collaboration and handoff.

---

## 🏗 System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        USER / CLIENT                         │
│                   Web Browser / API Call                     │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                     FASTAPI BACKEND                          │
│  • Receives workflow trigger requests                        │
│  • Exposes REST API endpoints                                │
│  • Auto docs at /docs                                        │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                     CREWAI ORCHESTRATOR                      │
│  • Manages agent sequence and task delegation                │
│  • Passes outputs between agents                             │
└──────────────────────────┬───────────────────────────────────┘
                           │
           ┌───────────────┼────────────────┐
           ▼               ▼                ▼               ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Engineering │  │   Backend    │  │   Frontend   │  │   QA Agent   │
│  Lead Agent  │  │    Agent     │  │    Agent     │  │              │
│              │  │              │  │              │  │              │
│ Design Docs  │  │ Python Module│  │  Gradio UI   │  │ Pytest Cases │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                      OUTPUT DIRECTORY                        │
│  • design.md  • backend.py  • app.py  • test_backend.py      │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    GRADIO FRONTEND UI                        │
│  • Auto-generated interface from crew output                 │
│  • Runs as standalone Python application                     │
└──────────────────────────────────────────────────────────────┘
```

---

## 🧰 Technology Stack

| Layer | Technology |
|---|---|
| **Agent Framework** | CrewAI |
| **LLM Backend** | LiteLLM + Ollama (Local LLM) |
| **API Server** | FastAPI |
| **Frontend UI** | Gradio (auto-generated) |
| **Language** | Python 3.10 – 3.12 |
| **Dependency Manager** | UV |
| **Deployment** | Render |

---

## ⚙ Installation

**1. Ensure Python 3.10–3.12 is installed**

```bash
python --version
```

**2. Install UV package manager**

```bash
pip install uv
```

**3. Install project dependencies**

```bash
crewai install
```

**4. Create environment file**

```env
OPENAI_API_KEY=your_key_here
```

---

## 🤖 Running the Crew Locally

```bash
crewai run
```

This executes the full multi-agent engineering workflow and generates all output modules inside the `output/` directory.

---

## 🖥 Running the API Server

```bash
uvicorn api:app --reload
```

API documentation will be available at:

```
http://127.0.0.1:8000/docs
```

---

## 🎨 Running the Generated Frontend

After crew execution, the Gradio interface is generated inside the `output/` folder.

```bash
python output/app.py
```

The Gradio UI will open automatically in your browser.

---

## 🌐 Deployment

```
Platform    →  Render (Cloud)
Backend     →  FastAPI service
Frontend    →  Gradio interface
Endpoint    →  Public URL hosting
```

Deployed at: **[https://engineering-team.onrender.com](https://engineering-team.onrender.com)**

---

## 📂 Project Structure

```
engineering-team/
│
├── src/
│   └── engineering_team/
│       ├── config/
│       │   ├── agents.yaml       # Agent role definitions
│       │   └── tasks.yaml        # Task workflow definitions
│       ├── crew.py               # Crew execution logic
│       └── main.py               # Entry point
│
├── output/                       # Auto-generated files
│   ├── design.md                 # Technical design document
│   ├── backend.py                # Generated Python module
│   ├── app.py                    # Generated Gradio frontend
│   └── test_backend.py           # Generated pytest test cases
│
├── api.py                        # FastAPI server
├── pyproject.toml
├── .env
└── README.md
```

---

## 🔧 Customization

**Modify agent roles and behavior:**

```
src/engineering_team/config/agents.yaml
```

**Modify workflow tasks:**

```
src/engineering_team/config/tasks.yaml
```

**Modify crew execution logic:**

```
src/engineering_team/crew.py
```

---

## 📄 Output Files

The crew automatically generates the following files inside `output/`:

```
output/
├── design.md           →  Technical design document (Markdown)
├── backend.py          →  Backend Python module
├── app.py              →  Gradio frontend UI
└── test_backend.py     →  Automated pytest test cases
```

---

## 🚀 Future Improvements

```
[ ] Improve LLM output accuracy and consistency
[ ] Add persistent database storage for generated modules
[ ] Add authentication layer for API access control
[ ] Support multi-module generation in a single run
[ ] Improve auto-generated UI styling
[ ] Add streaming output during agent execution
[ ] Support additional LLM providers
```

---

## 📚 Support

| Resource | Link |
|---|---|
| CrewAI Documentation | [docs.crewai.com](https://docs.crewai.com) |
| CrewAI Repository | [github.com/joaomdmoura/crewai](https://github.com/joaomdmoura/crewai) |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with CrewAI · FastAPI · Gradio · LiteLLM · Render**

⭐ Star this repo if you found it helpful!

</div>
