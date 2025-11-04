"""
Docker Basics Tasks

Practice Docker commands and concepts through hands-on exercises.
These tasks complement the Docker Basics Guide documentation.

Note: These tasks are meant to be run in a terminal, not as Python code.
They serve as a reference for what you should practice.
"""


class DockerBasicsTasks:
    """
    Docker Basics Practice Exercises
    
    Complete these exercises using Docker CLI commands.
    Refer to docs/docker/docker_basics.md for guidance.
    """
    
    @staticmethod
    def task_1_hello_world():
        """
        Task 1: Run your first container
        
        Objective: Verify Docker installation and run a simple container.
        
        Steps:
        1. Check Docker version: docker --version
        2. Run hello-world container: docker run hello-world
        3. List all containers: docker ps -a
        
        Expected outcome:
        - Hello from Docker! message appears
        - Container exits successfully
        
        Validation:
        Run: docker ps -a | grep hello-world
        Should show the hello-world container
        """
        # TODO: Complete this exercise in your terminal
        pass
    
    @staticmethod
    def task_2_interactive_ubuntu():
        """
        Task 2: Run an interactive Ubuntu container
        
        Objective: Learn to run containers interactively.
        
        Steps:
        1. Run Ubuntu container: docker run -it ubuntu:22.04 bash
        2. Inside container, run: cat /etc/os-release
        3. Install a package: apt-get update && apt-get install -y curl
        4. Test curl: curl --version
        5. Exit the container: exit
        
        Expected outcome:
        - You enter the Ubuntu container shell
        - You can run commands inside the container
        - Changes are made within the container
        
        Validation:
        The container should be listed when you run: docker ps -a
        """
        # TODO: Complete this exercise in your terminal
        pass
    
    @staticmethod
    def task_3_nginx_web_server():
        """
        Task 3: Run Nginx web server with port mapping
        
        Objective: Learn port mapping and running containers in detached mode.
        
        Steps:
        1. Run Nginx: docker run -d -p 8080:80 --name my-nginx nginx
        2. Check running containers: docker ps
        3. Test in browser or curl: curl http://localhost:8080
        4. View logs: docker logs my-nginx
        5. Stop container: docker stop my-nginx
        6. Remove container: docker rm my-nginx
        
        Expected outcome:
        - Nginx welcome page appears at localhost:8080
        - Container runs in background
        - Can view logs and control container
        
        Validation:
        Run: docker ps
        Should show my-nginx container running
        """
        # TODO: Complete this exercise in your terminal
        pass
    
    @staticmethod
    def task_4_volume_mounting():
        """
        Task 4: Mount a volume to persist data
        
        Objective: Understand volume mounting for data persistence.
        
        Steps:
        1. Create a directory: mkdir ~/docker-test
        2. Create a file: echo "Hello from host" > ~/docker-test/message.txt
        3. Run container with volume: 
           docker run -it -v ~/docker-test:/data ubuntu:22.04 bash
        4. Inside container: cat /data/message.txt
        5. Inside container: echo "Hello from container" > /data/response.txt
        6. Exit container
        7. Check host: cat ~/docker-test/response.txt
        
        Expected outcome:
        - Files from host are accessible in container
        - Files created in container appear on host
        - Data persists after container exits
        
        Validation:
        Both message.txt and response.txt should exist in ~/docker-test/
        """
        # TODO: Complete this exercise in your terminal
        pass
    
    @staticmethod
    def task_5_environment_variables():
        """
        Task 5: Use environment variables in containers
        
        Objective: Learn to pass configuration via environment variables.
        
        Steps:
        1. Run Python container with env var:
           docker run -it -e MY_VAR="Hello Docker" python:3.11-slim bash
        2. Inside container: echo $MY_VAR
        3. Inside container: python -c "import os; print(os.getenv('MY_VAR'))"
        4. Exit
        
        Expected outcome:
        - Environment variable is accessible in container
        - Both shell and Python can read the variable
        
        Validation:
        The MY_VAR value should be printed correctly
        """
        # TODO: Complete this exercise in your terminal
        pass
    
    @staticmethod
    def task_6_image_management():
        """
        Task 6: Work with Docker images
        
        Objective: Practice pulling, listing, and removing images.
        
        Steps:
        1. Search for Python images: docker search python
        2. Pull specific version: docker pull python:3.11-slim
        3. Pull another version: docker pull python:3.10-slim
        4. List images: docker images
        5. Remove an image: docker rmi python:3.10-slim
        6. Verify removal: docker images
        
        Expected outcome:
        - Multiple Python images are downloaded
        - Images appear in the list
        - Removed image no longer appears
        
        Validation:
        Run: docker images | grep python
        Should show python:3.11-slim but not python:3.10-slim
        """
        # TODO: Complete this exercise in your terminal
        pass
    
    @staticmethod
    def task_7_container_inspection():
        """
        Task 7: Inspect container details
        
        Objective: Learn to inspect container configuration and state.
        
        Steps:
        1. Run container: docker run -d --name inspect-test nginx
        2. Inspect container: docker inspect inspect-test
        3. Get specific info: docker inspect -f '{{.NetworkSettings.IPAddress}}' inspect-test
        4. View stats: docker stats inspect-test --no-stream
        5. Clean up: docker stop inspect-test && docker rm inspect-test
        
        Expected outcome:
        - Detailed JSON configuration is displayed
        - Can extract specific fields
        - Can view resource usage
        
        Validation:
        Inspect command should show detailed container information
        """
        # TODO: Complete this exercise in your terminal
        pass
    
    @staticmethod
    def task_8_cleanup():
        """
        Task 8: Clean up Docker resources
        
        Objective: Practice cleaning up unused containers, images, and volumes.
        
        Steps:
        1. Create some test containers:
           docker run -d --name test1 nginx
           docker run -d --name test2 nginx
        2. Stop them: docker stop test1 test2
        3. View stopped containers: docker ps -a
        4. Remove stopped containers: docker container prune
        5. Remove unused images: docker image prune
        6. See disk usage: docker system df
        
        Expected outcome:
        - Stopped containers are removed
        - Unused images are cleaned up
        - Disk space is freed
        
        Validation:
        Run: docker ps -a
        Should not show test1 or test2
        """
        # TODO: Complete this exercise in your terminal
        pass


