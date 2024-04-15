# -- Path setup --------------------------------------------------------------
# Add any paths that contain custom modules or templates here, relative to this directory.
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'Disney Plus Project'  # Replace with your project name
copyright = '2024, https://disneyplus-com-begin.readthedocs.io'  # Replace with your name or organization
author = 'disneyplus'  # Replace with your name

# The full version, including alpha/beta/rc tags.
release = '1.0'  # Replace with your project version

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings.
# Example: extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
extensions = [
    'sphinx.ext.autodoc',  # Automatically generate documentation from docstrings
    'sphinx.ext.napoleon', # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode', # Add links to the source code
]

# Paths that contain templates, relative to this directory.
templates_path = ['_templates']

# Patterns to ignore when searching for source files.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# Choose the theme for HTML pages.
html_theme = 'sphinx_rtd_theme'  # Popular theme; you can change it if needed.

# Paths that contain custom static files (such as CSS files), relative to this directory.
html_static_path = ['_static']

# HTML help builder output file base name.
htmlhelp_basename = f'{project}doc'

# -- Options for LaTeX output ------------------------------------------------
# Grouping the document tree into LaTeX files.
latex_documents = [
    (master_doc, f'{project}.tex', f'{project} Documentation',
     author, 'manual'),
]


man_pages = [
    (master_doc, project.lower(), f'{project} Documentation',
     [author], 1)
]


texinfo_documents = [
    (master_doc, project.lower(), f'{project} Documentation',
     author, project, 'Miscellaneous', 'Documentation for Disney Plus project.'),
]


epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']
