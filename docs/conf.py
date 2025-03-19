import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Product Introduction Blog'
author = 'Your Name'
release = '0.1'

extensions = [
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "your-github-username", # Username
    "github_repo": "product_intro_blog", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/docs/", # Path in the checkout to the docs root
}