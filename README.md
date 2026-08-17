# superkart-sales-prediction
Project Description: SuperKart Sales Forecasting Deployment
This repository contains a robust solution for forecasting sales revenue for SuperKart, a retail chain. The project encompasses building a machine learning model, developing a Flask-based API for inference, and creating a Streamlit user interface for interactive predictions.

Key Features:
Machine Learning Model: Utilizes a RandomForestRegressor for accurate sales predictions, with hyperparameters tuned using GridSearchCV.
Flask API Backend: A lightweight Flask application (superkart_api.py) exposes two key endpoints:
/v1/predict for online (single) predictions, accepting JSON input.
/v1/predictbatch for batch predictions, accepting CSV file uploads.
Streamlit Frontend: An interactive Streamlit application (streamlit_app.py) provides a user-friendly interface to input product and store details and receive real-time sales forecasts from the Flask API.
Containerization with Docker: Both the Flask API and the Streamlit UI are containerized using Docker, ensuring portability and consistent deployment environments.
Deployment with GitHub Codespaces: The entire solution is designed for seamless deployment within GitHub Codespaces, leveraging Docker Compose for multi-service orchestration.
Technologies Used:
Python: Primary programming language.
scikit-learn: For machine learning model development.
Pandas & NumPy: For data manipulation and numerical operations.
Flask: For building the RESTful API.
Streamlit: For creating the interactive web interface.
Docker: For containerization of services.
GitHub Codespaces: For cloud-based development and deployment environment.
This project demonstrates a complete end-to-end MLOps pipeline, from model training and serialization to API development and containerized deployment.
