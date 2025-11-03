# LearningSpace Makefile
# Automation for Python learning platform

.PHONY: help install test test-algorithms test-math test-data \
        clean lint format run-examples docker-build docker-run \
        docker-jupyter docker-test docker-clean docs

# Variables
PYTHON := python3
PYTEST := $(PYTHON) -m pytest
DOCKER_IMAGE := learningspace:latest
DOCKER_DEV_IMAGE := learningspace:dev

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

# Default target shows help
.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "$(BLUE)╔═══════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(BLUE)║$(NC)  $(GREEN)LearningSpace - Python Learning Platform$(NC)           $(BLUE)║$(NC)"
	@echo "$(BLUE)╚═══════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "$(YELLOW)Setup Commands:$(NC)"
	@echo "  $(GREEN)make install$(NC)         - Install dependencies"
	@echo "  $(GREEN)make dev-install$(NC)     - Install with dev dependencies"
	@echo ""
	@echo "$(YELLOW)Testing Commands:$(NC)"
	@echo "  $(GREEN)make test$(NC)            - Run all tests"
	@echo "  $(GREEN)make test-algorithms$(NC) - Run algorithm tests"
	@echo "  $(GREEN)make test-math$(NC)       - Run mathematics tests"
	@echo "  $(GREEN)make test-data$(NC)       - Run data analysis tests"
	@echo "  $(GREEN)make test-coverage$(NC)   - Run tests with coverage report"
	@echo ""
	@echo "$(YELLOW)Code Quality:$(NC)"
	@echo "  $(GREEN)make lint$(NC)            - Check code style"
	@echo "  $(GREEN)make format$(NC)          - Format code with black"
	@echo ""
	@echo "$(YELLOW)Running:$(NC)"
	@echo "  $(GREEN)make run-examples$(NC)    - Run example demonstrations"
	@echo "  $(GREEN)make clean$(NC)           - Clean generated files"
	@echo ""
	@echo "$(YELLOW)Docker Commands:$(NC)"
	@echo "  $(GREEN)make docker-build$(NC)    - Build Docker image"
	@echo "  $(GREEN)make docker-run$(NC)      - Run in Docker container"
	@echo "  $(GREEN)make docker-jupyter$(NC)  - Run Jupyter in Docker"
	@echo "  $(GREEN)make docker-test$(NC)     - Run tests in Docker"
	@echo "  $(GREEN)make docker-clean$(NC)    - Clean Docker resources"
	@echo ""
	@echo "$(YELLOW)Docker Compose:$(NC)"
	@echo "  $(GREEN)make compose-up$(NC)      - Start all services"
	@echo "  $(GREEN)make compose-down$(NC)    - Stop all services"
	@echo "  $(GREEN)make compose-jupyter$(NC) - Start Jupyter only"
	@echo "  $(GREEN)make compose-test$(NC)    - Run tests via compose"
	@echo ""

# Install dependencies
install:
	@echo "$(BLUE)Installing dependencies...$(NC)"
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	@echo "$(GREEN)✓ Dependencies installed$(NC)"

# Install development dependencies
dev-install: install
	@echo "$(BLUE)Installing development dependencies...$(NC)"
	$(PYTHON) -m pip install pytest-cov black flake8 mypy ipython
	@echo "$(GREEN)✓ Development environment ready$(NC)"

# Run all tests
test:
	@echo "$(BLUE)Running all tests...$(NC)"
	$(PYTEST) tests/ -v
	@echo "$(GREEN)✓ All tests passed$(NC)"

# Run algorithm tests
test-algorithms:
	@echo "$(BLUE)Running algorithm tests...$(NC)"
	$(PYTEST) tests/test_algorithms.py -v

# Run mathematics tests
test-math:
	@echo "$(BLUE)Running mathematics tests...$(NC)"
	$(PYTEST) tests/test_mathematics.py -v

# Run data analysis tests
test-data:
	@echo "$(BLUE)Running data analysis tests...$(NC)"
	$(PYTEST) tests/test_data_analysis.py -v

# Run tests with coverage
test-coverage:
	@echo "$(BLUE)Running tests with coverage...$(NC)"
	$(PYTEST) tests/ -v --cov=solutions --cov-report=html --cov-report=term
	@echo "$(GREEN)✓ Coverage report generated in htmlcov/$(NC)"

# Lint code
lint:
	@echo "$(BLUE)Checking code style...$(NC)"
	@command -v flake8 >/dev/null 2>&1 || (echo "$(YELLOW)Installing flake8...$(NC)" && pip install flake8)
	$(PYTHON) -m flake8 tasks/ solutions/ tests/ --max-line-length=100 --extend-ignore=E203,W503
	@echo "$(GREEN)✓ Code style check passed$(NC)"

# Format code
format:
	@echo "$(BLUE)Formatting code...$(NC)"
	@command -v black >/dev/null 2>&1 || (echo "$(YELLOW)Installing black...$(NC)" && pip install black)
	black tasks/ solutions/ tests/ --line-length=100
	@echo "$(GREEN)✓ Code formatted$(NC)"

