# 📄 AI Resume Screening Dashboard

An AI-powered Resume Screening and ATS Analysis Dashboard built using **Python, Streamlit, Plotly, and PDF Processing**.

This application helps recruiters, HR professionals, and job seekers analyze resumes against job descriptions, calculate ATS scores, identify skill gaps, and generate interview recommendations.

---

## 🚀 Features

### ✅ Resume Upload & Parsing

* Upload Resume in PDF format
* Extract text automatically using PyPDF2
* Resume validation to ensure proper professional format

### ✅ Job Description Analysis

* Paste any job description
* Validates JD structure and completeness
* Detects likely source of the JD (LinkedIn, Naukri, Indeed, Internshala, AI Generated, etc.)

### ✅ ATS Score Calculation

* Calculates Resume Match Score
* Generates ATS Compatibility Score
* Measures skill alignment between resume and JD

### ✅ Candidate Information Extraction

Automatically extracts:

* Email Address
* Phone Number
* Experience Level
* Project Information

### ✅ Role Detection

Supports multiple career domains:

* Data Analyst
* AI/ML Engineer
* Backend Developer
* Java Full Stack Developer
* Cyber Security
* Cloud Engineer
* UI/UX Designer
* Digital Marketing
* MBA Finance
* HR Recruiter
* BCA
* MCA
* MTech

### ✅ Skill Gap Analysis

Identifies:

* Matched Skills
* Missing Skills
* Candidate Strengths
* Improvement Areas

### ✅ Interactive Dashboard

Includes:

* ATS Metrics
* Resume Match Percentage
* Gauge Charts
* Pie Charts
* Candidate Summary

### ✅ Project Recommendations

Suggests advanced projects based on the detected career role.

### ✅ Interview Preparation

Generates role-specific interview questions automatically.

---

# 🛠️ Tech Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Core Development           |
| Streamlit  | Web Interface              |
| PyPDF2     | Resume PDF Parsing         |
| Plotly     | Interactive Visualizations |
| Regex (re) | Data Extraction            |
| Pandas     | Data Handling              |

---

# 📂 Project Structure

```bash
AI-Resume-Screening/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_resume.pdf
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screening.git

cd AI-Resume-Screening
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 📋 Requirements

Create a `requirements.txt` file:

```txt
streamlit
PyPDF2
plotly
pandas
```

Install using:

```bash
pip install -r requirements.txt
```

---

# 🎯 Workflow

1. Upload Resume PDF
2. Paste Job Description
3. Click "Analyze Resume"
4. System extracts:

   * Contact Information
   * Skills
   * Experience
   * Projects
5. ATS Score is generated
6. Skill Gap Analysis is performed
7. Interview Questions are suggested
8. Advanced Project Recommendations are displayed

---

# 📊 Dashboard Outputs

### ATS Analysis

* Resume Match %
* ATS Score %
* Skills Found
* Experience Level

### Candidate Details

* Detected Role
* Email
* Phone Number
* JD Source Prediction

### Visual Analytics

* ATS Gauge Chart
* Skills Pie Chart

### Recommendations

* Missing Skills
* Interview Questions
* Career Projects
* Candidate Summary

---

# 🔮 Future Improvements

* AI-based Resume Summarization using LLMs
* GPT-powered Interview Question Generation
* Resume Ranking System
* Multi-Resume Screening
* Resume Download Report (PDF)
* Skill Recommendation Engine
* Job Recommendation System
* LinkedIn Profile Analysis

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Shaurya Gupta**

AI/ML Engineering Student | Machine Learning Enthusiast | Building AI-Powered Solutions

If you found this project useful, consider giving it a ⭐ on GitHub.
