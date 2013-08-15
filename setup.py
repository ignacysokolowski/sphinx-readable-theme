import os
from setuptools import setup

import sphinx_readable_theme


def read_file(filename):
    """Open and a file, read it and return its contents."""
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()


setup(
    name='sphinx-readable-theme',
    version=sphinx_readable_theme.__version__,
    author='Ignacy Sokolowski',
    author_email='ignacy.sokolowski@gmail.com',
    description='Sphinx Readable Theme',
    long_description=read_file('README.rst'),
    url='https://github.com/ignacysokolowski/sphinx-readable-theme',
    license=read_file('LICENSE'),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Documentation',
    ],
    packages=['sphinx_readable_theme'],
    include_package_data=True,
    zip_safe=False
)
