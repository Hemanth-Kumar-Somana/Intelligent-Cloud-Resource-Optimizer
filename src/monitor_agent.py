from agentkit import Tool, LlmAgent
from google.cloud import monitoring_v3
from google.cloud import billing_v1
import os
from datetime import datetime, timedelta

project_id = os.getenv("PROJECT_ID")

# Tool 1: Fetch CPU usage for a VM
class GetCPUUsage(Tool):
    def run(self, instance_name: str) -> str:
        client = monitoring_v3.MetricServiceClient()
        project_name = f"projects/{project_id}"
        interval = monitoring_v3.TimeInterval(
            end_time={"seconds": int(datetime.utcnow().timestamp())},
            start_time={"seconds": int((datetime.utcnow() - timedelta(minutes=60)).timestamp())}
        )

        results = client.list_time_series(
            request={
                "name": project_name,
                "filter": f'metric.type = "compute.googleapis.com/instance/cpu/utilization" AND '
                          f'resource.labels.instance_id = "{instance_name}"',
                "interval": interval,
                "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
            }
        )

        for result in results:
            points = result.points
            if points:
                avg_util = sum([point.value.double_value for point in points]) / len(points)
                return f"Average CPU utilization for {instance_name} over the last hour is {avg_util:.2%}"
        return f"No CPU data found for instance {instance_name}."

# Tool 2 (Optional): Fetch billing account info
class GetBillingInfo(Tool):
    def run(self) -> str:
        client = billing_v1.CloudBillingClient()
        billing_accounts = list(client.list_billing_accounts())
        if billing_accounts:
            info = "\n".join([f"Billing Account: {acc.name}, Display Name: {acc.display_name}" for acc in billing_accounts])
            return f"Found billing accounts:\n{info}"
        return "No billing accounts found."

# Monitor Agent Definition
class MonitorAgent(LlmAgent):
    def setup(self):
        self.name = "monitor_agent"
        self.description = "Collects GCP monitoring and billing data."
        self.tools = [GetCPUUsage(), GetBillingInfo()]
