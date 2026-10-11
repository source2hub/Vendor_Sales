VENDOR PERFORMANCE\n& INVENTORY ANALYSIS

Final Exploratory Data Analysis Report

Charts and findings reproduced only from the supplied EDA__f.ipynb notebook.

| Notebook finding | Value / result |

| --- | --- |

| Initial vendor-brand summary rows | 10,692 |

| Filtered rows used for main EDA | 8,564 |

| Top 10 vendors’ purchase contribution | 65.69% |

| Total unsold inventory capital reported | Notebook output reports approx. $2.71M |

| Mean unit purchase price by order size | Small: $39.07 \| Medium: $15.49 \| Large: $10.78 |

| Profit-margin confidence intervals | Top-sales group: 30.74%–31.61%; low-sales group: 40.48%–42.62% |

Purpose: summarize the notebook’s existing charts, analysis tables, and stated findings for vendor selection, purchasing, pricing, and inventory management.

# 1. Executive Summary

- The notebook creates a vendor–brand summary joining purchase transactions, sales transactions, freight costs, and product pricing.

- The main EDA filters to GrossProfit > 0, ProfitMargin > 0, and TotalQuantity > 0. The displayed filtered dataset contains 8,564 rows, compared with 10,692 rows in the initial summary.

- The top ten vendors account for 65.69% of purchase contribution in the notebook’s displayed Pareto analysis.

- The notebook’s bulk-purchasing boxplot shows a lower central unit-price distribution for larger orders, although there are substantial outliers.

- The notebook reports higher average profit margins for the low-sales quartile than the top-sales quartile and displays their confidence-interval comparison.

## Priority recommendations based on notebook findings

| Area | Action to consider | Notebook evidence |

| --- | --- | --- |

| Supplier concentration | Review alternate sourcing and dependency exposure. | Top 10 purchase contribution = 65.69%. |

| Inventory | Investigate unsold capital and vendors with turnover below 1. | Notebook computes unsold inventory value and lists low-turnover vendors. |

| Pricing / promotion | Test selected low-sales, high-margin brands in controlled campaigns. | Notebook identifies target brands using 15th/85th percentile thresholds. |

| Bulk purchasing | Compare savings with storage, carrying cost, and demand risk. | Unit price is lower on average in the Large order group. |

| Data quality | Validate zero denominators, negative gross profit, outliers and extreme turnover. | Initial summary statistics show negative/zero and extreme values. |

# 2. Data Preparation and EDA

The notebook explores the vendor_sales_summary table, containing fields such as VendorNumber, VendorName, Brand, Description, PurchasePrice, ActualPrice, Volume, TotalPurchaseQuantity, TotalPurchaseDollars, FreightCost, TotalQuantity, TotalSalesDollars, TotalSalesPrice, TotalExciseTax, GrossProfit, ProfitMargin, StockTurnover, and SalestoPurchaseRatio.

| Step | Notebook operation | Interpretation |

| --- | --- | --- |

| Summary statistics | df.describe().T | Shows ranges, means, quartiles and extremes for numeric fields. |

| Initial distribution plots | Cell 58 | Histograms for numerical columns before filtering. |

| Initial outlier boxplots | Cell 59 | Boxplots reveal extreme values across numerical fields. |

| Filtering | GrossProfit > 0; ProfitMargin > 0; TotalQuantity > 0 | Removes loss-making, invalid-margin and zero-sales-quantity rows from later analyses. |

| Post-filter distributions | Cell 63 | Histograms after the notebook’s filters. |

| Categorical counts | Cell 64 | Count plots for VendorName and Description. |

| Correlation | Cell 65 | Heatmap for numeric columns in the filtered dataset. |

## Original EDA charts — distribution and quality checks

Figure 1. Original notebook chart: numerical distributions before filtering (cell 58).

Figure 2. Original notebook chart: numerical boxplots before filtering (cell 59).

Figure 3. Original notebook chart: numerical distributions after filtering (cell 63).

