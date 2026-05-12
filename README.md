# ExcuseAI

An entertaining multi-agent AI web app where users enter a situation and receive believable, human-like excuses generated collaboratively by multiple AI agents.

## Features
- **Multi-Agent Orchestration:** Powered by CrewAI with 5 specialized agents.
- **FastAPI Backend:** High-performance Python API.
- **React Frontend:** Modern, futuristic UI built with Vite, Tailwind CSS 4, and shadcn/ui.
- ** believable results:** Generates the excuse, emotional justification, and multi-channel messages (WhatsApp/Email).

## Tech Stack
- **Frontend:** React, TypeScript, Vite, Tailwind CSS 4, shadcn/ui, Lucide Icons.
- **Backend:** FastAPI, CrewAI, Pydantic.
- **LLM:** OpenAI (gpt-4o-mini) or OpenRouter.

## Getting Started

### Prerequisites
- Node.js & npm
- Python 3.12+

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Add your `OPENAI_API_KEY`.
5. Start the backend:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

## Architecture
ExcuseAI uses a sequential process where agents collaborate:
1. **Context Analyzer:** Understands the social stakes.
2. **Excuse Writer:** Generates the core narrative.
3. **Humanizer:** Adds emotional depth and natural phrasing.
4. **Consistency Checker:** Audits for logical flaws.
5. **Message Formatter:** Packages the result for different channels.
