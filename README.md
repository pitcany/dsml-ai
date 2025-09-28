# dsml-ai

DS + Machine Learning playground with modular stacks.

## Installation

Install core dependencies:

```bash
poetry install
```

Install optional feature groups (e.g., deep learning, visualization extensions, explainability, big-data, geospatial):
```bash
poetry install --with dl,viz_ext,explainability,bigdata,geospatial
```

Or install all optional extras:
```bash
poetry install --with all
```

If you are working in another Poetry project and want to add `dsml-ai` as a dependency:

```bash
poetry add dsml-ai --with dl,vision,viz_ext,explainability,bigdata,geospatial
```

Alternatively, outside of Poetry you can install via pip:

```bash
pip install dsml-ai[dl,vision,viz_ext,explainability,bigdata,geospatial]
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
