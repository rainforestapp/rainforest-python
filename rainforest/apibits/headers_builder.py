import rainforest

from .errors import AuthenticationError

import base64
import json
import platform

class HeadersBuilder(object):
    @classmethod
    def default_headers(cls):
        user_agent = {
            'bindings_version': '0.0.1',
            'lang': 'python',
            'publisher': 'paid',
            'httplib': 'requests',
        }

        for attr, func in [['lang_version', platform.python_version],
                       ['platform', platform.platform],
                       ['uname', lambda: ' '.join(platform.uname())]]:
            try:
                val = func()
            except Exception as e:
                val = "!! %s" % (e,)
            user_agent[attr] = val

        headers = {
            'X-Paid-Client-User-Agent': json.dumps(user_agent),
            'User-Agent': 'Rainforest/v1 PythonBindings/%s' % ('0.0.1',),
            'Rainforest-Version': 'v1',
            "Content-Type" : "application/json",
"CLIENT_TOKEN" : rainforest.API_KEY,
        }
        
        return headers



    @classmethod
    def build(cls, dev_headers):
        headers = cls.default_headers()
        headers.update(dev_headers)
        return headers


