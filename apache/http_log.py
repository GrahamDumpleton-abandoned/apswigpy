import apache

if apache.version == (2, 2):
    from apache22.http_log import *
else:
    raise RuntimeError('Apache version not supported.')
