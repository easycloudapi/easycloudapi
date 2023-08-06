# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
# sys.path.insert(0, os.path.abspath(os.path.join(__file__ ,"../..")))
import src.easycloudapi

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EasyCloudApi Python Utility'
copyright = '2023, Indranil Pal'
author = 'Indranil Pal'
release = '0.0.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    # 'numpydoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
    # 'sphinx.ext.linkcode',
]

numpydoc_show_class_members = False

# generate autosummary even if no references
autosummary_generate = True
autosummary_imported_members = True

templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  #'nature', 'alabaster'
html_theme_options = {'navigation_depth': 2}

html_static_path = ['_static']
