from ..apibits import *
from ..endpoints import IntegrationsEndpoint

class Integration(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().integrations().all(params, headers)
        return res

    @classmethod
    def retrieve(cls, integration_id, params={}, headers={}):
        res = cls.default_client().integrations().retrieve(integration_id, params, headers)
        return res

    @classmethod
    def update(cls, integration_id, params={}, headers={}):
        res = cls.default_client().integrations().update(integration_id, params, headers)
        return res

    def refresh(self, params={}, headers={}):
        res = self.get_client().integrations().retrieve(self.id, params, headers)
        return self.refresh_from(res.json, res.api_method, res.client)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(Integration, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "integration")

    _api_attributes = {
        "created_at" : {},
        "id" : {},
        "recent_upstream_errors" : {},
        "settings" : {},
        "state" : {},
        "type" : {},
    }
