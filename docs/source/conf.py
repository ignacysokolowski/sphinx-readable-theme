# -*- coding: utf-8 -*-
"""Sphinx Readable Theme documentation build configuration file.

This file is execfile()d with the current directory set to its containing dir.

"""

import os
import sys

import sphinx_readable_theme


# Adding this directory to the sys path, to build autodoc of example module.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


# -- General configuration ----------------------------------------------------

# Defining Sphinx extension modules.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx']

autodoc_default_flags = ['members', 'show-inheritance']
autodoc_member_order = 'bysource'

# Don't display module names before objects titles, it's more readable.
add_module_names = False

intersphinx_mapping = {
    'python': ('http://docs.python.org/2.7', None),
}

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Sphinx Readable Theme'
copyright = u'2013, Ignacy Sokołowski'

# The version info for the project, acts as replacement for |version| and
# |release|, also used in various other places throughout the built documents.
#
# The short X.Y version.
version = sphinx_readable_theme.__version__
# The full version, including alpha/beta/rc tags.
release = sphinx_readable_theme.__version__

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_theme = 'readable'

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinxreadablethemedoc'


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        'index',
        'Sphinx Readable Theme',
        u'Sphinx Readable Theme Documentation',
        [u'Ignacy Sokołowski'],
        1,
    )
]
