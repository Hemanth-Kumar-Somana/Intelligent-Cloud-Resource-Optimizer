# Testing Instructions: Intelligent Cloud Resource Optimizer

This document provides detailed, step-by-step instructions for testing the "Intelligent Cloud Resource Optimizer" multi-agent application. These instructions are designed to help verify the core functionalities of the system, including its ability to monitor Google Cloud resources, analyze for inefficiencies, generate intelligent optimization recommendations, and adhere to predefined policies.

---

## 🎯 Purpose of Testing

The primary goal of these tests is to confirm that the Intelligent Cloud Resource Optimizer successfully:
* Collects relevant data from Google Cloud Monitoring.
* Identifies valid optimization opportunities (e.g., underutilized VMs, idle resources).
* Formulates clear and actionable recommendations.
* Enforces predefined compliance policies.
* Provides a responsive and informative user experience via the ADK Web UI.

---

## ⚙️ Environment Setup

Before you begin testing, ensure your environment is configured as follows:

* **Google Cloud Project:**
    * You must have a Google Cloud Project with **billing enabled**.
    * The following Google Cloud APIs must be enabled in your project:
        * `Vertex AI API`
        * `Cloud Monitoring API`
        * (Optional, but recommended for more realistic data) `Compute Engine API`, `Cloud Storage API`, etc., depending on what specific resources you plan to monitor and optimize.
* **Authentication:**
    * Your local environment (where you run the application) must be authenticated to Google Cloud using Application Default Credentials (ADC).
    * Run: `gcloud auth application-default login`
* **Python Environment:**
    * Ensure you have **Python 3.10+** installed.
    * **Activate a virtual environment.** Navigate to your project's root directory and run:
        ```bash
        python -m venv .venv
        # On macOS/Linux:
        source .venv/bin/activate
        # On Windows CMD:
        .venv\Scripts\activate.bat
        # On Windows PowerShell:
        .venv\Scripts\Activate.ps1
        ```
    * **Install dependencies.** Make sure all required Python libraries are installed. If you have a `requirements.txt` file (as recommended in `README.md`), run:
        ```bash
        pip install -r requirements.txt
        ```
        Otherwise, manually install: `pip install google-adk google-cloud-monitoring google-cloud-billing` (and any other specific libraries your agents/tools use, e.g., `pandas`).
* **Application Code:**
    * Ensure you have the `intelligent-cloud-resource-optimizer` project directory cloned and all source files are correctly placed within the `src/` folder as per the repository blueprint.
* **.env file:**
    * Verify that your `.env` file (in the root directory, alongside `src/`) is correctly configured with your `GOOGLE_CLOUD_PROJECT` ID and `GOOGLE_CLOUD_LOCATION`.
        ```
        GOOGLE_CLOUD_PROJECT=your-gcp-project-id
        GOOGLE_CLOUD_LOCATION=us-central1 # Or your preferred region
        GOOGLE_GENAI_USE_VERTEXAI=True
        ```

---

## ▶️ How to Run the Application for Testing

1.  **Open Terminal:** Open your command-line interface.
2.  **Navigate to Project Root:** Change your current directory to the `intelligent-cloud-resource-optimizer` root folder (the one containing `src/`, `README.md`, etc.).
    ```bash
    cd intelligent-cloud-resource-optimizer
    ```
3.  **Activate Virtual Environment:** (If not already active)
    ```bash
    source .venv/bin/activate # Or the appropriate command for your OS
    ```
4.  **Launch ADK Web UI:** This will start the local ADK developer user interface.
    ```bash
    adk web
    ```
5.  **Open Browser:** Your terminal will display a URL (e.g., `http://localhost:8000`). Open this URL in your web browser.
6.  **Select Agent:** In the top-left corner of the ADK Web UI, use the dropdown menu to select `main_orchestrator_agent`. This is your main entry point for interacting with the multi-agent system.

---

## 🧪 Test Cases

Perform the following test cases to validate the application's functionality. Pay close attention to the chat output and, crucially, the "Events" tab in the ADK Web UI for debugging and observing agent interactions.

---

