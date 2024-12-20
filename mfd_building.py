import pandas as pd
import re

# Load your dataset (replace 'tweets.csv' with the path to your dataset)
df = pd.read_csv('dataset.csv')  # Ensure there's a 'tweet' column

# Load the MFD dictionary and map to primary categories (e.g., care, fairness)
mfd_file = 'mfd2.0.dic'

# Initialize a dictionary to store words and their foundations
mfd = {}

with open(mfd_file, 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('%') or line.isdigit():  # Skip comments and metadata
            continue
        word, category_code = line.split('\t')
        category_code = int(category_code)

        # Map category codes to primary moral foundation categories
        category_map = {
            range(1, 3): 'Care',       # care.virtue and care.vice
            range(3, 5): 'Fairness',   # fairness.virtue and fairness.vice
            range(5, 7): 'Loyalty',    # loyalty.virtue and loyalty.vice
            range(7, 9): 'Authority',  # authority.virtue and authority.vice
            range(9, 11): 'Sanctity',  # sanctity.virtue and sanctity.vice
        }

        # Map the category code to the corresponding foundation
        for key, value in category_map.items():
            if category_code in key:
                mfd[word.lower()] = value
                break

# Function to clean text (remove special characters, URLs, etc.)
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    return text

# Function to classify text using the MFD
def classify_text(text):
    tokens = text.split()  # Simple tokenization using spaces
    foundation_counts = {foundation: 0 for foundation in set(mfd.values())}

    for token in tokens:
        if token in mfd:
            foundation_counts[mfd[token]] += 1

    # Return the foundation with the highest count
    most_common = max(foundation_counts, key=foundation_counts.get)
    return most_common if foundation_counts[most_common] > 0 else 'None'

# Apply the functions to the dataset
df['cleaned_tweet'] = df['Tweet Text'].apply(clean_text)
df['Foundation'] = df['cleaned_tweet'].apply(classify_text)

# Save the classified data to a new CSV
df.to_csv('classified_tweets.csv', index=False)
