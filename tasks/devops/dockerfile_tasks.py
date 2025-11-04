"""
Dockerfile Tasks

Practice writing Dockerfiles for various Python applications.
These tasks complement the Dockerfile Guide documentation.

These tasks involve creating actual Dockerfiles that can be built and tested.
"""


class DockerfileTasks:
    """
    Dockerfile Writing Exercises
    
    Complete these exercises by creating Dockerfiles.
    Refer to docs/docker/dockerfile_guide.md for guidance.
    """
    
    @staticmethod
    def task_1_simple_python_app():
        """
        Task 1: Create a basic Python application Dockerfile
        
        Objective: Write a Dockerfile for a simple Python script.
        
        Steps:
        1. Create a directory: mkdir ~/dockerfile-task1 && cd ~/dockerfile-task1
        2. Create app.py:
           ```python
           print("Hello from Docker!")
           print("Python version:", __import__('sys').version)
           ```
        3. Create Dockerfile with:
           - FROM python:3.11-slim
           - WORKDIR /app
           - COPY app.py .
           - CMD ["python", "app.py"]
        4. Build: docker build -t task1-app .
        5. Run: docker run task1-app
        
        Expected outcome:
        - Image builds successfully
        - Container prints the hello message and Python version
        
        Validation:
        Run: docker run task1-app
        Should print: "Hello from Docker!" and Python version
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_2_app_with_dependencies():
        """
        Task 2: Dockerfile with requirements.txt
        
        Objective: Create a Dockerfile that installs Python dependencies.
        
        Steps:
        1. Create directory: mkdir ~/dockerfile-task2 && cd ~/dockerfile-task2
        2. Create requirements.txt:
           ```
           requests==2.31.0
           colorama==0.4.6
           ```
        3. Create app.py:
           ```python
           import requests
           from colorama import Fore, Style
           
           print(Fore.GREEN + "Dependencies installed successfully!" + Style.RESET_ALL)
           print(f"Requests version: {requests.__version__}")
           ```
        4. Create Dockerfile:
           - Use python:3.11-slim base
           - Set WORKDIR to /app
           - COPY requirements.txt first
           - RUN pip install --no-cache-dir -r requirements.txt
           - COPY app.py
           - CMD to run app.py
        5. Build: docker build -t task2-app .
        6. Run: docker run task2-app
        
        Expected outcome:
        - Dependencies are installed during build
        - App runs successfully with colored output
        
        Best Practice Note:
        Copy requirements.txt before app code to leverage Docker's build cache.
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_3_flask_web_app():
        """
        Task 3: Dockerfile for Flask web application
        
        Objective: Create a containerized Flask web server.
        
        Steps:
        1. Create directory: mkdir ~/dockerfile-task3 && cd ~/dockerfile-task3
        2. Create requirements.txt:
           ```
           flask==2.3.0
           ```
        3. Create app.py:
           ```python
           from flask import Flask
           
           app = Flask(__name__)
           
           @app.route('/')
           def hello():
               return "<h1>Hello from Dockerized Flask!</h1>"
           
           if __name__ == '__main__':
               app.run(host='0.0.0.0', port=5000)
           ```
        4. Create Dockerfile:
           - FROM python:3.11-slim
           - WORKDIR /app
           - COPY requirements.txt
           - RUN pip install --no-cache-dir -r requirements.txt
           - COPY app.py
           - EXPOSE 5000
           - CMD ["python", "app.py"]
        5. Build: docker build -t task3-flask .
        6. Run: docker run -p 5000:5000 task3-flask
        7. Test: curl http://localhost:5000 or open in browser
        
        Expected outcome:
        - Flask app runs on port 5000
        - Accessible from host machine
        - Returns HTML response
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_4_multi_stage_build():
        """
        Task 4: Multi-stage Dockerfile for smaller images
        
        Objective: Use multi-stage builds to reduce image size.
        
        Steps:
        1. Create directory: mkdir ~/dockerfile-task4 && cd ~/dockerfile-task4
        2. Create requirements.txt:
           ```
           numpy==1.24.0
           ```
        3. Create app.py:
           ```python
           import numpy as np
           print("NumPy version:", np.__version__)
           arr = np.array([1, 2, 3, 4, 5])
           print("Array:", arr)
           print("Mean:", arr.mean())
           ```
        4. Create multi-stage Dockerfile:
           ```dockerfile
           # Build stage
           FROM python:3.11 AS builder
           WORKDIR /app
           COPY requirements.txt .
           RUN pip install --user --no-cache-dir -r requirements.txt
           
           # Runtime stage
           FROM python:3.11-slim
           WORKDIR /app
           COPY --from=builder /root/.local /root/.local
           COPY app.py .
           ENV PATH=/root/.local/bin:$PATH
           CMD ["python", "app.py"]
           ```
        5. Build: docker build -t task4-multistage .
        6. Run: docker run task4-multistage
        7. Compare sizes: docker images | grep task4
        
        Expected outcome:
        - Smaller final image (using slim base)
        - App works correctly
        - Only runtime dependencies in final image
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_5_environment_variables():
        """
        Task 5: Dockerfile with environment variables
        
        Objective: Use ENV and ARG for configuration.
        
        Steps:
        1. Create directory: mkdir ~/dockerfile-task5 && cd ~/dockerfile-task5
        2. Create app.py:
           ```python
           import os
           
           env = os.getenv('ENVIRONMENT', 'development')
           debug = os.getenv('DEBUG', 'false').lower() == 'true'
           port = int(os.getenv('PORT', '8000'))
           
           print(f"Environment: {env}")
           print(f"Debug mode: {debug}")
           print(f"Port: {port}")
           ```
        3. Create Dockerfile:
           ```dockerfile
           FROM python:3.11-slim
           
           WORKDIR /app
           
           # Build-time variable
           ARG VERSION=1.0
           
           # Runtime environment variables
           ENV ENVIRONMENT=production \
               DEBUG=false \
               PORT=8000
           
           COPY app.py .
           
           CMD ["python", "app.py"]
           ```
        4. Build: docker build -t task5-env --build-arg VERSION=2.0 .
        5. Run with defaults: docker run task5-env
        6. Run with overrides: docker run -e ENVIRONMENT=staging -e DEBUG=true task5-env
        
        Expected outcome:
        - Default env vars work
        - Can override env vars at runtime
        - ARG is used during build only
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_6_non_root_user():
        """
        Task 6: Create Dockerfile with non-root user (Security)
        
        Objective: Follow security best practice of not running as root.
        
        Steps:
        1. Create directory: mkdir ~/dockerfile-task6 && cd ~/dockerfile-task6
        2. Create app.py:
           ```python
           import os
           import getpass
           
           print(f"Running as user: {getpass.getuser()}")
           print(f"User ID: {os.getuid()}")
           print(f"Working directory: {os.getcwd()}")
           ```
        3. Create Dockerfile:
           ```dockerfile
           FROM python:3.11-slim
           
           # Create non-root user
           RUN useradd -m -u 1000 appuser
           
           WORKDIR /app
           
           COPY app.py .
           
           # Change ownership
           RUN chown -R appuser:appuser /app
           
           # Switch to non-root user
           USER appuser
           
           CMD ["python", "app.py"]
           ```
        4. Build: docker build -t task6-secure .
        5. Run: docker run task6-secure
        
        Expected outcome:
        - App runs as 'appuser', not root
        - User ID is 1000
        - Security best practice is followed
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_7_dockerignore():
        """
        Task 7: Use .dockerignore to optimize builds
        
        Objective: Exclude unnecessary files from Docker context.
        
        Steps:
        1. Create directory: mkdir ~/dockerfile-task7 && cd ~/dockerfile-task7
        2. Create some files:
           - app.py (simple print script)
           - README.md (documentation)
           - .git/ directory (git init)
           - test_data/ directory with large files
           - __pycache__/ directory
        3. Create .dockerignore:
           ```
           .git
           .gitignore
           README.md
           *.md
           test_data/
           __pycache__/
           *.pyc
           *.pyo
           *.pyd
           .pytest_cache/
           venv/
           .venv/
           ```
        4. Create Dockerfile:
           ```dockerfile
           FROM python:3.11-slim
           WORKDIR /app
           COPY . .
           CMD ["python", "app.py"]
           ```
        5. Build: docker build -t task7-ignore .
        6. Check what was copied: docker run task7-ignore ls -la
        
        Expected outcome:
        - Only necessary files are copied
        - Build context is smaller
        - Faster builds
        
        Note: Without .dockerignore, all files would be copied.
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_8_health_check():
        """
        Task 8: Add HEALTHCHECK to Dockerfile
        
        Objective: Monitor container health.
        
        Steps:
        1. Create directory: mkdir ~/dockerfile-task8 && cd ~/dockerfile-task8
        2. Create requirements.txt:
           ```
           flask==2.3.0
           ```
        3. Create app.py:
           ```python
           from flask import Flask
           
           app = Flask(__name__)
           
           @app.route('/')
           def home():
               return "OK"
           
           @app.route('/health')
           def health():
               return "healthy", 200
           
           if __name__ == '__main__':
               app.run(host='0.0.0.0', port=5000)
           ```
        4. Create Dockerfile:
           ```dockerfile
           FROM python:3.11-slim
           
           WORKDIR /app
           
           COPY requirements.txt .
           RUN pip install --no-cache-dir -r requirements.txt
           
           COPY app.py .
           
           EXPOSE 5000
           
           # Health check
           HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
               CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"
           
           CMD ["python", "app.py"]
           ```
        5. Build: docker build -t task8-health .
        6. Run: docker run -d -p 5000:5000 --name health-test task8-health
        7. Check health: docker ps (wait and look for "healthy" status)
        8. Inspect: docker inspect --format='{{.State.Health.Status}}' health-test
        9. Cleanup: docker stop health-test && docker rm health-test
        
        Expected outcome:
        - Container reports healthy status
        - Health check runs automatically
        - Status visible in docker ps
        """
        # TODO: Complete this exercise
        pass


def get_dockerfile_best_practices():
    """
    Summary of Dockerfile best practices.
    
    Returns:
        dict: Categories of best practices
    """
    return {
        "Base Images": [
            "Use official images when possible",
            "Use specific tags, not 'latest'",
            "Prefer slim/alpine variants for smaller sizes"
        ],
        "Layer Optimization": [
            "Order commands from least to most frequently changing",
            "Combine RUN commands to reduce layers",
            "Copy requirements.txt before application code",
            "Use .dockerignore to exclude unnecessary files"
        ],
        "Security": [
            "Don't run containers as root (use USER)",
            "Don't store secrets in Dockerfiles",
            "Scan images for vulnerabilities",
            "Keep base images updated"
        ],
        "Efficiency": [
            "Use multi-stage builds for smaller images",
            "Clean up in the same RUN command (rm -rf)",
            "Use --no-cache-dir with pip",
            "Minimize number of layers"
        ],
        "Maintainability": [
            "Add comments for complex steps",
            "Use meaningful image tags",
            "Document exposed ports",
            "Add HEALTHCHECK when applicable"
        ]
    }


# Instructions for learners
INSTRUCTIONS = """
Dockerfile Tasks - Getting Started

These tasks involve creating actual Dockerfiles and building images.
Each task teaches important Dockerfile concepts and best practices.

Prerequisites:
1. Docker installed and running
2. Basic terminal/command line knowledge
3. Completed docker_basics.py tasks
4. Read docs/docker/dockerfile_guide.md

How to use these tasks:
1. Read each task's docstring
2. Create the specified files and directories
3. Write the Dockerfile as instructed
4. Build and run the image
5. Verify it works as expected

Tips:
- Use 'docker build --progress=plain' to see detailed build output
- Check image sizes with 'docker images'
- Use 'docker history image_name' to see layer sizes
- Don't forget .dockerignore for optimization

Learning Progression:
- Tasks 1-3: Basic Dockerfile structure
- Tasks 4-5: Optimization and configuration
- Tasks 6-8: Security and monitoring

Complete tasks in order for best results!
"""