def get_docker_commands_reference():
    """
    Quick reference of Docker commands used in these tasks.
    
    Returns:
        dict: Dictionary of command categories and their commands
    """
    return {
        "Container Management": [
            "docker run [options] image",
            "docker ps [-a]",
            "docker stop container_name",
            "docker start container_name",
            "docker restart container_name",
            "docker rm container_name",
            "docker exec -it container_name command"
        ],
        "Image Management": [
            "docker images",
            "docker pull image:tag",
            "docker search image_name",
            "docker rmi image_name",
            "docker build -t name:tag ."
        ],
        "Information & Logs": [
            "docker logs container_name",
            "docker inspect container_name",
            "docker stats [container_name]",
            "docker system df"
        ],
        "Cleanup": [
            "docker container prune",
            "docker image prune",
            "docker volume prune",
            "docker system prune"
        ]
    }


# Instructions for learners
INSTRUCTIONS = """
Docker Basics Tasks - Getting Started

These tasks are designed to be completed in your terminal, not run as Python code.
Each task teaches a fundamental Docker concept through hands-on practice.

Prerequisites:
1. Docker installed on your system
2. Access to terminal/command line
3. Read docs/docker/docker_basics.md

How to use these tasks:
1. Read each task's docstring carefully
2. Follow the steps in your terminal
3. Verify the expected outcome
4. Use the validation command to check your work

Tips:
- Keep the docs/docker/docker_basics.md guide open for reference
- Don't worry about mistakes - containers are disposable!
- Use 'docker --help' and 'docker <command> --help' for assistance
- If a container is stuck, use: docker stop container_name

Complete the tasks in order for the best learning experience.
"""
