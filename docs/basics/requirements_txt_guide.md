# Requirements.txt Guide

## What is requirements.txt?

`requirements.txt` is a file used in Python projects to list all the dependencies (packages) your project needs. It allows others (or yourself on a different machine) to easily install all the required packages.

## Basic Format

```txt
# Basic format: package_name==version
numpy==1.24.0
pandas==2.0.0
matplotlib==3.7.0

# Without version (installs latest)
requests

# Minimum version
scipy>=1.10.0

# Version range
pytest>=7.4.0,<8.0.0
```

## Common Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Exact version | `numpy==1.24.0` |
| `>=` | Minimum version | `pandas>=2.0.0` |
| `<=` | Maximum version | `scipy<=1.11.0` |
| `>` | Greater than | `pytest>7.0.0` |
| `<` | Less than | `matplotlib<4.0.0` |
| `~=` | Compatible version | `seaborn~=0.12.0` |

## Creating requirements.txt

### Method 1: Manual Creation
Create a file and list your dependencies:
```txt
numpy==1.24.0
pandas==2.0.0
matplotlib>=3.7.0
```

### Method 2: From Current Environment
Generate from your current Python environment:
```bash
pip freeze > requirements.txt
```

⚠️ **Warning**: This includes ALL packages, even indirect dependencies!

### Method 3: Selective Freeze
Better approach - only main dependencies:
```bash
# Install pipreqs first
pip install pipreqs

# Generate based on actual imports in your code
pipreqs /path/to/project
```

## Installing from requirements.txt

```bash
# Basic installation
pip install -r requirements.txt

# Upgrade all packages
pip install -r requirements.txt --upgrade

# Install in specific environment
python -m pip install -r requirements.txt
```

## Best Practices

### 1. Pin Important Versions
```txt
# Good - reproducible builds
numpy==1.24.0
pandas==2.0.3

# Risky - versions may change
numpy
pandas
```

### 2. Use Comments
```txt
# Core data processing
numpy==1.24.0
pandas==2.0.0

# Visualization
matplotlib==3.7.0
seaborn==0.12.0

# Testing
pytest>=7.4.0
```

### 3. Separate Dev Dependencies
Create `requirements-dev.txt` for development tools:
```txt
# requirements-dev.txt
-r requirements.txt  # Include main requirements
pytest==7.4.0
black==23.7.0
flake8==6.0.0
```

### 4. Environment-Specific Files
```
requirements.txt           # Production
requirements-dev.txt       # Development
requirements-test.txt      # Testing only
requirements-prod.txt      # Production only
```

## Advanced Features

### Including Other Files
```txt
# Base requirements
-r requirements-base.txt

# Additional requirements
numpy==1.24.0
```

### Specifying Index URL
```txt
--index-url https://pypi.org/simple
--trusted-host pypi.org

numpy==1.24.0
```

### Installing from Git
```txt
# From GitHub
git+https://github.com/user/repo.git@v1.0#egg=package

# From specific branch
git+https://github.com/user/repo.git@main#egg=package
```

### Hash Checking (Security)
```txt
numpy==1.24.0 --hash=sha256:abc123...
pandas==2.0.0 --hash=sha256:def456...
```

Generate hashes:
```bash
pip hash numpy==1.24.0
```

## Common Issues and Solutions

### Issue 1: Version Conflicts
```txt
# Problem: Package A needs numpy<1.24, Package B needs numpy>=1.24
# Solution: Find compatible versions
numpy==1.23.5  # Works for both
```

### Issue 2: Too Strict Versions
```txt
# Problem: Exact versions make updates difficult
numpy==1.24.0
pandas==2.0.0

# Solution: Use compatible release
numpy~=1.24.0  # Allows 1.24.x but not 1.25.0
pandas~=2.0.0
```

### Issue 3: Platform-Specific Dependencies
```txt
# Windows only
pywin32==306; sys_platform == 'win32'

# Linux only
python-magic==0.4.27; sys_platform == 'linux'

# Python version specific
typing-extensions==4.7.1; python_version < '3.10'
```

## Project Structure Example

```
my_project/
├── requirements.txt          # Main dependencies
├── requirements-dev.txt      # Development dependencies
├── requirements-test.txt     # Testing dependencies
├── setup.py                  # Package configuration
└── README.md
```

## LearningSpace Example

Our project's `requirements.txt`:

```txt
# Core scientific computing
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0

# Testing
pytest>=7.4.0

# Additional utilities
scipy>=1.10.0
```

### Why We Chose These Versions:
- `>=` operator: Allows updates for bug fixes and security patches
- `numpy>=1.24.0`: Need modern features and performance
- `pytest>=7.4.0`: Latest testing features

## Updating Dependencies

```bash
# Check outdated packages
pip list --outdated

# Update a specific package
pip install --upgrade numpy

# Update all packages (dangerous!)
pip install --upgrade -r requirements.txt

# Update requirements.txt after changes
pip freeze > requirements.txt
```

## Virtual Environments

Always use virtual environments with requirements.txt:

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

## Testing Requirements

```bash
# Verify all packages install correctly
pip install -r requirements.txt

# Check for security vulnerabilities
pip install safety
safety check -r requirements.txt

# Check for conflicts
pip check
```

## Quick Reference

```bash
# Create requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Install with upgrade
pip install -r requirements.txt --upgrade

# Install in editable mode (for development)
pip install -e .

# Uninstall all packages in requirements.txt
pip uninstall -r requirements.txt -y
```

## Additional Resources

- [pip documentation](https://pip.pypa.io/en/stable/)
- [PEP 440 - Version Identification](https://www.python.org/dev/peps/pep-0440/)
- [Python Packaging Guide](https://packaging.python.org/)

---

**Next Steps**: Learn about Docker for containerizing your Python applications!
