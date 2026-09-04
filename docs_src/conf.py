#Sphinx build for the FSR Lab resource dictionary.
#
#The page content lives in index.md at the repository root, so that one file
#serves both GitHub (where people land first) and this site. MyST parses the
#Markdown; a symlink in this directory points at it.

project = 'FSR Lab Computational Resources'
copyright = '2026'
author = 'Kexin Dong'

extensions = ['myst_parser']

#Match the PEGG and H2M documentation, which this page indexes.
html_theme = 'nltk_theme'

source_suffix = {'.md': 'markdown', '.rst': 'restructuredtext'}
master_doc = 'index'

html_static_path = ['_static']
html_css_files = ['custom.css']
exclude_patterns = ['_build']

myst_enable_extensions = ['linkify', 'colon_fence']
myst_heading_anchors = 3
