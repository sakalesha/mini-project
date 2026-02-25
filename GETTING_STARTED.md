# Getting Started Guide

Welcome to the **SmartBiz-Insight** project! This guide will help you set up your local environment and start contributing to the project.

## 1. Repository Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sakalesha/mini-project.git
   cd mini-project
   ```

2. **Set Up Your Environment**:
   It is recommended to use a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/scripts/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 2. Project Workflow (Asynchronous Collaboration)

We use Git for all our collaboration. Since we work at different times, follow these steps:

- **Pick a Task**: Refer to the [CHECKLIST.md](CHECKLIST.md). Your assigned tasks are labeled with your Member number.
- **Stay Updated**: Always run `git pull origin main` before starting any work.
- **Commit Often**: Use descriptive commit messages as outlined in [CONTRIBUTING.md](CONTRIBUTING.md).
- **Push Changes**: Once your task is done and tested, run `git push origin [your-branch-name]`.
- **Update Checklist**: Mark your task as `[x]` in `CHECKLIST.md` once finished and pushed.

## 3. Folder Structure Reference

- `data/`: Raw and processed stock data.
- `ml/`: Model architecture and training scripts.
- `notebooks/`: EDA and visualization.
- `DOCS/`: Research papers and project proposals.
- `results/`: Saved model weights (`.h5`) and plots.

---
*Happy Coding!*
