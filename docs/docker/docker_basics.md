# Docker Basics Guide

## What is Docker?

Docker is a platform for developing, shipping, and running applications in containers. Containers package your application with all its dependencies, ensuring it runs consistently across different environments.

## Why Use Docker?

✅ **Consistency**: "It works on my machine" → "It works everywhere"  
✅ **Isolation**: Each container runs independently  
✅ **Portability**: Run anywhere Docker is installed  
✅ **Efficiency**: Lighter than virtual machines  
✅ **Scalability**: Easy to replicate and scale  

## Core Concepts

### 1. Images
A blueprint/template for creating containers. Think of it as a snapshot of your application.

### 2. Containers
A running instance of an image. Like a virtual machine but more lightweight.

### 3. Dockerfile
A text file with instructions to build a Docker image.

### 4. Docker Hub
A registry where Docker images are stored and shared.

## Installation

### Linux (Ubuntu/Debian)
```bash
# Update package index
sudo apt-get update

# Install Docker
sudo apt-get install docker.io

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group (avoid using sudo)
sudo usermod -aG docker $USER
```

### macOS
```bash
# Install using Homebrew
brew install --cask docker

# Or download Docker Desktop from:
# https://www.docker.com/products/docker-desktop
```

### Windows
Download Docker Desktop from:
https://www.docker.com/products/docker-desktop

### Verify Installation
```bash
docker --version
docker run hello-world
```

## Basic Docker Commands

### Working with Images

```bash
# List local images
docker images

# Pull an image from Docker Hub
docker pull ubuntu:22.04

# Search for images
docker search python

# Remove an image
docker rmi image_name

# Build an image from Dockerfile
docker build -t myapp:1.0 .

# Tag an image
docker tag myapp:1.0 myapp:latest
```

### Working with Containers

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Run a container
docker run ubuntu:22.04

# Run container in detached mode (background)
docker run -d nginx

# Run with custom name
docker run --name mycontainer ubuntu:22.04

# Run with port mapping
docker run -p 8080:80 nginx

# Run with volume mount
docker run -v /host/path:/container/path ubuntu:22.04

# Run with environment variables
docker run -e MY_VAR=value ubuntu:22.04

# Execute command in running container
docker exec -it container_name bash

# Stop a container
docker stop container_name

# Start a stopped container
docker start container_name

# Restart a container
docker restart container_name

# Remove a container
docker rm container_name

# Remove all stopped containers
docker container prune
```

### Useful Flags

| Flag | Description | Example |
|------|-------------|---------|
| `-d` | Detached mode (background) | `docker run -d nginx` |
| `-it` | Interactive terminal | `docker run -it ubuntu bash` |
| `-p` | Port mapping (host:container) | `docker run -p 8080:80 nginx` |
| `-v` | Volume mount | `docker run -v $(pwd):/app python` |
| `-e` | Environment variable | `docker run -e DB_HOST=localhost app` |
| `--name` | Container name | `docker run --name myapp nginx` |
| `--rm` | Auto-remove on stop | `docker run --rm ubuntu` |

## Dockerfile Basics

A `Dockerfile` is a script with instructions to build a Docker image.

### Simple Example

```dockerfile
# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["python", "app.py"]
```

### Common Dockerfile Instructions

| Instruction | Description | Example |
|------------|-------------|---------|
| `FROM` | Base image | `FROM python:3.11` |
| `WORKDIR` | Set working directory | `WORKDIR /app` |
| `COPY` | Copy files from host to container | `COPY . /app` |
| `ADD` | Copy and extract archives | `ADD archive.tar.gz /app` |
| `RUN` | Execute command during build | `RUN pip install flask` |
| `CMD` | Default command to run | `CMD ["python", "app.py"]` |
| `ENTRYPOINT` | Command prefix | `ENTRYPOINT ["python"]` |
| `ENV` | Set environment variable | `ENV PORT=8000` |
| `EXPOSE` | Document port | `EXPOSE 8000` |
| `VOLUME` | Create mount point | `VOLUME /data` |
| `USER` | Set user | `USER appuser` |
| `ARG` | Build-time variable | `ARG VERSION=1.0` |

## Python Project Example

### Project Structure
```
my_python_app/
├── app.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

### app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

### requirements.txt
```txt
flask==2.3.0
```

### Dockerfile
```dockerfile
# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["python", "app.py"]
```

### .dockerignore
```
__pycache__/
*.pyc
*.pyo
*.pyd
.git
.gitignore
.venv
venv/
*.md
tests/
```

### Build and Run
```bash
# Build image
docker build -t myapp:1.0 .

# Run container
docker run -p 8000:8000 myapp:1.0

# Access at http://localhost:8000
```

## Best Practices

### 1. Use Official Base Images
```dockerfile
# Good
FROM python:3.11-slim

# Avoid
FROM ubuntu:22.04
# Then installing Python yourself
```

### 2. Use Specific Tags
```dockerfile
# Good - reproducible
FROM python:3.11.5-slim

# Bad - unpredictable
FROM python:latest
```

### 3. Minimize Layers
```dockerfile
# Good - single layer
RUN apt-get update && \
    apt-get install -y package1 package2 && \
    rm -rf /var/lib/apt/lists/*

# Bad - multiple layers
RUN apt-get update
RUN apt-get install -y package1
RUN apt-get install -y package2
```

### 4. Leverage Build Cache
```dockerfile
# Good - copy requirements first
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Bad - copy everything first
COPY . .
RUN pip install -r requirements.txt
```

### 5. Don't Run as Root
```dockerfile
# Create non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Or use existing user
USER nobody
```

### 6. Use .dockerignore
```
# Exclude unnecessary files
.git
.gitignore
*.md
tests/
.venv
__pycache__/
```

### 7. Multi-Stage Builds
```dockerfile
# Build stage
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

## Docker Compose Preview

For multi-container applications:

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
```

Run with: `docker-compose up`

## Debugging

```bash
# View container logs
docker logs container_name

# Follow logs in real-time
docker logs -f container_name

# Inspect container
docker inspect container_name

# View container stats
docker stats

# Access running container
docker exec -it container_name bash

# Copy files from container
docker cp container_name:/app/file.txt ./
```

## Cleaning Up

```bash
# Remove unused containers
docker container prune

# Remove unused images
docker image prune

# Remove unused volumes
docker volume prune

# Remove everything unused
docker system prune

# Remove everything (including volumes)
docker system prune -a --volumes
```

## Quick Reference Card

```bash
# Build
docker build -t name:tag .

# Run
docker run -d -p 8080:80 --name myapp image:tag

# Stop/Start
docker stop myapp
docker start myapp

# View
docker ps                  # Running
docker ps -a               # All
docker logs myapp          # Logs
docker exec -it myapp bash # Access

# Clean
docker rm myapp            # Remove container
docker rmi image:tag       # Remove image
docker system prune        # Clean all
```

## Common Use Cases

### 1. Development Environment
```bash
docker run -it -v $(pwd):/app -w /app python:3.11 bash
```

### 2. Run Tests
```bash
docker run --rm -v $(pwd):/app -w /app python:3.11 pytest
```

### 3. Temporary Database
```bash
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=secret postgres:15
```

## Next Steps

- Learn about Docker Compose for multi-container apps
- Explore Docker networking
- Study container orchestration (Kubernetes)
- Practice building your own images

---

**See Also**: `docker_compose.md` for orchestrating multiple containers!
