# E-commerce Sales Analytics & Business Intelligence

## Project Overview

An end-to-end retail sales analytics project built using Python, Pandas, SQL, and Streamlit. This project analyzes sales performance, profitability, customer behavior, products, discounts, regional performance, and business trends using the Sample Superstore dataset.

The goal is to transform raw sales data into actionable business insights through data analysis, SQL queries, and an interactive dashboard.

## Tech Stack

- Python
- Pandas
- NumPy
- SQL (SQLite)
- Matplotlib
- Seaborn
- Plotly
- Streamlit

## Project Structure

```text
ecommerce-sales-analytics/
│
├── data/
│   ├── raw/
│   │   └── Sample - Superstore.csv
│   └── processed/
│       └── superstore.db
│
├── src/
│   ├── analysis.py
│   ├── visualizations.py
│   ├── category_analysis.py
│   ├── monthly_analysis.py
│   ├── region_analysis.py
│   ├── customer_analysis.py
│   ├── load_database.py
│   └── sql_analysis.py
│
├── sql/
│   ├── 01_business_kpis.sql
│   ├── 02_category_analysis.sql
│   ├── 03_regional_analysis.sql
│   ├── 04_product_analysis.sql
│   ├── 05_customer_analysis.sql
│   ├── 06_order_analysis.sql
│   └── 07_advanced_sql.sql
│
├── reports/
│   └── business_insights_report.md
│
├── dashboard.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset

**Sample Superstore Dataset**

The dataset contains retail transactions with information about:

- Orders and order dates
- Sales and profit
- Products and categories
- Customers and segments
- Regions and states
- Discounts
- Shipping methods

**Dataset size:** 9,994 records

## Business KPIs

| KPI | Value |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Average Order Value | $458.61 |
| Profit Margin | 12.47% |
| Total Records | 9,994 |

## Dashboard Features

Interactive Streamlit dashboard featuring:

- KPI overview
- Sales and profit trends
- Category performance
- Regional performance
- Product performance
- Customer segment analysis
- Customer profitability
- Discount analysis

### Interactive Filters

- Region
- Category
- Customer Segment
- Order Date Range

## Key Business Insights

### Category Performance

- Technology generated the highest sales and profit.
- Office Supplies generated strong profit relative to sales.
- Furniture generated substantial revenue but comparatively low profitability.

### Regional Performance

- West generated the highest total sales and profit.
- West had the highest regional profit margin.
- Central had the lowest regional profit margin, indicating an area for further investigation.

### Discount Analysis

- High discount levels were associated with negative aggregate profitability.
- Discount groups at 30% and above showed negative aggregate profit in the analyzed data.
- Discount strategy may require further evaluation.

### Customer Analysis

- Consumer segment contributed the largest share of sales.
- Corporate and Home Office segments had higher profit margins than Consumer.
- Some high-revenue customers generated negative profits, showing that revenue alone does not measure customer value.

### Product Analysis

- Some high-sales products generated negative profits.
- Tables was a major loss-making subcategory.
- Product-level profitability should be considered alongside sales volume.

### Sales Trends

- Sales increased year over year in the analyzed period.
- 2016 showed strong growth over 2015.
- 2017 sales continued to increase.

## SQL Analysis

The project includes 25 SQL analyses covering:

- Business KPIs
- Category and subcategory analysis
- Regional performance
- Product performance
- Customer profitability
- Order-level analysis
- Discount analysis
- Common Table Expressions (CTEs)
- Subqueries
- Window functions
- Ranking
- Year-over-year growth using LAG
- CASE statements

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/iamrahm4n/ecommerce-sales-analytics.git
cd ecommerce-sales-analytics
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser.

## Business Insights Report

Detailed business findings, analysis, and recommendations are available in:

`reports/business_insights_report.md`

## Project Purpose

This project demonstrates practical skills in:

- Data cleaning and analysis
- Python and Pandas
- SQL querying and business analysis
- KPI development
- Data visualization
- Interactive dashboard development
- Business insight generation
- Analytical thinking

---

**Author:** Rahman  
**GitHub:** https://github.com/iamrahm4n  
**LinkedIn:** https://www.linkedin.com/in/rahman-khan-34564a209/