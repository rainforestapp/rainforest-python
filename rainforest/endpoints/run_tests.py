from ..apibits import *

class RunTestsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Test
        method = ApiMethod("get", "/runs/:id/tests", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Test, json, method, client=self.client)
        
    def retrieve(self, test_id, params={}, headers={}):
        from ..resources import Test
        params = ParamsBuilder.merge({
            "test_id" : test_id,
        }, params)
        method = ApiMethod("get", "/runs/:id/tests/:test_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Test(json, method, client=self.client)
