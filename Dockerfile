# Use an appropriate base image with Python
FROM python:3.9

# Set the working directory inside the Docker container
WORKDIR /app

# Copy the requirements file to the Docker container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the Docker container
COPY . .

# Expose the necessary port(s)
EXPOSE 8000

# Define the command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
