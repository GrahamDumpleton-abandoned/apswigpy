import apache

if apache.version == (2, 2):
    from apache22.ap_mmn import *
else:
    raise RuntimeError('Apache version not supported.')
