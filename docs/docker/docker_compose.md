# Docker Compose Guide

## What is Docker Compose?

Docker Compose is a tool for defining and running multi-container Docker applications. You define your services in a YAML file, then start everything with a single command.

## Why Use Docker Compose?

✅ **Multi-container apps**: Web app + database + cache  
✅ **Simple configuration**: One YAML file  
✅ **Easy networking**: Containers can communicate easily  
✅ **Volume management**: Persistent data handling  
✅ **Development**: Consistent dev environments  

## Installation

### Linux
```bash
# Download
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Make executable
sudo chmod +x /usr/local/bin/docker-compose

# Verify
docker-compose --version
```

### macOS/Windows
Included with Docker Desktop!

## Basic docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

Run with: `docker-compose up`

## Complete Example: Python Web App

### Project Structure
```
myapp/
├── docker-compose.yml
├── Dockerfile
├── app.py
├── requirements.txt
└── data/
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  # Web application
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
      - redis
    command: python app.py

  # PostgreSQL database
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  # Redis cache
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

# Named volumes
volumes:
  postgres_data:
  redis_data:
```

## docker-compose.yml Structure

### Version
```yaml
version: '3.8'  # Compose file version
```

Common versions:
- `3.8` - Latest stable (recommended)
- `3.7`, `3.6` - Older versions
- `2.x` - Legacy

### Services

Define your application containers:

```yaml
services:
  service_name:
    image: image:tag        # Or use 'build'
    ports:
      - "host:container"
    environment:
      - VAR=value
    volumes:
      - ./host:/container
```

### Volumes

Persistent data storage:

```yaml
volumes:
  volume_name:              # Named volume
  volume_name_2:
    driver: local
    driver_opts:
      type: none
      device: /path/on/host
      o: bind
```

### Networks

Container networking:

```yaml
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
```

## Service Configuration

### Build Context

```yaml
services:
  app:
    # Simple build
    build: .
    
    # Or with options
    build:
      context: .
      dockerfile: Dockerfile.dev
      args:
        - VERSION=1.0
```

### Image

```yaml
services:
  app:
    image: python:3.11
    # Or
    image: myregistry.com/myapp:1.0
```

### Ports

```yaml
services:
  app:
    ports:
      # host:container
      - "8000:8000"
      - "8001:8001"
      
      # Range
      - "5000-5010:5000-5010"
      
      # Container only (random host port)
      - "8000"
```

### Environment Variables

```yaml
services:
  app:
    # Inline
    environment:
      - DEBUG=1
      - DB_HOST=db
      
    # From file
    env_file:
      - .env
      - .env.prod
```

### Volumes

```yaml
services:
  app:
    volumes:
      # Named volume
      - data:/app/data
      
      # Bind mount (host path)
      - ./src:/app/src
      
      # Read-only
      - ./config:/app/config:ro
      
      # Anonymous volume
      - /app/cache
```

### Networks

```yaml
services:
  app:
    networks:
      - frontend
      - backend

networks:
  frontend:
  backend:
```

### Dependencies

```yaml
services:
  web:
    depends_on:
      - db
      - redis
  db:
    image: postgres:15
  redis:
    image: redis:7
```

⚠️ Note: `depends_on` only waits for container start, not readiness!

### Command

```yaml
services:
  app:
    # Override default CMD
    command: python app.py --debug
    
    # Or shell form
    command: python app.py
    
    # Or list form
    command: ["python", "app.py", "--debug"]
```

### Restart Policy

```yaml
services:
  app:
    restart: no           # Default
    restart: always       # Always restart
    restart: on-failure   # Only on failure
    restart: unless-stopped
```

### Health Checks

```yaml
services:
  app:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

## Common Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Build images
docker-compose build

# Build and start
docker-compose up --build

# Stop services
docker-compose stop

# Stop and remove containers
docker-compose down

# Stop and remove everything (including volumes)
docker-compose down -v

# View logs
docker-compose logs

# Follow logs
docker-compose logs -f

# Logs for specific service
docker-compose logs -f web

# List running services
docker-compose ps

# Execute command in running service
docker-compose exec web bash

# Run one-off command
docker-compose run web python manage.py migrate

# Scale services
docker-compose up -d --scale web=3

# Restart service
docker-compose restart web

# Validate config
docker-compose config
```

