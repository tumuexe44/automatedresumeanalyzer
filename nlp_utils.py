import spacy
import json

# spaCy modelini yükleyin
nlp = spacy.load('en_core_web_sm')

def extract_keywords(text):
    # spaCy ile metin analiz etme
    doc = nlp(text)
    keywords = set()  # Anahtar kelimeleri kümeye eklemek için set kullanıyoruz

    # Önemli isimler, fiiller ve isim tamlamalarını çıkartma
    for ent in doc.ents:
        keywords.add(ent.text.lower())

    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN', 'ADJ', 'VERB', 'ADV']:
            keywords.add(token.text.lower())

    return list(keywords)  # Liste yerine küme döndürüyoruz

def compare_cv_with_jobs(cv_keywords, job_file='jobs.json'):
    # JSON Dosyasını okuma
    with open(job_file, 'r') as f:
        jobs = json.load(f)
    results = []
    threshold = 50  # Eşleşme eşiği
    
    results = []
    for job in jobs:
        job_keywords = set(job['skills_required'])
        
    # Anahtar kelimeleri yazdırma
        print("CV Keywords:", cv_keywords)
        print("Job Keywords:", job_keywords)

        # cv_keywords bir liste olabilir, bu yüzden kümeye dönüştürün
        if isinstance(cv_keywords, list):
            cv_keywords = set(cv_keywords)
        
        common_keywords = cv_keywords & job_keywords
        match_score = len(common_keywords) / len(job_keywords) * 100 if job_keywords else 0

        if match_score >= threshold:
            results.append({
            "title": job["title"],
            "description": job["description"],
            "match_score": match_score
        })
    return results

# Örnek kullanım
cv_text = "Experienced software engineer with skills in Python, machine learning, and data analysis."
keywords = extract_keywords(cv_text)
print("Extracted Keywords:", keywords)
