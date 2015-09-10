from ..apibits import *
from ..endpoints import UsersEndpoint

class User(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().users().all(params, headers)
        return res

    @classmethod
    def retrieve(cls, user_id, params={}, headers={}):
        res = cls.default_client().users().retrieve(user_id, params, headers)
        return res

    @classmethod
    def update(cls, user_id, params={}, headers={}):
        res = cls.default_client().users().update(user_id, params, headers)
        return res

    @classmethod
    def create(cls, params={}, headers={}):
        res = cls.default_client().users().create(params, headers)
        return res

    def refresh(self, params={}, headers={}):
        res = self.get_client().users().retrieve(self.id, params, headers)
        return self.refresh_from(res.json, res.api_method, res.client)

    def reset_password(self, params={}, headers={}):
        res = self.get_client().users().reset_password(self.email, params, headers)
        return res

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(User, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "user")

    _api_attributes = {
        "analytics_id" : {},
        "client_analytics_id" : {},
        "created_at" : {},
        "email" : {},
        "id" : {},
        "name" : {},
        "profiles" : {},
        "role" : {},
        "settings" : {},
        "state" : {},
    }
