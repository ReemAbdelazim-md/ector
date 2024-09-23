# Ector Project

Ector is a data pipeline project that focuses on **data consolidation** and **descriptive analytics**. It processes data from the **Igraine** Gold layer (S1), applying a series of cleaning, transformation, and consolidation steps, before visualizing the results. The project follows a **modular pipeline structure**, where each component has a distinct role from data ingestion to visualization.

## Project Overview

The Ector project is designed to:

- **Ingest data** from the Igraine project’s **Gold layer**, which contains already processed and clean data.
- **Consolidate** and further clean data, ensuring its standardization and accuracy across multiple data streams.
- Process data in **three distinct workflows**: 
  - **Patient level**: Detailed patient-specific data processing.
  - **Surgeon level**: Data specific to surgeon activities and outcomes.
  - **Site level**: Data related to different locations or sites involved in the processes.
- Perform reusable **data transformations** (such as filtering, joining, and aggregating) as part of the processing.
- Generate **visualizations and dashboards** for easy reporting of processed data.

## Features

- **Automated Pipeline**: All components, from data ingestion to visualization, are connected in a unified pipeline.
- **Data Consolidation**: Handles data cleaning, deduplication, and standardization to ensure data integrity.
- **Multiple Data Workflows**: Processes data in parallel streams for patients, surgeons, and sites.
- **Reusable Transformations**: Contains modular, reusable transformations to be applied across workflows.
- **Visualization and Reporting**: Automatically generates visual dashboards based on the processed data.


## Folder Structure

This project is organized into the following main directories, each serving a specific purpose in the Ector data pipeline.

### **1. `config/`**:
- **Purpose**: Stores configuration files and environment-specific settings.
- **Details**: 
  - Contains configuration for database connections, environment variables, and other settings required by the pipeline.
  - Example: `configuration.yaml` stores connection details for accessing Igraine’s Gold layer.

---

### **2. `data_ingestion/`**:
- **Purpose**: Handles the ingestion of data from external sources.
- **Details**:
  - This folder contains scripts responsible for pulling data from Igraine's Gold layer or other external sources.
  - Example: `igraine_ingest.py` retrieves data and loads it into the pipeline for further processing.

---

### **3. `data_consolidation/`**:
- **Purpose**: Data cleaning and standardization processes (Data Hygiene).
- **Details**:
  - This folder’s scripts clean and standardize ingested data, ensuring it is ready for processing.
  - Example: `consolidate.py` removes duplicates, handles missing values, and applies consistent data formatting.

---

### **4. `data_processing/`**:
- **Purpose**: Holds reusable data transformations, such as filtering, joining, aggregating, and applying business logic.
- **Details**:
  - This folder contains functions to apply transformations and business logic to the data after consolidation.
  - Example: `transformations.py` holds reusable data processing functions applied across multiple workflows.

---

### **5. `pipeline/`**:
- **Purpose**: Orchestrates the entire data pipeline.
- **Details**:
  - Contains the main orchestration script, bringing together data ingestion, consolidation, processing, and visualization steps.
  - Example: `pipeline.py` is the entry point for running the full data pipeline from start to finish.

---

### **6. `src/`**:
- **Purpose**: Core source code and utilities for the pipeline.
- **Details**:
  - This folder holds reusable code and utility functions used throughout the pipeline.
  - Example: Logging, error handling, and utility functions can be placed here.

---

### **7. `tests/`**:
- **Purpose**: Contains unit and integration tests.
- **Details**:
  - This folder contains tests for individual pipeline components, ensuring the system behaves as expected.
  - Example: `test_ingestion.py` tests the data ingestion logic to validate its functionality.

---

### **8. `visualizations/`**:
- **Purpose**: Handles data visualization and dashboard generation.
- **Details**:
  - After data processing, this folder’s scripts generate visual reports and dashboards for analysis.
  - Example: `dashboards.py` can generate patient-level or site-level visualizations of the processed data.

---

### **9. `workflows/`**:
- **Purpose**: Manages the data workflows for different streams (patient, surgeon, site).
- **Details**:
  - Each script in this folder processes a specific data stream (patient, surgeon, or site), handling its specific transformations and logic.
  - Example: `patient_workflow.py` handles patient data transformations.

---

## Key Files

### **`.gitignore`**:
- **Purpose**: Specifies files and directories to be ignored by Git.
- **Details**:
  - Ensures that sensitive files like `.env` or temporary files like `.pyc` are excluded from version control.

---

### **`bitbucket-pipelines.yml`**:
- **Purpose**: CI/CD configuration for Bitbucket Pipelines.
- **Details**:
  - Automates testing, building, and deploying the project in Bitbucket Pipelines.
  - Example: This file runs tests automatically when code is pushed to the repository.

---

### **`configuration.yaml`**:
- **Purpose**: Stores configuration for the project.
- **Details**:
  - Contains environment-specific settings such as database connection strings or API credentials.

---

### **`README.md`**:
- **Purpose**: Provides project documentation.
- **Details**:
  - Contains an overview of the project, setup instructions, and a description of the folder structure.

---

### **`requirements.txt`**:
- **Purpose**: Lists the Python dependencies required by the project.
- **Details**:
  - Contains a list of required Python libraries to ensure the project has the necessary packages installed.
  - Example: Run `pip install -r requirements.txt` to install the required dependencies.

## File Visual Breakdown 

Ector/
│
├── /config                         # Stores configuration files and environment-specific settings
│   └── configuration.yaml          # Contains environment-specific settings like database connections
│
├── /data_ingestion                 # Handles the ingestion of data from external sources
│   ├── igraine_ingest.py           # Script to connect to Igraine’s Gold layer and retrieve data
│   └── __init__.py                 # Makes the folder a Python package
│
├── /data_consolidation             # Data cleaning, deduplication, and standardization processes (Data Hygiene)
│   ├── consolidate.py              # Cleans and consolidates ingested data before processing
│   └── __init__.py                 # Makes the folder a Python package
│
├── /data_processing                # Holds reusable data transformations (filtering, joining, aggregating, etc.)
│   ├── transformations.py          # Functions for reusable data transformations across workflows
│   └── __init__.py                 # Makes the folder a Python package
│
├── /pipeline                       # Orchestrates the entire data pipeline
│   ├── pipeline.py                 # Main script to orchestrate the entire pipeline
│   └── __init__.py                 # Makes the folder a Python package
│
├── /src                            # Core source code and utilities for the pipeline
│   └── utils.py                    # Utility functions such as logging, error handling
│
├── /tests                          # Contains all the unit tests to ensure each part of the pipeline works as expected
│   ├── test_ingestion.py           # Tests the data ingestion functionality
│   ├── test_consolidation.py       # Tests the data consolidation functionality
│   ├── test_processing.py          # Tests the reusable data transformations
│   └── __init__.py                 # Makes the folder a Python package
│
├── /visualizations                 # Handles data visualization and dashboard generation
│   ├── dashboards.py               # Generates visual reports from processed data
│   └── __init__.py                 # Makes the folder a Python package
│
├── /workflows                      # Manages the data workflows for different streams (patient, surgeon, site)
│   ├── patient_workflow.py         # Processes patient-level data
│   ├── surgeon_workflow.py         # Processes surgeon-level data
│   ├── site_workflow.py            # Processes site-level data
│   └── __init__.py                 # Makes the folder a Python package
│
├── .gitignore                      # Specifies files and directories to be ignored by Git
├── bitbucket-pipelines.yml         # CI/CD configuration for Bitbucket Pipelines
├── README.md                       # Project documentation
└── requirements.txt                # Lists Python dependencies required by the project
