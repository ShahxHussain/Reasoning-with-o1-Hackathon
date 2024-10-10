# idea_generation_agent.py

import openai

from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_ideas(literature_review, subject_area):
    prompt = f"""
    You are an expert researcher in the field of {subject_area}. Based on the following literature review, generate a list of 10 innovative and feasible scientific research ideas that build upon the existing knowledge. Each idea should be:
    - Original and not a repetition of existing studies.
    - Specific and clearly defined.
    - Potentially impactful in advancing the field.

    Literature Review:
    {literature_review}

    Provide the ideas in a numbered list, with each idea described in approximately 150 words.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.7
    )

    ideas = response.choices[0].text.strip()
    return ideas

# Example usage
literature_review = "Your literature review content goes here."
subject_area = "quantum computing and information theory"
ideas = generate_ideas(literature_review, subject_area)
print(ideas)
