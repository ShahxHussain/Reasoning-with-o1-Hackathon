# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# EPO API Credentials
EPO_CLIENT_ID = os.getenv("EPO_CLIENT_ID")
EPO_CLIENT_SECRET = os.getenv("EPO_CLIENT_SECRET")

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# File Paths
IDEAS_OUTPUT_FILE = 'data/ideas.json'
PATENT_VALIDATION_OUTPUT_FILE = 'data/patent_validation.json'