### **Test Case 1: Identify Underutilized Compute Engine VMs**

* **Objective:** Verify that the system can identify underutilized Compute Engine Virtual Machine instances and suggest appropriate resizing recommendations.
* **Preconditions:**
    * You have at least one running Google Compute Engine VM in your configured Google Cloud Project that has been *consistently underutilized* (e.g., average CPU utilization below 10-20% for the last 24 hours).
    * The application is running, and `main_orchestrator_agent` is selected in the ADK UI.
* **Test Steps:**
    1.  In the chat input box of the ADK Web UI, type:
        `Analyze my Compute Engine VMs for underutilization and recommend cost savings.`
    2.  Press Enter.
* **Expected Results:**
    * **ADK Events Tab:** You should observe the `MainOrchestratorAgent` delegating to the `MonitorAgent` (which calls GCP Monitoring tools), then to the `AnalysisAgent`, and finally to the `RecommendationAgent` and `PolicyAgent`.
    * **Chat Output:** The system should present clear, actionable recommendations for at least one underutilized VM. Example output:
        "VM 'your-vm-name' appears underutilized (Avg CPU: 5%). Consider resizing from `e2-medium` to `e2-small` for an estimated monthly saving of $X.XX. This recommendation is compliant with current policies."
    * **Verification:** Confirm the VM name and the recommended change align with your expectations for an underutilized instance.

---

### **Test Case 2: Check for Idle Cloud Storage Buckets (or other idle resources)**

* **Objective:** Verify the system's ability to detect idle or infrequently accessed Cloud Storage buckets (or similar idle resources like unattached persistent disks, unused static IPs) and recommend appropriate actions.
* **Preconditions:**
    * You have at least one Google Cloud Storage bucket (or unattached persistent disk/unused static IP) in your configured Google Cloud Project that has had *minimal to no activity* (read/write operations) over a significant period (e.g., 30+ days).
    * The application is running, and `main_orchestrator_agent` is selected in the ADK UI.
* **Test Steps:**
    1.  In the chat input box, type:
        `Are there any idle cloud storage buckets or unattached disks I can optimize?`
    2.  Press Enter.
* **Expected Results:**
    * **ADK Events Tab:** Observe the agent workflow involving `MonitorAgent` (fetching storage/disk metrics) and `AnalysisAgent` (identifying idle resources).
    * **Chat Output:** A recommendation should be generated for the idle resource, suggesting deletion or a change in storage class/lifecycle policy. Example output:
        "The Cloud Storage bucket 'my-old-bucket-123' has not been accessed recently. Consider deleting it to save $Y.YY/month, or applying a lifecycle policy to transition to Archive storage. This recommendation is compliant."
        "Unattached Persistent Disk 'unused-disk-xyz' found. Deleting this could save $Z.ZZ/month. This action is policy compliant."
    * **Verification:** Confirm the identified resources are indeed idle and the recommendations are relevant.

---

### **Test Case 3: Policy Enforcement Test (Simulated Policy Violation)**

* **Objective:** Verify that the `PolicyAgent` correctly flags recommendations that violate a predefined policy and explains the violation.
* **Preconditions:**
    * **Crucial:** Temporarily modify your `src/policy_agent.py` or the internal policy rules within your code to include a very simple, testable policy. For this test, let's assume a policy like: **"All production VMs must have at least 2 vCPUs."**
    * You need to have a way for the `RecommendationAgent` to *try* to recommend a production VM be resized to *less than 2 vCPUs*. You might achieve this by:
        * Having a small "production" VM that is highly underutilized.
        * Alternatively, for hackathon demonstration, you could temporarily hardcode the `RecommendationAgent` to generate such a "violating" recommendation for a specific VM.
    * The application is running, and `main_orchestrator_agent` is selected in the ADK UI.
* **Test Steps:**
    1.  In the chat input box, type a query that would trigger a VM optimization for a "production" VM (e.g., `Optimize the 'prod-webserver' VM for cost savings.`).
    2.  (Internally, ensure your agents would generate a recommendation that *violates* the 2 vCPU policy for this specific VM, e.g., suggesting `e2-micro`).
    3.  Press Enter.
