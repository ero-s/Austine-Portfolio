import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Austine Lomocso | Digital Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.jpg"


CONFIG = {
    "PROFILE": {
        "name": "Austine Lomocso",
        "title": "Full-Stack Developer & Godot Enthusiast",
        "profile_pic": profile_pic_path,
        "resume_file": resume_file,
    },
    "LINKS": {
        "LinkedIn": "https://www.linkedin.com/in/austine-lomocso-bb1448255/",
        "GitHub": "https://github.com/ero-s",
    },
    "ABOUT": {
        "summary": """
        Hello! I'm Austine Lomocso, a passionate and dedicated 3rd-year Computer Science student.

As a developer, I've built a strong proficiency in core languages like C++, Java, and Python. My technical skills extend to full-stack development, where I'm comfortable building robust backend systems with Spring Boot and crafting dynamic, end-to-end applications using the MERN (MongoDB, Express.js, React, Node.js) stack. I also have experience leveraging modern frontend tools like Vite to create fast and efficient user interfaces.

Beyond my CS coursework, I currently work as a Math tutor, where I help students from elementary through high school grasp complex concepts. This role has significantly sharpened my ability to communicate clearly and break down difficult problems into simple, understandable steps.

I thrive in collaborative environments and am known for being a cooperative and engaging team member. I'm always eager to learn, contribute, and tackle new challenges in the world of technology.
        """,
        "metrics": [
            {"label": "Years of Experience", "value": "3"},
            {"label": "Projects Completed", "value": "3"},
            {"label": "Programming Languages", "value": "5"},
        ]
    },
    "SKILLS": {
        "Backend": [
            {"name": "Python & Django", "level": 95},
            {"name": "Java & Spring Boot", "level": 90},
            {"name": "Node.js & Express", "level": 80},
            {"name": "Databases (PostgreSQL, MySQL, MongoDB)", "level": 85},
        ],
        "Frontend": [
            {"name": "React.js", "level": 95},
            {"name": "JavaScript (ES6+)", "level": 90},
            {"name": "HTML5 & CSS3", "level": 90},
            {"name": "Material-UI & Bootstrap", "level": 80},
        ],
        "Game Development": [
            {"name": "Godot Engine & GDScript", "level": 85},
            {"name": "C# (for Godot)", "level": 75},
            {"name": "Game Design Principles", "level": 70},
        ],
        "Tools & DevOps": [
            {"name": "Git & GitHub", "level": 95},
            {"name": "Docker & CI/CD", "level": 70},
            {"name": "AWS & Heroku", "level": 65},
        ]
    },
    "PROJECTS": [
        {
            "title": "Planomatik - Event Management System",
            "description": "A full-stack Django application for organizing and managing large-scale events. Features include user auth, event scheduling, and a REST API for mobile integration.",
            "technologies": ["Python", "Django", "Django REST Framework", "PostgreSQL", "React"],
            "image_url": "https://placehold.co/600x400/000000/FFFFFF/png?text=Planomatik",
            "repo_link": "https://github.com/BrentTolentino/Planomatilk"
        },

        {
            "title": "BlueHire",
            "description": "A realtime localized job hunting app for blue-collar workers looking for job opportunities, Spring Security for auth, and Stripe integration for payments.",
            "technologies": ["Java", "Spring Boot", "Spring Security", "JPA/Hibernate", "MySQL"],
            "image_url": "https://placehold.co/600x400/3C4F76/FFFFFF/png?text=BlueHire",
            "repo_link": "https://github.com/ero-s/BlueHire"
        },
        {
            "title": "Clean And Respond",
            "description": "A 2D Indie platformer game developed in Godot. Features custom physics, state machine for character controls, and a procedurally generated level system.",
            "technologies": ["Godot Engine", "GDScript", "Aseprite"],
            "image_url": "https://placehold.co/600x400/822E81/FFFFFF/png?text=Clean+and+Respond+(Godot)",
            "repo_link": "https://github.com/Pinghtdog/Clean-And-Respond"
        }
    ],
    "EXPERIENCE": [
        {
            "role": "Full-Stack Developer",
            "company": "CodeBlooded",
            "period": "2023 - Present",
            "details": [
                "Led the development of a high-traffic React and Spring Boot application.",
            ]
        },
        {
            "role": "Math Tutor",
            "company": "Brighterly",
            "period": "Present",
            "details": [
                "Aiding kids of wide ranges of ages in Math classes through online one-on-one tutoring sessions"
            ]
        }
    ]
}



