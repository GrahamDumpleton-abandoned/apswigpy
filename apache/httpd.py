import apache

if apache.version == (2, 2):
    from apache22.httpd import *
else:
    raise RuntimeError('Apache version not supported.')
