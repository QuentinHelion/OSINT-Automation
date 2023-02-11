# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory
WORKDIR ./OSINT-Automation/

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port that the app will run on
EXPOSE 8000

# Run setup
RUN ./setup.sh

# Run the application
CMD ["python", "./OSINT-Automation/main.py"]


# Build
# docker build -t app .

# Run
# docker run -p 8000:8000 app
