# Use official Python image from Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy Python scripts into the container
COPY main.py ./
COPY fetch_models.py ./

# Set the entry point to run the main script
CMD ["python", "main.py"]

