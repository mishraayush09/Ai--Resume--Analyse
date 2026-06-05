import streamlit as st
import PyPDF2
import plotly.graph_objects as go
import re

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="wide"
)

# ================= TITLE ================= #

st.title("AI Resume Screening Dashboard")

st.write(
    "Upload a valid resume and compare it with the job description using AI-powered ATS screening."
)

st.divider()

# ================= INPUT SECTION ================= #

col1, col2 = st.columns(2)

with col1:

    st.subheader("Upload Resume")

    resume = st.file_uploader(
        "Upload Resume (PDF Only)",
        type=["pdf"]
    )

with col2:

    st.subheader("Paste Job Description")

    job_description = st.text_area(
        "Paste Complete Job Description",
        height=320,
        placeholder="""
Job Title: Data Analyst

Company: ABC Technologies

Responsibilities:
- Analyze business data
- Create dashboards
- Generate reports

Required Skills:
- Python
- SQL
- Power BI
- Tableau
- Excel

Experience:
- 1+ years preferred

Location:
- Bangalore
"""
    )

st.divider()

# ================= BUTTON ================= #

analyze = st.button("Analyze Resume")

# ================= CAREER DATA ================= #

career_data = {

    "Data Analyst": {
        "skills": [
            "python",
            "sql",
            "power bi",
            "tableau",
            "excel",
            "analytics",
            "data visualization"
        ]
    },

    "AI/ML Engineer": {
        "skills": [
            "python",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "nlp",
            "pandas"
        ]
    },

    "Java Full Stack Developer": {
        "skills": [
            "java",
            "spring boot",
            "react",
            "javascript",
            "html",
            "css",
            "sql"
        ]
    },

    "Backend Developer": {
        "skills": [
            "python",
            "django",
            "flask",
            "api",
            "docker",
            "database"
        ]
    },

    "MBA Finance": {
        "skills": [
            "finance",
            "financial analysis",
            "budgeting",
            "forecasting",
            "investment",
            "accounting",
            "excel"
        ]
    },

    "Digital Marketing": {
        "skills": [
            "seo",
            "social media",
            "marketing",
            "google ads",
            "analytics",
            "content marketing"
        ]
    },

    "HR Recruiter": {
        "skills": [
            "recruitment",
            "talent acquisition",
            "screening",
            "communication",
            "hr"
        ]
    },

    "Cyber Security": {
        "skills": [
            "cyber security",
            "ethical hacking",
            "penetration testing",
            "network security",
            "siem"
        ]
    },

    "Cloud Engineer": {
        "skills": [
            "aws",
            "azure",
            "cloud",
            "docker",
            "kubernetes",
            "devops"
        ]
    },

    "UI/UX Designer": {
        "skills": [
            "figma",
            "prototype",
            "wireframe",
            "ui",
            "ux",
            "design"
        ]
    },

    "BCA": {
        "skills": [
            "programming",
            "database",
            "java",
            "python",
            "web development"
        ]
    },

    "MCA": {
        "skills": [
            "software development",
            "java",
            "python",
            "database",
            "cloud"
        ]
    },

    "MTech": {
        "skills": [
            "research",
            "machine learning",
            "cloud",
            "ai",
            "development"
        ]
    }

}

# ================= PDF READER ================= #

def read_pdf(file):

    try:

        pdf = PyPDF2.PdfReader(file)

        text = ""

        for page in pdf.pages:

            try:
                text += page.extract_text() + " "

            except:
                pass

        return text.lower()

    except:
        return ""

# ================= VALID RESUME ================= #

def validate_resume(text):

    text = text.lower()

    required_keywords = [
        "education",
        "skills",
        "experience",
        "project",
        "resume",
        "internship",
        "certification",
        "objective",
        "summary"
    ]

    score = 0

    for word in required_keywords:

        if word in text:
            score += 1

    if len(text) < 300:
        return False

    return score >= 2

# ================= VALID JOB DESCRIPTION ================= #

def validate_jd(jd):

    jd = jd.lower()

    jd_keywords = [
        "job title",
        "responsibilities",
        "required skills",
        "requirements",
        "qualification",
        "experience",
        "company",
        "location"
    ]

    score = 0

    for word in jd_keywords:

        if word in jd:
            score += 1

    if len(jd) < 120:
        return False

    return score >= 2

# ================= EMAIL ================= #

def extract_email(text):

    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    emails = re.findall(pattern, text)

    if emails:
        return emails[0]

    return "Not Found"

# ================= PHONE ================= #

def extract_phone(text):

    pattern = r'(\+91[\-\s]?)?[6-9]\d{9}'

    matches = re.finditer(pattern, text)

    phones = []

    for match in matches:
        phones.append(match.group())

    if phones:
        return phones[0]

    return "Not Found"

