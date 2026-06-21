# COVID-19 Data Analysis Project

## Project Overview
This project analyzes global COVID-19 data using Python, Pandas, Matplotlib, and SQL.

The objective is to clean, process, analyze, and visualize COVID-19 trends across different countries and identify key insights.

---

## Project Structure

COVID-19-DATA-ANALYSIS/

├── data/
│   ├── covid_19_clean_complete.csv
│   └── processed/
│       └── cleaned_covid_data.csv

├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   └── 02_eda_analysis.ipynb

├── images/
│   ├── covid_trend_over_time.png
│   ├── top10_confirmed_cases.png
│   ├── top10_deaths.png
│   ├── top10_recovered_cases.png
│   └── top10_active_cases.png

├── sql/
│   └── covid_analysis.sql

└── README.md

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- SQL

---

## Data Cleaning

The following preprocessing steps were performed:

- Checked dataset structure
- Removed duplicate records
- Handled missing values
- Converted Date column to datetime format
- Exported cleaned dataset

---

## Exploratory Data Analysis

The following analyses were performed:

1. Global COVID-19 trend over time
2. Top 10 countries by confirmed cases
3. Top 10 countries by deaths
4. Top 10 countries by recoveries
5. Top 10 countries by active cases

---

## Key Insights

- United States recorded the highest number of confirmed cases.
- A small number of countries contributed to a large share of global deaths.
- Recovery numbers increased significantly over time.
- COVID-19 spread rapidly during major outbreak periods.
- Pandemic impact varied significantly across countries.

---

## SQL Analysis

SQL queries were written to:

- Count total records
- Identify top countries by confirmed cases
- Identify top countries by deaths
- Identify top countries by recoveries

---

## Author

Prabha Rampurapu