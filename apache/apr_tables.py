import apache

if apache.version == (2, 2):
    from apache22.apr_tables import *
else:
    raise RuntimeError('Apache version not supported.')
