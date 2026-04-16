import pandas as pd
import glob

# 1. Find all the CSV files in the data folder
# (Assumes your CSVs are in a folder named 'data')
files = glob.glob("data/*.csv")

dataframes = []

for file in files:
    # Read the file
    df = pd.read_csv(file)
    
    # 2. Filter for only "Pink Morsel"
    # Note: Using .lower() ensures we catch it even if the capitalization is messy
    df = df[df['product'].str.lower() == 'pink morsel']
    
    # 3. Calculate "Sales" (Price * Quantity)
    # We strip the '$' sign from the price and convert to float
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['sales'] = df['price'] * df['quantity']
    
    # 4. Keep only the required columns
    df = df[['sales', 'date', 'region']]
    
    dataframes.append(df)

# 5. Combine all three files into one
merged_df = pd.concat(dataframes)

# 6. Export the final formatted file
merged_df.to_csv('formatted_data.csv', index=False)

print("Data processing complete! 'formatted_data.csv' has been created.")