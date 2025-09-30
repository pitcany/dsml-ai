# 🤖 AGENTS.md — Guidance for DS/ML Agents & Collaborators

This file defines **workflow conventions** and **operational guardrails** for anyone (human or AI agent) contributing to this repository.  
The focus is **reproducible, high-performance data science & machine learning engineering** on hybrid Mac (M-series) and Linux (multi-GPU) systems.

---

## 🧭 Project Scope
This repository supports:
- End-to-end **data science & analytics pipelines**
- **Machine learning modeling**, experimentation, and evaluation
- **MLOps** practices (CI/CD, environment reproducibility, deployment)
- **GPU-accelerated training & inference** (local & remote)

Agents should **automate**, **validate**, and **document** all steps for clarity and reproducibility.

---

## ⚙️ Environment & Dependency Management

### 🐍 Python
- Primary version: **3.13.x** (via Conda or Mamba)
- Manage environments with:  
  - **Conda** (for low-level libs like CUDA, PyTorch)  
  - **Poetry** (for pure Python deps + packaging)

#### 📦 Rules
- Always pin versions in `environment.yml` and `pyproject.toml`
- Prefer `conda-forge` channel for consistency
- Never install heavy packages with `pip` unless unavailable via Conda
- Use `mamba` instead of `conda` for speed (`mamba install …`)
- Use `pipx` for global CLI tools (`poetry`, `ruff`, `black`, `pre-commit`, etc.)

#### 📁 Environment Files
| File | Purpose |
|------|----------|
| `environment.yml` | Base DS/ML environment (CUDA, PyTorch, Jupyter, etc.) |
| `requirements-dev.txt` | Dev-only pip dependencies |
| `Makefile` | Declarative env build commands |
| `.condarc` | Channels & solver config |
| `.python-version` | For editors (Pyenv / VSCode) |

> 💡 Run `make env` to rebuild environments reproducibly.

---

## 🧪 Experimentation & Reproducibility

### 📁 Folder Structure
```
├── data/          # immutable raw data (never overwrite)
├── notebooks/     # exploratory analysis & prototypes
├── src/           # production-ready code
├── models/        # saved model artifacts (versioned)
├── configs/       # YAML configs for experiments
├── scripts/       # runnable utilities
├── tests/         # unit & integration tests
└── reports/       # generated outputs, metrics, visuals
```

### 🧬 Conventions
- Use **Hydra** or **Pydantic** for experiment configs  
- Store each run under `experiments/<timestamp>_<slug>/`
- Log metrics to **MLflow** or **Weights & Biases**
- Seed all randomness (`torch.manual_seed`, `np.random.seed`)  
- Use **deterministic cuDNN** where possible  
- Persist all hyperparameters, metrics, and dataset hashes

---

## 🚀 GPU / Compute Guidelines

### 🖥️ Hardware Profiles
- **Linux Workstation**: Dual RTX 4090 (CUDA 12.x, 128 GB DDR5)
- **MacBook M4 Max**: MLX / Metal backend for lightweight runs

### 🧠 Rules
- Use **CUDA** for large-scale model training  
- Use **MLX** or **PyTorch Metal** for local prototyping on Mac  
- Offload long-running jobs to workstation via SSH / Tmux  
- Profile GPU memory with `torch.cuda.memory_summary()`  
- Always log `nvidia-smi` snapshot before/after runs

---

## 🧹 Code Quality & Tooling

### 🧰 Pre-Commit Hooks
Install once:
```bash
pre-commit install
```

Hooks enforced:
- `black` (formatting)
- `ruff` (lint + import sort)
- `mypy` (type checks)
- `nbstripout` (clean Jupyter output)
- `pytest` (tests must pass before merge)

### 📜 Style
- PEP8 compliant  
- Type-hint all functions  
- Document non-trivial logic with docstrings  
- Use `dataclasses` or `pydantic` models for configs  

---

## 🔬 Testing & CI/CD
- Run `pytest` for unit tests (`tests/` directory)
- Require ≥80 % coverage for core modules
- Include reproducibility tests (seeded outputs)
- Use GitHub Actions or local CI runner for PR validation

---

## 🔄 Git Workflow

| Action | Command | Notes |
|--------|----------|-------|
| Create feature | `git checkout -b feat/<slug>` | Short descriptive slug |
| Commit | `git add . && git commit -m "feat: add model pipeline"` | Conventional commits |
| Rebase | `git pull --rebase origin main` | Keep history linear |
| Push | `git push -u origin feat/<slug>` | Trigger CI |
| Merge | PR + review | Must pass CI tests |

> 🔒 Never commit data, credentials, or notebooks with outputs.

---

## 📈 ML Lifecycle

1. **Define** problem + metrics (precision, recall, AUC, etc.)
2. **Ingest** data (ETL scripts under `src/data/`)
3. **Explore** via notebooks (`notebooks/`)
4. **Preprocess** (feature engineering, pipelines)
5. **Train** model (CatBoost, XGBoost, PyTorch)
6. **Evaluate** (calibration, fairness, uplift)
7. **Deploy** (via FastAPI, Gradio, or batch jobs)
8. **Monitor** (drift, latency, performance)

---

## 🔒 Security & Secrets
- Never commit `.env` or credentials  
- Store keys in OS keychain or `.envrc` (Direnv)  
- Use `dotenv` or `pydantic-settings` for loading secrets  
- Gitignore: `.env`, `.envrc`, `*.key`, `*.pem`, `*.json`

---

## 🧩 Agents' Behavior
Agents (AI or human assistants) must:
- 🔍 Inspect existing scripts before generating new ones  
- 📘 Read `environment.yml`, `pyproject.toml`, and `Makefile` for context  
- 🧠 Prefer **extending** modules, not rewriting them  
- 🧪 Validate outputs with tests, type checks, and docstrings  
- 🧹 Maintain consistency with repo structure & style rules  
- 🗂️ Keep generated files isolated under `experiments/` or `sandbox/`

---

## 🧭 Deployment Targets
- 🧠 Local: Mac (Metal), Linux (CUDA)
- ☁️ Remote: AWS EC2 p4d, GCP A2, or Lambda Labs GPU
- 📦 Containers: `Dockerfile` + `docker-compose.yml` (CUDA base)
- 🧰 Model Serving: FastAPI, BentoML, or Gradio

---

## 🧭 Logging & Observability
- Use `loguru` or `structlog` for structured logs  
- Log hyperparams + metrics to MLflow/W&B  
- Store logs in `logs/<date>/<run_id>.log`  

---

## 🧩 Example Commands
```bash
# Rebuild environment
make env

# Run all tests
pytest -v --maxfail=1 --disable-warnings

# Format code
black src/ tests/
ruff check src/ --fix

# Run experiment
python src/train.py +experiment=baseline

# Launch JupyterLab
jupyter lab
```

---

## ✅ Summary
This repository enforces:
- 🧠 **Reproducibility**
- ⚙️ **Performance**
- 🧹 **Clean code**
- 🔄 **Versioned workflows**
- 🔒 **Secure & modular pipelines**

Follow this `AGENTS.md` as your source of truth for environment setup, code style, experiment tracking, and deployment.
