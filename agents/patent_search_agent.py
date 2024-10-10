# agents/patent_search_agent.py

import json
from utils.patent_search_utils import search_patents_epo
from config import IDEAS_OUTPUT_FILE, PATENT_VALIDATION_OUTPUT_FILE

def run_patent_search_agent():
    with open(IDEAS_OUTPUT_FILE, 'r', encoding='utf-8') as f:
        ideas = json.load(f)
    
    validation_results = []
    for idx, idea in enumerate(ideas, 1):
        print(f"Validating Idea {idx}: {idea}")
        is_original = search_patents_epo(idea)
        originality = 'Yes' if is_original else 'No'
        explanation = 'No similar patents found.' if is_original else 'Similar patents exist.'

        validation_results.append({
            'Idea': idea,
            'Original': originality,
            'Explanation': explanation
        })
    
    with open(PATENT_VALIDATION_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(validation_results, f, ensure_ascii=False, indent=4)
    
    print(f"Patent validation completed. Results saved to '{PATENT_VALIDATION_OUTPUT_FILE}'.")

if __name__ == "__main__":
    run_patent_search_agent()
