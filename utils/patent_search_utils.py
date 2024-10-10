# utils/patent_search_utils.py

import requests
from config import EPO_CLIENT_ID, EPO_CLIENT_SECRET
from urllib.parse import quote

def get_epo_access_token():
    url = 'https://ops.epo.org/3.2/auth/accesstoken'
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, data=data, auth=(EPO_CLIENT_ID, EPO_CLIENT_SECRET))
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print(f"Failed to get access token: {response.status_code}")
        return None

def search_patents_epo(idea_description):
    access_token = get_epo_access_token()
    if not access_token:
        return None

    query = construct_patent_query(idea_description)
    encoded_query = quote(query)
    url = f'https://ops.epo.org/3.2/rest-services/published-data/search/biblio/?q={encoded_query}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return analyze_patent_results(data)
    else:
        print(f"Patent search failed: {response.status_code}")
        return None

def construct_patent_query(idea_description):
    keywords = extract_keywords(idea_description)
    return ' AND '.join(keywords)

def extract_keywords(text):
    words = text.split()
    return [word for word in words if len(word) > 3][:5]

def analyze_patent_results(data):
    total_results = data['ops:world-patent-data']['ops:biblio-search']['@total-result-count']
    return int(total_results) == 0  # True if no similar patents found
