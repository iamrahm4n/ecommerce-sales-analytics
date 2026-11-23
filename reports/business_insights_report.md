# E-commerce Sales Analytics & Business Intelligence Report

## 1. Executive Summary

This project analyzes retail sales data to evaluate sales performance, profitability, customer segments, products, regional performance, discounts, and trends over time.

The analysis was performed using Python, Pandas, SQL (SQLite), and Plotly/Streamlit.

The dataset contains 9,994 records and represents sales transactions across multiple years.

### Key Findings

- Total sales were approximately $2.30 million.
- Total profit was approximately $286.4K.
- Technology generated the highest sales and profit among the three categories.
- West had the strongest regional profit margin.
- Central had the weakest regional profit margin.
- Consumer customers generated the largest share of sales.
- High discount levels were associated with negative profitability.
- Furniture generated substantial sales but comparatively low profit.

---

## 2. Business KPIs

| KPI | Value |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Average Order Value | $458.61 |
| Total Records | 9,994 |
| Total Orders | 5,009 |
| Total Quantity Sold | 37,873 |
| Overall Profit Margin | 12.47% |

---

## 3. Category Performance

| Category | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| Technology | $836,154.03 | $145,454.95 | 17.40% |
| Furniture | $741,999.80 | $18,451.27 | 2.49% |
| Office Supplies | $719,047.03 | $122,490.80 | 17.04% |

### Insights

- Technology leads in both sales and profit.
- Office Supplies generates strong profit despite lower sales than Technology.
- Furniture has a comparatively weak profit margin despite significant sales.

### Recommendations

- Investigate Furniture pricing, discounting, and product mix.
- Identify high-margin Technology and Office Supplies products.
- Evaluate opportunities to improve Furniture profitability without unnecessarily reducing sales.

---

## 4. Regional Performance

| Region | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| West | $725,457.82 | $108,418.45 | 14.94% |
| East | $678,781.24 | $91,522.78 | 13.48% |
| Central | $501,239.89 | $39,706.36 | 7.92% |
| South | $391,721.91 | $46,749.43 | 11.93% |

### Insights

- West leads in total sales, profit, and profit margin.
- East is the second strongest region in overall sales and profit.
- Central has the lowest profit margin.
- South generates lower sales than the other regions but maintains a better margin than Central.

### Recommendations

- Investigate Central's pricing, discount levels, and product mix.
- Study West's sales and profitability patterns for potential best practices.
- Evaluate regional product demand and profitability before making expansion decisions.

---

## 5. Product Performance

### Top Products by Sales

The product analysis identified high-revenue products, including:

- Fellowes PB500 Electric Punch Binding Machine
- Cisco TelePresence System EX90
- HON 5400 Series Task Chairs
- GBC DocuBind TL300
- GBC Ibimaster 500
- Hewlett Packard LaserJet 3310 Copier

### Loss-Making Products

Products identified with notable negative profits include:

- Lexmark MX611dhe Monochrome Laser Printer
- Cubify CubeX 3D Printer
- Chromcraft Bull-Nose Wood Oval Conference Tables
- Bush Advantage Racetrack Conference Table
- GBC DocuBind P400

### Insights

- High sales do not always translate into high profits.
- Some products with substantial sales are loss-making.
- Product-level profitability should be considered alongside revenue.

### Recommendations

- Review pricing and discount strategies for loss-making products.
- Investigate shipping costs and product cost structures.
- Monitor product profit instead of ranking products by sales alone.

---

## 6. Customer Segment Analysis

| Segment | Sales | Profit | Orders | Profit Margin |
|---|---:|---:|---:|---:|
| Consumer | $1,161,401.34 | $134,119.21 | 2,586 | 11.55% |
| Corporate | $706,146.37 | $91,979.13 | 1,514 | 13.03% |
| Home Office | $429,653.15 | $60,298.68 | 909 | 14.03% |

### Insights

- Consumer represents approximately 50.5% of sales.
- Corporate represents approximately 30.7%.
- Home Office represents approximately 18.7%.
- Consumer generates the highest total sales and profit.
- Home Office has the highest profit margin among the three segments.

### Recommendations

