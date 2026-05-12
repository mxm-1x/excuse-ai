from crewai import Agent, LLM
from ..core.config import settings
import os

# Configure custom LLM if using OpenRouter or custom OpenAI settings
llm = None
if settings.OPENROUTER_API_KEY:
    model_name = settings.OPENROUTER_MODEL_NAME
    if not model_name.startswith("openrouter/"):
        model_name = f"openrouter/{model_name}"
    
    llm = LLM(
        model=model_name,
        api_key=settings.OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )
elif settings.OPENAI_API_KEY:
    llm = LLM(
        model=settings.OPENAI_MODEL_NAME,
        api_key=settings.OPENAI_API_KEY
    )

class ExcuseAgents:
    def architect_agent(self):
        return Agent(
            role="Creative Excuse Architect",
            goal="Analyze the situation and draft a highly believable, emotionally authentic excuse.",
            backstory="""You are a master of social psychology and creative writing. 
            You can quickly assess the social stakes of a situation and weave a narrative that is both realistic and emotionally resonant. 
            Your writing feels naturally human, including subtle indicators of stress or casualness appropriate to the relationship.""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def auditor_agent(self):
        return Agent(
            role="Credibility & Format Auditor",
            goal="Verify the excuse's logic and format it for multiple communication channels.",
            backstory="""You have a detective's eye for logical consistency and an expert's grasp of digital communication styles. 
            You ensure no excuse has 'holes' that could be discovered, and you perfectly adapt the message for WhatsApp, Email, and follow-up defense.""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
