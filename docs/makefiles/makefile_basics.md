# Makefile Basics Guide

## What is a Makefile?

A Makefile is a file containing a set of directives used by the `make` build automation tool. It defines how to compile and build your project, run tests, and perform other tasks.

## Why Use Makefiles?

✅ **Automation**: Run complex commands with simple `make` commands  
✅ **Consistency**: Same commands work for everyone  
✅ **Efficiency**: Only rebuild what changed  
✅ **Documentation**: Self-documenting project tasks  
✅ **Cross-platform**: Works on Linux, macOS, and Windows (with make)  

## Basic Syntax

```makefile
target: dependencies
	commands
```

**Important**: Commands MUST be indented with a TAB, not spaces!

## Simple Example

```makefile
# This is a comment

# Target with no dependencies
hello:
	echo "Hello, World!"

# Target with dependencies
build: clean
	python setup.py build

# Target to clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
```

Usage:
```bash
make hello    # Run hello target
make build    # Run build target
make clean    # Run clean target
make          # Run first target (hello)
```

## Basic Concepts

### 1. Targets

A target is typically:
- A file to be created (e.g., `app.o`, `main.exe`)
- A phony target (task name like `clean`, `test`)

```makefile
# File target
app.o: app.c
	gcc -c app.c

# Phony target (not a file)
clean:
	rm -f *.o
```

### 2. Dependencies

Targets can depend on other targets or files:

```makefile
# app depends on app.o and lib.o
app: app.o lib.o
	gcc -o app app.o lib.o

app.o: app.c
	gcc -c app.c

lib.o: lib.c
	gcc -c lib.c
```

### 3. Commands

Commands are shell commands executed for a target:

```makefile
test:
	pytest tests/
	flake8 src/
	mypy src/
```

### 4. Variables

```makefile
# Define variable
CC = gcc
CFLAGS = -Wall -O2

# Use variable
app.o: app.c
	$(CC) $(CFLAGS) -c app.c
```

### 5. Phony Targets

Declare targets that don't create files:

```makefile
.PHONY: clean test install

clean:
	rm -rf build/

test:
	pytest tests/

install:
	pip install -e .
```

## Python Project Makefile

```makefile
# Variables
PYTHON := python3
PIP := pip3
PYTEST := pytest

# Phony targets
.PHONY: help install dev-install test lint clean run

# Default target
help:
	@echo "Available commands:"
	@echo "  make install     - Install dependencies"
	@echo "  make dev-install - Install dev dependencies"
	@echo "  make test        - Run tests"
	@echo "  make lint        - Run linters"
	@echo "  make clean       - Clean generated files"
	@echo "  make run         - Run application"

# Install production dependencies
install:
	$(PIP) install -r requirements.txt

# Install development dependencies
dev-install: install
	$(PIP) install -r requirements-dev.txt

# Run tests
test:
	$(PYTEST) tests/ -v

# Run linters
lint:
	flake8 src/
	black --check src/
	mypy src/

# Format code
format:
	black src/
	isort src/

# Clean generated files
clean:
	rm -rf __pycache__/
	rm -rf **/__pycache__/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf *.egg-info/
	find . -type f -name '*.pyc' -delete

# Run application
run:
	$(PYTHON) app.py
```

## LearningSpace Makefile

```makefile
.PHONY: help install test test-algorithms test-math test-data \
        clean lint format run-examples docker-build docker-run

# Variables
PYTHON := python3
PYTEST := pytest
DOCKER_IMAGE := learningspace:latest

# Default target shows help
help:
	@echo "LearningSpace - Python Learning Platform"
	@echo ""
	@echo "Available commands:"
	@echo "  make install         - Install dependencies"
	@echo "  make test            - Run all tests"
	@echo "  make test-algorithms - Run algorithm tests"
	@echo "  make test-math       - Run mathematics tests"
	@echo "  make test-data       - Run data analysis tests"
	@echo "  make lint            - Check code style"
	@echo "  make format          - Format code"
	@echo "  make clean           - Clean generated files"
	@echo "  make run-examples    - Run example demonstrations"
	@echo "  make docker-build    - Build Docker image"
	@echo "  make docker-run      - Run in Docker container"

# Install dependencies
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	@echo "✓ Dependencies installed"

# Run all tests
test:
	$(PYTEST) tests/ -v
	@echo "✓ All tests passed"

# Run algorithm tests
test-algorithms:
	$(PYTEST) tests/test_algorithms.py -v

# Run mathematics tests
test-math:
	$(PYTEST) tests/test_mathematics.py -v

# Run data analysis tests
test-data:
	$(PYTEST) tests/test_data_analysis.py -v

# Run tests with coverage
test-coverage:
	$(PYTEST) tests/ -v --cov=solutions --cov-report=html
	@echo "✓ Coverage report generated in htmlcov/"

# Lint code
lint:
	@echo "Checking code style..."
	$(PYTHON) -m flake8 tasks/ solutions/ tests/ --max-line-length=100
	@echo "✓ Code style check passed"

# Format code (if you have black installed)
format:
	@echo "Formatting code..."
	@command -v black >/dev/null 2>&1 && black tasks/ solutions/ tests/ || echo "Install black: pip install black"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache/ .coverage htmlcov/
	@echo "✓ Cleaned"

# Run example demonstrations
run-examples:
	$(PYTHON) run_example.py

# Build Docker image
docker-build:
	docker build -t $(DOCKER_IMAGE) .
	@echo "✓ Docker image built: $(DOCKER_IMAGE)"

# Run in Docker container
docker-run:
	docker run -it --rm -v $(PWD):/app $(DOCKER_IMAGE)

# Run Jupyter notebook in Docker
docker-jupyter:
	docker run -it --rm -p 8888:8888 -v $(PWD):/app $(DOCKER_IMAGE) \
		bash -c "pip install jupyter && jupyter notebook --ip=0.0.0.0 --allow-root"
```

