from Candidate import Candidate
from GeminiGenerator import GeminiGenerator

generator = GeminiGenerator("gemini-2.5-flash")

def generateCoverLetters(candidates: list[Candidate]):
    coverLetters = []
    for candidate in candidates:
        prompt = candidate.generatePrompt()
        coverLetter = generator.generate(prompt)
        coverLetters.append({
            "name": candidate.name,
            "coverLetter": coverLetter
        })
    return coverLetters
    

if __name__ == '__main__':
    candidates = [
        Candidate("Efe Kwode",
        "BSc Computer Science, Baze University, 2024",
        "Machine Learning Intern at Godaffi Softwares (Oct 2023 – Mar 2024): Built ML models for forecasting, API development with Django. Infotech Intern at CFAO Motors Nigeria (Jan 2023 – May 2023): Networking, troubleshooting, data analysis",
        "Python, SQL, JavaScript, Streamlit, Django, Supabase, scikit-learn, Pandas, NumPy, Machine Learning, Recommender Systems",
        "Book Recommendation System (Matrix Factorization, Django, Goodreads dataset), Inventory Management System (Streamlit, Supabase), Kaggle Notebooks (EDA, classification, regression)",
        "Great Learning: Data Science Foundations, Python Fundamentals. Kaggle: Intermediate Machine Learning. Green Gaming: AI for Sustainability",
        "Looking for a data scientist to build scalable AI solutions",
        "", "", ""),
        Candidate("John",
        "Senior Secondary School Certificate (SSCE) - Wellspring College",
        "",
        "UI/UX Design, Wireframing & Prototyping (Figma, Adobe XD), User Research & Testing, Visual Design & Branding, Responsive Web Design, Problem-Solving & Critical Thinking",
        "School Social Club Website (Personal Project) - Designed a user-friendly website for a school social club to improve event organization and engagement.Focused on creating a simple, clean, and functional UI for students and staff. Eco-Friendly Booking Website (Personal Project) - Designed a landing page that enables users to book eco-friendly travel locations, reducing carbon footprints. Inspired by an article about travelers struggling to find sustainable destinations.",
        "",
        "Looking for a UI/UX designer to pilot designs for software team",
        "", "", ""),
    ]

    coverLetters = generateCoverLetters(candidates)
    for coverLetter in coverLetters: # type: ignore
        print(f"Cover letter for {coverLetter['name']}:\n")
        print(coverLetter['coverLetter'])
        print("=" * 60)