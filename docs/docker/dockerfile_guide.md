# Dockerfile Complete Guide

## What is a Dockerfile?

A Dockerfile is a text document containing all commands needed to build a Docker image. It's like a recipe for creating your containerized application.

## Basic Structure

```dockerfile
# Comment
INSTRUCTION arguments
```

## Core Instructions

### FROM - Base Image

Every Dockerfile starts with `FROM`. It specifies the base image.

```dockerfile
# Official Python image
FROM python:3.11

# Specific version
FROM python:3.11.5-slim

# Alpine (smallest)
FROM python:3.11-alpine

# Multiple stages
FROM python:3.11 AS builder
FROM python:3.11-slim AS runtime
```

### WORKDIR - Set Working Directory

Sets the working directory for subsequent instructions.

```dockerfile
WORKDIR /app

# All subsequent commands run from /app
COPY . .
RUN pip install -r requirements.txt
```

### COPY - Copy Files

Copies files from host to container.

```dockerfile
# Copy single file
COPY requirements.txt .

# Copy directory
COPY src/ /app/src/

# Copy everything (use .dockerignore to exclude)
COPY . .

# Copy with ownership
COPY --chown=user:group file.txt /app/
```

### ADD - Advanced Copy

Like COPY but with extra features (URL download, auto-extraction).

```dockerfile
# Copy file
ADD requirements.txt .

# Download from URL
ADD https://example.com/file.tar.gz /app/

# Auto-extract tar archives
ADD archive.tar.gz /app/
```

⚠️ **Best Practice**: Use `COPY` unless you need `ADD`'s special features.

### RUN - Execute Commands

Executes commands during image build.

```dockerfile
# Shell form (runs in shell)
RUN pip install flask

# Exec form (no shell)
RUN ["pip", "install", "flask"]

# Multiple commands (single layer)
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Multiple commands (multiple layers - avoid!)
RUN apt-get update
RUN apt-get install -y curl
RUN rm -rf /var/lib/apt/lists/*
```

### CMD - Default Command

Provides defaults for executing container.

```dockerfile
# Exec form (preferred)
CMD ["python", "app.py"]

# Shell form
CMD python app.py

# Parameters for ENTRYPOINT
CMD ["--port", "8000"]
```

**Only the last CMD matters!**

### ENTRYPOINT - Command Prefix

Configure container to run as executable.

```dockerfile
# Exec form
ENTRYPOINT ["python"]
CMD ["app.py"]
# Runs: python app.py

# Override CMD at runtime
docker run myimage script.py
# Runs: python script.py

# Shell form
ENTRYPOINT python app.py
```

### ENV - Environment Variables

Set environment variables.

```dockerfile
# Single variable
ENV PORT=8000

# Multiple variables
ENV PORT=8000 \
    DEBUG=1 \
    LOG_LEVEL=info

# Use in subsequent commands
ENV APP_HOME=/app
WORKDIR $APP_HOME
```

### EXPOSE - Document Ports

Documents which ports the container listens on.

```dockerfile
# Single port
EXPOSE 8000

# Multiple ports
EXPOSE 8000 8001 8002

# TCP (default) or UDP
EXPOSE 8000/tcp
EXPOSE 9000/udp
```

⚠️ **Note**: EXPOSE is documentation only. Use `-p` flag when running container.

### VOLUME - Create Mount Point

Creates a mount point for external volumes.

```dockerfile
# Single volume
VOLUME /data

# Multiple volumes
VOLUME ["/data", "/logs"]

# Used for persistent data
VOLUME /var/lib/mysql
```

### USER - Set User

Sets the user for subsequent instructions.

```dockerfile
# Create user and switch
RUN useradd -m -u 1000 appuser
USER appuser

# Use existing user
USER nobody

# Switch back to root
USER root
```

### ARG - Build Arguments

Defines build-time variables.

```dockerfile
# Define argument
ARG VERSION=1.0
ARG PYTHON_VERSION=3.11

# Use in FROM
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}

# Use in RUN
ARG APP_ENV=production
RUN echo "Building for ${APP_ENV}"

# Build with custom value
# docker build --build-arg VERSION=2.0 .
```

**ARG vs ENV**:
- `ARG`: Only available during build
- `ENV`: Available during build AND runtime

### LABEL - Add Metadata

Adds metadata to image.

```dockerfile
LABEL maintainer="you@example.com"
LABEL version="1.0"
LABEL description="My Python application"

# Multiple labels
LABEL maintainer="you@example.com" \
      version="1.0" \
      description="My app"
```

## LearningSpace Dockerfile

