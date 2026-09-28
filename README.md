<div align="center">

# 🧪 Pytest Practice

**A personal collection of snippets exploring pytest features, organized topic by topic.**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-tested-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)
![Made with](https://img.shields.io/badge/made%20with-%E2%98%95%20and%20snippets-blueviolet?style=flat-square)

</div>

Each folder focuses on one pytest feature, so you can read and run the examples topic by topic.

## Repository Structure

| Folder | Topic |
| --- | --- |
| [`assertions/`](assertions) | Plain `assert` statements, `pytest.raises`, `pytest.approx`, assertion introspection |
| [`fixtures/`](fixtures) | Setup and teardown, fixture scopes, `conftest.py`, fixture composition |
| [`markers/`](markers) | Built-in markers (`skip`, `skipif`, `xfail`), custom markers, selecting tests with `-m` |
| [`mocking/`](mocking) | Replacing dependencies and isolating code under test |
| [`parametrization/`](parametrization) | Running one test against multiple inputs with `@pytest.mark.parametrize` |

## Getting Started

**Prerequisites:** Python 3.8 or newer.

```bash
# Clone the repository
git clone https://github.com/KKoshy/pytest-practice.git
cd pytest-practice

# (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Tests

```bash
# Run everything
pytest

# Run a single topic
pytest fixtures/

# Run a single file, verbose
pytest -v <folder>/<test_file>.py

# Run tests matching a marker
pytest -m <marker_name>
```

## How to Use

- Read a test, predict whether it passes or fails, then run it to check.
- Deliberately break assertions and fixtures to see how pytest reports failures.
- Try `-v`, `-s`, `-k` and `--tb=short` to see how output and selection change.

## Contributing

This is a personal learning repo, but suggestions and corrections are welcome. Feel free to open an issue or pull request.
