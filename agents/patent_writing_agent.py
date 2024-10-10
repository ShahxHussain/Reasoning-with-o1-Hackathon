# patent_writing_agent.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def draft_patent_application(idea, subject_area):
    prompt = f"""
    You are a skilled patent attorney with expertise in {subject_area}. Draft a patent application for the following invention, including the following sections:
    1. Title of the Invention
    2. Abstract: (150-250 words summarizing the invention)
    3. Background of the Invention: Explain the problem or gap in current technology.
    4. Summary of the Invention: Provide an overview of how the invention addresses the problem.
    5. Detailed Description: Explain the invention in detail, including embodiments and variations.
    6. Claims: List the legal claims defining the scope of patent protection.

    Invention Description:
    {idea}
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5
    )

    return response.choices[0].text.strip()

# Example usage
subject_area = "renewable energy technologies"
idea_description = "Your idea description here."
patent_application = draft_patent_application(idea_description, subject_area)
print(patent_application)
