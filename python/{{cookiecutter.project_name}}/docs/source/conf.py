# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import git

sys.path.insert(0, os.path.abspath("../../"))


# -- Project information -----------------------------------------------------

project = "{{ cookiecutter.project_name }}"
copyright = "{{ cookiecutter._year }}, {{ cookiecutter.company }}"
author = "{{ cookiecutter.author }}"

# The full version, including alpha/beta/rc tags
release = "0.0.1"

source_suffix = {
  ".rst": "restructuredtext",
  ".txt": "restructuredtext",
  ".md": "markdown",
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
  "sphinx.ext.viewcode",
  "sphinx.ext.githubpages",
  "sphinx.ext.napoleon",
  "sphinx.ext.todo",
  "sphinx.ext.extlinks",
  "sphinx.ext.intersphinx",
  "sphinx.ext.mathjax",
  "myst_parser",
  "sphinx.ext.autosectionlabel",
  "sphinx.ext.autodoc.typehints",
  "sphinx_copybutton",
  "autoapi.extension",
]

# -- Options for autodoc extension -------------------------------------------

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
simplify_optional_unions = False

# -- Options for viewCode extension -------------------------------------------
viewcode_line_numbers = True

# -- Options for CopyButton extension -----------------------------------------
copybutton_prompt_text = ">>> "
copybutton_prompt_text = (
  r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
)
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True
copybutton_remove_prompts = True
copybutton_copy_empty_lines = True


# -- Options for MyST extension -----------------------------------------------
myst_enable_extensions = [
  "amsmath",
  "colon_fence",
  "deflist",
  "dollarmath",
  "html_admonition",
  "html_image",
  "replacements",
  "smartquotes",
  "substitution",
]

pygments_style = "sphinx"

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["*personal_*"]

# -- Options for autoapi extension -------------------------------------------
autoapi_dirs = ["../../{{ cookiecutter.package_name }}", "../../examples"]
autoapi_options = ["members", "undoc-members"]
autoapi_ignore = ["tests"]
autoapi_python_class_content = "init"
autoapi_add_toctree_entry = False
autoapi_root = "autoapi"
autoapi_keep_files = False

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
  "python": ("https://docs.python.org/3/", None),
  "numpy": ("https://numpy.org/doc/stable/", None),
  "torch": ("https://pytorch.org/docs/stable/", None),
  "pandas": ("https://pandas.pydata.org/docs/", None),
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = [
  "_themes",
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
  "display_version": True,
  "prev_next_buttons_location": "bottom",
  "style_external_links": False,
  # Toc options
  "collapse_navigation": False,
  "sticky_navigation": True,
  "navigation_depth": 4,
  "titles_only": True,
}

repo = git.Repo(search_parent_directories=True)
versions = [
  (tag_ref.name, f"{{ cookiecutter.hosted_docs_url }}/docs/{{ cookiecutter.project_name }}/pages/{tag_ref.name}")
  for tag_ref in git.Repo("../../").tags
]

versions.append(("latest", "{{ cookiecutter.hosted_docs_url }}/docs/{{ cookiecutter.project_name }}/latest"))

html_context = {
  "current_version": "0.0.1",
  "versions": versions,
}


# Enable eval_rst in markdown
def setup(app):
  app.add_config_value(
    "recommonmark_config",
    {"enable_math": True, "enable_inline_math": True, "enable_eval_rst": True},
    True,
  )
  app.add_object_type(
    "confval",
    "confval",
    objname="configuration value",
    indextemplate="pair: %s; configuration value",
  )