Figure 4. Original notebook chart: count plots for vendor and product description (cell 64).

Figure 5. Original notebook chart: correlation heatmap (cell 65).

# 3. Brands for Promotional or Pricing Adjustments

The notebook aggregates brand-level TotalSalesDollars and mean ProfitMargin. It sets the low-sales threshold to the 15th percentile of brand sales and the high-margin threshold to the 85th percentile of mean brand margin, then highlights target brands meeting both conditions.

| Notebook criterion | Threshold shown in notebook |

| --- | --- |

| Low sales threshold | $560.299 |

| High profit-margin threshold | 64.9702% |

| Target group | Brands at or below low-sales threshold and at or above high-margin threshold |

Figure 6. Original notebook target-brand scatterplot (cell 73).

Figure 7. Original notebook scatterplot after limiting the all-brand display to sales below $10,000 (cell 75).

- Use the target brands as candidates for controlled promotion tests rather than assuming that a discount will increase profit.

- Track incremental sales, gross profit dollars, sell-through, and margin against a control group.

# 4. Vendor and Brand Sales Performance

The notebook ranks the top ten vendors and top ten brands by TotalSalesDollars.

Figure 8. Original notebook chart: top 10 vendors and top 10 brands by sales (cell 79).

| Top vendors shown in chart | Top brands shown in chart |

| --- | --- |

| DIAGEO NORTH AMERICA INC | Jack Daniels No 7 Black |

| MARTIGNETTI COMPANIES | Tito’s Handmade Vodka |

| PERNOD RICARD USA | Grey Goose Vodka |

| JIM BEAM BRANDS COMPANY | Capt Morgan Spiced Rum |

| BACARDI USA INC | Absolut 80 Proof |

| CONSTELLATION BRANDS INC | Jameson Irish Whiskey |

| E & J GALLO WINERY | Ketel One Vodka |

| BROWN-FORMAN CORP | Baileys Irish Cream |

| ULTRA BEVERAGE COMPANY LLP | Kahlua |

| M S WALKER INC | Tanqueray |

The figure is the notebook’s own combined bar chart. Use the chart for ranking and relative scale; vendor sales alone should not be treated as a profitability score.

# 5. Purchase Contribution and Supplier Concentration

The notebook groups purchase dollars by vendor, calculates PurchaseContribution%, sorts the result, and plots the top ten vendors with cumulative contribution.

Figure 9. Original notebook Pareto chart: vendor contribution to total purchases (cell 90).

| Vendor in chart | Purchase contribution shown (%) |

| --- | --- |

| DIAGEO NORTH AMERICA INC | 16.30 |

| MARTIGNETTI COMPANIES | 8.30 |

| PERNOD RICARD USA | 7.76 |

| JIM BEAM BRANDS COMPANY | 7.64 |

| BACARDI USA INC | 5.67 |

| CONSTELLATION BRANDS INC | 4.97 |

| BROWN-FORMAN CORP | 4.31 |

| E & J GALLO WINERY | 3.93 |

| ULTRA BEVERAGE COMPANY LLP | 3.63 |

| M S WALKER INC | 3.18 |

The notebook reports that the top ten vendors contribute 65.69% of total purchase dollars. The chart’s cumulative line makes the concentration visible. Supplier dependency should be evaluated alongside product availability, substitutability, lead time, and vendor service performance.

# 6. Bulk Purchasing and Unit Price

The notebook calculates UnitPurchasePrice as TotalPurchaseDollars / TotalPurchaseQuantity and divides records into three quantity-based quantile groups using pandas qcut: Small, Medium, and Large.

Figure 10. Original notebook boxplot: impact of bulk purchasing on unit price (cell 98).

| Order-size group | Mean unit purchase price in notebook |

| --- | --- |

| Small | $39.07 |

| Medium | $15.49 |

| Large | $10.78 |

- The Large group has the lowest mean unit purchase price in the notebook output.

- The boxplot also shows extreme outliers, especially in the Small group; investigate product mix and premium products before generalizing.

