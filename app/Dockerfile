# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Install Curl
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# Download and install Poetry
RUN curl -sSL https://install.python-poetry.org -o install-poetry.py \
    && python3 install-poetry.py

# Add Poetry to the PATH
ENV PATH="/root/.local/bin:$PATH"

# Verify Poetry installation
RUN poetry --version

# Configure Poetry
RUN poetry config virtualenvs.create false

# Copy only the pyproject.toml and poetry.lock (if exists) to cache the dependencies layer
COPY pyproject.toml poetry.lock* /code/

# Install dependencies without creating virtual environments
RUN poetry install --only=main --no-root --no-interaction --no-ansi

# Copy the rest of your application code
COPY . /code

# Expose the port the app runs on
EXPOSE 80

# Clean up (remove curl and the poetry installer script)
RUN apt-get purge -y --auto-remove curl \
    && rm install-poetry.py

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
