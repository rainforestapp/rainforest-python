from ..apibits import *
from ..endpoints import ClientStatsEndpoint

class ClientStats(ApiResource):

    @classmethod
    def retrieve(cls, params={}, headers={}):
        res = cls.default_client().client_stats().retrieve(params, headers)
        return res

    def refresh(self, params={}, headers={}):
        res = self.get_client().client_stats().retrieve(params, headers)
        return self.refresh_from(res.json, res.api_method, res.client)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(ClientStats, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "client_stats")

    _api_attributes = {
        "has_runs" : {},
        "has_schedules" : {},
        "has_step_variables" : {},
        "has_steps" : {},
        "has_test_steps" : {},
        "has_tests" : {},
    }
