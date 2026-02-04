from fastapi import FastAPI
from pydantic import BaseModel
from src.engineering_team.crew import run_engineering_workflow
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="CrewAI Engineering Team API")


class EngineeringRequest(BaseModel):
    requirements: str
    module_name: str
    class_name: str


@app.get("/")
def home():
    return {"message": "CrewAI Engineering Team API Running"}


@app.post("/run-engineering-team")
def run_team(request: EngineeringRequest):

    output = run_engineering_workflow(
        request.requirements,
        request.module_name,
        request.class_name
    )

    return {"result": output}
