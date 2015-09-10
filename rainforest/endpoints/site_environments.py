from ..apibits import *

class SiteEnvironmentsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import SiteEnvironment
        method = ApiMethod("get", "/site_environments", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(SiteEnvironment, json, method, client=self.client)
        
    def update(self, site_environment_id, params={}, headers={}):
        from ..resources import SiteEnvironment
        params = ParamsBuilder.merge({
            "site_environment_id" : site_environment_id,
        }, params)
        method = ApiMethod("put", "/site_environments/:site_environment_id", params, headers, self.parent)
        json = self.client.execute(method)
        return SiteEnvironment(json, method, client=self.client)