- The notebook does not establish a single optimal purchase volume. Assess landed cost, carrying cost, storage, expiry, demand forecasts, and stockout risk before changing order sizes.

# 7. Slow-Moving Inventory and Unsold Capital

The notebook identifies vendors whose average StockTurnover is below 1 and calculates UnsoldInventoryValue as (TotalPurchaseQuantity − TotalQuantity) × PurchasePrice. It reports total unsold capital of approximately $2.71M.

| Analysis | Notebook method / result |

| --- | --- |

| Low-turnover vendor list | Filter StockTurnover < 1, group by VendorName, sort ascending, show first 10. |

| Unsold inventory estimate | (TotalPurchaseQuantity − TotalQuantity) × PurchasePrice. |

| Total unsold capital | Approximately $2.71M as reported by the notebook output. |

- Prioritize reconciliation against on-hand stock, returns, transfers, shrinkage, and the approved inventory valuation method before treating the estimate as a financial balance.

- Use SKU-level age, last-sale date, available quantity and carrying value to determine specific actions.

# 8. Profit-Margin Confidence Intervals and Statistical Test

The notebook separates records into the upper sales quartile (top-performing) and lower sales quartile (low-performing), then compares ProfitMargin distributions. The final chart below is the original notebook chart and is included without redrawing or replacing it.

Figure 11. Original notebook confidence-interval comparison for top- vs. low-sales vendors (cell 110).

| Group | 95% confidence interval for mean profit margin |

| --- | --- |

| Top-sales quartile | 30.74% to 31.61% |

| Low-sales quartile | 40.48% to 42.62% |

The notebook narrative states that the low-sales group’s confidence interval is higher than the top-sales group’s. The subsequent Welch two-sample t-test is documented in the notebook as testing whether the mean profit margins differ. Statistical significance does not explain the cause of the difference; investigate product mix, price positioning, cost, and volume.

# 9. Correlation Insights from the Notebook

Use Figure 5—the notebook’s original correlation heatmap—as the source of correlation values. The notebook narrative specifically notes the following relationships:

| Variable pair | Correlation stated in notebook | Interpretation in notebook |

| --- | --- | --- |

| PurchasePrice vs TotalSalesDollars | -0.012 | Weak negative relationship. |

| PurchasePrice vs GrossProfit | -0.016 | Weak negative relationship. |

| TotalPurchaseQuantity vs TotalSalesQuantity | 0.999 | Very strong positive relationship. |

| ProfitMargin vs TotalSalesPrice | -0.179 | Weak negative relationship. |

| StockTurnover vs GrossProfit | -0.038 | Very weak negative relationship. |

| StockTurnover vs ProfitMargin | -0.055 | Very weak negative relationship. |

Correlation does not establish causation. The near-perfect quantity correlation should be interpreted carefully because it may reflect how the summary fields are aggregated or defined.

# 10. Conclusions and Recommended Follow-up

| Focus | Recommended follow-up | Evidence to monitor |

| --- | --- | --- |

| Supplier concentration | Review contingency suppliers and concentration by category. | Purchase contribution and cumulative share. |

| Inventory capital | Reconcile unsold inventory and investigate low-turnover vendors. | Verified on-hand value, age, and sell-through. |

| Brand promotion | Run controlled tests for low-sales/high-margin target brands. | Incremental gross profit and sell-through. |

| Bulk purchasing | Validate unit-price differences with landed cost and holding cost. | Net savings after carrying and freight costs. |

| Data quality | Document filtering, zero-denominator handling and outlier rules. | Reconciled metrics and repeatable pipeline. |

## Limitations

- All charts in this document are embedded from the supplied notebook outputs; no replacement or newly designed charts have been added.

- The main analyses use the notebook’s filtered dataset, excluding rows with non-positive gross profit, profit margin, or total quantity.

- The report preserves notebook terminology and reported results; it does not rerun the database queries or independently verify the underlying transactions.

- Inventory value is an estimate produced by the notebook formula and should be reconciled before financial use.
