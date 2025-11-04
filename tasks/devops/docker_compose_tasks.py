"""
Docker Compose Tasks

Practice orchestrating multi-container applications with Docker Compose.
These tasks complement the Docker Compose documentation.

These tasks involve creating docker-compose.yml files and running multi-container setups.
"""


class DockerComposeTasks:
    """
    Docker Compose Exercises
    
    Complete these exercises by creating docker-compose.yml files.
    Refer to docs/docker/docker_compose.md for guidance.
    """
    
    @staticmethod
    def task_1_simple_web_app():
        """
        Task 1: Single service with Docker Compose
        
        Objective: Create a basic docker-compose.yml for a single service.
        
        Steps:
        1. Create directory: mkdir ~/compose-task1 && cd ~/compose-task1
        2. Create app.py:
           ```python
           from flask import Flask
           app = Flask(__name__)
           
           @app.route('/')
           def hello():
               return "Hello from Docker Compose!"
           
           if __name__ == '__main__':
               app.run(host='0.0.0.0', port=5000)
           ```
        3. Create requirements.txt:
           ```
           flask==2.3.0
           ```
        4. Create Dockerfile:
           ```dockerfile
           FROM python:3.11-slim
           WORKDIR /app
           COPY requirements.txt .
           RUN pip install -r requirements.txt
           COPY app.py .
           CMD ["python", "app.py"]
           ```
        5. Create docker-compose.yml:
           ```yaml
           version: '3.8'
           
           services:
             web:
               build: .
               ports:
                 - "5000:5000"
           ```
        6. Start: docker-compose up
        7. Test: curl http://localhost:5000
        8. Stop: Ctrl+C or docker-compose down
        
        Expected outcome:
        - Service builds and starts automatically
        - Accessible on port 5000
        - Easy to stop and start
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_2_app_with_database():
        """
        Task 2: Multi-service application (Web + Database)
        
        Objective: Connect a web app to a PostgreSQL database.
        
        Steps:
        1. Create directory: mkdir ~/compose-task2 && cd ~/compose-task2
        2. Create requirements.txt:
           ```
           flask==2.3.0
           psycopg2-binary==2.9.6
           ```
        3. Create app.py:
           ```python
           from flask import Flask
           import psycopg2
           import os
           
           app = Flask(__name__)
           
           @app.route('/')
           def hello():
               return "App is running!"
           
           @app.route('/db-test')
           def db_test():
               try:
                   conn = psycopg2.connect(
                       host=os.getenv('DB_HOST', 'db'),
                       database=os.getenv('DB_NAME', 'testdb'),
                       user=os.getenv('DB_USER', 'user'),
                       password=os.getenv('DB_PASSWORD', 'password')
                   )
                   conn.close()
                   return "Database connection successful!"
               except Exception as e:
                   return f"Database error: {str(e)}", 500
           
           if __name__ == '__main__':
               app.run(host='0.0.0.0', port=5000)
           ```
        4. Create Dockerfile (same as task 1)
        5. Create docker-compose.yml:
           ```yaml
           version: '3.8'
           
           services:
             web:
               build: .
               ports:
                 - "5000:5000"
               environment:
                 - DB_HOST=db
                 - DB_NAME=testdb
                 - DB_USER=user
                 - DB_PASSWORD=password
               depends_on:
                 - db
             
             db:
               image: postgres:15
               environment:
                 - POSTGRES_DB=testdb
                 - POSTGRES_USER=user
                 - POSTGRES_PASSWORD=password
               volumes:
                 - postgres_data:/var/lib/postgresql/data
           
           volumes:
             postgres_data:
           ```
        6. Start: docker-compose up
        7. Test: curl http://localhost:5000/db-test
        8. Cleanup: docker-compose down -v
        
        Expected outcome:
        - Both services start together
        - Web app can connect to database
        - Data persists in named volume
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_3_development_environment():
        """
        Task 3: Development setup with hot reload
        
        Objective: Create a dev environment with volume mounting for live updates.
        
        Steps:
        1. Create directory: mkdir ~/compose-task3 && cd ~/compose-task3
        2. Create requirements.txt:
           ```
           flask==2.3.0
           ```
        3. Create app.py (simple Flask app)
        4. Create Dockerfile:
           ```dockerfile
           FROM python:3.11-slim
           WORKDIR /app
           COPY requirements.txt .
           RUN pip install -r requirements.txt
           CMD ["python", "-u", "app.py"]
           ```
        5. Create docker-compose.yml:
           ```yaml
           version: '3.8'
           
           services:
             web:
               build: .
               ports:
                 - "5000:5000"
               volumes:
                 - .:/app
               environment:
                 - FLASK_ENV=development
                 - FLASK_DEBUG=1
           ```
        6. Start: docker-compose up
        7. Edit app.py while container is running
        8. Observe automatic reload
        9. Stop: docker-compose down
        
        Expected outcome:
        - Code changes reflect immediately
        - No need to rebuild image
        - Flask runs in debug mode
        
        Note: This setup is for development only, not production!
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_4_multi_tier_application():
        """
        Task 4: Three-tier application (Frontend, Backend, Database)
        
        Objective: Orchestrate a complete application stack.
        
        Steps:
        1. Create directory: mkdir ~/compose-task4 && cd ~/compose-task4
        2. Create directory structure:
           - backend/
           - frontend/
        3. Backend (Flask API):
           - backend/requirements.txt: flask, flask-cors, redis
           - backend/app.py: Simple API with Redis cache
           - backend/Dockerfile
        4. Frontend (Nginx):
           - frontend/index.html: HTML page that calls API
           - frontend/nginx.conf: Nginx configuration
           - frontend/Dockerfile
        5. Create docker-compose.yml:
           ```yaml
           version: '3.8'
           
           services:
             frontend:
               build: ./frontend
               ports:
                 - "80:80"
               depends_on:
                 - backend
             
             backend:
               build: ./backend
               ports:
                 - "5000:5000"
               environment:
                 - REDIS_HOST=redis
               depends_on:
                 - redis
             
             redis:
               image: redis:7-alpine
               volumes:
                 - redis_data:/data
           
           volumes:
             redis_data:
           ```
        6. Start: docker-compose up --build
        7. Access: http://localhost
        8. Cleanup: docker-compose down -v
        
        Expected outcome:
        - All three services work together
        - Frontend calls backend API
        - Backend uses Redis for caching
        - Services communicate via Docker network
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_5_environment_files():
        """
        Task 5: Use .env file for configuration
        
        Objective: Manage configuration with environment files.
        
        Steps:
        1. Create directory: mkdir ~/compose-task5 && cd ~/compose-task5
        2. Create .env file:
           ```
           # Application config
           APP_ENV=development
           APP_DEBUG=true
           
           # Database config
           DB_HOST=postgres
           DB_NAME=myapp
           DB_USER=appuser
           DB_PASSWORD=secret123
           
           # Ports
           WEB_PORT=8000
           DB_PORT=5432
           ```
        3. Create app (Flask with database connection)
        4. Create docker-compose.yml:
           ```yaml
           version: '3.8'
           
           services:
             web:
               build: .
               ports:
                 - "${WEB_PORT}:5000"
               environment:
                 - APP_ENV=${APP_ENV}
                 - APP_DEBUG=${APP_DEBUG}
                 - DB_HOST=${DB_HOST}
                 - DB_NAME=${DB_NAME}
                 - DB_USER=${DB_USER}
                 - DB_PASSWORD=${DB_PASSWORD}
               depends_on:
                 - db
             
             db:
               image: postgres:15
               environment:
                 - POSTGRES_DB=${DB_NAME}
                 - POSTGRES_USER=${DB_USER}
                 - POSTGRES_PASSWORD=${DB_PASSWORD}
               ports:
                 - "${DB_PORT}:5432"
           ```
        5. Start: docker-compose up
        6. Test different .env values
        7. Cleanup: docker-compose down
        
        Expected outcome:
        - Configuration is externalized
        - Easy to change settings without editing docker-compose.yml
        - Different .env files for different environments
        
        Security Note: Never commit .env to version control!
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_6_networking():
        """
        Task 6: Custom networks and service communication
        
        Objective: Understand Docker Compose networking.
        
        Steps:
        1. Create directory: mkdir ~/compose-task6 && cd ~/compose-task6
        2. Create two simple services that communicate
        3. Create docker-compose.yml:
           ```yaml
           version: '3.8'
           
           services:
             service-a:
               image: python:3.11-slim
               networks:
                 - frontend
                 - backend
               command: >
                 bash -c "
                 pip install flask &&
                 python -c '
                 from flask import Flask;
                 app = Flask(__name__);
                 @app.route(\"/\") 
                 def hello(): return \"Service A\";
                 app.run(host=\"0.0.0.0\", port=5000)
                 '
                 "
             
             service-b:
               image: python:3.11-slim
               networks:
                 - backend
               command: >
                 bash -c "
                 sleep 10 &&
                 python -c '
                 import urllib.request;
                 response = urllib.request.urlopen(\"http://service-a:5000\");
                 print(\"Response from Service A:\", response.read().decode());
                 import time; time.sleep(3600)
                 '
                 "
             
             service-c:
               image: python:3.11-slim
               networks:
                 - frontend
               command: sleep 3600
           
           networks:
             frontend:
               driver: bridge
             backend:
               driver: bridge
           ```
        4. Start: docker-compose up -d
        5. Test connectivity:
           - docker-compose exec service-b ping service-a
           - docker-compose exec service-c ping service-a
           - docker-compose exec service-c ping service-b (should fail)
        6. View networks: docker network ls
        7. Cleanup: docker-compose down
        
        Expected outcome:
        - Services on same network can communicate
        - Services on different networks cannot
        - Service names work as hostnames
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_7_scaling_services():
        """
        Task 7: Scale services with Docker Compose
        
        Objective: Run multiple instances of a service.
        
        Steps:
        1. Create directory: mkdir ~/compose-task7 && cd ~/compose-task7
        2. Create a simple web service
        3. Create docker-compose.yml:
           ```yaml
           version: '3.8'
           
           services:
             web:
               build: .
               environment:
                 - INSTANCE_ID=${HOSTNAME}
             
             nginx:
               image: nginx:alpine
               ports:
                 - "80:80"
               volumes:
                 - ./nginx.conf:/etc/nginx/nginx.conf:ro
               depends_on:
                 - web
           ```
        4. Create nginx.conf for load balancing:
           ```nginx
           events {
               worker_connections 1024;
           }
           
           http {
               upstream web_backend {
                   server web:5000;
               }
               
               server {
                   listen 80;
                   location / {
                       proxy_pass http://web_backend;
                   }
               }
           }
           ```
        5. Start with scaling: docker-compose up --scale web=3
        6. Check: docker-compose ps
        7. Test load balancing: for i in {1..10}; do curl localhost; done
        8. Cleanup: docker-compose down
        
        Expected outcome:
        - Multiple web service instances run
        - Nginx distributes requests
        - Easy to scale up/down
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_8_production_setup():
        """
        Task 8: Production-ready docker-compose configuration
        
        Objective: Create a production-grade multi-container setup.
        
        Steps:
        1. Create directory: mkdir ~/compose-task8 && cd ~/compose-task8
        2. Create docker-compose.yml with best practices:
           ```yaml
           version: '3.8'
           
           services:
             web:
               build:
                 context: .
                 dockerfile: Dockerfile
               restart: always
               ports:
                 - "8000:5000"
               environment:
                 - DB_HOST=db
                 - REDIS_HOST=redis
               depends_on:
                 db:
                   condition: service_healthy
                 redis:
                   condition: service_started
               healthcheck:
                 test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
                 interval: 30s
                 timeout: 3s
                 retries: 3
               networks:
                 - app_network
               logging:
                 driver: "json-file"
                 options:
                   max-size: "10m"
                   max-file: "3"
             
             db:
               image: postgres:15
               restart: always
               environment:
                 - POSTGRES_DB=proddb
                 - POSTGRES_USER=produser
                 - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
               volumes:
                 - postgres_data:/var/lib/postgresql/data
               healthcheck:
                 test: ["CMD-SHELL", "pg_isready -U produser"]
                 interval: 10s
                 timeout: 5s
                 retries: 5
               networks:
                 - app_network
               secrets:
                 - db_password
             
             redis:
               image: redis:7-alpine
               restart: always
               volumes:
                 - redis_data:/data
               networks:
                 - app_network
           
           volumes:
             postgres_data:
               driver: local
             redis_data:
               driver: local
           
           networks:
             app_network:
               driver: bridge
           
           secrets:
             db_password:
               file: ./secrets/db_password.txt
           ```
        3. Create secrets directory: mkdir secrets
        4. Create secrets/db_password.txt: echo "supersecret" > secrets/db_password.txt
        5. Start: docker-compose up -d
        6. Check health: docker-compose ps
        7. View logs: docker-compose logs
        8. Cleanup: docker-compose down -v
        
        Expected outcome:
        - Services restart on failure
        - Health checks monitor service status
        - Secrets are handled securely
        - Logs are managed properly
        - Production-ready configuration
        """
        # TODO: Complete this exercise
        pass


def get_docker_compose_commands():
    """
    Common Docker Compose commands.
    
    Returns:
        dict: Categories of commands
    """
    return {
        "Basic Operations": [
            "docker-compose up",
            "docker-compose up -d",
            "docker-compose down",
            "docker-compose down -v",
            "docker-compose restart"
        ],
        "Building & Pulling": [
            "docker-compose build",
            "docker-compose build --no-cache",
            "docker-compose pull"
        ],
        "Viewing & Monitoring": [
            "docker-compose ps",
            "docker-compose logs",
            "docker-compose logs -f service_name",
            "docker-compose top"
        ],
        "Scaling": [
            "docker-compose up --scale service=3",
            "docker-compose scale service=5"
        ],
        "Execution": [
            "docker-compose exec service_name command",
            "docker-compose run service_name command"
        ],
        "Cleanup": [
            "docker-compose down",
            "docker-compose down -v --remove-orphans"
        ]
    }


# Instructions for learners
INSTRUCTIONS = """
Docker Compose Tasks - Getting Started

These tasks focus on orchestrating multi-container applications.
Progress from simple single-service setups to complex production configurations.

Prerequisites:
1. Docker and Docker Compose installed
2. Completed docker_basics.py and dockerfile_tasks.py
3. Read docs/docker/docker_compose.md

How to use these tasks:
1. Read the task description
2. Create the necessary files and directories
3. Write docker-compose.yml as specified
4. Run docker-compose up and test
5. Verify the expected behavior

Tips:
- Use 'docker-compose config' to validate your YAML
- Use 'docker-compose logs -f' to watch logs in real-time
- Use 'docker-compose down -v' to clean up volumes
- Check service health with 'docker-compose ps'

Learning Path:
- Tasks 1-3: Basic multi-container setups
- Tasks 4-5: Configuration and environment management
- Tasks 6-7: Networking and scaling
- Task 8: Production-ready configuration

Work through tasks sequentially for best learning experience!
"""
