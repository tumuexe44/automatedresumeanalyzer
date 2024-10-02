# automatedresumeanalyzer
Automated Resume Analyzer
This project is an automated resume analysis tool designed to evaluate job applications. It allows users to upload their resumes, analyze the content, and compare it with job listings. Below is a summary of the main components and functionalities of the project.

Main Components:
Flask Web Framework: Flask is used to create the web interface, enabling users to upload resume files and view analysis results.

File Upload: Users can upload PDF and DOCX files. The uploaded file is checked to ensure it is in the appropriate format.

Text Extraction:

The docx2txt library is used to extract text from DOCX files.
The pdfminer library is used to extract text from PDF files.
Keyword Extraction: Keywords are extracted from the resume text and compared with job listings. This process is carried out using functions defined in the nlp_utils module, such as extract_keywords and compare_cv_with_jobs.

Results Visualization:

Matplotlib is used to visualize the matching scores between the job listings and the resumes.
A bar chart is created to display the matching percentages between job listings and resumes.
Display Results: Users can see the keywords extracted from their resumes and the matching results.

Technologies Used:
Python: The primary programming language for the project.
Flask: Used for developing the web interface.
Docx2txt: Used for extracting text from DOCX files.
PDFMiner: Used for extracting text from PDF files.
Matplotlib: Used for data visualization.
NumPy: Used for numerical operations.
Usage Instructions:
Ensure that the necessary libraries are installed.
Start the Flask application (e.g., python app.py).
Navigate to http://127.0.0.1:5000/ in your web browser.
Upload your resume file and view the analysis results.
Conclusion:
This project helps users analyze their resumes and assess their compatibility with job listings. It provides insights for users to prepare better job applications.