* **Expected Results:**
    * **ADK Events Tab:** Observe the flow from `RecommendationAgent` to `PolicyAgent`. The `PolicyAgent`'s output should clearly state a policy violation.
    * **Chat Output:** The system should explicitly state that the recommendation cannot be approved due to a policy violation. Example output:
        "Recommendation for 'prod-webserver': Resize to `e2-micro`. **POLICY VIOLATION:** This recommendation conflicts with the 'All production VMs must have at least 2 vCPUs' policy. Action cannot be approved."
    * **Verification:** Confirm the policy violation is detected and clearly communicated.

---

### **Test Case 4: General Optimization Query**

* **Objective:** Verify that the `MainOrchestratorAgent` can handle a broad optimization query, delegate tasks across multiple resource types, and present a comprehensive set of recommendations.
* **Preconditions:**
    * A mix of Google Cloud resources (e.g., several VMs, multiple storage buckets with varying activity levels) in your GCP project.
    * The application is running and `main_orchestrator_agent` is selected in the ADK UI.
* **Test Steps:**
    1.  In the chat input box, type:
        `What cloud optimizations can I make across all my Google Cloud resources to save money and improve performance?`
    2.  Press Enter.
* **Expected Results:**
    * **ADK Events Tab:** A complex interaction pattern should be visible, with the `MainOrchestratorAgent` orchestrating calls to multiple specialized agents to gather and analyze data from various services.
    * **Chat Output:** The final response should provide a comprehensive summary of various optimization recommendations, potentially covering multiple services (e.g., both VM resizing suggestions, storage tiering recommendations, and idle resource cleanups).
    * **Verification:** The recommendations should be diverse and relevant to your actual GCP setup.

---

### **Test Case 5: Handling Unknown or Out-of-Scope Queries**

* **Objective:** Verify that the system provides a graceful fallback or relevant redirection when presented with queries outside its current scope or understanding.
* **Preconditions:**
    * The application is running and `main_orchestrator_agent` is selected in the ADK UI.
* **Test Steps:**
    1.  In the chat input box, type:
        `Tell me a funny joke about a server rack.`
    2.  Press Enter.
* **Expected Results:**
    * **Chat Output:** The agent should respond gracefully, indicating it cannot fulfill the request as it's outside its area of expertise. Example output:
        "I'm designed to help with Google Cloud resource optimization. How can I assist you with that?"
    * **Verification:** The agent should not crash or provide a nonsensical, irrelevant response.

---

## 💡 General Testing Tips for ADK Applications

* **Utilize the ADK Web UI Debug Panel:** This is your most powerful tool. The "Events" tab on the left-hand side provides a detailed trace of:
    * Which agent is active.
    * The LLM's thought process (`thoughts`).
    * Which tools are being called, along with their inputs and outputs.
    * Intermediate responses and state changes.
    * Use this to understand why an agent makes a certain decision or if a tool is returning unexpected data.
* **Inspect Tool Outputs:** If an agent isn't behaving as expected, often the issue lies in the data retrieved by your custom tools from Google Cloud APIs. Check the raw outputs within the "Events" tab.
* **Iterate on Prompts and Tool Descriptions:** Clearer, more precise prompts for your `LlmAgent` and detailed `description` fields for your `Tool` objects are crucial for optimal agent behavior. Refine them based on observed agent performance during testing.
* **Monitor Terminal Logs:** Keep an eye on the terminal where you ran `adk web` for any Python stack traces or detailed logging messages from your agents. These can pinpoint deeper code issues.
* **Simulate Google Cloud Resources (for rapid iteration):** If setting up complex GCP scenarios is time-consuming, consider adding a flag or configuration to your `MonitorAgent`'s tools to return mocked or simulated Google Cloud data for quicker local testing. Remember to revert this for a final deployment!
* **Test Edge Cases:** While not all included above, think about edge cases:
    * What if there are no VMs?
    * What if all resources are perfectly optimized?
    * What if a required API call fails?

By following these instructions, you can effectively test and demonstrate the capabilities of your Intelligent Cloud Resource Optimizer.
