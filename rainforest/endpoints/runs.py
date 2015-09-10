from ..apibits import *

class RunsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Run
        method = ApiMethod("get", "/runs", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Run, json, method, client=self.client)
        
    def retrieve(self, run_id, params={}, headers={}):
        from ..resources import Run
        params = ParamsBuilder.merge({
            "run_id" : run_id,
        }, params)
        method = ApiMethod("get", "/runs/:run_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Run(json, method, client=self.client)
        
    def delete(self, run_id, params={}, headers={}):
        from ..resources import Run
        params = ParamsBuilder.merge({
            "run_id" : run_id,
        }, params)
        method = ApiMethod("delete", "/runs/:run_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Run(json, method, client=self.client)
        
    def abort(self, run_id, params={}, headers={}):
        from ..resources import Run
        params = ParamsBuilder.merge({
            "run_id" : run_id,
        }, params)
        method = ApiMethod("delete", "/runs/:run_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Run(json, method, client=self.client)
        
    def create(self, params={}, headers={}):
        from ..resources import Run
        method = ApiMethod("post", "/runs", params, headers, self.parent)
        json = self.client.execute(method)
        return Run(json, method, client=self.client)
