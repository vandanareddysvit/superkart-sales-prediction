# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the FLASK_APP environment variable
ENV FLASK_APP=superkart_api.py


# Run the Flask application
# For development, you might use 'flask run --host=0.0.0.0'
CMD ["python", "superkart_api.py"]
