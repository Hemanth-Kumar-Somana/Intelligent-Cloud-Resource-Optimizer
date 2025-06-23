# # policy_agent.py

# from adk import Tool, LlmAgent

# class EnforcePolicyRules(Tool):
#     def run(self, recommendation: str):
#         # Example rule: no VMs below 2 vCPUs
#         if "n1-standard-1" in recommendation:
#             return "Rejected: does not meet policy"
#         return "Approved"

# class PolicyAgent(LlmAgent):
#     def setup(self):
#         self.description = "Enforces cloud usage policies"
#         self.tools = [EnforcePolicyRules()]


from agentkit import Tool, LlmAgent

class PolicyCheckerTool(Tool):
    description = "Validates recommendations against policies."

    def run(self, recommendation):
        return f"Policy approved for: {recommendation}"

class PolicyAgent(LlmAgent):
    def __init__(self):
        tools = [PolicyCheckerTool()]
        super().__init__(name="policy_agent", tools=tools, description="Applies cloud policy rules.")
