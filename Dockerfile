# LearningSpace Dockerfile
# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set metadata
LABEL maintainer="learning@example.com" \
      version="1.0" \
      description="Python Learning Space - Algorithm, Math, and Data Analysis Tasks"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    LANG=C.UTF-8

# Set working directory
WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY tasks/ ./tasks/
COPY solutions/ ./solutions/
COPY tests/ ./tests/
COPY *.py ./
COPY *.md ./

# Copy documentation
COPY docs/ ./docs/

# Create non-root user for security
RUN useradd -m -u 1000 learner && \
    chown -R learner:learner /app

# Switch to non-root user
USER learner

# Run tests by default
CMD ["pytest", "tests/", "-v"]
