EngineeringTeam Crew Project

This project demonstrates a multi agent software engineering workflow built using crewAI. The system simulates an engineering team where multiple AI agents collaborate to design, develop, test, and generate application modules automatically.

## Live Application

Application is deployed and accessible here

[https://engineering-team.onrender.com](https://engineering-team.onrender.com)

---

## Project Overview

EngineeringTeam Crew is designed to simulate a real software engineering team using AI agents. Each agent performs a dedicated responsibility such as design, backend development, frontend generation, and testing.

The workflow automatically:

1 Generates technical design
2 Generates backend python module
3 Generates frontend interface
4 Generates test cases

All generated files are stored inside the output folder.

---

## Technology Stack

This project uses the following technologies

Python
CrewAI
LiteLLM
FastAPI
Gradio
Ollama Local LLM
Render Deployment
UV Dependency Manager

---

## Installation

Ensure Python version between 3.10 and 3.12 is installed.

Install UV package manager

```bash
pip install uv
```

Install project dependencies

```bash
crewai install
```

Create environment file and add your API key if needed

```bash
OPENAI_API_KEY=your_key_here
```

---

## Project Structure

```
engineering_team
│
├── src
│   └── engineering_team
│       ├── config
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── crew.py
│
├── output
│   ├── app.py
│   ├── generated modules
│   ├── design documents
│   └── test files
│
├── api.py
├── requirements.txt
└── README.md
```

---

## Running The Crew Locally

Run crew workflow

```bash
crewai run
```

This will execute the engineering workflow and generate output modules.

---

## Running API Server

Start FastAPI backend

```bash
uvicorn api:app --reload
```

API Documentation will be available at

```
http://127.0.0.1:8000/docs
```

---

## Running Generated Frontend

After crew execution, frontend Gradio interface is generated inside output folder.

Run generated interface

```bash
python output app.py
```

Gradio UI will open in browser.

---

## Deployment

This project is deployed using Render cloud platform.

Deployment uses

FastAPI for backend service
Gradio for frontend interface
Public endpoint hosting


---

## How Workflow Works

Step 1 Engineering Lead Agent creates technical design
Step 2 Backend Agent implements python module
Step 3 Frontend Agent builds UI using Gradio
Step 4 QA Agent generates pytest test cases

Each step uses output from previous agent to simulate real team collaboration.

---

## Customization

Modify agent behavior

```
src engineering_team config agents.yaml
```

Modify workflow tasks

```
src engineering_team config tasks.yaml
```

Modify crew execution logic

```
src engineering_team crew.py
```

---

## Output Files

Crew automatically generates

Design documents in markdown
Backend python modules
Frontend UI code
Automated test cases

All files are saved inside output directory.

---

## Support

CrewAI Documentation
[https://docs.crewai.com](https://docs.crewai.com)

CrewAI Repository
[https://github.com/joaomdmoura/crewai](https://github.com/joaomdmoura/crewai)

---

## Future Improvements

Improve LLM output accuracy
Add persistent database storage
Add authentication layer
Add multi module generation
Improve UI styling

---


