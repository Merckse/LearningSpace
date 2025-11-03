# Quick Start Guide

Welcome to LearningSpace! This guide will help you get started with your Python learning journey.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Merckse/LearningSpace.git
cd LearningSpace
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Your First Task

Let's start with a simple algorithm task!

### Example: Bubble Sort

1. Open `tasks/algorithms/sorting.py`
2. Find the `bubble_sort` function
3. Implement your solution:

```python
def bubble_sort(arr):
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

4. Test your solution:
```bash
python -m pytest tests/test_algorithms.py::TestSorting::test_bubble_sort -v
```

## Task Categories Overview

### 🎯 Algorithms (Start here if you're a beginner)

**Easy Tasks:**
- `tasks/algorithms/searching.py` - Linear Search
- `tasks/algorithms/recursion.py` - Factorial, Fibonacci

**Medium Tasks:**
- `tasks/algorithms/sorting.py` - Bubble Sort, Insertion Sort
- `tasks/algorithms/recursion.py` - Tower of Hanoi

**Hard Tasks:**
- `tasks/algorithms/dynamic_programming.py` - Knapsack, LCS

### 📐 Mathematics

**Easy Tasks:**
- `tasks/mathematics/geometry.py` - Area calculations
- `tasks/mathematics/statistics.py` - Mean, Median

**Medium Tasks:**
- `tasks/mathematics/number_theory.py` - Prime numbers, GCD
- `tasks/mathematics/statistics.py` - Variance, Correlation

**Hard Tasks:**
- `tasks/mathematics/number_theory.py` - Sieve of Eratosthenes

### 📊 Data Analysis

**Easy Tasks:**
- `tasks/data_analysis/numpy_basics.py` - Array creation, basic operations
- `tasks/data_analysis/pandas_basics.py` - DataFrame creation, filtering

**Medium Tasks:**
- `tasks/data_analysis/pandas_basics.py` - Group by, merge operations
- `tasks/data_analysis/data_visualization.py` - Line plots, bar charts

**Hard Tasks:**
- `tasks/data_analysis/data_visualization.py` - Complex subplots, heatmaps

## Testing Your Solutions

### Test a specific function:
```bash
python -m pytest tests/test_algorithms.py::TestSorting::test_bubble_sort -v
```

### Test a specific file:
```bash
python -m pytest tests/test_algorithms.py -v
```

### Test all:
```bash
python -m pytest tests/ -v
```

### See which tests are failing:
```bash
python -m pytest tests/ --tb=short
```

## Recommended Learning Path

### Week 1: Basics
- [ ] Complete all recursion tasks (factorial, fibonacci, power)
- [ ] Complete linear_search and basic geometry (area functions)
- [ ] Complete basic statistics (mean, median, mode)

### Week 2: Algorithms
- [ ] Complete all sorting algorithms
- [ ] Complete all searching algorithms
- [ ] Practice with number theory problems

### Week 3: Advanced Algorithms
- [ ] Tackle dynamic programming problems
- [ ] Work on complex recursion (Tower of Hanoi)
- [ ] Solve geometry challenges

### Week 4: Data Analysis
- [ ] Master NumPy operations
- [ ] Learn Pandas data manipulation
- [ ] Create visualizations with matplotlib

## Tips for Success

1. **Read the docstrings carefully** - They contain important requirements and examples
2. **Start simple** - Begin with easy tasks before moving to harder ones
3. **Test frequently** - Run tests after every change to catch errors early
4. **Don't peek at solutions immediately** - Try for at least 15-20 minutes first
5. **Use Python documentation** - Learn to read official docs for help
6. **Experiment** - Try different approaches and learn from mistakes

## Getting Help

- Check the docstrings in task files for detailed requirements
- Look at the example usage in each function's documentation
- Run tests to see what's expected: `pytest tests/ -v`
- If stuck, peek at solutions in `solutions/` directory
- Read Python documentation: https://docs.python.org/3/

## Next Steps

After completing the tasks, try:
- Optimizing your solutions for better performance
- Solving the same problems with different approaches
- Contributing new tasks to the repository
- Building a small project using what you've learned

Happy Learning! 🚀