- Continue monitoring Consumer sales because it is the largest revenue segment.
- Explore profitable growth opportunities within Corporate and Home Office.
- Compare customer segment performance using profit margins as well as revenue.

---

## 7. Customer Profitability

The customer analysis evaluated sales and profit at the individual customer level.

### Key Insights

- High-revenue customers may not necessarily be highly profitable.
- Sean Miller had the highest sales among the customers shown in the dashboard but recorded a negative total profit.
- Some customers generate substantial losses despite generating revenue.

### Recommendations

- Review profitability for high-sales customers.
- Investigate the discount and product mix associated with loss-making customers.
- Use customer profit and profit margin when evaluating customer value.

---

## 8. Discount Analysis

### Profit by Discount Level

| Discount | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| 0% | $1,087,908.47 | $320,987.60 | 29.51% |
| 10% | $54,369.35 | $9,029.18 | 16.61% |
| 15% | $27,558.52 | $1,418.99 | 5.15% |
| 20% | $764,594.37 | $90,337.31 | 11.82% |
| 30% | $103,226.65 | -$10,369.28 | -10.05% |
| 32% | $14,493.46 | -$2,391.14 | -16.50% |
| 40% | $116,417.78 | -$23,057.05 | -19.81% |
| 45% | $5,484.97 | -$2,493.11 | -45.45% |
| 50% | $58,918.54 | -$20,506.43 | -34.80% |
| 60% | $6,644.70 | -$5,944.66 | -89.46% |
| 70% | $40,620.28 | -$40,075.36 | -98.66% |
| 80% | $16,963.76 | -$30,539.04 | -180.03% |

### Insights

- The no-discount group generated the highest total profit.
- Discount groups at 30% and above show negative aggregate profit in this dataset.
- Profitability generally weakens at higher discount levels.
- The results show an association and do not establish that discounting alone caused losses.

### Recommendations

- Review discount approval policies.
- Evaluate profitability before offering high discounts.
- Monitor margin impact rather than discount-driven sales volume alone.

---

## 9. Sales Trend Analysis

Annual performance:

| Year | Sales | Profit | Orders |
|---|---:|---:|---:|
| 2014 | $484,247.50 | $49,543.97 | 969 |
| 2015 | $470,532.51 | $61,618.60 | 1,038 |
| 2016 | $609,205.60 | $81,795.17 | 1,315 |
| 2017 | $733,215.26 | $93,439.27 | 1,687 |

### Year-over-Year Sales Growth

| Year | Sales Change | Growth |
|---|---:|---:|
| 2015 | -$13,714.99 | -2.83% |
| 2016 | $138,673.09 | 29.47% |
| 2017 | $124,009.66 | 20.36% |

### Insights

- Sales declined slightly in 2015.
- Sales recovered strongly in 2016.
- 2017 recorded the highest sales and profit in the period analyzed.
- Sales increased for two consecutive years following 2015.

### Recommendations

- Investigate the drivers behind the 2016 and 2017 growth.
- Monitor yearly revenue, profit, and order trends together.
- Evaluate whether growth is being achieved profitably.

---

## 10. Order-Level Analysis

Orders were classified based on total order profit.

### Insights

- Orders were classified as profitable, break-even, or loss-making.
- Order-level profitability gives a different view from transaction-row profitability.
- A profitable transaction does not necessarily mean the entire order is profitable.

### Recommendations

- Track profitability at the order level.
- Investigate recurring loss-making orders.
- Review the combined impact of discounts, shipping, and product combinations.

---

## 11. Tools and Technologies

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Matplotlib
- Plotly
- Streamlit

---

## 12. Project Limitations

- The analysis is based on the provided sample retail dataset.
- Observed relationships should not automatically be interpreted as causal.
- Customer and product recommendations are based on historical transactions.
- Further analysis would be required to evaluate external factors, inventory, marketing costs, and customer lifetime value.

---

## 13. Conclusion

This analysis demonstrates how sales data can be transformed into actionable business insights using Python, SQL, and business intelligence techniques.

The project highlights the importance of evaluating revenue alongside profitability, identifying loss-making products and customers, reviewing discount policies, and comparing performance across regions and customer segments.

The interactive dashboard provides a way to explore the data using filters and visualizations, supporting data-driven business decisions.
