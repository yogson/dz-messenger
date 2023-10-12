# Use the official Python image as a base
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files
COPY pyproject.toml poetry.lock ./

# Install Poetry and project dependencies
RUN pip install poetry && poetry install --no-root

# Copy your FastAPI application code into the container
COPY src /app

# Expose the port your FastAPI application is running on
EXPOSE 8000

# Command to start the application using Uvicorn
CMD ["poetry", "run", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
