# E-commerce Sales Analytics — Business Insights Report

## 1. Project Overview

This project analyzes retail sales data using Python, Pandas, SQLite, SQL, and data visualization to identify patterns in sales, profitability, customer behavior, products, discounts, regions, and shipping.

## 2. Key Performance Indicators (KPIs)

| KPI | Value |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Average Order Value | $458.61 |
| Total Records | 9,994 |

## 3. Category Performance

| Category | Sales | Profit |
|---|---:|---:|
| Technology | $836,154.03 | $145,454.95 |
| Furniture | $741,999.80 | $18,451.27 |
| Office Supplies | $719,047.03 | $122,490.80 |

### Findings
- Technology generated the highest sales and profit.
- Office Supplies generated strong profit despite lower sales than Technology.
- Furniture generated substantial sales but comparatively low profit.

## 4. Regional Performance

| Region | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| West | $725,457.82 | $108,418.45 | 14.94% |
| East | $678,781.24 | $91,522.78 | 13.48% |
| Central | $501,239.89 | $39,706.36 | 7.92% |
| South | $391,721.91 | $46,749.43 | 11.93% |

### Findings
- West leads in sales and total profit.
- Central has the lowest regional profit margin.
- Regional differences may warrant further investigation into product mix, pricing, and discounts.

## 5. Customer Segment Analysis

| Segment | Sales | Profit | Orders | Profit Margin |
|---|---:|---:|---:|---:|
| Consumer | $1,161,401.34 | $134,119.21 | 2,586 | 11.55% |
| Corporate | $706,146.37 | $91,979.13 | 1,514 | 13.03% |
| Home Office | $429,653.15 | $60,298.68 | 909 | 14.03% |

### Findings
- Consumer represents the largest sales segment.
- Home Office has the highest profit margin among the segments.
- Sales volume and profit margin differ by customer segment.

## 6. Product Profitability

### Findings
- Some high-selling products are also loss-making.
- Cisco TelePresence System EX90 and GBC DocuBind P400 appeared in both the high-sales and loss-making product analyses.
- Tables was the most loss-making furniture subcategory in the analysis.
- Bookcases also generated negative profit.

### Recommendation
Investigate pricing, discounting, product costs, and product mix for loss-making products before making pricing or inventory decisions.

## 7. Discount Analysis

| Discount Level | Sales | Profit | Average Discount |
|---|---:|---:|---:|
| No Discount | $1,087,908.47 | $320,987.60 | 0.00% |
| Low Discount | $846,522.24 | $100,785.47 | 19.68% |
| High Discount | $298,541.41 | -$58,817.00 | 36.70% |
| Very High Discount | $64,228.74 | -$76,559.05 | 71.89% |

### Findings
- High and very high discount groups generated negative aggregate profit.
- The very-high-discount group had the largest aggregate loss despite lower sales.
- The results show an association between discount level and profitability, not proof of causation.

### Recommendation
Review discount policies, particularly products and transactions with large discounts and negative profits.

## 8. Shipping Mode Analysis

| Shipping Mode | Sales | Profit | Orders | Margin |
|---|---:|---:|---:|---:|
| Standard Class | $1,358,215.74 | $164,088.79 | 2,994 | 12.08% |
| Second Class | $459,193.57 | $57,446.64 | 964 | 12.51% |
| First Class | $351,428.42 | $48,969.84 | 787 | 13.93% |
| Same Day | $128,363.13 | $15,891.76 | 264 | 12.38% |

### Findings
- Standard Class generated the most sales and profit.
- First Class had the highest profit margin.
- All four shipping modes were profitable in aggregate.

## 9. Annual Sales Trends

| Year | Sales | Profit | Orders |
|---|---:|---:|---:|
| 2014 | $484,247.50 | $49,543.97 | 969 |
| 2015 | $470,532.51 | $61,618.60 | 1,038 |
| 2016 | $609,205.60 | $81,795.17 | 1,315 |
| 2017 | $733,215.26 | $93,439.27 | 1,687 |

### Year-over-Year Sales Growth

| Year | Sales Growth | Growth Rate |
|---|---:|---:|
| 2015 | -$13,714.99 | -2.83% |
| 2016 | +$138,673.09 | +29.47% |
| 2017 | +$124,009.66 | +20.36% |

### Findings
- Sales and order volume increased substantially from 2015 through 2017.
- 2016 had the highest year-over-year growth rate.
- 2017 achieved the highest annual sales.

## 10. Order Profitability

| Order Status | Orders | Sales | Profit |
|---|---:|---:|---:|
| Profitable Orders | 3,970 | $1,815,075.30 | $426,330.80 |
| Break-Even Orders | 17 | $8,631.50 | $0.00 |
| Loss-Making Orders | 1,022 | $473,494.06 | -$139,933.78 |

### Findings
- 3,970 orders were profitable.
- 1,022 orders were loss-making.
- Loss-making orders generated approximately $473,494 in sales but lost approximately $139,934.
- The average profitable order generated $107.39 profit.
- The average loss-making order lost $136.92.

### Recommendation
Analyze loss-making orders by product, customer, discount, region, and shipping characteristics to identify opportunities to improve profitability.

## 11. Regional Category Findings

The regional and category analysis revealed differences in performance between product categories and regions.

Examples:
- East Technology: 17.91% profit margin.
- East Furniture: 1.46% profit margin.
- West Office Supplies: 23.82% profit margin.
- West Furniture: 4.55% profit margin.
- South Furniture: 5.77% profit margin.

Furniture had comparatively low margins in the examples analyzed. Further investigation into pricing, product mix, and discount strategy may help explain these differences.

## 12. Final Business Recommendations

1. Investigate loss-making products and subcategories.
2. Review high-discount transactions and discount policies.
3. Analyze the Central region's lower profit margin.
4. Examine loss-making orders rather than focusing only on revenue.
5. Identify opportunities to improve Furniture profitability.
6. Monitor yearly sales growth and order volume.
7. Compare customer segments by sales and profitability.

## 13. Conclusion

The analysis demonstrates that revenue alone is not enough to measure business performance. Product mix, discount levels, regional performance, customer segments, and order profitability provide additional insights that can support more informed business decisions.

This project demonstrates practical skills in Python, Pandas, SQL, SQLite, data analysis, aggregation, subqueries, CTEs, window functions, and business insight generation.
