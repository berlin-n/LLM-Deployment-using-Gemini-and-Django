from Candidate import Candidate
from GeminiGenerator import GeminiGenerator
from CoverLetterService import CoverLetterService

candidate1 = Candidate("Efe Kwode",
    "BSc Computer Science, Baze University, 2024",
    "Machine Learning Intern at Godaffi Softwares (Oct 2023 – Mar 2024): Built ML models for forecasting, API development with Django. Infotech Intern at CFAO Motors Nigeria (Jan 2023 – May 2023): Networking, troubleshooting, data analysis",
    "Python, SQL, JavaScript, Streamlit, Django, Supabase, scikit-learn, Pandas, NumPy, Machine Learning, Recommender Systems",
    "Book Recommendation System (Matrix Factorization, Django, Goodreads dataset), Inventory Management System (Streamlit, Supabase), Kaggle Notebooks (EDA, classification, regression)",
    "Great Learning: Data Science Foundations, Python Fundamentals. Kaggle: Intermediate Machine Learning. Green Gaming: AI for Sustainability",
    "Looking for a data scientist to build scalable AI solutions",
    "", "", "")

service = CoverLetterService(GeminiGenerator("gemini-2.5-flash"))
print(service.generateTokenUsage(candidate1))


