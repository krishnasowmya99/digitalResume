from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "SowmyaKothwalgudem.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "👋 | Sowmya K"
# PAGE_ICON = ":wave:"
NAME = "Sowmya Kothwalgudem"
DESCRIPTION = """
Computer Science graduate with expertise in software development, machine learning, and data analysis using Python, SQL, and AWS.
"""
EMAIL = "kothwalgudemsowmya@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sowm-yaa/",
    "GitHub": "https://github.com/krishnasowmya99",
}
PROJECTS = {
    "🏆 AWS Certified Cloud Practitioner - Issued April 2023": "https://www.credly.com/badges/4acadbb6-542d-45f2-8936-21e5b0ae86be/public_url",
    "🏆 Fake News Detection - Uses Bidirectional Neural Network and LSTM-based deep learning model to detect fake news": "https://github.com/krishnasowmya99/FakeNewsDetector",
    "🏆 Covid 19 Data Analysis - Correlation of the impact of Covid 19 on worlds' happiness report": "https://github.com/krishnasowmya99/covid19Anal-Viz",
    "🏆 Netflix Movies/Series Dashboard - Netflix Data Analysis using Tableau": "https://public.tableau.com/app/profile/sowmya.kothwalgudem/viz/NetflixDashboard_16856465405970/Netflix",
    
}


st.set_page_config(page_title=PAGE_TITLE)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Proficient in Python, SQL, JavaScript, and cloud platforms (AWS), with expertise in database management and software development.
- ✔️ Proficient in leveraging Python for data analysis, machine learning model development, and impactful data visualization.
- ✔️ Possess a solid grasp of fundamental machine learning principles and techniques.
- ✔️ Demonstrated strong teamwork through active participation in Agile methodologies and effectively streamlined software delivery with CI/CD pipelines.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, JavaScript, HTML/CSS
- 🗄️ Databases: MySQL, Postgres, MongoDB 
- ☁️ Cloud Platforms: AWS (EC2, S3, Lambda, CloudFormation), DataBricks
- 💻 Frameworks/Version Control Systems: Flask, Django, PySpark, Docker, Git
- 📊 Data Visulization: Tableau, PowerBi, MS Excel, Plotly

"""
)

#--- Education ---
st.write('\n')
st.subheader("Education")
st.write("---")

st.write("📖","Master's in Computer Science | University of Dayton")
st.write("👩🏼‍🎓","May 2023")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Associate Professional Software Engineer | DXC Technology **")
st.write("06/2020 - 05/2021")
st.write(
    """
- ► Conducted healthcare data analysis, applied statistical methods, and created interactive visualizations to drive data insights.
- ► Designed data analysis dashboards using AWS QuickSight, enabling data-driven strategic decisions and achieving a 20-fold project outcome improvement.
- ► Optimized relational database efficiency with indexing and query optimization techniques, reducing query execution time by 50%.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Software Developer Intern | Mahindra Rise**")
st.write("07/2019 - 06/2020")
st.write(
    """
- ► Analyzed customer feedback using Pandas and NumPy, leading to a 15% product design improvement.
- ► Applied Agile methodologies, reducing project delivery time by 20% through daily stand-ups and sprint planning.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")