=====================
Sphinx Readable Theme
=====================

A clean and readable `Sphinx <http://sphinx-doc.org>`_ theme with focus on
`autodoc` -- documentation from docstrings.

Inspired by
`flask-sphinx-themes <https://github.com/mitsuhiko/flask-sphinx-themes>`_.


Installation and setup
======================


Install from PyPI::

    $ pip install sphinx-readable-theme

And add this to your ``conf.py``:

.. code-block:: python

    import sphinx_readable_theme

    html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
    html_theme = 'readable'


Documentation and examples
==========================

Documentation with examples is available at
https://sphinx-readable-theme.readthedocs.org


License
=======

Sphinx Readable Theme is licensed under the MIT license.