def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_path}")


def load_pdf(file_path):
    try:
        with open(file_path, "rb") as pdf_file:
            return pdf_file.read()
    except FileNotFoundError:
        st.error(f"PDF file not found: {file_path}")
        return None


load_css(css_file)
profile_pic = CONFIG["PROFILE"]["profile_pic"]
resume_bytes = load_pdf(CONFIG["PROFILE"]["resume_file"])

with st.sidebar:
    st.set_page_config(
        initial_sidebar_state="expanded"
    )
    st.image(str(profile_pic), width=200)
    st.title(CONFIG["PROFILE"]["name"])
    st.subheader(CONFIG["PROFILE"]["title"])

    st.write("---")
    st.markdown("### 🔗 Connect with Me")
    cols = st.columns(len(CONFIG["LINKS"]))
    for i, (platform, link) in enumerate(CONFIG["LINKS"].items()):
        cols[i].link_button(platform, link, use_container_width=True)

    st.write("---")
    if resume_bytes:
        st.download_button(
            label="📄 Download My Resume",
            data=resume_bytes,
            file_name=CONFIG["PROFILE"]["resume_file"].name,
            mime="application/octet-stream",
            use_container_width=True,
        )

    st.write("---")
    st.markdown("### Contact Me")
    with st.form(key="contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message", height=150)
        submit_button = st.form_submit_button(
            label="Send Message",
            use_container_width=True
        )
        if submit_button:
            if not name or not email or not message:
                st.warning("Please fill out all fields.")
            else:
                st.success("Message sent successfully! I'll get back to you soon.")

tab_about, tab_projects, tab_skills_exp = st.tabs(
    ["🏠 About Me", "🚀 My Projects", "🛠️ Skills & Experience"]
)

with tab_about:
    st.header("About Me")
    st.write(CONFIG["ABOUT"]["summary"], unsafe_allow_html=True)
    st.write("---")

    st.subheader("At a Glance")
    cols = st.columns(len(CONFIG["ABOUT"]["metrics"]))
    for i, item in enumerate(CONFIG["ABOUT"]["metrics"]):
        cols[i].metric(label=item["label"], value=item["value"])

with tab_projects:
    st.header("My Projects")
    st.write("Here are some of the key projects I've worked on, showcasing my skills across different technologies.")
    st.write("---")

    for project in CONFIG["PROJECTS"]:
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(project["image_url"])

            with col2:
                st.subheader(project["title"])
                st.write(project["description"])

                st.markdown(f"**Technologies Used:**")
                tech_str = ", ".join(project['technologies'])
                st.text(tech_str)
                st.link_button("View on GitHub ↗", project["repo_link"])

with tab_skills_exp:
    st.header("Technical Skills")
    st.write("I am proficient in a wide range of technologies. Here's a breakdown:")

    for category, skills in CONFIG["SKILLS"].items():
        st.subheader(category)
        for skill in skills:
            st.progress(skill["level"], text=f"{skill['name']} ({skill['level']}%)")

    st.write("---")

    st.header("Work Experience")

    for job in CONFIG["EXPERIENCE"]:
        with st.container(border=True):
            st.subheader(f"**{job['role']}** | {job['company']}")
            st.caption(f"_{job['period']}_")

            with st.expander("Key Responsibilities & Achievements"):
                for detail in job['details']:
                    st.markdown(f"* {detail}")