## LearningSpace Example

### docker-compose.yml for Development

```yaml
version: '3.8'

services:
  # Learning environment
  learning:
    build: .
    volumes:
      # Mount code for live editing
      - ./tasks:/app/tasks
      - ./solutions:/app/solutions
      - ./tests:/app/tests
    environment:
      - PYTHONUNBUFFERED=1
    command: bash
    stdin_open: true
    tty: true
    
  # Jupyter notebook for interactive learning
  jupyter:
    build: .
    ports:
      - "8888:8888"
    volumes:
      - ./tasks:/app/tasks
      - ./solutions:/app/solutions
      - ./notebooks:/app/notebooks
    environment:
      - JUPYTER_ENABLE_LAB=yes
    command: >
      bash -c "pip install jupyter jupyterlab &&
               jupyter lab --ip=0.0.0.0 --allow-root --no-browser"
  
  # Test runner
  test:
    build: .
    volumes:
      - ./tasks:/app/tasks
      - ./solutions:/app/solutions
      - ./tests:/app/tests
    command: pytest tests/ -v --cov=solutions
    depends_on:
      - learning
```

### Usage

```bash
# Start interactive learning environment
docker-compose run --rm learning

# Start Jupyter notebook
docker-compose up jupyter

# Run tests
docker-compose run --rm test

# Run specific test
docker-compose run --rm test pytest tests/test_algorithms.py
```

## Advanced Patterns

### Multiple Environments

```yaml
# docker-compose.yml (base)
version: '3.8'
services:
  web:
    build: .
    environment:
      - DEBUG=0

# docker-compose.override.yml (auto-loaded)
version: '3.8'
services:
  web:
    environment:
      - DEBUG=1
    volumes:
      - .:/app

# docker-compose.prod.yml
version: '3.8'
services:
  web:
    image: myregistry.com/web:prod
    restart: always
```

Run production:
```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### Environment Files

```yaml
# .env
POSTGRES_USER=myuser
POSTGRES_PASSWORD=secret
APP_VERSION=1.0

# docker-compose.yml
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
```

### Profiles

```yaml
version: '3.8'

services:
  web:
    image: nginx
    
  db:
    image: postgres:15
    profiles: ["dev"]
    
  debug:
    image: busybox
    profiles: ["debug"]
```

Use profiles:
```bash
# Start only web
docker-compose up

# Start with dev profile
docker-compose --profile dev up

# Start with multiple profiles
docker-compose --profile dev --profile debug up
```

## Real-World Example: Full Stack App

```yaml
version: '3.8'

services:
  # Frontend
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    networks:
      - frontend

  # Backend API
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    networks:
      - frontend
      - backend

  # Database
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend

  # Cache
  redis:
    image: redis:7-alpine
    networks:
      - backend

  # Background worker
  worker:
    build: ./backend
    command: celery -A app worker -l info
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    networks:
      - backend

  # Nginx reverse proxy
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - frontend
      - backend
    networks:
      - frontend

volumes:
  postgres_data:

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
```

## Best Practices

### 1. Use .env Files
```bash
# .env
DB_PASSWORD=secret
API_KEY=key123
```

### 2. Don't Commit Secrets
```bash
# .gitignore
.env
.env.local
docker-compose.override.yml
```

### 3. Use Named Volumes
```yaml
volumes:
  postgres_data:  # Named volume
  redis_data:
```

### 4. Health Checks
```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 3s
      retries: 3
```

### 5. Resource Limits
```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

## Troubleshooting

```bash
# View logs
docker-compose logs -f

# Inspect containers
docker-compose ps
docker-compose top

# Restart service
docker-compose restart service_name

# Rebuild service
docker-compose up -d --build service_name

# Check config
docker-compose config

# Remove orphan containers
docker-compose up --remove-orphans
```

## Quick Reference

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# Rebuild
docker-compose up --build

# Logs
docker-compose logs -f

# Execute
docker-compose exec service_name bash

# Scale
docker-compose up -d --scale service=3
```

## Next Steps

- Learn Docker networking in depth
- Explore Docker Swarm for orchestration
- Study Kubernetes for production
- Practice CI/CD with Docker Compose

---

**See Also**: `docker_basics.md` for Docker fundamentals!
