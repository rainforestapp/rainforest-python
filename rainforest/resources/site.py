from ..apibits import *
from ..endpoints import SitesEndpoint

class Site(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().sites().all(params, headers)
        return res

    @classmethod
    def update(cls, site_id, params={}, headers={}):
        res = cls.default_client().sites().update(site_id, params, headers)
        return res

    @classmethod
    def create(cls, params={}, headers={}):
        res = cls.default_client().sites().create(params, headers)
        return res

    def delete(self, params={}, headers={}):
        res = self.get_client().sites().delete(self.id, params, headers)
        return res

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(Site, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "site")

    _api_attributes = {
        "created_at" : {},
        "default" : {},
        "id" : {},
        "name" : {},
    }
