# Start with a base image that has Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies (assuming you have a requirements.txt file)
RUN pip install --no-cache-dir -r requirements.txt

# Command to run when the container starts
CMD ["python", "calculator.py"]
