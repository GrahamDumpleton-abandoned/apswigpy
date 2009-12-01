import apache

if apache.version == (2, 2):
    from apache22.http_request import *
else:
    raise RuntimeError('Apache version not supported.')