# ================= EXPERIENCE ================= #

def detect_experience(text):

    patterns = [
        "1 year",
        "2 years",
        "3 years",
        "4 years",
        "5 years",
        "6 years",
        "7 years"
    ]

    for p in patterns:

        if p in text:

            if "1 year" in p or "2 years" in p:
                return "Intermediate"

            else:
                return "Experienced"

    return "Fresher"

# ================= SKILL EXTRACTION ================= #

def extract_skills(text, skills):

    found = []

    for skill in skills:

        if skill.lower() in text:
            found.append(skill)

    return list(dict.fromkeys(found))

# ================= PROJECT DETECTION ================= #

def detect_projects(text):

    keywords = [
        "project",
        "developed",
        "built",
        "created",
        "designed",
        "implemented"
    ]

    lines = text.split("\n")

    projects = []

    for line in lines:

        clean = line.strip()

        if len(clean) > 25:

            for keyword in keywords:

                if keyword in clean.lower():

                    projects.append(clean)
                    break

    projects = list(dict.fromkeys(projects))

    return projects[:5]

# ================= SOURCE PREDICTION ================= #

def detect_job_source(jd_text):

    jd = jd_text.lower()

    scores = {

        "LinkedIn": 0,
        "Naukri": 0,
        "Indeed": 0,
        "Internshala": 0,
        "ChatGPT Generated": 0,
        "Google Search": 0,
        "AI Generated": 0
    }

    linkedin = [
        "easy apply",
        "linkedin",
        "professional network",
        "cross-functional",
        "team collaboration",
        "connections"
    ]

    naukari = [
        "notice period",
        "ctc",
        "immediate joiner",
        "salary",
        "joining"
    ]

    indeed = [
        "benefits",
        "remote",
        "work environment",
        "indeed"
    ]

    internshala = [
        "internship",
        "stipend",
        "training",
        "fresher"
    ]

    chatgpt = [
        "ideal candidate",
        "problem-solving skills",
        "fast-paced environment",
        "strong communication skills",
        "ability to work independently"
    ]

    google = [
        "job summary",
        "responsibilities",
        "requirements",
        "preferred qualifications"
    ]

    ai = [
        "dynamic team",
        "cutting-edge technologies",
        "innovative solutions",
        "detail-oriented"
    ]

    for word in linkedin:
        if word in jd:
            scores["LinkedIn"] += 3

    for word in naukari:
        if word in jd:
            scores["Naukri"] += 3

    for word in indeed:
        if word in jd:
            scores["Indeed"] += 3

    for word in internshala:
        if word in jd:
            scores["Internshala"] += 3

    for word in chatgpt:
        if word in jd:
            scores["ChatGPT Generated"] += 4

    for word in google:
        if word in jd:
            scores["Google Search"] += 2

    for word in ai:
        if word in jd:
            scores["AI Generated"] += 4

    predicted = max(scores, key=scores.get)

    confidence = scores[predicted] * 10

    if confidence <= 10:
        return "Unknown Source"

    return f"{predicted} ({confidence}% confidence)"

# ================= MAIN ================= #

