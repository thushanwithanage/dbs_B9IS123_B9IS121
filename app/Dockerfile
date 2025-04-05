FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application code from the app folder into the Docker container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Expose the application port
EXPOSE 3000

# Run the FastAPI application with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]