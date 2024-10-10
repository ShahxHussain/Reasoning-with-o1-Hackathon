document.getElementById('generateIdeasBtn').addEventListener('click', generateIdeas);
document.getElementById('validateIdeasBtn').addEventListener('click', validateIdeas);
document.getElementById('draftApplicationBtn').addEventListener('click', draftApplication);

async function generateIdeas() {
    const literatureReview = document.getElementById('literatureReview').value;
    const response = await fetch('http://localhost:5000/generate_ideas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ literature_review: literatureReview })
    });
    const data = await response.json();
    const ideasList = document.getElementById('ideasList');
    ideasList.innerHTML = '';
    data.ideas.forEach((idea, index) => {
        ideasList.innerHTML += `<li>${index + 1}: ${idea}</li>`;
    });
}

async function validateIdeas() {
    const response = await fetch('http://localhost:5000/validate_ideas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    });
    const data = await response.json();
    const validationResults = document.getElementById('validationResults');
    validationResults.innerHTML = '';
    data.results.forEach(result => {
        validationResults.innerHTML += `<li>${result.Idea}: ${result.Original} - ${result.Explanation}</li>`;
    });
}

async function draftApplication() {
    const selectedIdea = document.querySelector('#ideasList li')?.innerText || '';
    const subjectArea = 'Your Subject Area Here';  // Replace with actual subject area
    const response = await fetch('http://localhost:5000/draft_application', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ idea: selectedIdea, subject_area: subjectArea })
    });
    const data = await response.json();
    document.getElementById('draftApplication').value = data.application;
}
