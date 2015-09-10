from ..apibits import *

class EnvironmentRunsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Run
        method = ApiMethod("get", "/environments/:id/runs", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Run, json, method, client=self.client)
