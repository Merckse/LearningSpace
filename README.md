# LearningSpace

A comprehensive Python learning resource with practical tasks focused on:
- **Algorithms** (sorting, searching, recursion, dynamic programming)
- **Mathematics** (number theory, geometry, statistics)
- **Data Analysis** (pandas, numpy, visualization)

## 🎯 Purpose

This repository helps you relearn Python basics through hands-on practice with real-world problems. Each task is designed to strengthen your understanding of core concepts while solving interesting challenges.

## 📁 Structure

```
LearningSpace/
├── tasks/              # Task descriptions and starter code
│   ├── algorithms/     # Algorithm-focused exercises
│   ├── mathematics/    # Mathematical problems
│   ├── data_analysis/  # Data analysis tasks
│   └── devops/         # DevOps and tooling practice
├── solutions/          # Reference solutions
│   ├── algorithms/
│   ├── mathematics/
│   └── data_analysis/
├── tests/              # Test files to validate your solutions
├── docs/               # Documentation on tools and best practices
│   ├── basics/         # Requirements.txt guide
│   ├── docker/         # Docker tutorials
│   └── makefiles/      # Makefile guides
├── Dockerfile          # Container configuration
├── docker-compose.yml  # Multi-container setup
└── Makefile           # Build automation
```

## 🚀 Getting Started

### Quick Start (Traditional)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   # Or use: make install
   ```

2. **Choose a Task**
   - Browse the `tasks/` directory
   - Read the task description and requirements
   - Implement your solution in the task file

3. **Test Your Solution**
   ```bash
   python -m pytest tests/
   # Or use: make test
   ```

### Quick Start (Docker)

```bash
# Build and run with Docker
make docker-build
make docker-test

# Or use Docker Compose
docker-compose up test

# Interactive environment
docker-compose run learning
```

### Quick Start (Automated with Make)

```bash
# See all available commands
make help

# Quick setup
make quickstart

# Run examples
make run-examples
```

## 📚 Task Categories

### Algorithms (tasks/algorithms/)
- Sorting algorithms (bubble, merge, quick sort)
- Searching algorithms (binary search, linear search)
- Recursion problems (fibonacci, factorial, towers of hanoi)
- Dynamic programming (knapsack, longest common subsequence)
- Graph algorithms (BFS, DFS, shortest path)

### Mathematics (tasks/mathematics/)
- Number theory (primes, GCD, LCM)
- Geometry (area, perimeter, distance)
- Statistics (mean, median, mode, standard deviation)
- Probability problems
- Mathematical sequences

### Data Analysis (tasks/data_analysis/)
- Data cleaning and preprocessing
- Statistical analysis with pandas
- Data visualization with matplotlib
- Numpy array operations
- Real-world dataset analysis

### DevOps (tasks/devops/)
- Docker basics and CLI commands
- Writing Dockerfiles and optimization
- Docker Compose for multi-container apps
- Makefile creation and automation

## 💡 Tips

- Start with easier tasks and progress to more complex ones
- Try to solve tasks without looking at solutions first
- Run tests frequently to verify your implementations
- Read the docstrings carefully for requirements
- Experiment and learn from mistakes!

## 🧪 Running Tests

Test individual task categories:
```bash
# Test algorithms only
python -m pytest tests/test_algorithms.py

# Test mathematics only
python -m pytest tests/test_mathematics.py

# Test data analysis only
python -m pytest tests/test_data_analysis.py

# Test devops tasks structure
python -m pytest tests/test_devops.py
```

## 📖 Learning Paths

### Python Learning Path
**Beginner**: Start with basic mathematics and simple algorithms  
**Intermediate**: Move to recursion, sorting, and data analysis  
**Advanced**: Tackle dynamic programming and complex data analysis  

👉 See [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md) for detailed curriculum

### DevOps Learning Path
Learn essential development tools:
1. **Requirements.txt** - Dependency management → [Guide](docs/basics/requirements_txt_guide.md)
2. **Docker** - Containerization → [Basics](docs/docker/docker_basics.md) | [Dockerfile](docs/docker/dockerfile_guide.md) | [Compose](docs/docker/docker_compose.md)
3. **Makefiles** - Build automation → [Guide](docs/makefiles/makefile_basics.md)

👉 See [docs/README.md](docs/README.md) for complete documentation index

## 🛠️ Available Tools

This project includes ready-to-use configurations:

- **Makefile** - Run `make help` to see all commands
- **Dockerfile** - Containerize the learning environment
- **docker-compose.yml** - Multi-container setup with Jupyter
- **Comprehensive Documentation** - In the `docs/` folder

## 📚 Documentation

- [QUICKSTART.md](QUICKSTART.md) - Get started immediately
- [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md) - 8-week structured curriculum
- [docs/](docs/) - Tools and best practices guides
  - Requirements.txt management
  - Docker tutorials
  - Makefile automation

Happy Learning! 🐍