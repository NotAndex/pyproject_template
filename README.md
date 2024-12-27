# Python Project Template

This repository serves as a template for Python projects with the following goals:

* Centralized storage of metadata for the project setup
* Reproducibility and shareability
* Local (tox) & Remote (GitHub Actions) unit and integration testing

## `src`
...

## `tests`
...

## `pyproject.toml`

### `[build-system]`
Interesting read: [[1]](https://discuss.python.org/t/user-experience-with-porting-off-setup-py/37502/33), [[2]](https://github.com/tinygrad/tinygrad/pull/2277)
### `[project]`
...

### `[project.scripts]`
A Entrypoint can be added to the package, by adding the following lines
```toml
[project.scripts]
entrypoint = "main:main"
```
After installing the package, a user may invoke the function by simply calling the entry point on the command line. The entry point can be extended by adding an argument parser to the script using argparse.

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