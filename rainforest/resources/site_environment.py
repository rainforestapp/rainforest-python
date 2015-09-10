from ..apibits import *
from ..endpoints import SiteEnvironmentsEndpoint

class SiteEnvironment(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().site_environments().all(params, headers)
        return res

    @classmethod
    def update(cls, site_environment_id, params={}, headers={}):
        res = cls.default_client().site_environments().update(site_environment_id, params, headers)
        return res

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(SiteEnvironment, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "site_environment")

    _api_attributes = {
        "created_at" : {},
        "environment_id" : {},
        "id" : {},
        "site_id" : {},
        "url" : {},
    }
