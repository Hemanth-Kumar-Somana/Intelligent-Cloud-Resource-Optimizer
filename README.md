# Intelligent Cloud Resource Optimizer

## 🚀 Project Overview (ADK Hackathon Submission)

The **Intelligent Cloud Resource Optimizer** is an innovative multi-agent system built using the Google Agent Development Kit (ADK) that intelligently monitors, analyzes, and recommends optimizations for Google Cloud resources to enhance cost efficiency, performance, and compliance.

In today's dynamic cloud environments, organizations often struggle with spiraling costs due to over-provisioning, idle resources, and a lack of real-time visibility. This project aims to address these challenges by providing an autonomous, intelligent solution that simplifies cloud resource management and ensures optimal utilization.

This project was developed for the purpose of entering the **Agent Development Kit Hackathon**.

## ✨ Features & What It Does

The Intelligent Cloud Resource Optimizer acts as a smart Cloud FinOps assistant, comprising specialized agents that collaborate seamlessly:

1.  **Monitor Agent:** Continuously gathers vital metrics and usage data for Google Cloud services (e.g., Compute Engine VMs, Cloud Storage buckets) using Google Cloud Monitoring APIs.
2.  **Analysis Agent:** Processes the collected data to identify inefficiencies such as underutilized VMs, idle resources (e.g., unattached disks), and potential performance bottlenecks. It could leverage Vertex AI for anomaly detection or predictive analytics.
3.  **Recommendation Agent:** Formulates concrete, actionable recommendations based on the analysis. Examples include right-sizing VMs, suggesting optimal storage tiers, or recommending the deletion of idle resources.
4.  **Execution Agent (Optional/Simulated for Hackathon):** If safe and feasible, this agent could trigger automated actions based on approved recommendations (e.g., using Google Cloud Deployment Manager or custom scripts). For this hackathon, we focused on simulating the execution or generating detailed scripts.
5.  **Policy Agent:** Acts as a crucial guardrail, ensuring all generated recommendations comply with predefined organizational policies (e.g., minimum VM size, security standards) before they are presented.

**Why this project for the hackathon?**

* **Leverages ADK's multi-agent capabilities:** Clearly demonstrates how different agents can collaborate.
* **Integrates with Google Cloud:** Utilizes various Google Cloud services (Monitoring, Vertex AI).
* **Addresses a real-world problem:** Cloud cost optimization and resource management are critical for many businesses.
* **Offers clear success metrics:** Potential for cost savings, performance improvements, and compliance adherence.

## 🧠 How We Built It

This project was built leveraging the power of the **Google Agent Development Kit (ADK)** for its multi-agent capabilities and deep integration with **Google Cloud Platform (GCP)** services.

* **Multi-Agent Architecture (ADK):** We designed a modular system with distinct `MonitorAgent`, `AnalysisAgent`, `RecommendationAgent`, and `PolicyAgent`. A `MainOrchestratorAgent` (an `LlmAgent` for dynamic routing) intelligently delegates tasks and manages the workflow between these specialized agents.
* **Google Cloud Integration:**
    * **Google Cloud Monitoring API:** Utilized by the `MonitorAgent` to fetch real-time metrics for various GCP resources.
    * **Vertex AI (Gemini Models):** Powers the underlying Large Language Models for our ADK agents, enabling natural language understanding, reasoning, and recommendation generation.
    * **Google Cloud SDK & Application Default Credentials (ADC):** Ensured seamless and authenticated interaction with GCP services from our agent environment.
    * **(Optional) Cloud Billing API:** Considered for direct billing data integration.
    * **(Optional) Compute Engine API, Cloud SQL Admin API, etc.:** To retrieve specific resource details for optimization.
* **Workflow & Logic:** The orchestrator agent processes user queries (e.g., "Optimize my cloud costs"), triggers data collection via the Monitor Agent, passes data for analysis, generates recommendations, and finally validates them against policies before presenting to the user.
* **Development Environment:** We used the ADK CLI and Web UI extensively for local development, testing, and debugging, taking advantage of its visual trace to understand agent thought processes and tool calls.

## 🛠️ Setup and Installation

Follow these steps to get the Intelligent Cloud Resource Optimizer running locally:

### 1. Google Cloud Setup

1.  **Sign in to Google Cloud:** If you don't have a Google Cloud account, create one at [Google Cloud Console](https://console.cloud.google.com/). New customers often get free credits.
2.  **Create a New Project:** In the Google Cloud Console, use the project selector to create a new project (e.g., `adk-cloud-optimizer`). This keeps your hackathon resources isolated.
3.  **Enable Billing:** Ensure billing is enabled for your new project. (Necessary for using Google Cloud services).
4.  **Enable Required APIs:** Navigate to "APIs & Services" > "Enabled APIs & Services" and enable the following:
    * `Vertex AI API` (Crucial for ADK and Gemini models)
    * `Cloud Monitoring API` (For monitoring cloud resources)
    * `Cloud Billing API` (If you want to pull billing data directly - *Note: This might incur costs.*)
    * Potentially other APIs depending on the specific services you want to optimize (e.g., `Compute Engine API`, `Cloud SQL Admin API`, etc.)
