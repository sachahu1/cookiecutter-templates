# {{ cookiecutter.project_name }}

{% if cookiecutter.ci == "github" -%}

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/run-tests.yaml?branch=main&label=Tests)
{% endif %}
![GitHub Release](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }})
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }})
![GitHub Repo stars](https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }})

## Installation

### Installing the package (from PyPI)
You can install this package from PyPI using:
```shell
pip install {{ cookiecutter.project_name }}
```

### Installing the package (from source)
You can install this package from source using:
```shell
pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
```

### Installing the package (Manual)
You can also install the package yourself by cloning the repo:
```shell
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
```

And installing the package with poetry:
```shell
poetry install
```

## Getting Started
< Add instructions on how to use project here >
## Building the documentation
### Using Docker
To access the documentation locally, the easiest way is to use the docker image. To do so, simply run:
```shell
docker build . -f Dockerfile --target documentation -t {{cookiecutter.package_name}}-docs
docker run -p 80:80 -it {{cookiecutter.package_name}}-docs
```
Then navigate to [http://localhost](http://localhost)

### Manually
Alternatively you can build the documentation yourself.
First, make sure you have the dependencies installed:
```shell
poetry install --with=documentation
```
Then build the documentation:
```shell
poetry run sphinx-build -M html docs/source/ docs/build
```
Then open the documentation in your browser:
```shell
open docs/build/html/index.html
```
