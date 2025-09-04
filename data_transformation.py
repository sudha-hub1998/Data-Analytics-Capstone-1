import pandas as pd
import json
import os

# Define the file paths
raw_data_path = os.path.join('data', 'raw_products.json')
transformed_data_path = os.path.join('data', 'transformed_products.csv')

def transform_data(input_path, output_path):
    """
    Reads raw JSON data, transforms it, and saves it as a cleaned CSV file.
    """
    try:
        # Check if the raw data file exists
        if not os.path.exists(input_path):
            print(f"Error: Raw data file not found at {input_path}")
            return False

        # Read the raw JSON data
        with open(input_path, 'r') as f:
            data = json.load(f)

        # Convert the JSON data to a pandas DataFrame
        df = pd.DataFrame(data)

        # --- Data Transformation Steps ---
        # 1. Select relevant columns
        # The API we used is a sample, so we will assume we only need 'API', 'Description', 'Auth', 'HTTPS'
        # Adjust these columns based on the actual data you received
        df = df[['userId', 'id', 'title', 'body']]

        # 2. Handle missing values (for this example, we drop rows with any missing values)
        df.dropna(inplace=True)

        # 3. Rename columns for clarity
        df.rename(columns={'userId': 'user_id', 'id': 'post_id', 'title': 'post_title', 'body': 'post_body'}, inplace=True)
        
        # 4. Convert to a different data type if needed (e.g., convert 'id' to integer)
        # This step is optional but shows a good practice
        df['post_id'] = df['post_id'].astype(int)

        # Save the transformed DataFrame to a CSV file
        df.to_csv(output_path, index=False)
        print(f"Data successfully transformed and saved to {output_path}")
        return True

    except Exception as e:
        print(f"An error occurred during transformation: {e}")
        return False

# This block ensures the transformation function runs when the script is executed
if __name__ == "__main__":
    transform_data(raw_data_path, transformed_data_path)