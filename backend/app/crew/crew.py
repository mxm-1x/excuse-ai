from crewai import Crew, Process
from .agents import ExcuseAgents
from .tasks import ExcuseTasks
from ..models import ExcuseResponse

class ExcuseCrew:
    def __init__(self, situation, relationship, tone, urgency):
        self.situation = situation
        self.relationship = relationship
        self.tone = tone
        self.urgency = urgency

    def run(self):
        agents = ExcuseAgents()
        tasks = ExcuseTasks()

        # Consolidated Agents
        architect = agents.architect_agent()
        auditor = agents.auditor_agent()

        # Consolidated Tasks
        task1 = tasks.creative_development_task(architect, self.situation, self.relationship, self.tone, self.urgency)
        task2 = tasks.review_and_format_task(auditor)

        # Crew
        crew = Crew(
            agents=[architect, auditor],
            tasks=[task1, task2],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return result
