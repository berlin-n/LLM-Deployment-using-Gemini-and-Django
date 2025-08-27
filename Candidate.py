class Candidate:
    def __init__(self, name, education, experience, skills, projects, achievements, jobDescription, jobSource, companyName, hiringManager):
        self.name = name
        self.education = education
        self.experience = experience
        self.skills = skills
        self.projects = projects
        self.achievements = achievements
        self.jobDescription = jobDescription
        self.jobSource = jobSource
        self.companyName = companyName
        self.hiringManager = hiringManager


    def generatePrompt(self) -> str:
        prompt = f"You are an expert career coach and recruiter. Write a complete, professional cover letter for the following candidate, using the provided information. Do not include placeholders; use the actual candidate name and details provided.\n\nThe cover letter must be:\n- Between 250–350 words\n- Written in a confident, professional tone\n- Structured with greeting, 2–3 body paragraphs, and a closing signature with the candidate’s name\n- Tailored to the specific job description\nDo NOT include any placeholders or square brackets (e.g., [Your Name]).\nIf jobSource is not provided, omit mentioning where the job was found.\nIf hiring manager details are missing, simply use 'Dear Hiring Team'. If companyName is missing, refer to it only as 'your company'.\nReturn ONLY the final cover letter text with no extra commentary.\n\nCandidate Information:\nName: {self.name}\nEducation: {self.education}\nExperience: {self.experience}\nSkills: {self.skills}\nProjects: {self.projects}\nAchievements: {self.achievements}\nJob Description: {self.jobDescription}\nJob Source: {self.jobSource}\nCompany Name: {self.companyName}\nHiring Manager: {self.hiringManager}"
        return prompt
    
if __name__ == "__main__":
    candidate = Candidate("Efe Kwode", "BSc Computer Science, Baze University, 2024", "Machine Learning Intern at Godaffi Softwares (Oct 2023 – Mar 2024): Built ML models for forecasting, API development with Django. Infotech Intern at CFAO Motors Nigeria (Jan 2023 – May 2023): Networking, troubleshooting, data analysis", "Python, SQL, JavaScript, Streamlit, Django, Supabase, scikit-learn, Pandas, NumPy, Machine Learning, Recommender Systems", "Book Recommendation System (Matrix Factorization, Django, Goodreads dataset), Inventory Management System (Streamlit, Supabase), Kaggle Notebooks (EDA, classification, regression)", "Great Learning: Data Science Foundations, Python Fundamentals. Kaggle: Intermediate Machine Learning. Green Gaming: AI for Sustainability", "Looking for a data scientist to build scalable AI solutions", "", "", "")
    print(candidate.generatePrompt())