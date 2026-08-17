# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app/model_api

# Copy the current directory contents into the container at /app/model_api
COPY . /app/model_api

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the FLASK_APP environment variable
ENV FLASK_APP=superkart_api.py

# Move the 'backend_files' directory into /app (same level as 'model_api')
# This ensures both the Flask app and the model/preprocessor are accessible
RUN mv /app/backend_files /app/

# Run the Flask application
# For development, you might use 'flask run --host=0.0.0.0'
# For production, it's recommended to use a production-ready WSGI server like Gunicorn or uWSGI
CMD ["python", "superkart_api.py"]
