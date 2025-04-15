# Global Music Streaming Trends & Listener Insights (2018–2024)

This project explores global music streaming behavior between 2018 and 2024 across platforms such as Spotify, Apple Music, and YouTube. The goal is to analyse listener demographics, engagement habits, genre preferences, and uncover trends — all through different technical approaches.

---

## How to Run

1. **Clone the repository**
2. **Install dependencies** using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Install the project locally:**
   ```bash
   pip install .
   ```
4. **Run the ETL pipeline (optional)** to create the database:
   ```bash
   python scripts/run_etl.py
   ```
5. **Launch the Streamlit app:**
   ```bash
   streamlit run scripts/app.py
   ```

---

## Project Overview

This project was designed to **demonstrate multiple approaches** to answering the same set of analytical questions. While not all steps are necessary given the dataset’s cleanliness, the full pipeline reflects best practices that would apply to more complex or less structured data environments.

### ETL Pipeline

- **Extract**: Read in data from a clean CSV file.
- **Transform**: Basic column name sanitisation and formatting using `pandas`.
- **Load**: Data is loaded into an **SQLite database** using `sqlite3`.  
   _The database file (`music.db`) can be found in the `data/` folder._

> ⚠️ This step is intentionally more complex than necessary — it simulates what would be required in a real-world setting with messy or multi-source data.

---

### Exploratory Data Analysis

Two parallel approaches were used to answer the same analytical questions:

1. **SQL Queries on SQLite database**  
   Used `sqlite3` to query and aggregate data into insights.  
    _SQL queries are stored in the `sql/` folder._

2. **Pandas-Based Notebook Analysis**  
   Used `pandas` to perform similar transformations and groupings, allowing quick comparison of methods.  
    _The analysis notebook is located in the `notebooks/` folder._

---

### Visualization with Streamlit

A **Streamlit dashboard** was built to visualise answers to key questions using interactive charts and summaries:

- Most popular streaming platforms globally
- Genre preferences by age group and country
- Listener engagement over time (Discover Weekly, Repeat Rate)
- Streaming behavior by time of day
- Subscription type trends
- Artist and platform correlation

  _The script for the Streamlit app is located at `scripts/app.py`._

---

## Key Questions Investigated

- What are the most popular streaming platforms across the globe?
- Which genres are most preferred by different age groups?
- Do free users stream less than premium users?
- When do users typically listen to music (morning, afternoon, night)?
- Which countries have the highest average listening time?
- How do repeat rates and discovery engagement vary by platform?

---

## Tech Stack

- **Python**
- **pandas**
- **sqlite3**
- **SQL**
- **Streamlit**
- **Jupyter Notebook**

---
