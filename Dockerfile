# Use an official Python runtime as a parent image
FROM python:3.11-slim 

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project folder into the container
COPY . .

# The command to run your ETL scripts in order
CMD python data_extraction.py && python data_transformation.py && python data_loading.py