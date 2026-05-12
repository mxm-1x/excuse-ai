# PRD — AI Excuse Generator Company Simulator

## Project Name
**ExcuseAI**

An entertaining multi-agent AI web app where users enter a situation and receive believable, human-like excuses generated collaboratively by multiple AI agents.

---

## 1. Product Overview

### Goal
Build a creative AI-powered application using CrewAI where multiple AI agents collaborate to generate:
- Realistic excuses
- Emotional justification
- Apology messages
- Follow-up responses
- Believable timelines

The app should feel fun, polished, and slightly absurd while showcasing real multi-agent orchestration.

## 2. Core Concept
Instead of one LLM generating everything, multiple specialized agents collaborate.

**Example:**

**User Input**
- **Situation:** Missed internship meeting
- **Tone:** Professional
- **Urgency:** High

**AI Output**
- **Excuse:** "My internet completely crashed during a power fluctuation..."
- **Apology Message:** "Hi, I'm extremely sorry for missing the meeting..."
- **If They Ask Follow-Up Questions:** "I contacted my ISP immediately and restored access..."

## 3. Target Users
- Developers learning CrewAI
- AI enthusiasts
- Hackathon participants
- Social media demo creators
- People exploring multi-agent systems

## 4. Tech Stack
- **Frontend:** React (Vite) / Next.js, Tailwind CSS, shadcn/ui
- **Backend:** FastAPI or Next.js API routes
- **AI Framework:** CrewAI
- **LLM:** openrouter
- **Optional:** Firebase/Supabase for history storage

## 5. MVP Features

### 1. Excuse Generation Form
Inputs:
- Situation
- Tone
- Urgency
- Relationship

### 2. Multi-Agent Workflow
Agents collaborate to produce:
- Main excuse
- Emotional reasoning
- Apology message
- Backup explanation
- Follow-up answers

### 3. Final Structured Response
Output sections:
- Main Excuse
- Emotional Justification
- Message Version
- Emergency Backup
- Risk Score

### 4. Copy Buttons
Users can copy:
- Excuse
- Email
- Text message

### 5. History Panel (Optional MVP+)
Store previous excuses locally.

## 6. User Inputs
- **Situation:** Text input (e.g., missed class, late assignment, forgot birthday, skipped meeting)
- **Tone:** Dropdown (Professional, Casual, Dramatic, Funny, Emotional)
- **Urgency:** Slider (Low, Medium, High)
- **Relationship:** Dropdown (Boss, Friend, Teacher, Partner, Parent)

## 7. Multi-Agent Architecture

### Agent 1 — Context Analyzer
- **Responsibility:** Understand seriousness, social context, and acceptable excuse types.
- **Output:** Structured context summary.

### Agent 2 — Excuse Writer
- **Responsibility:** Generate believable excuse.
- **Requirements:** Realistic, concise, tone-matching.

### Agent 3 — Humanizer Agent
- **Responsibility:** Make response feel emotionally authentic.
- **Adds:** Hesitation, natural phrasing, realistic emotions.

### Agent 4 — Consistency Checker
- **Responsibility:** Detect logical inconsistencies, unrealistic details, and contradictions.
- **Returns:** Credibility score, improved version.

### Agent 5 — Message Formatter
- **Responsibility:** Generate WhatsApp version, Email version, short apology, and follow-up answers.

## 8. CrewAI Workflow
```text
User Input
   ↓
Context Analyzer
   ↓
Excuse Writer
   ↓
Humanizer Agent
   ↓
Consistency Checker
   ↓
Message Formatter
   ↓
Final Output
```

## 9. Frontend Pages

### Home Page
Contains:
- Hero section
- Form
- Generate button

### Results Section
Cards for:
- Main Excuse
- Text Message
- Email
- Follow-Up Responses
- Risk Score

## 10. UI/UX Requirements
- **Design Style:** Modern, playful, dark mode friendly, slightly futuristic.
- **Colors:** Primary (purple, black, white).
- **Animations:** Typing animation, loading states, agent processing visualization.

## 11. Loading Experience
While generating:
1. Analyzing situation...
2. Creating believable excuse...
3. Humanizing response...
4. Checking inconsistencies...
5. Generating messages...

## 12. API Architecture

### Endpoint
`POST /api/generate`

**Request:**
```json
{
  "situation": "Missed internship meeting",
  "tone": "Professional",
  "urgency": "High",
  "relationship": "Boss"
}
```

**Response:**
```json
{
  "main_excuse": "...",
  "emotional_reasoning": "...",
  "whatsapp_message": "...",
  "email_message": "...",
  "follow_up_answers": [],
  "risk_score": 7.8
}
```

## 13. Suggested Folder Structure
```text
project/
├── frontend/
│   ├── src/
│   ├── components/
│   ├── lib/
├── backend/
│   ├── agents/
│   ├── crews/
│   ├── tasks/
│   ├── tools/
│   ├── api/
├── shared/
├── prompts/
└── README.md
```

## 14. Agent Definitions
**Example — Excuse Writer Agent**
```python
Agent(
    role="Professional Excuse Writer",
    goal="Create believable and context-aware excuses",
    backstory="Expert in generating realistic human excuses",
    verbose=True
)
```

## 15. Prompt Engineering Requirements
Prompts must:
- Avoid repetitive wording
- Sound natural
- Avoid overdramatic excuses
- Maintain realism
- Adapt to tone

## 16. Error Handling
Handle:
- Empty inputs
- API failures
- Timeout issues
- Malformed responses
- Show friendly UI errors

## 17. Future Features (V2 Ideas)
- Voice excuses
- Celebrity excuse mode
- Fake timeline generator
- Excuse difficulty level
- AI lie detector
- Meme mode

## 18. Performance Goals
- **Target:** Response under 10 seconds
- Mobile responsive
- Smooth loading UX

## 19. Security
- Rate limiting
- API key protection
- Sanitize inputs

## 20. Deliverables
The AI code editor should generate:
- **Frontend:** Responsive UI, form components, result cards, loading animations.
- **Backend:** CrewAI workflow, API endpoint, agent/task setup.
- **AI Integration:** OpenAI integration, environment variable setup.
- **Documentation:** README, setup guide, environment instructions.

## 21. Environment Variables
`OPENAI_API_KEY=`

## 22. Success Criteria
The app is successful if:
- Multiple agents collaborate correctly.
- Excuses feel believable.
- UI feels polished.
- Users can generate/share outputs easily.
- CrewAI orchestration is clearly demonstrated.