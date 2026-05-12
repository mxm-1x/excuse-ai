from crewai import Task
from .agents import ExcuseAgents
from ..models import ExcuseResponse

class ExcuseTasks:
    def creative_development_task(self, agent, situation, relationship, tone, urgency):
        return Task(
            description=f"""1. Analyze the social stakes of the situation: '{situation}' for a {relationship}.
            2. Draft a believable excuse with a {tone} tone and {urgency}/100 urgency.
            3. Humanize the text with natural speech patterns and appropriate emotional weight.""",
            expected_output="A structured draft containing the primary excuse and the emotional strategy used.",
            agent=agent
        )

    def review_and_format_task(self, agent):
        return Task(
            description="""1. Audit the excuse for logical consistency and credibility (assign a score 0-10).
            2. Format the finalized excuse into:
               - A WhatsApp/Text message.
               - A formal/styled Email.
            3. Generate 3 likely follow-up questions and their best defensive answers.""",
            expected_output="""A structured response containing:
            - main_excuse: The finalized audited excuse.
            - emotional_reasoning: Explanation of the strategy.
            - whatsapp_message: Text version.
            - email_message: Email version.
            - follow_up_answers: List of question/answer strings.
            - risk_score: Credibility score from 0.0 to 10.0.""",
            agent=agent,
            output_pydantic=ExcuseResponse
        )
