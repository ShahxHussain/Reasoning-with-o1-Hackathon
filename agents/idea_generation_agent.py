# idea_generation_agent.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")  # Fetch API key from environment variable

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

    response = openai.ChatCompletion.create(
        model="o1-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.7
    )

    ideas = response.choices[0].message['content'].strip()
    return ideas

# Example usage
if __name__ == "__main__":
    literature_review = "Your literature review content goes here."
    subject_area = "quantum computing and information theory"
    ideas = generate_ideas(literature_review, subject_area)
    print(ideas)
