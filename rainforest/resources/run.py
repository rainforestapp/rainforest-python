from ..apibits import *
from ..endpoints import RunsEndpoint
from ..endpoints import RunTestsEndpoint

class Run(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().runs().all(params, headers)
        return res

    @classmethod
    def retrieve(cls, run_id, params={}, headers={}):
        res = cls.default_client().runs().retrieve(run_id, params, headers)
        return res

    @classmethod
    def create(cls, params={}, headers={}):
        res = cls.default_client().runs().create(params, headers)
        return res

    def refresh(self, params={}, headers={}):
        res = self.get_client().runs().retrieve(self.id, params, headers)
        return self.refresh_from(res.json, res.api_method, res.client)

    def delete(self, params={}, headers={}):
        res = self.get_client().runs().delete(self.id, params, headers)
        return res

    def abort(self, params={}, headers={}):
        res = self.get_client().runs().delete(self.id, params, headers)
        return res

    def associated_tests(self):
        from ..endpoints import RunTestsEndpoint
        return RunTestsEndpoint(self.client, self)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(Run, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "run")

    _api_attributes = {
        "browsers" : {},
        "created_at" : {},
        "current_progress" : {},
        "description" : {},
        "environment" : {},
        "filters" : {},
        "frontend_url" : {},
        "id" : {},
        "log_url" : {},
        "real_cost_to_run" : {},
        "result" : {},
        "sample_test_titles" : {},
        "state" : {},
        "state_details" : {},
        "stats" : {},
        "timestamps" : {},
        "total_failed_tests" : {},
        "total_no_result_tests" : {},
        "total_passed_tests" : {},
        "total_tests" : {},
    }
