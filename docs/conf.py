# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = 'PYCELLGA Documentation'
copyright = '2024, Sevgi Akten Karakaya, Mehmet Hakan Satman'
author = 'Sevgi Akten Karakaya, Mehmet Hakan Satman'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.autosectionlabel"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

add_module_names = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', 'images']


html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True, 
    'navigation_depth': 4,
    'titles_only': False
}

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'special-members': '__init__',  # Only include __init__, exclude others like __dict__
    'exclude-members': '__dict__,__weakref__,__module__,__annotations__'
}

def skip(app, what, name, obj, would_skip, options):
    # Skip all special members except __init__
    if name in ('__dict__', '__weakref__', '__module__', '__annotations__'):
        return True
    return would_skip

def setup(app):
    app.connect('autodoc-skip-member', skip)

