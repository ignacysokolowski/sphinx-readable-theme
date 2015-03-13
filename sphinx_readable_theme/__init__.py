"""Sphinx Readable Theme.

A clean and readable Sphinx theme with focus on `autodoc` -- documentation
from docstrings.

"""

import os

__version__ = '1.2.0'


def get_html_theme_path():
    """Return path to directory containing package theme."""
    return os.path.abspath(os.path.dirname(__file__))
