import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)

def create_vendor_summary(conn):
    ''' this function will merge the different tables to get the overall summary and adding new columns in the resultant data'''
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS (
        SELECT 
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    PurchaseSummary AS (
       SELECT
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price AS ActualPrice,
            pp.Volume,
            SUM(p.Quantity) AS TotalQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars,
        FROM purchase p
        JOIN purchase_price pp 
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume    
   ),

    SalesSummary AS (
        SELECT
            s.VendorNo,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(salesDollars) AS TotalSalesDollars
            SUM(salesPrice) AS TotalSalesPrice
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales 
        GROUP BY VendorNo, Brand
    )

    SELECT
     ps.VendorNumber,
     ps.VendorName,
     ps.Brand,
     ps.Description,
     ps.PurchasePrice,
     ps.ActualPrice,
     ps.Volume,
     ps.TotalPurchaseQuantity,
     ps.TotalPurchaseDollars,
     fs.FreightCost,
     ss.TotalQuantity,
     ss.TotalSalesDollars,
     ss.TotalSalesPrice,
     ss.TotalExciseTax
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
     ON ps.VendorNumber = ss.VendorNo
     AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
     ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC""", conn)

    return vendor_sales_summary


def clean_data(df):
    ''' this function will clean the data'''
    # changing datatype to float
    df['Volume'] = df['Volume'].astype(float)

    # filling null values with 0
    df.fillna(0, inplace=True)

    # removing spaces from categoricat columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # creating new columns for better analysis
    vendor_sales_summary['GrossProfit'] = vendor_sales_summary['TotalSalesDollars'] - vendor_sales_summary['TotalPurchaseDollars']
    vendor_sales_summary['ProfitMargin'] = (vendor_sales_summary['GrossProfit'] / vendor_sales_summary['TotalSalesDollars']) * 100
    vendor_sales_summary['StockTurnover'] = vendor_sales_summary['TotalQuantity'] / vendor_sales_summary['TotalPurchaseQuantity']
    vendor_sales_summary['SalestoPurchaseRatio'] = vendor_sales_summary['TotalSalesDollars'] / vendor_sales_summary['TotalPurchaseDollars']

    return df



    
if __name__ == "__main__":
    # creating database connection
    conn = sqlite3.connect("inventory.db")  

    logging.info("Creating vendor summary Table......")
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info("Cleaning the data......")
    cleaned_df = clean_data(summary_df)
    logging.info(cleaned_df.head())

    logging.info("Ingesting the data into database......")
    ingest_db(cleaned_df, conn, "vendor_summary",conn)  
    logging.info('Completed')