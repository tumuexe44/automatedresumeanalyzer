import json
import spacy

def compare_cv_with_jobs(cv_keywords, job_file='jobs.json'):
    # JSON Dosyasını okuma
    with open(job_file, 'r') as f:
        jobs = json.load(f)

    results = [
        {"title": "Software Engineer", "match_score": 85},
    {"title": "Data Scientist", "match_score": 75},
]

    for job in jobs:
        job_keywords = set(job['skills_required'])
        common_keywords = cv_keywords & job_keywords
        match_score = len(common_keywords) / len(job_keywords) * 100

        results.append({
            "title": job["title"],
            "description": job["description"],
            "match_score": match_score
        })

        return results

nlp = spacy.load('en_core_web_sm')
def extract_keywords(text):
    doc = nlp(text)
    keywords = set()
    
    for ent in doc.ents:
        keywords.add(ent.text.lower())

    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN', 'ADJ', 'VERB']:
            keywords.add(token.text.lower())

    return list(keywords)

job_matches = [
    {"title": "Software Engineer", "match_score": 75},
    {"title": "Data Scientist", "match_score": 85},
    {"title": "DevOps Engineer", "match_score": 65},
]


# Örnek Bulma
cv_text = "Experienced software engineer with skills in Python, machine learning, and data analysis."
cv_keywords = set(extract_keywords(cv_text))

job_matches = compare_cv_with_jobs(cv_keywords)
print("Job Matches:", job_matches)
