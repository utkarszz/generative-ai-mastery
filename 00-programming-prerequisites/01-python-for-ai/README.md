# 00.01 Python for AI

Foundational Python for numerical computing, data work, machine learning, and model development.

## Planned scope
Specific lessons will be added as topics are taught. Use the shared [Learning Review Template](../../README.md#learning-review-template) for completed lessons.

## Status
No lessons started.

# Python for AI — Scientific Computing

This module builds the Python foundations required for scientific computing, machine learning experiments, and understanding model implementations.

Python acts as our scientific and model-engineering runtime, while TypeScript/Node.js serves as our application and backend runtime.

## 1. Python Fundamentals

### Variables and data types

Variables store values. Common built-in types include:

- `int` — integers
- `float` — decimal numbers
- `str` — text
- `bool` — Boolean values

Use `type(value)` to inspect a value's type.

### Control flow

- `if`, `elif`, `else` — conditional execution.
- `for` — iterate over sequences.
- `while` — repeat while a condition is true.
- `break` — terminate a loop.
- `continue` — skip the current iteration.

`range(start, stop, step)` generates a sequence of integers, excluding the stop value.

## 2. Functions

Functions organize reusable logic.

```python
def add(a, b):
    return a + b
```

- Parameters are variables defined in a function.
- Arguments are values passed during a call.
- `return` sends a result back.
- `print()` displays information but does not return the displayed value.

Additional concepts:

- Default arguments
- Positional and keyword arguments
- `*args` — collects positional arguments into a tuple.
- `**kwargs` — collects keyword arguments into a dictionary.
- Local and global scope
- Lambda functions

## 3. Comprehensions

Comprehensions provide concise ways to construct collections.

```python
squares = [x ** 2 for x in range(5)]

evens = [x for x in range(10) if x % 2 == 0]

square_map = {x: x ** 2 for x in range(5)}

unique_squares = {x ** 2 for x in range(5)}
```

List comprehensions create lists, dictionary comprehensions create dictionaries, and set comprehensions create sets.

## 4. Iterators and Generators

An iterable can provide an iterator. An iterator maintains its position and produces values through `next()`.

```python
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))
```

Generators produce values lazily instead of constructing the entire result upfront.

```python
def generate_numbers():
    yield 1
    yield 2
    yield 3
```

`yield` pauses a generator and allows it to resume later.

## 5. Exceptions

Exceptions represent errors that occur during execution.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup")
```

- `try` — code that may fail.
- `except` — handles an exception.
- `else` — runs if no exception occurs.
- `finally` — runs during cleanup.
- `raise` — explicitly raises an exception.

Custom exceptions represent application-specific error conditions.

## 6. Object-Oriented Programming

Core concepts:

- Classes and objects
- Constructors (`__init__`)
- `self` — reference to the current instance
- Instance and class attributes
- Inheritance and `super()`
- Encapsulation
- Abstraction
- Polymorphism
- Composition

A class defines structure and behaviour; an object is an instance of that class.

### Dataclasses

Dataclasses reduce boilerplate for data-focused classes.

```python
from dataclasses import dataclass, field

@dataclass
class ModelConfig:
    model_name: str
    learning_rate: float
    batch_size: int
    tags: list[str] = field(default_factory=list)
```

`@dataclass` generates useful methods such as `__init__`, `__repr__`, and `__eq__`.

`default_factory` creates a fresh mutable default for each instance.

## 7. Type Hints

Python is dynamically typed. Type hints describe expected types but do not enforce them automatically at runtime.

```python
def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)
```

Useful annotations include:

- `list[int]`
- `dict[str, int]`
- `tuple[int, int]`
- `int | str`
- `str | None`
- `Any`

Type hints improve readability, editor support, and static analysis.

## 8. Modules, Packages and File I/O

A module is a Python file that can be imported. A package organizes related modules into a directory structure.

```python
import math
```

The `if __name__ == "__main__":` pattern separates script execution from imported functionality.

File I/O concepts:

- `open()` — opens a file.
- `read()` — reads content.
- `write()` — writes content.
- `with open(...)` — manages resource cleanup.
- `json.load()` / `json.dump()` — read and write JSON.
- `csv.DictReader` — reads CSV rows as dictionaries.

## 9. Context Managers and Decorators

Context managers manage resource lifecycles.

```python
with open("data.txt", "r") as file:
    content = file.read()
