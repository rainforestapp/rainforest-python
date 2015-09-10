from ..apibits import *
from ..endpoints import TestsEndpoint

class Test(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().tests().all(params, headers)
        return res

    @classmethod
    def retrieve(cls, test_id, params={}, headers={}):
        res = cls.default_client().tests().retrieve(test_id, params, headers)
        return res

    @classmethod
    def update(cls, test_id, params={}, headers={}):
        res = cls.default_client().tests().update(test_id, params, headers)
        return res

    @classmethod
    def create(cls, params={}, headers={}):
        res = cls.default_client().tests().create(params, headers)
        return res

    def refresh(self, params={}, headers={}):
        res = self.get_client().tests().retrieve(self.id, params, headers)
        return self.refresh_from(res.json, res.api_method, res.client)

    def delete(self, params={}, headers={}):
        res = self.get_client().tests().delete(self.id, params, headers)
        return res

    def history(self, params={}, headers={}):
        res = self.get_client().tests().history(self.id, params, headers)
        return res

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(Test, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "test")

    _api_attributes = {
        "browsers" : {},
        "created_at" : {},
        "deletable" : {},
        "deleted" : {},
        "description" : {},
        "dry_run_url" : {},
        "editable" : {},
        "elements" : {},
        "has_been_dry_run" : {},
        "id" : {},
        "last_run" : {},
        "result" : {},
        "run_mode" : {},
        "site_id" : {},
        "start_uri" : {},
        "step_count" : {},
        "tags" : {},
        "test_id" : {},
        "title" : {},
    }
