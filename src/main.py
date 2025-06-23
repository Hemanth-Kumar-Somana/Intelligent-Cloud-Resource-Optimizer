# from fastapi import FastAPI
# from main_orchestrator_agent import run_orchestrator
# from monitor_agent import run_monitor
# from policy_agent import run_policy
# from recommendation_agent import run_recommendation
# from analysis_agent import run_analysis

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Cloud Optimizer Agent API Running"}

# @app.get("/run-all")
# def run_all_agents():
#     run_monitor()
#     run_analysis()
#     run_policy()
#     run_recommendation()
#     run_orchestrator()
#     return {"status": "All agents executed"}
from fastapi import FastAPI
from agentkit.adapter.fastapi import AgentRouter
from src.main_orchestrator_agent import MainOrchestratorAgent

app = FastAPI()

# Initialize your main orchestrator agent
main_agent = MainOrchestratorAgent()

# Create an API router using the agent
agent_router = AgentRouter(agent=main_agent)

# Mount the router at the root path
app.include_router(agent_router.router)


# from fastapi import FastAPI
# from agentkit.interface.fastapi import mount_agent_interface
# from src.main_orchestrator_agent import MainOrchestratorAgent

# app = FastAPI()
# agent = MainOrchestratorAgent()

# mount_agent_interface(app, agent)
