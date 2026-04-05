🧪 Forensic Science Report Generator
A web-based application built using Flask that allows users to securely sign up, log in, and generate forensic science reports in PDF format by entering patient details.
🚀 Features
🔐 User Authentication (Sign Up / Sign In)
🧾 Patient Details Form
📄 Automatic PDF Report Generation
💾 Secure Session Management
🎨 Simple and Clean UI using HTML & CSS
⚡ Lightweight Flask Backend
🛠️ Tech Stack
Backend: Python (Flask)
Frontend: HTML, CSS
PDF Generation: ReportLab / FPDF (based on your implementation)
Authentication: Flask Sessions
📁 Project Structure

forensic-report-app/
│
├── app.py
├── templates/
│   ├── signin.html
│   ├── signup.html
│   ├── form.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   └── assets/
│
├── reports/
│   └── generated_pdfs/
│
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/your-username/forensic-report-app.git
cd forensic-report-app
2. Create Virtual Environment
Bash
python -m venv venv
3. Activate Environment
Windows:
Bash
venv\Scripts\activate
Mac/Linux:
Bash
source venv/bin/activate
4. Install Dependencies
Bash
pip install -r requirements.txt
▶️ Run the Application
Bash
python app.py
Open your browser and go to:

http://127.0.0.1:5000/
🧾 How It Works
User registers using the Sign Up page
Logs in via the Sign In page
Fills in patient forensic details (name, age, case info, observations, etc.)
Submits the form
Application generates a PDF forensic report
PDF is saved/downloaded automatically
📄 PDF Report Includes
Patient Information
Case Details
Forensic Observations
Analysis Results
Final Conclusion
🔒 Security Features
Password-based authentication
Session handling using Flask
Restricted access to report generation page
📦 Requirements
Example requirements.txt:

Flask
reportlab
(or replace reportlab with fpdf if used)
💡 Future Enhancements
🗄️ Database integration (SQLite/MySQL)
📊 Admin dashboard
📥 Download & email report option
🔍 Search previous reports
🧠 AI-based forensic analysis (advanced)
👩‍💻 Author
Rutuja Tiwari

🔑 Core Features
🔐 User Authentication
Secure Sign Up and Sign In system
Session-based login using Flask
Prevents unauthorized access to report generation
🧾 Patient Data Entry Form
Easy-to-use form for entering:
Patient name, age, gender
Case ID and case description
Forensic observations
Test results and remarks
📄 PDF Report Generation
Automatically generates a professional forensic report in PDF format
Structured layout including:
Header (report title)
Patient details
Observations & analysis
Final conclusion
💾 Report Storage
Generated PDFs are:
Saved locally in the system
Can be downloaded by the user
🖥️ User Dashboard
After login, users can:
Access report form
Generate new reports
Navigate easily through the app
🎨 Simple UI Design
Clean and responsive interface
Built using HTML, CSS (and optionally Bootstrap)
Easy navigation for all users
⚡ Lightweight & Fast
Built with Flask (minimal and efficient backend)
Quick form submission and PDF generation
🔒 Security Features
Password protection for user accounts
Session management to keep users logged in
Restricted access to sensitive pages
📌 Functional Features
Form validation (ensures required data is entered)
Organized file structure for reports
Easy integration with additional features
Developed by Your Name
📜 License
This project is for educational purposes.
