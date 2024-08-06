{{ cookiecutter.package_name }} Documentation
===================================

{% if cookiecutter.ci == "github" -%}

.. image:: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/run-tests.yaml?branch=main&label=Tests
   :alt: GitHub Actions Workflow Status
{% endif %}
.. image:: https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
   :alt: GitHub Release
.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}
   :alt: PyPI - Python Version
.. image:: https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
   :alt: GitHub Repo stars



.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Contents:


   custom/pre-modules/*

   API Reference <autoapi/{{ cookiecutter.package_name }}/index>

   examples.rst
   custom/post-modules/*


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
