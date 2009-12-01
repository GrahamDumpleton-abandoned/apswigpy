import apache

if apache.version == (2, 2):
    from apache22.apr_strings import *
else:
    raise RuntimeError('Apache version not supported.')