Here's a production-ready Dockerfile for the LearningSpace project:

```dockerfile
# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set metadata
LABEL maintainer="learning@example.com"
LABEL version="1.0"
LABEL description="Python Learning Space"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Set working directory
WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY tasks/ ./tasks/
COPY solutions/ ./solutions/
COPY tests/ ./tests/
COPY *.py ./
COPY *.md ./

# Create non-root user
RUN useradd -m -u 1000 learner && \
    chown -R learner:learner /app
USER learner

# Run tests by default
CMD ["pytest", "tests/", "-v"]
```

## Multi-Stage Builds

Build smaller images by using multiple stages:

```dockerfile
# Stage 1: Builder
FROM python:3.11 AS builder

WORKDIR /app

# Install dependencies in user directory
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Copy only installed packages from builder
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Copy application
COPY . .

CMD ["python", "app.py"]
```

**Benefits**:
- Smaller final image
- No build tools in production
- Better security

## Advanced Examples

### Development Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

# Install dev dependencies
COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements.txt -r requirements-dev.txt

# Install code in editable mode
COPY . .
RUN pip install -e .

# Expose port for development server
EXPOSE 8000

# Use development server
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
```

### Production Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Only production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files
COPY app/ ./app/
COPY config/ ./config/

# Security: non-root user
RUN useradd -m appuser
USER appuser

# Production server (gunicorn)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

### Testing Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

# Install test dependencies
COPY requirements.txt requirements-test.txt ./
RUN pip install -r requirements.txt -r requirements-test.txt

# Copy application and tests
COPY . .

# Run tests
CMD ["pytest", "-v", "--cov=app"]
```

## Best Practices

### 1. Order Matters (Caching)

```dockerfile
# ✅ Good - dependencies cached separately
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ❌ Bad - any code change invalidates cache
COPY . .
RUN pip install -r requirements.txt
```

### 2. Combine RUN Commands

```dockerfile
# ✅ Good - single layer
RUN apt-get update && \
    apt-get install -y package && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ❌ Bad - multiple layers
RUN apt-get update
RUN apt-get install -y package
RUN apt-get clean
```

### 3. Use .dockerignore

Create `.dockerignore`:
```
__pycache__/
*.pyc
.git/
.gitignore
*.md
tests/
.env
venv/
```

### 4. Don't Install Unnecessary Packages

```dockerfile
# ✅ Good
RUN apt-get install -y --no-install-recommends curl

# ❌ Bad (installs recommended packages too)
RUN apt-get install -y curl
```

### 5. Clean Up in Same Layer

```dockerfile
# ✅ Good - cleanup in same RUN
RUN apt-get update && \
    apt-get install -y package && \
    rm -rf /var/lib/apt/lists/*

# ❌ Bad - cleanup doesn't reduce image size
RUN apt-get update
RUN apt-get install -y package
RUN rm -rf /var/lib/apt/lists/*
```

### 6. Use Specific Tags

```dockerfile
# ✅ Good - reproducible
FROM python:3.11.5-slim

# ❌ Bad - unpredictable
FROM python:latest
```

### 7. Security Best Practices

```dockerfile
# Run as non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Don't store secrets
# ❌ Bad
ENV API_KEY=secret123

# ✅ Good - pass at runtime
# docker run -e API_KEY=secret123 myapp
```

## Common Patterns

### Python Web App

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

### Python CLI Tool

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "cli.py"]
CMD ["--help"]
```

### Jupyter Notebook

```dockerfile
FROM python:3.11

WORKDIR /notebooks

RUN pip install jupyter numpy pandas matplotlib

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
```

## Build Tips

```bash
# Build with tag
docker build -t myapp:1.0 .

# Build with build args
docker build --build-arg VERSION=2.0 -t myapp:2.0 .

# Build without cache
docker build --no-cache -t myapp:1.0 .

# Build specific target (multi-stage)
docker build --target builder -t myapp:builder .

# See build output
docker build --progress=plain -t myapp:1.0 .
```

## Troubleshooting

### Check Built Image

```bash
# View image layers
docker history myapp:1.0

# Inspect image
docker inspect myapp:1.0

# Run and debug
docker run -it myapp:1.0 bash
```

### Optimize Image Size

```bash
# Check image size
docker images myapp:1.0

# Use dive to analyze layers
docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock \
  wagoodman/dive:latest myapp:1.0
```

## Next Steps

- Learn Docker Compose for multi-container apps
- Explore Docker networking
- Study container orchestration
- Practice CI/CD with Docker

---

**See Also**: `docker_compose.md` for orchestrating services!
