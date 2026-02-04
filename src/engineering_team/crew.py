import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LITELLM_LOG"] = "ERROR"
os.environ["LITELLM_MODE"] = "PRODUCTION"
os.environ["LITELLM_DISABLE_PROXY_LOGGING"] = "true"
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class EngineeringTeam:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ---------- AGENTS ---------- #

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config["engineering_lead"],
            verbose=True,
            allow_delegation=False,
            max_iter=1
        )

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["backend_engineer"],
            verbose=True,
            max_iter=1
        )

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["frontend_engineer"],
            verbose=True,
            max_iter=1
        )

    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["test_engineer"],
            verbose=True,
            max_iter=1
        )

    # ---------- TASKS ---------- #

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config["design_task"]
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config["code_task"]
        )

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config["frontend_task"]
        )

    @task
    def test_task(self) -> Task:
        return Task(
            config=self.tasks_config["test_task"]
        )

    # ---------- CREW ---------- #

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=False,
            share_crew=False
        )


# ---------- WORKFLOW ---------- #

def run_engineering_workflow(requirements, module_name, class_name):

    crew_instance = EngineeringTeam().crew()

    return crew_instance.kickoff(
        inputs={
            "requirements": requirements,
            "module_name": module_name,
            "class_name": class_name
        }
    )