# Clean generated files
clean:
	@echo "$(BLUE)Cleaning generated files...$(NC)"
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@rm -rf .pytest_cache/ .coverage htmlcov/ .mypy_cache/
	@echo "$(GREEN)✓ Cleaned$(NC)"

# Run example demonstrations
run-examples:
	@echo "$(BLUE)Running examples...$(NC)"
	$(PYTHON) run_example.py

# Docker: Build production image
docker-build:
	@echo "$(BLUE)Building Docker image...$(NC)"
	docker build -t $(DOCKER_IMAGE) .
	@echo "$(GREEN)✓ Docker image built: $(DOCKER_IMAGE)$(NC)"

# Docker: Build development image
docker-build-dev:
	@echo "$(BLUE)Building development Docker image...$(NC)"
	docker build -f Dockerfile.dev -t $(DOCKER_DEV_IMAGE) .
	@echo "$(GREEN)✓ Docker dev image built: $(DOCKER_DEV_IMAGE)$(NC)"

# Docker: Run interactive container
docker-run:
	@echo "$(BLUE)Starting Docker container...$(NC)"
	docker run -it --rm -v $(PWD):/app $(DOCKER_DEV_IMAGE)

# Docker: Run Jupyter notebook
docker-jupyter:
	@echo "$(BLUE)Starting Jupyter in Docker...$(NC)"
	@echo "$(YELLOW)Access at: http://localhost:8888$(NC)"
	docker run -it --rm -p 8888:8888 -v $(PWD):/app $(DOCKER_DEV_IMAGE) \
		bash -c "jupyter lab --ip=0.0.0.0 --allow-root --no-browser"

# Docker: Run tests
docker-test:
	@echo "$(BLUE)Running tests in Docker...$(NC)"
	docker run --rm -v $(PWD):/app $(DOCKER_IMAGE)

# Docker: Clean Docker resources
docker-clean:
	@echo "$(BLUE)Cleaning Docker resources...$(NC)"
	-docker rmi $(DOCKER_IMAGE) $(DOCKER_DEV_IMAGE) 2>/dev/null || true
	-docker system prune -f
	@echo "$(GREEN)✓ Docker resources cleaned$(NC)"

# Docker Compose: Start all services
compose-up:
	@echo "$(BLUE)Starting services with Docker Compose...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)✓ Services started$(NC)"

# Docker Compose: Stop all services
compose-down:
	@echo "$(BLUE)Stopping services...$(NC)"
	docker-compose down
	@echo "$(GREEN)✓ Services stopped$(NC)"

# Docker Compose: Start Jupyter only
compose-jupyter:
	@echo "$(BLUE)Starting Jupyter notebook...$(NC)"
	@echo "$(YELLOW)Access at: http://localhost:8888$(NC)"
	docker-compose up jupyter

# Docker Compose: Run tests
compose-test:
	@echo "$(BLUE)Running tests via Docker Compose...$(NC)"
	docker-compose run --rm test

# Docker Compose: Interactive shell
compose-shell:
	@echo "$(BLUE)Starting interactive shell...$(NC)"
	docker-compose run --rm learning

# Create notebooks directory
notebooks:
	@mkdir -p notebooks
	@echo "$(GREEN)✓ Notebooks directory created$(NC)"

# Quick start for new users
quickstart: install
	@echo ""
	@echo "$(GREEN)╔═══════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(GREEN)║$(NC)  $(YELLOW)Quick Start Successful!$(NC)                              $(GREEN)║$(NC)"
	@echo "$(GREEN)╚═══════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "Try these commands:"
	@echo "  $(GREEN)make test$(NC)          - Run all tests"
	@echo "  $(GREEN)make run-examples$(NC)  - See example solutions"
	@echo ""
	@echo "Start learning:"
	@echo "  1. Open files in $(BLUE)tasks/$(NC) directory"
	@echo "  2. Implement the functions"
	@echo "  3. Run $(GREEN)make test$(NC) to validate"
	@echo ""

# Verify installation
verify:
	@echo "$(BLUE)Verifying installation...$(NC)"
	@$(PYTHON) --version
	@$(PYTHON) -c "import numpy, pandas, matplotlib; print('✓ All required packages installed')"
	@echo "$(GREEN)✓ Installation verified$(NC)"

# Show project statistics
stats:
	@echo "$(BLUE)Project Statistics:$(NC)"
	@echo "  Task files:     $$(find tasks -name '*.py' ! -name '__init__.py' | wc -l)"
	@echo "  Solution files: $$(find solutions -name '*.py' ! -name '__init__.py' | wc -l)"
	@echo "  Test files:     $$(find tests -name 'test_*.py' | wc -l)"
	@echo "  Documentation:  $$(find docs -name '*.md' | wc -l) files"
	@echo "  Total functions: $$(grep -r '^def ' tasks/ solutions/ | wc -l)"
