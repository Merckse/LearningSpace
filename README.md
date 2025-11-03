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
│   └── data_analysis/  # Data analysis tasks
├── solutions/          # Reference solutions
│   ├── algorithms/
│   ├── mathematics/
│   └── data_analysis/
└── tests/             # Test files to validate your solutions
```

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Choose a Task**
   - Browse the `tasks/` directory
   - Read the task description and requirements
   - Implement your solution in the task file

3. **Test Your Solution**
   ```bash
   python -m pytest tests/
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
```

## 📖 Learning Path

**Beginner**: Start with basic mathematics and simple algorithms
**Intermediate**: Move to recursion, sorting, and data analysis
**Advanced**: Tackle dynamic programming and complex data analysis

Happy Learning! 🐍