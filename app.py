from flask import Flask, render_template, request
import os
import docx2txt
import matplotlib
matplotlib.use('Agg')  # Arka planı kullan
import matplotlib.pyplot as plt
import numpy as np
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
from nlp_utils import extract_keywords, compare_cv_with_jobs

# WEB ARAYÜZÜ OLUŞTURMA
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'docx'}

# Geçerli dosya formatını kontrol eden fonksiyon
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Ana sayfa route'u
@app.route('/')
def index():
    return render_template('index.html')

# Dosya yükleme route'u
@app.route('/upload', methods=['POST'])
def upload_cv():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Dosyanın kaydedilmesi
        file.save(filepath)
        
        # Dosya içeriğini çıkarma
        if filename.endswith('.pdf'):
            cv_text = extract_text_from_pdf(filepath)
        elif filename.endswith('.docx'):
            cv_text = extract_text_from_docx(filepath)
        else:
            return "Unsupported file format."

        # Anahtar kelimeleri çıkarma
        cv_keywords = extract_keywords(cv_text)

        # İş ilanları ile karşılaştırma
        job_matches = compare_cv_with_jobs(cv_keywords)

        # Sonuçları görselleştirme
        plot_results(job_matches)

        return render_template('results.html', keywords=cv_keywords, job_matches=job_matches)

# DOCX dosyasındaki metni çıkaran fonksiyon
def extract_text_from_docx(filepath):
    return docx2txt.process(filepath)

# PDF dosyasındaki metni çıkaran fonksiyon
def extract_text_from_pdf(filepath):
    try:
        return extract_text(filepath)
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# Sonuçları görselleştiren fonksiyon
def plot_results(job_matches):
    titles = [job['title'] for job in job_matches]
    scores = [job['match_score'] for job in job_matches]

    plt.figure(figsize=(8, 6))
    plt.barh(titles, scores, color='skyblue')
    plt.xlabel('Match Score (%)')
    plt.title('Job Match Scores')
    plt.xlim(0, 100)

    # Görseli kaydetme
    plt.savefig('static/job_match_scores.png')
    plt.close()

# Flask uygulamasını çalıştırma
if __name__ == '__main__':
    app.run(debug=True)
