# pr-review-agent
Phase 1
│
├── Step 1: Project setup ✅
├── Step 2: FastAPI server
├── Step 3: GitHub integration
├── Step 4: Ollama integration
├── Step 5: Review generation
└── Step 6: Streamlit UI

## 🚀 Current Progress (Phase 1)

### ✅ Project Initialization

- Set up a modular and scalable project structure following separation of concerns.
- Initialized a Python virtual environment and dependency management using `requirements.txt`.
- Configured Git repository with a dedicated feature branch workflow.
- Added `.gitignore` to exclude virtual environments, environment variables, cache files, and IDE-specific files.

### ✅ Backend Foundation

- Built the initial FastAPI application.
- Added centralized configuration management using environment variables (`.env`).
- Created a health check endpoint (`/health`) to verify service availability.
- Enabled automatic API documentation using FastAPI Swagger UI (`/docs`).

### ✅ Project Organization

Implemented the following project structure:

```text
app/
├── api/
├── core/
├── models/
├── prompts/
├── services/
└── main.py

ui/
tests/
```

This structure separates API routes, business logic, configuration, models, prompts, and future UI components, making the project easier to extend and maintain.

### 🔜 Next Milestone

- Integrate GitHub API.
- Fetch Pull Request metadata and changed files.
- Build the review service to process PR diffs before connecting the local LLM (Ollama).

✅ Phase 2 – GitHub Integration
Implemented end-to-end GitHub Pull Request integration.
Features completed
Integrated GitHub API using PyGithub.
Added request and response models using Pydantic.   
Implemented GitHub Personal Access Token authentication.
Parsed GitHub Pull Request URLs.
Retrieved Pull Request metadata.
Retrieved changed files and unified diffs (patch).
Exposed a POST /review API endpoint.
Validated the complete workflow using FastAPI Swagger.

### ✅ Current Architecture

Client
   │
   ▼
FastAPI
   │
   ▼
GitHub Service
   │
   ▼
GitHub API
   │
   ▼
Structured JSON Response

✅ Phase 3 – AI-Powered PR Review
Integrated a local Large Language Model (LLM) to automatically review Pull Requests.
Features Completed
Integrated Ollama for local LLM inference
Added LLMService for AI communication
Added PromptService for prompt management
Added ReviewService to orchestrate the review workflow
Created reusable reviewer prompt templates
Generated AI-powered code review comments from GitHub diffs
Added review execution timing
Skipped unsupported or non-reviewable files
Returned structured AI review responses through the API

✅ Phase 4 - Multi-Agent AI Review
## 

### Features Added

- Introduced a multi-agent architecture for PR reviews.
- Added specialized AI agents:
  - Security Agent
  - Performance Agent
  - Readability Agent
- Added a Summary Agent to consolidate all agent feedback into an executive summary.
- Refactored PromptService to dynamically load prompts.
- Enhanced ReviewService to orchestrate multiple AI agents.
- Updated API response schema to include agent-wise reviews and an overall summary.

### Sample Response

- Executive Summary
- Security Review
- Performance Review
- Readability Review

## Phase 5 – Advanced Review Pipeline

### Features Added

- Executed specialist AI review agents concurrently using `ThreadPoolExecutor`.
- Introduced automated risk assessment with risk score and severity level.
- Added a dedicated `ReportService` for Markdown report generation.
- Generated human-readable review reports under the `reports/` directory.
- Improved service separation by keeping orchestration, prompt management, and report generation independent.

### Sample Output

- Executive Summary
- Risk Assessment
- Security Review
- Performance Review
- Readability Review
- Generated Markdown Report

✅ Phase 6: Interactive Streamlit dashboard
Enter PR URL
Trigger AI review
Display executive summary
Show risk assessment
Expandable agent reviews
Download Markdown report