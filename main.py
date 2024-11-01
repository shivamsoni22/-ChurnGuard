from scr.data_preprocessing import load_all_data, clean_data

raw_data = load_all_data()
cleaned_data = clean_data(raw_data)
cleaned_data.to_csv(r"D:\-ChurnGuard\Data\processed\cleaned_data.csv", index=False)
print("Cleaned data saved to processed folder.")
