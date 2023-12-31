# conf.py

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add the project root directory to the sys.path
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "LeetCode Python Solutions"
author = "Daniel Tal"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
]

# Set the master document (index.rst by default)
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for autodoc extension -------------------------------------------

# Include both class docstring and __init__ docstring
autoclass_content = "both"

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# -- Options for napoleon extension ------------------------------------------

# Use Google-style docstrings
napoleon_google_docstring = True
napoleon_use_param = False
napoleon_use_ivar = True
napoleon_use_rtype = False
