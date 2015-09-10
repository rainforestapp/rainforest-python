from ..apibits import *

class EnvironmentsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Environment
        method = ApiMethod("get", "/environments", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Environment, json, method, client=self.client)
        
    def retrieve(self, environment_id, params={}, headers={}):
        from ..resources import Environment
        params = ParamsBuilder.merge({
            "environment_id" : environment_id,
        }, params)
        method = ApiMethod("get", "/environments/:environment_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Environment(json, method, client=self.client)
        
    def delete(self, environment_id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "environment_id" : environment_id,
        }, params)
        method = ApiMethod("delete", "/environments/:environment_id", params, headers, self.parent)
        json = self.client.execute(method)
        return json
        
    def update(self, environment_id, params={}, headers={}):
        from ..resources import Environment
        params = ParamsBuilder.merge({
            "environment_id" : environment_id,
        }, params)
        method = ApiMethod("put", "/environments/:environment_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Environment(json, method, client=self.client)
        
    def create(self, params={}, headers={}):
        from ..resources import Environment
        method = ApiMethod("post", "/environments", params, headers, self.parent)
        json = self.client.execute(method)
        return Environment(json, method, client=self.client)
