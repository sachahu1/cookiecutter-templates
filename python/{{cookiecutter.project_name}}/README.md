# {{ cookiecutter.project_name }}

{% if cookiecutter.ci == "github" -%}

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/run-tests.yaml?branch=main&label=Tests)
{% endif %}
![GitHub Release](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }})
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }})
![GitHub Repo stars](https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }})

## Installation
### Installing Poetry
This tool uses poetry. If you already have poetry installed,
please skip to the next section. Otherwise, let's first setup poetry.

To install poetry, simply run this command:
```shell
curl -sSL https://install.python-poetry.org | python3 -
```
You can find out more about poetry installation [here](https://python-poetry.org/docs/master/#installation).

That's it, poetry is set up.

### Installing the package
Thanks to poetry, installing this package is very simple and can be done in a single command. Simply run:
```shell
poetry install
```
That's it, the package is installed. Move to the next section to learn how to use this package.

## Getting Started
< Add instructions on how to use project here >
## Building the documentation
To build the documentation you can simply use the docker image. To do so, simply run:
```shell
docker build . -f Dockerfile --target documentation -t {{cookiecutter.package_name}}-docs
```

[//]: # (//# todo:  Add AWS Account ID and AWS Region)
