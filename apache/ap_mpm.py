import apache

if apache.version == (2, 2):
    from apache22.ap_mpm import *
else:
    raise RuntimeError('Apache version not supported.')
