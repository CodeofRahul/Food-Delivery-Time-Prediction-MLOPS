# Food Delivery Time Prediction: A Modular Machine Learning Pipeline

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/CodeofRahul/Machine_Learning_Modular_Coding_Project/graphs/commit-activity)

## Project Overview

In today's fast-paced world, efficient food delivery is crucial. This project presents a robust and modular end-to-end machine learning pipeline designed to **accurately predict food delivery times**. By leveraging a rich dataset containing delivery personnel details, restaurant locations, order information, and environmental factors like weather and traffic, I've developed a model capable of providing valuable insights for optimizing delivery operations.

This project emphasizes clean, maintainable, and reproducible code, showcasing best practices in modern machine learning engineering. It's built to handle real-world challenges, offering a scalable and adaptable solution for predicting delivery times.

## Key Features

* **Accurate Delivery Time Prediction:** Utilizes a comprehensive dataset to build a predictive model for food delivery times.
* **Modular Architecture:** The pipeline is designed with a clear separation of concerns, facilitating easy understanding, modification, and extension.
    * **Components:** Independent modules for data ingestion, transformation, model training, and evaluation.
    * **Pipelines:** Orchestrated end-to-end workflows for training and prediction.
* **Batch Prediction:** Implements a batch prediction system for processing multiple orders efficiently.
* **Robust Error Handling:** Custom exception handling and logging ensure stability and maintainability.
* **Data Validation:** Utilizes schema validation to maintain data integrity.
* **Reproducibility:** `requirements.txt` and `setup.py` ensure consistent environments.

* **`Artifact`:** Stores trained models and other artifacts.
* **`Data`:** Contains data ingestion related files.
* **`Prediction`:** Handles batch prediction outputs.
* **`config`:** Stores configuration templates.
* **`src`:** Contains the core application code.
    * **`components`:** Individual modules for different pipeline stages.
    * **`config`:** Configuration-related code.
    * **`constants`:** Project constants.
    * **`entity`:** Data entity definitions.
    * **`exception`:** Custom exception handling.
    * **`logger`:** Logging utilities.
    * **`pipeline`:** End-to-end pipeline logic.
    * **`utils`:** Utility functions.
    * **`__init__.py`:** Makes directories Python packages.
* **`templates`:** HTML templates for web app.
* **`app.py`:** Main application file.
* **`exception.py`:** Custom exception definitions.
* **`logs.py`:** Logging configuration.
* **`main.py`:** Main execution script.
* **`pipeline.txt`:** Pipeline execution details.
* **`requirement.txt`:** Project dependencies.
* **`schema.yaml`:** Data schema definition.
* **`setup.py`:** Project setup and packaging.

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/CodeofRahul/Food-Delivery-Time-Prediction-MLOPS.git
    cd Food_Delivery_Time_Prediction-MLOPS
    ```

2.  **Create a virtual environment:**

    ```bash
    conda create -p env python=3.9 -y
    conda activate env/ --> CMD <br>
    source activate env/ --> git bash
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    python app.py
    ```

5.  **Run the training pipeline:**

    ```bash
    python main.py
    ```

## Usage

This project can be used as a foundation for building and deploying food delivery time prediction systems. Its modular design allows for easy customization and extension.

## Contributing

Contributions are welcome! Please submit pull requests or open issues to contribute.


