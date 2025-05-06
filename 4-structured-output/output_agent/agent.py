from google.adk.agents.llm_agent import LlmAgent
from pydantic import BaseModel, Field

class Feedback(BaseModel):
    """Feedback model for structured output."""
    question: str = Field(
        description="The question asked to the agent."
    )
    answer: str = Field(
        description="The answer provided by the agent."
    )

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='feedback_agent',
    instruction=
        """You are a feedback collection agent. Based on the company given by the user, you need to come up with atleast 3 mock feedback question and their relevant answers. 
        The feedback should be in the format of a JSON object with the following fields:
        {
            "question": "<question>",
            "answer": "<answer>"
        }
        where:
        - question: The question asked to the agent.
        - answer: The answer provided by the agent.
        """,
    description="Feedback collection agent",
    output_schema=Feedback, #Output schema for the agent (Pydantic model)
    output_key="feedback", #Key to store the output in the response
)