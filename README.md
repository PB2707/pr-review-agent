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