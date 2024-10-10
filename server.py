# server.py

import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from agents.idea_generation_agent import generate_ideas
from agents.patent_search_agent import run_patent_search_agent
from agents.patent_writing_agent import draft_patent_application

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate_ideas', methods=['POST'])
def generate_ideas_route():
    data = request.json
    literature_review = data.get('literature_review')
    subject_area = "Your Subject Area Here"  # Replace with the appropriate subject area
    ideas = generate_ideas(literature_review, subject_area)
    return jsonify({"ideas": ideas.split('\n')})

@app.route('/validate_ideas', methods=['POST'])
def validate_ideas_route():
    run_patent_search_agent()  # Assumes this function saves results to a JSON file
    with open('data/patent_validation.json', 'r', encoding='utf-8') as f:
        results = json.load(f)
    return jsonify({"results": results})

@app.route('/draft_application', methods=['POST'])
def draft_application_route():
    data = request.json
    idea = data.get('idea')
    subject_area = data.get('subject_area')
    application = draft_patent_application(idea, subject_area)
    return jsonify({"application": application})

if __name__ == '__main__':
    app.run(port=5000)
