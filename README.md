# dsml-ai

DS + Machine Learning playground with modular stacks.

## Installation

Install the package and its dependencies:

```bash
poetry install
```

## Usage

Start a Jupyter Lab session:

```bash
poetry run jupyter lab
```

Import the package in Python:

```python
import dsml_ai
print(dsml_ai.hello())
```

## Modular Structure

The package provides modules for different areas:

- `dsml_ai.core`: Core utilities for data processing.
- `dsml_ai.viz`: Visualization utilities.
- `dsml_ai.dl`: Deep learning utilities.
- `dsml_ai.bayes`: Bayesian modeling utilities.
- `dsml_ai.time`: Time series analysis utilities.

## Running tests

```bash
poetry run pytest
```
