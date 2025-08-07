import pandas as pd

# Step 1: Load the data
df = pd.read_csv("sample_lab_data.csv")

# Step 2: Print basic info
print("Original Data:")
print(df)

# Step 3: Drop rows with missing test results or dates
df_clean = df.dropna(subset=["Test_Result", "Result_Date"])

# Step 4: Convert date to datetime format
df_clean["Result_Date"] = pd.to_datetime(df_clean["Result_Date"])

# Step 5: Save the cleaned data
df_clean.to_csv("cleaned_lab_data.csv", index=False)

print("\nCleaned Data:")
print(df_clean)


