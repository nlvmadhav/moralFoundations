import pandas as pd

# Load the CSV file
file_path = 'updated_data.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Find the number of rows for each unique value in the first column
class_counts = df.iloc[:, 0].value_counts()

# Print the counts for each class
print("Number of rows for each class:")
print(class_counts)

# Print the total number of rows
total_rows = df.shape[0]
print("\nTotal number of rows:", total_rows)
