"""
Makefile Tasks

Practice writing Makefiles for build automation and task management.
These tasks complement the Makefile Basics Guide documentation.

These tasks involve creating actual Makefiles that can be executed.
"""


class MakefileTasks:
    """
    Makefile Writing Exercises
    
    Complete these exercises by creating Makefiles.
    Refer to docs/makefiles/makefile_basics.md for guidance.
    """
    
    @staticmethod
    def task_1_hello_makefile():
        """
        Task 1: Create your first Makefile
        
        Objective: Understand basic Makefile syntax and targets.
        
        Steps:
        1. Create directory: mkdir ~/makefile-task1 && cd ~/makefile-task1
        2. Create Makefile (note the capital M):
           ```makefile
           # My first Makefile
           
           hello:
           	echo "Hello, Make!"
           
           goodbye:
           	echo "Goodbye, Make!"
           
           all: hello goodbye
           ```
        3. Run targets:
           - make hello
           - make goodbye
           - make all
           - make (runs first target)
        
        Expected outcome:
        - Each target prints its message
        - 'make' without arguments runs 'hello'
        - 'make all' runs both targets in order
        
        Important: Commands MUST be indented with TAB, not spaces!
        
        Validation:
        Running 'make hello' should print "Hello, Make!"
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_2_python_project():
        """
        Task 2: Makefile for a Python project
        
        Objective: Automate common Python development tasks.
        
        Steps:
        1. Create directory: mkdir ~/makefile-task2 && cd ~/makefile-task2
        2. Create requirements.txt:
           ```
           pytest>=7.4.0
           flake8>=6.0.0
           ```
        3. Create simple Python files:
           - app.py (main application)
           - test_app.py (tests)
        4. Create Makefile:
           ```makefile
           .PHONY: help install test lint clean run
           
           PYTHON := python3
           PIP := pip3
           
           help:
           	@echo "Available targets:"
           	@echo "  make install - Install dependencies"
           	@echo "  make test    - Run tests"
           	@echo "  make lint    - Check code style"
           	@echo "  make clean   - Remove generated files"
           	@echo "  make run     - Run application"
           
           install:
           	$(PIP) install -r requirements.txt
           
           test:
           	$(PYTHON) -m pytest -v
           
           lint:
           	$(PYTHON) -m flake8 *.py
           
           clean:
           	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
           	find . -type f -name "*.pyc" -delete
           	rm -rf .pytest_cache/
           
           run:
           	$(PYTHON) app.py
           ```
        5. Test each target:
           - make help
           - make install
           - make test
           - make lint
           - make clean
           - make run
        
        Expected outcome:
        - All development tasks automated
        - Variables make it easy to change Python version
        - Help target documents usage
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_3_dependencies():
        """
        Task 3: Makefile with target dependencies
        
        Objective: Understand how targets can depend on other targets.
        
        Steps:
        1. Create directory: mkdir ~/makefile-task3 && cd ~/makefile-task3
        2. Create Makefile:
           ```makefile
           .PHONY: all clean build test deploy
           
           all: test
           
           clean:
           	@echo "Cleaning..."
           	rm -rf build/
           	@echo "Clean complete!"
           
           build: clean
           	@echo "Building..."
           	mkdir -p build
           	echo "Built at $$(date)" > build/timestamp.txt
           	@echo "Build complete!"
           
           test: build
           	@echo "Testing..."
           	test -f build/timestamp.txt && echo "Test passed!"
           
           deploy: test
           	@echo "Deploying..."
           	@echo "Deploy complete!"
           ```
        3. Run commands:
           - make (runs 'all', which depends on 'test')
           - make deploy
           - Observe the dependency chain
        
        Expected outcome:
        - Dependencies execute in correct order
        - 'make deploy' runs: clean → build → test → deploy
        - Each step completes before next starts
        
        Note: @ prefix suppresses command echo
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_4_variables():
        """
        Task 4: Using variables in Makefiles
        
        Objective: Master Makefile variables and substitution.
        
        Steps:
        1. Create directory: mkdir ~/makefile-task4 && cd ~/makefile-task4
        2. Create Makefile:
           ```makefile
           # Variables
           PROJECT_NAME := myapp
           VERSION := 1.0.0
           PYTHON := python3
           PIP := $(PYTHON) -m pip
           
           # Automatic variables in action
           SRC_DIR := src
           BUILD_DIR := build
           SOURCES := $(wildcard $(SRC_DIR)/*.py)
           
           .PHONY: info clean
           
           info:
           	@echo "Project: $(PROJECT_NAME)"
           	@echo "Version: $(VERSION)"
           	@echo "Python: $(PYTHON)"
           	@echo "Source dir: $(SRC_DIR)"
           	@echo "Sources: $(SOURCES)"
           
           setup:
           	mkdir -p $(SRC_DIR)
           	mkdir -p $(BUILD_DIR)
           	echo "print('Hello from $(PROJECT_NAME)')" > $(SRC_DIR)/main.py
           
           build: setup
           	@echo "Building $(PROJECT_NAME) v$(VERSION)..."
           	cp -r $(SRC_DIR)/* $(BUILD_DIR)/
           	@echo "Build complete!"
           
           clean:
           	rm -rf $(BUILD_DIR)
           	rm -rf $(SRC_DIR)
           ```
        3. Run:
           - make info
           - make build
           - make clean
        
        Expected outcome:
        - Variables are substituted correctly
        - Wildcards find source files
        - Easy to change values in one place
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_5_pattern_rules():
        """
        Task 5: Pattern rules and automatic variables
        
        Objective: Use pattern rules for repetitive tasks.
        
        Steps:
        1. Create directory: mkdir ~/makefile-task5 && cd ~/makefile-task5
        2. Create some .txt files:
           - echo "hello" > file1.txt
           - echo "world" > file2.txt
           - echo "make" > file3.txt
        3. Create Makefile:
           ```makefile
           # Pattern rule: convert .txt to .upper.txt
           %.upper.txt: %.txt
           	@echo "Converting $< to uppercase..."
           	tr '[:lower:]' '[:upper:]' < $< > $@
           	@echo "Created $@"
           
           # Pattern rule: convert .txt to .length.txt
           %.length.txt: %.txt
           	@echo "Counting characters in $<..."
           	wc -c < $< > $@
           	@echo "Created $@"
           
           .PHONY: all clean
           
           all: file1.upper.txt file2.upper.txt file3.upper.txt
           
           lengths: file1.length.txt file2.length.txt file3.length.txt
           
           clean:
           	rm -f *.upper.txt *.length.txt
           ```
        4. Run:
           - make all
           - cat file1.upper.txt
           - make lengths
           - make clean
        
        Expected outcome:
        - Pattern rules apply to multiple files
        - $< refers to first prerequisite (source .txt)
        - $@ refers to target (output file)
        
        Automatic Variables:
        - $@ = target name
        - $< = first prerequisite
        - $^ = all prerequisites
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_6_docker_integration():
        """
        Task 6: Makefile with Docker commands
        
        Objective: Integrate Docker operations into Makefile.
        
        Steps:
        1. Create directory: mkdir ~/makefile-task6 && cd ~/makefile-task6
        2. Create simple Dockerfile:
           ```dockerfile
           FROM python:3.11-slim
           WORKDIR /app
           COPY app.py .
           CMD ["python", "app.py"]
           ```
        3. Create app.py:
           ```python
           print("Hello from containerized app!")
           ```
        4. Create Makefile:
           ```makefile
           .PHONY: help build run stop clean docker-clean all
           
           IMAGE_NAME := myapp
           IMAGE_TAG := latest
           CONTAINER_NAME := myapp-container
           
           help:
           	@echo "Docker + Make Commands:"
           	@echo "  make build        - Build Docker image"
           	@echo "  make run          - Run container"
           	@echo "  make stop         - Stop container"
           	@echo "  make logs         - View container logs"
           	@echo "  make shell        - Open shell in container"
           	@echo "  make clean        - Remove container"
           	@echo "  make docker-clean - Remove image and container"
           
           build:
           	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
           	@echo "Image built: $(IMAGE_NAME):$(IMAGE_TAG)"
           
           run: build
           	docker run -d --name $(CONTAINER_NAME) $(IMAGE_NAME):$(IMAGE_TAG)
           	@echo "Container started: $(CONTAINER_NAME)"
           
           stop:
           	-docker stop $(CONTAINER_NAME)
           	@echo "Container stopped"
           
           logs:
           	docker logs $(CONTAINER_NAME)
           
           shell:
           	docker exec -it $(CONTAINER_NAME) bash
           
           clean: stop
           	-docker rm $(CONTAINER_NAME)
           	@echo "Container removed"
           
           docker-clean: clean
           	-docker rmi $(IMAGE_NAME):$(IMAGE_TAG)
           	@echo "Image removed"
           
           all: run
           ```
        5. Test:
           - make build
           - make run
           - make logs
           - make clean
        
        Expected outcome:
        - Docker commands wrapped in Make targets
        - Easy to remember commands
        - Consistent workflow
        
        Note: - prefix ignores errors (useful for stop/rm)
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_7_conditional_execution():
        """
        Task 7: Conditional execution in Makefiles
        
        Objective: Use conditionals for flexible Makefiles.
        
        Steps:
        1. Create directory: mkdir ~/makefile-task7 && cd ~/makefile-task7
        2. Create Makefile:
           ```makefile
           # Environment variable (override with: make ENV=prod target)
           ENV ?= dev
           
           # Conditional configuration
           ifeq ($(ENV),prod)
               PYTHON := python3
               DEBUG := false
               CONFIG := config.prod.yaml
           else ifeq ($(ENV),staging)
               PYTHON := python3
               DEBUG := true
               CONFIG := config.staging.yaml
           else
               PYTHON := python3
               DEBUG := true
               CONFIG := config.dev.yaml
           endif
           
           .PHONY: info setup test
           
           info:
           	@echo "Environment: $(ENV)"
           	@echo "Python: $(PYTHON)"
           	@echo "Debug: $(DEBUG)"
           	@echo "Config: $(CONFIG)"
           
           setup:
           	@echo "Setting up $(ENV) environment..."
           ifeq ($(ENV),prod)
           	@echo "Installing production dependencies..."
           else
           	@echo "Installing development dependencies..."
           endif
           	@echo "Setup complete!"
           
           test:
           	@echo "Running tests in $(ENV) mode..."
           ifeq ($(DEBUG),true)
           	@echo "Debug mode enabled - verbose output"
           else
           	@echo "Production mode - minimal output"
           endif
           ```
        3. Test with different environments:
           - make info
           - make info ENV=staging
           - make info ENV=prod
           - make setup ENV=prod
        
        Expected outcome:
        - Different configurations for different environments
        - Can override ENV from command line
        - Conditional logic works correctly
        """
        # TODO: Complete this exercise
        pass
    
    @staticmethod
    def task_8_complete_project():
        """
        Task 8: Complete project Makefile
        
        Objective: Create a comprehensive Makefile for a real project.
        
        Steps:
        1. Create directory: mkdir ~/makefile-task8 && cd ~/makefile-task8
        2. Create project structure:
           - requirements.txt
           - app.py
           - tests/test_app.py
           - Dockerfile
        3. Create comprehensive Makefile:
           ```makefile
           .PHONY: help install dev-install test test-coverage lint format \
                   clean build run docker-build docker-run docker-test \
                   docker-clean all
           
           # Variables
           PYTHON := python3
           PIP := $(PYTHON) -m pip
           PYTEST := $(PYTHON) -m pytest
           IMAGE_NAME := myproject
           IMAGE_TAG := latest
           
           # Colors for output
           BLUE := \033[0;34m
           GREEN := \033[0;32m
           RESET := \033[0m
           
           help:
           	@echo "$(BLUE)Available targets:$(RESET)"
           	@echo "  $(GREEN)install$(RESET)        - Install dependencies"
           	@echo "  $(GREEN)dev-install$(RESET)    - Install dev dependencies"
           	@echo "  $(GREEN)test$(RESET)           - Run tests"
           	@echo "  $(GREEN)test-coverage$(RESET)  - Run tests with coverage"
           	@echo "  $(GREEN)lint$(RESET)           - Check code style"
           	@echo "  $(GREEN)format$(RESET)         - Format code"
           	@echo "  $(GREEN)clean$(RESET)          - Clean generated files"
           	@echo "  $(GREEN)build$(RESET)          - Build package"
           	@echo "  $(GREEN)run$(RESET)            - Run application"
           	@echo "  $(GREEN)docker-build$(RESET)   - Build Docker image"
           	@echo "  $(GREEN)docker-run$(RESET)     - Run in Docker"
           	@echo "  $(GREEN)docker-test$(RESET)    - Run tests in Docker"
           	@echo "  $(GREEN)docker-clean$(RESET)   - Clean Docker resources"
           
           install:
           	@echo "Installing dependencies..."
           	$(PIP) install -r requirements.txt
           	@echo "$(GREEN)✓ Dependencies installed$(RESET)"
           
           dev-install: install
           	@echo "Installing dev dependencies..."
           	$(PIP) install pytest flake8 black coverage
           	@echo "$(GREEN)✓ Dev dependencies installed$(RESET)"
           
           test:
           	@echo "Running tests..."
           	$(PYTEST) tests/ -v
           	@echo "$(GREEN)✓ Tests passed$(RESET)"
           
           test-coverage:
           	@echo "Running tests with coverage..."
           	$(PYTEST) tests/ -v --cov=. --cov-report=html
           	@echo "$(GREEN)✓ Coverage report in htmlcov/$(RESET)"
           
           lint:
           	@echo "Checking code style..."
           	$(PYTHON) -m flake8 *.py tests/
           	@echo "$(GREEN)✓ Code style OK$(RESET)"
           
           format:
           	@echo "Formatting code..."
           	$(PYTHON) -m black *.py tests/
           	@echo "$(GREEN)✓ Code formatted$(RESET)"
           
           clean:
           	@echo "Cleaning generated files..."
           	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
           	find . -type f -name "*.pyc" -delete
           	rm -rf .pytest_cache/ htmlcov/ .coverage build/ dist/ *.egg-info
           	@echo "$(GREEN)✓ Cleaned$(RESET)"
           
           build:
           	@echo "Building package..."
           	$(PYTHON) setup.py build
           	@echo "$(GREEN)✓ Build complete$(RESET)"
           
           run:
           	@echo "Running application..."
           	$(PYTHON) app.py
           
           docker-build:
           	@echo "Building Docker image..."
           	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
           	@echo "$(GREEN)✓ Image built: $(IMAGE_NAME):$(IMAGE_TAG)$(RESET)"
           
           docker-run: docker-build
           	@echo "Running in Docker..."
           	docker run --rm $(IMAGE_NAME):$(IMAGE_TAG)
           
           docker-test: docker-build
           	@echo "Running tests in Docker..."
           	docker run --rm $(IMAGE_NAME):$(IMAGE_TAG) pytest tests/
           
           docker-clean:
           	@echo "Cleaning Docker resources..."
           	-docker rmi $(IMAGE_NAME):$(IMAGE_TAG)
           	@echo "$(GREEN)✓ Docker cleaned$(RESET)"
           
           all: clean dev-install lint test
           	@echo "$(GREEN)✓ All checks passed!$(RESET)"
           ```
        4. Test all targets:
           - make help
           - make dev-install
           - make test
           - make docker-build
           
        Expected outcome:
        - Complete automation of all project tasks
        - Colored output for better readability
        - Docker integration
        - Clear help documentation
        - Production-ready Makefile
        """
        # TODO: Complete this exercise
        pass