if analyze:

    if resume is None:

        st.error("Please upload a resume.")

    elif job_description.strip() == "":

        st.error("Please paste a job description.")

    else:

        resume_text = read_pdf(resume)

        # ================= RESUME VALIDATION ================= #

        if resume_text == "" or not validate_resume(resume_text):

            st.error(
                "Invalid Resume. Please upload a proper professional resume PDF."
            )

        # ================= JD VALIDATION ================= #

        elif not validate_jd(job_description):

            st.error(
                "Invalid Job Description Format."
            )

        else:

            st.success("Resume Analysis Completed Successfully")

            jd_text = job_description.lower()

            # ================= ROLE DETECTION ================= #

            best_match = None
            best_score = 0

            for role, data in career_data.items():

                matched = 0

                for skill in data["skills"]:

                    if skill in jd_text:
                        matched += 1

                if matched > best_score:

                    best_score = matched
                    best_match = role

            if best_match is None:
                best_match = "General Candidate"

            required_skills = career_data.get(
                best_match,
                {"skills": []}
            )["skills"]

            user_skills = extract_skills(
                resume_text,
                required_skills
            )

            missing_skills = [

                skill for skill in required_skills

                if skill not in user_skills
            ]

            score = round(
                (len(user_skills) /
                max(len(required_skills), 1)) * 100
            )

            ats_score = min(
                round(score + 15),
                100
            )

            email = extract_email(
                resume_text
            )

            phone = extract_phone(
                resume_text
            )

            experience = detect_experience(
                resume_text
            )

            projects = detect_projects(
                resume_text
            )

            source = detect_job_source(
                jd_text
            )

            # ================= DECISION ================= #

            if score >= 80:
                decision = "Strong Hire"

            elif score >= 60:
                decision = "Moderate Hire"

            else:
                decision = "Not Recommended"

            # ================= METRICS ================= #

            st.subheader("ATS Analysis")

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Resume Match",
                f"{score}%"
            )

            c2.metric(
                "ATS Score",
                f"{ats_score}%"
            )

            c3.metric(
                "Skills Found",
                len(user_skills)
            )

            c4.metric(
                "Experience",
                experience
            )

            st.divider()

            # ================= DETAILS ================= #

            st.subheader("Candidate Details")

            left, right = st.columns(2)

            with left:

                st.write(f"**Detected Role:** {best_match}")
                st.write(f"**Email:** {email}")
                st.write(f"**Phone:** {phone}")

            with right:

                st.write(f"**Predicted JD Source:** {source}")
                st.write(f"**Matched Skills:** {', '.join(user_skills)}")
                st.write(f"**Missing Skills:** {', '.join(missing_skills)}")

            st.divider()

            # ================= CHARTS ================= #

            st.subheader("Performance Dashboard")

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Resume Score"},
                gauge={
                    'axis': {'range': [0, 100]}
                }
            ))

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

            pie = go.Figure(data=[
                go.Pie(
                    labels=[
                        "Matched Skills",
                        "Missing Skills"
                    ],
                    values=[
                        len(user_skills),
                        len(missing_skills)
                    ],
                    hole=0.5
                )
            ])

            st.plotly_chart(
                pie,
                use_container_width=True
            )

            st.divider()

            # ================= PROJECTS ================= #

            st.subheader("Projects Extracted From Resume")

            if projects:

                for i, p in enumerate(projects, start=1):
                    st.write(f"{i}. {p}")

            else:

                st.warning("No projects detected.")

            st.divider()

            # ================= INTERVIEW QUESTIONS ================= #

            st.subheader("Recommended Interview Questions")

            interview_questions = []

            for skill in required_skills[:10]:

                interview_questions.append(
                    f"Explain your experience with {skill}."
                )

            interview_questions = interview_questions[:10]

            for i, q in enumerate(interview_questions, start=1):

                st.write(f"Q{i}. {q}")

            st.divider()

            # ================= PROJECT RECOMMENDATIONS ================= #

            st.subheader("Recommended Advanced Projects")

            project_map = {

                "Data Analyst": [
                    "Sales Dashboard Analytics",
                    "Financial KPI Dashboard",
                    "Retail Data Insights Platform",
                    "Customer Churn Prediction",
                    "Business Intelligence Reporting System"
                ],

                "AI/ML Engineer": [
                    "AI Resume Screening System",
                    "Chatbot using NLP",
                    "Stock Price Prediction",
                    "Recommendation System",
                    "Face Recognition AI"
                ],

                "Java Full Stack Developer": [
                    "E-Commerce Website",
                    "AI Recruitment Portal",
                    "Online Coding Platform",
                    "Employee Management System",
                    "Real-Time Chat Application"
                ],

                "MBA Finance": [
                    "Financial Forecasting Dashboard",
                    "Investment Portfolio Analyzer",
                    "Loan Risk Prediction",
                    "Budget Planning System",
                    "Stock Market Analytics"
                ],

                "Digital Marketing": [
                    "SEO Analytics Dashboard",
                    "Social Media Tracker",
                    "Campaign Performance Analyzer",
                    "Google Ads Optimization Tool",
                    "Customer Engagement Dashboard"
                ]
            }

            recommended_projects = project_map.get(
                best_match,
                [
                    "Enterprise Management System",
                    "Analytics Dashboard",
                    "Automation Tool",
                    "Cloud Application",
                    "AI Based Management System"
                ]
            )

            for i, project in enumerate(
                recommended_projects,
                start=1
            ):

                st.success(
                    f"Project {i}: {project}"
                )

            st.divider()

            st.subheader("Candidate Introduction Summary")

            skill_text = (
                ", ".join(user_skills[:5])
                if user_skills
                else "technical skills"
            )

            project_text = (
                ", ".join(projects[:2])
                if projects
                else "multiple academic projects"
            )

            summary = f"""

The candidate appears suitable for the role of
{best_match} based on the uploaded resume and job description.

The candidate demonstrates knowledge in
{skill_text} with {experience.lower()}-level
professional exposure.

The resume reflects practical implementation experience through projects such as
{project_text}.

The candidate achieved an ATS compatibility score of
{ats_score}% with a resume-job match score of {score}%.

Based on technical alignment, project exposure,
and resume analysis, the profile is evaluated as:

{decision}

"""

            st.write(summary)