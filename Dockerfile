# Use a Python base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Install tkinter (the GUI package for Python)
RUN apt-get update && apt-get install -y python3-tk

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the working directory
COPY . .

# Command to run the GUI application
CMD ["python", "main.py"]
