import csv

# Replace with your input and output file paths
input_file = 'dataset.csv'
output_file = 'output.csv'

# Open the input CSV file for reading
with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    rows = []
    
    # Process each row in the CSV
    for row in reader:
        # Replace occurrences in each cell of the row
        updated_row = [cell.replace("BrainDrain", "Brain Drain") for cell in row]
        rows.append(updated_row)

# Open the output CSV file for writing
with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print(f"Replacement complete. Updated file saved as {output_file}.")
