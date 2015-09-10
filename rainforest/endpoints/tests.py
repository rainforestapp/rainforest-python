from ..apibits import *

class TestsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Test
        method = ApiMethod("get", "/tests", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Test, json, method, client=self.client)
        
    def retrieve(self, test_id, params={}, headers={}):
        from ..resources import Test
        params = ParamsBuilder.merge({
            "test_id" : test_id,
        }, params)
        method = ApiMethod("get", "/tests/:test_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Test(json, method, client=self.client)
        
    def delete(self, test_id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "test_id" : test_id,
        }, params)
        method = ApiMethod("delete", "/tests/:test_id", params, headers, self.parent)
        json = self.client.execute(method)
        return json
        
    def update(self, test_id, params={}, headers={}):
        from ..resources import Test
        params = ParamsBuilder.merge({
            "test_id" : test_id,
        }, params)
        method = ApiMethod("put", "/tests/:test_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Test(json, method, client=self.client)
        
    def create(self, params={}, headers={}):
        from ..resources import Test
        method = ApiMethod("post", "/tests", params, headers, self.parent)
        json = self.client.execute(method)
        return Test(json, method, client=self.client)
        
    def history(self, test_id, params={}, headers={}):
        from ..resources import Run
        params = ParamsBuilder.merge({
            "test_id" : test_id,
        }, params)
        method = ApiMethod("get", "/tests/:test_id/history", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Run, json, method, client=self.client)
