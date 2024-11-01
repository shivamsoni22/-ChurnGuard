import pandas as pd

def load_csv_data(file_path):
    return pd.read_csv(file_path)

def load_excel_data(file_path, sheet_name=0):
    return pd.read_excel(file_path, sheet_name=sheet_name)

def load_all_data():
    file_paths = [
        r"D:\-ChurnGuard\Data\raw\Churn for Bank Customers.csv",
        r"D:\-ChurnGuard\Data\raw\Customer Segmentation Dataset.xlsx",
        r"D:\-ChurnGuard\Data\raw\IBM dataset.xlsx",
        r"D:\-ChurnGuard\Data\raw\online_retail.csv",
        r"D:\-ChurnGuard\Data\raw\Telco-Customer-Churn.csv"
    ]
    
    all_dataframes = []
    
    for file_path in file_paths:
        if file_path.endswith(".csv"):
            df = load_csv_data(file_path)
            print(f"Loaded CSV file: {file_path}, Shape: {df.shape}")
        elif file_path.endswith(".xlsx"):
            df = load_excel_data(file_path)
            print(f"Loaded Excel file: {file_path}, Shape: {df.shape}")
            
        all_dataframes.append(df)
    
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    return combined_df

def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(0)  # Replace missing values with 0
    return df

