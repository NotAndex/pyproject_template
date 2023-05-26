# Python Project Template

This repository serves as a template for Python projects with the following goals:

* Centralized storage of metadata for the project setup
* Reproducibility and shareability
* Local (tox) & Remote (GitHub Actions) unit and integration testing

## `pyproject.toml`
...

## `.devcontainer/`

### `devcontainer.json`
...
### `Dockerfile`
...
### `postCreateCommand.sh`
Since all the dependencies are packaged within the `pyproject.toml`, the easiest way to further develop this package within a devcontainer is by installing it in editable mode. Additionally, tox is installed for testing within the container, which includes `pytest` as a dependency in `tox.ini`. The following commands describe the process:

```bash
pip install -e .
pip install tox
```

## `.github/workflows`
...