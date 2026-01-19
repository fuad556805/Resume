import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Al Fahim Fuyad | Data Analyst",
    page_icon="📊",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e5e7eb;
    scroll-behavior: smooth;
}

/* Navigation Menu */
.navbar {
    position: sticky;
    top: 0;
    background: rgba(15,23,42,0.9);
    padding: 12px 20px;
    border-radius: 8px;
    display: flex;
    gap: 20px;
    z-index: 100;
    margin-bottom: 25px;
}
.navbar a {
    color: #38bdf8;
    font-weight: 600;
    text-decoration: none;
}
.navbar a:hover {
    text-decoration: underline;
}

/* Glass Card */
.glass {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-radius: 22px;
    padding: 28px;
    box-shadow: 0 25px 45px rgba(0,0,0,0.4);
    margin-bottom: 28px;
    transition: all 0.3s ease-in-out;
}
.glass:hover {
    transform: translateY(-5px);
    box-shadow: 0 30px 60px rgba(0,0,0,0.5);
}

/* Section Title */
.section {
    font-size: 30px;
    font-weight: 700;
    margin: 60px 0 25px 0;
    color: #38bdf8;
    border-left: 4px solid #38bdf8;
    padding-left: 12px;
}

/* Skill Title */
.skill-title {
    font-weight: 600;
    margin-bottom: 8px;
    font-size: 16px;
}

/* Progress Background */
.progress-bg {
    background: rgba(255,255,255,0.15);
    border-radius: 12px;
    height: 14px;
    overflow: hidden;
}

/* Project Images */
.project-img {
    width: 100%;
    border-radius: 12px;
    margin-bottom: 12px;
}

/* Equal Height for Project Cards */
.project-card {
    min-height: 400px;  /* Adjust as needed */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ================= NAVIGATION =================
st.markdown("""
<div class="navbar">
    <a href="#profile-summary">Profile Summary</a>
    <a href="#technical-skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#education">Education</a>
    <a href="#certification">Certification</a>
</div>
""", unsafe_allow_html=True)

# ================= HEADER =================
col1, col2 = st.columns([1.1, 3])

with col1:
    st.image("profile.jpg", width=170)

with col2:
    st.markdown("""
    <div class="glass">
        <h1 style="margin-bottom:5px;">Al Fahim Fuyad</h1>
        <h3 style="color:#38bdf8;">📊 Data Analyst | CSE Undergraduate</h3>
        <p>📍 South Banasree, Dhaka, Bangladesh</p>
        <p>📧 fuad556805@gmail.com | 📞 +8801609227183</p>
        <p>
            <a href="https://www.linkedin.com/in/al-fahim-36126636b" target="_blank">🔗 LinkedIn</a> |
            <a href="https://github.com/fuad556805" target="_blank">💻 GitHub</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ================= PROFILE SUMMARY =================
st.markdown('<div id="profile-summary" class="section">Profile Summary</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glass">
Motivated <b>Data Analyst fresher</b> and CSE undergraduate with hands-on experience in <b>SQL, Python, and statistical data analysis</b>. Skilled in data cleaning, exploratory analysis, hypothesis testing, and translating datasets into actionable business insights. Actively seeking an <b>entry-level Data Analyst role</b>.
</div>
""", unsafe_allow_html=True)

# ================= TECHNICAL SKILLS =================
st.markdown('<div id="technical-skills" class="section">Technical Skills</div>', unsafe_allow_html=True)

def skill_bar(skill, level, color):
    st.markdown(f"""
    <div class="glass">
        <div class="skill-title">{skill}</div>
        <div class="progress-bg">
            <div style="
                width:{level}%;
                background:{color};
                height:14px;
                border-radius:12px;
            "></div>
        </div>
        <div style="margin-top:6px; font-weight:600;">{level}%</div>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    skill_bar("🗄️ SQL / MySQL", 78, "linear-gradient(90deg,#38bdf8,#2563eb)")
    skill_bar("🧹 Data Cleaning", 76, "linear-gradient(90deg,#22c55e,#16a34a)")
    skill_bar("📊 Excel", 65, "linear-gradient(90deg,#facc15,#ca8a04)")

with col2:
    skill_bar("🐍 Python", 75, "linear-gradient(90deg,#a855f7,#9333ea)")
    skill_bar("📐 Statistics", 70, "linear-gradient(90deg,#fb7185,#db2777)")
    skill_bar("📈 Data Visualization", 75, "linear-gradient(90deg,#fb923c,#ea580c)")

with col3:
    skill_bar("🧮 Pandas", 71, "linear-gradient(90deg,#2dd4bf,#0d9488)")
    skill_bar("🔢 NumPy", 70, "linear-gradient(90deg,#22d3ee,#0891b2)")
    skill_bar("🌐 Django / HTML / CSS", 60, "linear-gradient(90deg,#9ca3af,#4b5563)")

# ================= PROJECTS =================
st.markdown('<div id="projects" class="section">Projects</div>', unsafe_allow_html=True)

p1, p2 = st.columns(2)

with p1:
    st.markdown("""
    <div class="glass project-card">
    <img src="project1.png" class="project-img">
    <h4>📊 Sales Data Analysis Using SQL</h4>
    <ul>
        <li>Star-schema sales database (fact & dimension tables)</li>
        <li>Advanced JOINs, CTEs, Window Functions</li>
        <li>Stored Procedures for reusable analysis</li>
        <li>Revenue trends & customer behavior insights</li>
    </ul>
    <a href="https://github.com/fuad556805/Sales-Data-Analysis-Using-SQL" target="_blank">🔗 View Project</a>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="glass project-card">
    <img src="project2.png" class="project-img">
    <h4>📈 Statistical Data Analysis Using Python</h4>
    <ul>
        <li>Hypothesis testing: t-test, ANOVA, Chi-square</li>
        <li>Assumption checking & interpretation</li>
        <li>Real-world datasets (health & business)</li>
    </ul>
    <a href="https://github.com/fuad556805/Statistical-Data-Analysis-Using-Python" target="_blank">🔗 View Project</a>
    </div>
    """, unsafe_allow_html=True)

# ================= EDUCATION =================
st.markdown('<div id="education" class="section">Education</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glass">
<b>BSc in Computer Science & Engineering</b><br>
East West University<br>
Expected Graduation: 2027
</div>
""", unsafe_allow_html=True)

# ================= CERTIFICATION =================
st.markdown('<div id="certification" class="section">Certification</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glass">
<b>Data Analysis with MySQL Database</b><br>
Issued by: Data Solution 360<br>
Credential ID: DSML250501<br><br>
<a href="https://drive.google.com/file/d/17jVDO3qc5sIK-uiHkB1fgQVzotl20uvC/view" target="_blank">
🔗 View Certificate
</a>
</div>
""", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
© 2026 <b>Al Fahim Fuyad</b> | Data Analyst Portfolio
</div>
""", unsafe_allow_html=True)
