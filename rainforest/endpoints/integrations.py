from ..apibits import *

class IntegrationsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Integration
        method = ApiMethod("get", "/integrations", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Integration, json, method, client=self.client)
        
    def retrieve(self, integration_id, params={}, headers={}):
        from ..resources import Integration
        params = ParamsBuilder.merge({
            "integration_id" : integration_id,
        }, params)
        method = ApiMethod("get", "/integrations/:integration_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Integration(json, method, client=self.client)
        
    def update(self, integration_id, params={}, headers={}):
        from ..resources import Integration
        params = ParamsBuilder.merge({
            "integration_id" : integration_id,
        }, params)
        method = ApiMethod("put", "/integrations/:integration_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Integration(json, method, client=self.client)
