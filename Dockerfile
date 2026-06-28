# Use official Python runtime as base image
FROM python:3.10-slim


# Install bash if not present (slim images sometimes lack it)
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Set environment variables to optimize Python behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the application
# CMD ["python", "generate_dataset.py"]   
CMD ["bash"]   