def get_makefile_best_practices():
    """
    Summary of Makefile best practices.
    
    Returns:
        dict: Categories of best practices
    """
    return {
        "Structure": [
            "Use .PHONY for targets that don't create files",
            "Add a help target as the first/default target",
            "Group related targets together",
            "Add comments to explain complex rules"
        ],
        "Variables": [
            "Use variables for repeated values",
            "Use := for immediate expansion",
            "Use ?= for conditional assignment",
            "Use uppercase for variables (convention)"
        ],
        "Commands": [
            "Use @ to suppress command echo",
            "Use - to ignore errors",
            "Use $(VAR) for variable substitution",
            "Chain commands with && for error propagation"
        ],
        "Dependencies": [
            "Declare dependencies explicitly",
            "Order targets from least to most frequently changing",
            "Use pattern rules for repetitive tasks",
            "Keep dependency chains simple"
        ],
        "Portability": [
            "Use portable shell commands",
            "Test on different systems",
            "Provide sane defaults",
            "Document platform-specific requirements"
        ]
    }


# Instructions for learners
INSTRUCTIONS = """
Makefile Tasks - Getting Started

These tasks teach you how to write Makefiles for build automation.
Progress from simple targets to complex project automation.

Prerequisites:
1. Make installed (usually pre-installed on Linux/Mac)
2. Basic command line knowledge
3. Read docs/makefiles/makefile_basics.md

Important Notes:
- Commands MUST be indented with TAB, not spaces!
- .PHONY declares targets that don't create files
- Variables use $(VAR) syntax
- @ suppresses command echo
- - ignores command errors

How to use these tasks:
1. Read the task description
2. Create the Makefile as specified
3. Test each target
4. Verify expected behavior

Tips:
- Use 'make -n target' to see what would run without executing
- Use 'make --debug' for verbose output
- Check for tab vs space with 'cat -A Makefile'
- Test each target individually

Learning Progression:
- Tasks 1-2: Basic syntax and simple targets
- Tasks 3-5: Dependencies, variables, and patterns
- Tasks 6-7: Docker integration and conditionals
- Task 8: Complete production-ready Makefile

Complete tasks in order for best results!
"""
