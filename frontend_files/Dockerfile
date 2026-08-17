# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the Streamlit app and requirements file into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r streamlit_requirements.txt

# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
