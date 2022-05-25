import os

extensions = ["sphinxcontrib.rst_table"]

rst_table_autonumber = False

test_dir = os.path.dirname(__file__)

# General information about the project.
project = "sphinxcontrib-rst-table test docs"
copyright = "2022, team procitec"
author = "team procitec"

# The master toctree document.
master_doc = "index"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.0"
# The full version, including alpha/beta/rc tags.
release = "1.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build"]
html_domain_indices = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Output file base name for HTML help builder.
htmlhelp_basename = "rsttabletestdocsdoc"


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "rsttabletestdocs.tex", "rst-table test docs Documentation", "team procitec", "manual"),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "rsttabletestdocs", "rst-table test docs Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "rsttabletestdocs",
        "rst-table test docs Documentation",
        author,
        "rsttabletestdocs",
        "One line description of project.",
        "Miscellaneous",
    ),
]
