
# Austine Portfolio

This is my autobiography/portfolio made in Streamlit


## Features

- Here's a concise list of your portfolio's features:

* **Layout:** A persistent, non-closable sidebar with a three-tab main content area ("About Me," "Projects," "Skills & Experience").
* **Branding:** A clean, custom UI with all default Streamlit branding and menus hidden via CSS.
* **Sidebar Content:**
    * Profile (Picture, Name, Title)
    * Clickable social links (LinkedIn, GitHub)
    * Resume download button
    * A functional contact form
* **"About Me" Tab:**
    * Formatted personal summary
    * "At a Glance" metrics (Experience, Projects, Languages)
* **"Projects" Tab:**
    * A card-like list of projects
    * Each card has an image, description, technology list, and a GitHub link
* **"Skills & Experience" Tab:**
    * Categorized skills with visual progress bars
    * Work history with collapsible `st.expander` sections for details
* **Modifiability:** All personal data is stored in a single `CONFIG` dictionary for easy updates.

## Installation

Clone this repository:

```bash
    git clone https://github.com/ero-s/Austine-Portfolio.git
    cd Austine-Portfolio
```

Install dependencies:

```bash
    pip install streamlit
```

Run app:
```bash
    streamlit run portfolio.py
```
    
