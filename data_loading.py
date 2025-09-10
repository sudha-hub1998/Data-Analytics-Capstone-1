import pandas as pd
import sqlalchemy as sa
import os

# Define the file paths
transformed_data_path = os.path.join('data', 'transformed_products.csv')
db_path = os.path.join('data', 'project_database.db')
table_name = 'api_data_posts'

def load_data(input_path, output_db_path, table):
    """
    Reads a transformed CSV file and loads it into a SQLite database table.
    """
    try:
        # Check if the transformed CSV file exists
        if not os.path.exists(input_path):
            print(f"Error: Transformed data file not found at {input_path}")
            return False

        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(input_path)

        # Create a database engine
        # 'sqlite:///' tells SQLAlchemy to use a SQLite database
        engine = sa.create_engine(f'sqlite:///{output_db_path}')

        # Load the DataFrame into the SQL database
        # if_exists='replace' will overwrite the table if it already exists
        df.to_sql(table, con=engine, if_exists='replace', index=False)

        print(f"Data successfully loaded into the '{table}' table in the database.")
        return True

    except Exception as e:
        print(f"An error occurred during loading: {e}")
        return False

# This block ensures the loading function runs when the script is executed
if __name__ == "__main__":
    load_data(transformed_data_path, db_path, table_name)