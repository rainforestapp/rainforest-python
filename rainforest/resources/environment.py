from ..apibits import *
from ..endpoints import EnvironmentsEndpoint
from ..endpoints import EnvironmentRunsEndpoint

class Environment(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().environments().all(params, headers)
        return res

    @classmethod
    def retrieve(cls, environment_id, params={}, headers={}):
        res = cls.default_client().environments().retrieve(environment_id, params, headers)
        return res

    @classmethod
    def update(cls, environment_id, params={}, headers={}):
        res = cls.default_client().environments().update(environment_id, params, headers)
        return res

    @classmethod
    def create(cls, params={}, headers={}):
        res = cls.default_client().environments().create(params, headers)
        return res

    def refresh(self, params={}, headers={}):
        res = self.get_client().environments().retrieve(self.id, params, headers)
        return self.refresh_from(res.json, res.api_method, res.client)

    def delete(self, params={}, headers={}):
        res = self.get_client().environments().delete(self.id, params, headers)
        return res

    def runs(self):
        from ..endpoints import EnvironmentRunsEndpoint
        return EnvironmentRunsEndpoint(self.client, self)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(Environment, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "environment")

    _api_attributes = {
        "created_at" : {},
        "default" : {},
        "id" : {},
        "name" : {},
        "site_environments" : {},
        "webhook" : {},
        "webhook_enabled" : {},
    }