## Common Patterns

### 1. Variables

```makefile
# Simple variables
CC = gcc
CFLAGS = -Wall -O2
SRC = main.c utils.c

# Automatic variables in recipes
# $@ - target name
# $< - first dependency
# $^ - all dependencies

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@
```

### 2. Pattern Rules

```makefile
# Compile all .c files to .o files
%.o: %.c
	gcc -c $< -o $@

# Convert all .md files to .html
%.html: %.md
	markdown $< > $@
```

### 3. Conditional Execution

```makefile
# Check if virtual environment exists
install:
ifeq ($(wildcard venv/),)
	python3 -m venv venv
endif
	venv/bin/pip install -r requirements.txt
```

### 4. Suppressing Output

```makefile
# @ suppresses command echo
quiet:
	@echo "This message appears"
	@echo "But not the commands themselves"

# - ignores errors
force:
	-rm nonexistent.txt
	@echo "Continues even if rm fails"
```

### 5. Multiple Commands

```makefile
# Multiple commands in sequence
deploy:
	@echo "Building..."
	@make build
	@echo "Testing..."
	@make test
	@echo "Deploying..."
	@./deploy.sh
```

## Advanced Features

### Including Other Makefiles

```makefile
# Include another Makefile
include config.mk

# Include with error handling
-include optional.mk  # Don't fail if missing
```

### Functions

```makefile
# Wildcard function
SOURCES = $(wildcard src/*.c)

# Pattern substitution
OBJECTS = $(SOURCES:.c=.o)

# Shell function
COMMIT = $(shell git rev-parse --short HEAD)

# Example usage
version:
	@echo "Commit: $(COMMIT)"
```

### Parallel Execution

```bash
# Run targets in parallel
make -j4 test

# Parallel in Makefile
all: task1 task2 task3
	# These run in parallel with -j flag
```

## Real-World Examples

### Web Development

```makefile
.PHONY: dev prod build test deploy

dev:
	npm run dev

prod:
	npm run build
	NODE_ENV=production node dist/server.js

build:
	npm run build

test:
	npm test
	npm run lint

deploy: test build
	./deploy.sh
```

### Data Science

```makefile
.PHONY: data train evaluate

data:
	python scripts/download_data.py
	python scripts/preprocess.py

train: data
	python train.py --epochs=100

evaluate: train
	python evaluate.py --model=models/best.pkl

all: evaluate
```

### Multi-Language Project

```makefile
.PHONY: all clean

# C++ compilation
CXX = g++
CXXFLAGS = -std=c++17 -Wall

# Python setup
PYTHON = python3

all: cpp python

cpp:
	$(CXX) $(CXXFLAGS) -c src/core.cpp
	$(CXX) -shared -o lib/core.so core.o

python: cpp
	$(PYTHON) setup.py build_ext --inplace

clean:
	rm -f *.o *.so
	rm -rf build/
```

## Best Practices

### 1. Always Use .PHONY

```makefile
.PHONY: clean test install

clean:
	rm -rf build/
```

### 2. Add Help Target

```makefile
help:
	@echo "Available targets:"
	@echo "  make build   - Build the project"
	@echo "  make test    - Run tests"
	@echo "  make clean   - Clean build files"
```

### 3. Use Variables

```makefile
# Good
PYTHON = python3
TEST_DIR = tests/

test:
	$(PYTHON) -m pytest $(TEST_DIR)

# Bad
test:
	python3 -m pytest tests/
```

### 4. Handle Errors Gracefully

```makefile
clean:
	-rm -f *.o          # Ignore if files don't exist
	@echo "Cleaned!"    # Always show message
```

### 5. Add Dependencies

```makefile
test: install lint    # Run install and lint before test
	pytest tests/
```

## Common Issues

### Issue 1: Tab vs Spaces
```makefile
# ❌ Wrong (spaces)
test:
    pytest tests/

# ✅ Correct (tab)
test:
	pytest tests/
```

### Issue 2: Blank Lines in Recipes
```makefile
# ❌ Wrong
test:
	pytest tests/
	
	echo "Done"

# ✅ Correct
test:
	pytest tests/
	@echo "Done"
```

### Issue 3: Shell Variables
```makefile
# ❌ Wrong (make variable)
test:
	for file in *.py; do echo $file; done

# ✅ Correct (shell variable)
test:
	for file in *.py; do echo $$file; done
```

## Quick Reference

```makefile
# Variables
VAR = value
VAR := value    # Immediate expansion

# Automatic variables
$@    # Target name
$<    # First dependency
$^    # All dependencies
$?    # Dependencies newer than target

# Functions
$(wildcard *.c)           # List files
$(patsubst %.c,%.o,...)   # Pattern substitution
$(shell command)           # Execute shell command

# Directives
.PHONY: target            # Declare phony target
include file.mk           # Include another Makefile
-include file.mk          # Include, don't fail if missing

# Special targets
.DEFAULT_GOAL := target   # Default target
.SILENT:                  # Suppress all output
```

## Next Steps

- Practice writing Makefiles for your projects
- Learn GNU Make advanced features
- Explore alternative build tools (CMake, Bazel)
- Integrate Makefiles with CI/CD pipelines

---

**See Also**: `makefile_python.md` for Python-specific examples!
