import sphinx

from pkg_resources import parse_version

from sphinxcontrib.rst_table.domain import TblDomain

from sphinx.util import logging

LOG = logging.getLogger(__name__)
VERSION = 0.1

def setup(app):
    app.add_domain(TblDomain)

    return {'version': VERSION,
            'parallel_read_safe': True,
            'parallel_write_safe': True}
