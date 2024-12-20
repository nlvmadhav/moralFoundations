import pandas as pd

# Read the CSV file
df = pd.read_csv('updated_main_data.csv')  # Replace with your actual file path

# Step 1: Replace occurrences of 'authorithy' with 'authority' in the Foundation column
df['Foundation'] = df['Foundation'].replace('authorithy', 'authority')

# Step 2: Convert the Foundation column to lowercase
df['Foundation'] = df['Foundation'].str.lower()

# Step 3: Save the updated dataset to a new CSV file
df.to_csv('updated_data.csv', index=False)

# Optionally, print the updated dataframe to verify
print(df)
