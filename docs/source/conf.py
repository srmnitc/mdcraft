# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import datetime
import pathlib
import sys

sys.path.insert(0, f"{pathlib.Path(__file__).resolve().parents[2]}/src")
from mdcraft import VERSION # noqa: E402

now = datetime.now()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "MDCraft"
copyright = f"2023–{now.year} Benjamin Ye, Pierre Walker, Alec Glisman"
author = "Benjamin Ye, Pierre Walker, Alec Glisman"
version = release = VERSION

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "numpydoc",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.duration",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode"
]
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']

autosummary_generate = True
intersphinx_mapping = {
    "dask": ("https://docs.dask.org/en/stable/", None),
    "joblib": ("https://joblib.readthedocs.io/en/latest/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "mdanalysis": ("https://docs.mdanalysis.org/stable/", None),
    "numba": ("https://numba.pydata.org/numba-doc/latest/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "openmm": ("http://docs.openmm.org/latest/api-python/", None),
    "pint": ("https://pint.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None)
}
numpydoc_show_class_members = False
toc_object_entries_show_parents = "hide"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = "../../assets/favicon.ico"
html_logo = "../../assets/logo.png"
html_show_sourcelink = False
html_static_path = ["_static"]
html_theme = "furo"
html_theme_options = {"sidebar_hide_name": True}