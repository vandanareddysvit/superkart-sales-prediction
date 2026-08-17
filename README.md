# SuperKart Sales Prediction and Deployment

## Project Overview
This repository provides an end-to-end solution for forecasting sales revenue for SuperKart, a retail chain. The project involves developing a machine learning model, creating a Flask-based API for model serving, and building a Streamlit user interface for interactive predictions. The entire system is designed for containerized deployment using Docker and GitHub Codespaces.

### Objective
SuperKart aims to optimize inventory management and refine regional sales strategies by accurately forecasting sales revenue for its outlets for the upcoming quarter. This solution operationalizes a predictive model based on historical sales data into a robust, deployable system.

## Key Features
- **Machine Learning Model:** A `RandomForestRegressor` trained on historical sales data, with hyperparameters optimized using `GridSearchCV`.
- **Flask API Backend:** A RESTful API built with Flask (`superkart_api.py`) exposing:
  - `/v1/predict`: For real-time, single-instance predictions (JSON input).
  - `/v1/predictbatch`: For batch predictions, accepting CSV file uploads.
- **Streamlit Frontend:** An interactive web application (`streamlit_app.py`) for users to input features and get sales predictions through an intuitive interface.
- **Containerization:** Both the Flask API and Streamlit UI are containerized using Docker, ensuring consistent environments and ease of deployment.
- **Orchestration:** `docker-compose.yml` (to be added/configured) orchestrates the multi-service application, enabling the backend and frontend to communicate seamlessly.
- **GitHub Codespaces Integration:** Designed for development and deployment within GitHub Codespaces for a streamlined MLOps workflow.

## Technologies Used
- **Python** (3.9+)
- **Data Science Libraries:** `pandas`, `numpy`, `scikit-learn`
- **Machine Learning Models:** `RandomForestRegressor`, `DecisionTreeRegressor`
- **API Framework:** `Flask`
- **Frontend Framework:** `Streamlit`
- **Containerization:** `Docker`
- **Development/Deployment Environment:** `GitHub Codespaces`
- **HTTP Requests:** `requests` library
- **Model Serialization:** `joblib`

## Getting Started
These instructions will get you a copy of the project up and running on your local machine or, ideally, within a GitHub Codespace for development and testing purposes.

### Prerequisites
- A GitHub account.
- Docker Desktop installed (if running locally).
- Access to GitHub Codespaces (recommended).

### Setup within GitHub Codespaces (Recommended)
1.  **Fork this repository** to your GitHub account.
2.  **Open the repository in a Codespace:** On your forked repository page, click the green `Code` button and select `Create codespace on main`.
3.  **Wait for Codespace to initialize:** Your Codespace will provision, and Docker containers will be built and started according to the `docker-compose.yml` (if provided, otherwise you will build them manually).
4.  **Forwarded Ports:** Ensure ports `5000` (for Flask API) and `8501` (for Streamlit UI) are forwarded and set to `Public` in the Codespaces 'Ports' tab.

### Local Setup (Alternative)
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vandanareddysvit/superkart-sales-prediction.git
    cd superkart-sales-prediction
    ```
2.  **Build and run Docker containers:**
    If a `docker-compose.yml` is provided:
    ```bash
    docker-compose up --build
    ```
    Otherwise, you'll need to build and run the Flask and Streamlit containers separately:
    ```bash
    # Build Flask API image
    docker build -t superkart-api -f model_api/Dockerfile .
    # Run Flask API container
    docker run -d -p 5000:5000 --name superkart_backend superkart-api

    # Build Streamlit UI image
    docker build -t superkart-streamlit -f model_api/Dockerfile.streamlit .
    # Run Streamlit UI container (linking to Flask backend)
    docker run -d -p 8501:8501 --name superkart_frontend --link superkart_backend:superkart_backend superkart-streamlit
    ```

## Usage
Once the containers are running and ports are forwarded:

- **Access the Streamlit UI:** Open your browser to the forwarded URL for port `8501` (e.g., `https://<your-codespace-url>-8501.app.github.dev`).
- **Test the Flask API (Health Check):** Access the `/health` endpoint at your forwarded API URL (e.g., `https://<your-codespace-url>-5000.app.github.dev/health`).
- **Test API endpoints using `curl` or `requests`:**
  - **Online Prediction (`/v1/predict`):**
    ```bash
    curl -X POST \
         -H "Content-Type: application/json" \
         -d '{ "Product_Weight": 12.66, "Product_Sugar_Content": "Low Sugar", "Product_Allocated_Area": 0.027, "Product_MRP": 117.08, "Store_Size": "Medium", "Store_Location_City_Type": "Tier 2", "Store_Type": "Supermarket Type2", "Product_Id_char": "FD", "Store_Age_Years": 16, "Product_Type_Category": "Non Perishables" }' \
         https://<your-codespace-url>-5000.app.github.dev/v1/predict
    ```
  - **Batch Prediction (`/v1/predictbatch`):**
    (First, create a `batch_data.csv` file with your batch input data)
    ```bash
    curl -X POST -F "file=@batch_data.csv" https://<your-codespace-url>-5000.app.github.dev/v1/predictbatch
    ```

## Project Structure
```
.github/
├── codespaces/
│   └── .devcontainer/
│       └── devcontainer.json  # Codespaces configuration
├── workflows/
│   └── ...                    # CI/CD workflows (if any)
├── README.md                  # This file
├── superkart_notebook.ipynb   # Jupyter Notebook for EDA, modeling, and deployment steps
├── model/
│   ├── superkart_model.joblib # Trained ML model
│   └── preprocessor.joblib    # Fitted preprocessor
└── model_api/
    ├── superkart_api.py       # Flask API application
    ├── streamlit_app.py       # Streamlit frontend application
    ├── requirements.txt       # Python dependencies for Flask
    ├── streamlit_requirements.txt # Python dependencies for Streamlit
    ├── Dockerfile             # Dockerfile for Flask API
    └── Dockerfile.streamlit   # Dockerfile for Streamlit UI

# ... other data files or configuration ...
```
