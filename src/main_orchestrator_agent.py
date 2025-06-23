# # main_orchestrator_agent.py

# from adk import WorkflowAgent

# class MainOrchestratorAgent(WorkflowAgent):
#     def setup(self):
#         self.description = "Coordinates all agents for cloud optimization"
#         self.steps = [
#             {"agent": "src.monitor_agent.MonitorAgent"},
#             {"agent": "src.analysis_agent.AnalysisAgent"},
#             {"agent": "src.recommendation_agent.RecommendationAgent"},
#             {"agent": "src.policy_agent.PolicyAgent"}
#         ]


# from agentkit import WorkflowAgent
# from src.monitor_agent import MonitorAgent
# from src.analysis_agent import AnalysisAgent
# from src.recommendation_agent import RecommendationAgent
# from src.policy_agent import PolicyAgent

from monitor_agent import MonitorAgent
from analysis_agent import AnalysisAgent
from recommendation_agent import RecommendationAgent
from policy_agent import PolicyAgent
from agentkit import WorkflowAgent


class MainOrchestratorAgent(WorkflowAgent):
    def __init__(self):
        super().__init__(
            name="main_orchestrator",
            description="Coordinates all agents for cloud optimization.",
            agents=[
                MonitorAgent(),
                AnalysisAgent(),
                RecommendationAgent(),
                PolicyAgent()
            ]
        )
