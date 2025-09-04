import requests
import json
import os

# create a 'data' folder to store raw data
if not os.path.exists('data'):
    os.makedirs('data')

# URL of the public API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts"

def get_product_data(url):
    """Fetches data from the API and saves it to json files."""
    try:
        response = requests.get(url)
        # Raise an exceptions for bad status codes(4xx or 5xx)
        response.raise_for_status()
        data = response.json()

        #define the output file path
        output_file_path = os.path.join('data', 'raw_products.json')

        #save the data to json file 
        with open(output_file_path, 'w') as f:
            json.dump(data, f, indent = 4)

        print(f"Data successfully saved to {output_file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    get_product_data(api_url)
