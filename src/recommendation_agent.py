# # recommendation_agent.py

# from adk import Tool, LlmAgent

# class RecommendResizeVM(Tool):
#     def run(self, vm_id: str):
#         return f"Recommend resizing {vm_id} to n1-standard-1 for cost savings"

# class RecommendationAgent(LlmAgent):
#     def setup(self):
#         self.description = "Generates optimization recommendations"
#         self.tools = [RecommendResizeVM()]


from agentkit import Tool, LlmAgent

class GenerateRecommendationsTool(Tool):
    description = "Generates cost-saving recommendations."

    def run(self, analysis_results):
        return f"Recommendation based on: {analysis_results}"

class RecommendationAgent(LlmAgent):
    def __init__(self):
        tools = [GenerateRecommendationsTool()]
        super().__init__(name="recommendation_agent", tools=tools, description="Suggests optimizations.")
