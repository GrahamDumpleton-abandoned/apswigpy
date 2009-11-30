from apache.httpd import *
from apache.http_protocol import *

import sys
import imp
import md5

_cache = {}

def handle_request(environ, start_response):
    filename = environ['SCRIPT_FILENAME']

    if filename not in _cache:
        label = '_ap_' + md5.new(filename).hexdigest()
        module = imp.new_module(label)
        module.__file__ = filename
        execfile(filename, module.__dict__)
        sys.modules[label] = module
        _cache[filename] = module
    else:
        module = _cache[filename]

    r = request_rec(environ['apache.request_rec'])

    if not hasattr(module, 'handler'):
        r.status = 404
        ap_rflush(r)

        start_response('200 OK', [])
        return []

    handler = getattr(module, 'handler')

    handler(r)

    ap_rflush(r)

    start_response('200 OK', [])
    return ['']