```

They use `__enter__()` and `__exit__()` to manage entry and cleanup.

Decorators wrap functions to add behaviour without modifying their original implementation.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper
```

The `@my_decorator` syntax applies a decorator to a function.

## 10. Environments and Dependency Management

Virtual environments isolate project dependencies.

```bash
python -m venv .venv
```

Activate the environment before installing packages.

### pip

```bash
python -m pip install numpy
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

### uv

`uv` provides modern Python project and dependency management.

```bash
uv init my-project
uv add numpy pandas
uv sync
uv run main.py
```

Important files:

- `requirements.txt` — dependency requirements.
- `pyproject.toml` — project metadata and declared dependencies.
- `uv.lock` — resolved dependency versions.

Version pinning and lockfiles help make environments reproducible.

## 11. Jupyter Notebooks

Jupyter notebooks (`.ipynb`) combine executable code, Markdown explanations, and outputs.

A notebook uses a Python kernel that maintains in-memory state.

Notebooks are useful for interactive experimentation, data analysis, and visual exploration.

## 12. Profiling and Testing

Profiling measures performance and helps locate bottlenecks.

- `time.perf_counter()` — measure elapsed time.
- `timeit` — benchmark small operations.
- `cProfile` — profile function calls.
- `tracemalloc` — inspect Python memory allocations.

Testing verifies correctness.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Popular tools include `unittest` and `pytest`.

Correctness should be verified before performance optimization.

## 13. Scientific Computing Stack

### Pandas

Used for structured data, CSV loading, DataFrames, missing values, and statistical inspection.

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())
```

### NumPy

Used for numerical arrays and efficient vectorized operations.

```python
import numpy as np

marks = df["marks"].to_numpy()

bonus_marks = marks + 5
high_scorers = marks[marks > 60]
```

Boolean masks select elements that satisfy a condition.

### Matplotlib

Used to visualize numerical data.

```python
import matplotlib.pyplot as plt

plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
```

Histograms visualize the distribution of a numerical variable.

```python
plt.hist(marks, bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
```

## 14. Scientific Sandbox Workflow

A practical data-analysis pipeline follows this sequence:

1. Load CSV data using Pandas.
2. Inspect rows, columns, types, and missing values.
3. Calculate descriptive statistics.
4. Convert numerical columns to NumPy arrays.
5. Apply vectorized transformations and Boolean filtering.
6. Visualize relationships and distributions using Matplotlib.
7. Verify expected results with pytest.
8. Use fixed random seeds for reproducible experiments.

### Randomness and reproducibility

A seed initializes a pseudorandom number generator.

Legacy NumPy API:

```python
np.random.seed(42)
values = np.random.randint(0, 101, size=5)
```

Modern recommended approach:

```python
rng = np.random.default_rng(42)
values = rng.integers(0, 101, size=5)
```

The same seed and sequence of operations reproduce the same generated sequence under the same generator.

## Key Data Flow

```text
CSV
 |
 v
Pandas DataFrame
 |
 v
NumPy Arrays
 |
 v
Numerical Transformations
 |
 v
Matplotlib Visualizations
 |
 v
Testing and Reproducibility
```

## Completion

This module provides the Python foundation for scientific computing and introductory ML experimentation. Advanced numerical computing, machine learning, and deep learning concepts will be developed in later roadmap phases.

**Python for AI — First-pass curriculum and scientific sandbox completed.**