5.  **Set up gcloud CLI & ADC:**
    * Install the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install).
    * Update gcloud components: `gcloud components update`
    * Generate Application Default Credentials: `gcloud auth application-default login` (This allows your local agent to authenticate with Google Cloud services.)

### 2. Local Environment Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/intelligent-cloud-resource-optimizer.git](https://github.com/YOUR_GITHUB_USERNAME/intelligent-cloud-resource-optimizer.git)
    cd intelligent-cloud-resource-optimizer
    ```
2.  **Python Environment:** Ensure you have Python 3.10+ installed.
    ```bash
    python -m venv .venv
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows CMD:
    .venv\Scripts\activate.bat
    # On Windows PowerShell:
    .venv\Scripts\Activate.ps1
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment Variables:**
    Create a `.env` file in the root of your project directory (at the same level as `src/`) and add your Google Cloud Project ID and location. See the `.env` section below for content.

### 3. Running the Application

1.  **Launch ADK Web UI:**
    Make sure your virtual environment is activated, and you are in the root directory of your project (the one containing `src/`).
    ```bash
    adk web
    ```
2.  **Open Browser:** Open your web browser and navigate to the URL provided in the terminal (typically `http://localhost:8000`).
3.  **Select Main Agent:** In the top-left dropdown of the ADK Web UI, select `main_orchestrator_agent`.
4.  **Start Interacting!** Type your optimization queries into the chat interface.

## 🧪 Testing Instructions

For detailed instructions on how to test the application, including specific test cases and expected outcomes, please refer to the [TESTING.md](TESTING.md) file in this repository.

## 📊 Architecture Diagram

![Architecture Diagram](images/architecture_diagram.png)

_This diagram illustrates the multi-agent collaboration within the ADK framework and its interaction with various Google Cloud services._

## 🎥 Demonstration Video

[Link to Demo Video Here](YOUR_DEMO_VIDEO_URL)

## 🏆 Accomplishments We're Proud Of

* **Functional Multi-Agent System:** Successfully implemented a collaborative multi-agent system for cloud optimization using ADK.
* **Real-world Problem Solving:** Directly addresses critical challenges in cloud cost management and resource efficiency, offering tangible value.
* **Seamless Google Cloud Integration:** Demonstrated effective integration with Google Cloud Monitoring and Vertex AI, showcasing ADK's capabilities with Google's ecosystem.
* **Intuitive User Experience:** Provides clear and actionable recommendations via the ADK Web UI, making complex cloud optimization accessible.

## 🚧 Challenges We Ran Into

* **API Rate Limits:** Encountered and mitigated Google Cloud API rate limits when fetching extensive monitoring data, requiring careful handling of API calls.
* **Complex Data Analysis:** Developing robust logic within the `AnalysisAgent` to aggregate and interpret diverse monitoring data for accurate optimization insights was a significant challenge.
* **Prompt Engineering for Actionable Recommendations:** Iteratively refined prompts for the `RecommendationAgent` to consistently generate precise, actionable, and contextually relevant suggestions.
* **Multi-Agent Orchestration:** Designing the `MainOrchestratorAgent` for seamless delegation and information passing between different specialized agents proved complex but rewarding.

## 📚 What We Learned

* **Power of ADK for Multi-Agent Systems:** Gained a deep appreciation for how ADK simplifies the development of complex, collaborative AI systems.
* **Importance of Clear Tool Definitions:** Understood that well-defined `Tool` descriptions and input schemas are crucial for LLMs to effectively utilize them.
* **Iterative Prompt Engineering:** Learned that developing effective agent behavior is an iterative process requiring continuous refinement of prompts and instructions.
* **Cloud API Capabilities:** Deepened our expertise in leveraging Google Cloud APIs for automation and data extraction in real-world scenarios.

## ⏭️ What's Next

* **Automated Execution:** Implement an `ExecutionAgent` (with proper guardrails and approval workflows) to automatically apply approved recommendations using Google Cloud Deployment Manager or custom scripts.
* **Predictive Optimization:** Integrate more advanced Vertex AI capabilities for predictive analytics to anticipate future resource needs or cost spikes, enabling proactive optimization.
* **Broader Service Coverage:** Extend support to optimize more Google Cloud services, such as Cloud SQL, BigQuery, GKE clusters, and networking resources.
* **Customizable Policies:** Allow users to easily define and manage their own custom optimization and compliance policies through a user-friendly interface.
* **Enhanced Reporting:** Develop comprehensive reporting and dashboard features (perhaps using Looker Studio or BigQuery) to visualize cost savings and performance improvements over time.
* **Alerting and Notifications:** Implement proactive alerts for cost anomalies or non-compliant resource usage, integrating with services like Cloud Monitoring Alerts or Pub/Sub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please open an issue in this GitHub repository.
