# Data Analytics Capstone Project

# End-to-End Data Analytics Capstone Project This project is a comprehensive, end-to-end data analytics pipeline that demonstrates proficiency in a wide range of tools and methodologies. It covers the full lifecycle of a data project, from initial planning and data extraction to automated deployment and final visualization.
1. Project Architecture
This project follows an automated ETL (Extract, Transform, Load) pipeline. Data is extracted from an API, cleaned and processed, and then loaded into a database. The entire process is containerized and automated with CI/CD.

The key components are:

Data Source: A public API.

ETL Pipeline: Python scripts run inside a Docker container.

Database: A SQLite database to store the final, cleaned data.

Dashboards: Visualizations created in Power BI and Tableau.

2. Technical Stack
This project exercises a wide range of skills and tools, including:

Project Management: Jira/Agile

Version Control: Git, GitHub

Data Extraction & Processing: Python, Pandas, APIs

Data Storage: Excel, SQL (SQLite)

Automation & DevOps: Docker, CI/CD (GitHub Actions)

Business Intelligence: Power BI, Tableau

Quality Assurance: Testing (Pytest)

Documentation: Markdown

3. Setup Instructions
To run this project, you will need the following tools installed:

Python 3.9 or higher

Docker Desktop

Git

Step-by-Step Setup:

Clone the repository: git clone [Your-GitHub-Repository-URL]

Navigate to the project directory: cd [Your-Project-Folder]

Build the Docker image: docker build -t etl-pipeline-image .

Run the ETL pipeline: docker run --rm -v "$(pwd)/data:/app/data" etl-pipeline-image

This command will execute the ETL pipeline, creating a data folder with raw.json, transformed.csv, and project_database.db files.

4. Key Findings & Insights
(This section is a placeholder for you to fill in based on your analysis)

Insight 1: Briefly describe a key finding from your Power BI dashboard. For example, "The data reveals that there is a high number of posts associated with a single user, suggesting that the data is not evenly distributed."

Insight 2: Summarize another key finding from your Tableau dashboard. For example, "The post titles are often short, which indicates the data is well-suited for text analysis and natural language processing in future work."

5. Conclusion
This project demonstrates the complete end-to-end process of building a data analytics pipeline. The use of modern DevOps practices ensures the project is not only functional but also scalable and repeatable.

6. Acknowledgments
API: Data for this project was extracted from the JSONPlaceholder API.

Guidance: This project was built with step-by-step guidance.
