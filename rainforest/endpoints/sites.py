from ..apibits import *

class SitesEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Site
        method = ApiMethod("get", "/sites", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Site, json, method, client=self.client)
        
    def delete(self, site_id, params={}, headers={}):
        from ..resources import Site
        params = ParamsBuilder.merge({
            "site_id" : site_id,
        }, params)
        method = ApiMethod("delete", "/sites/:site_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Site(json, method, client=self.client)
        
    def update(self, site_id, params={}, headers={}):
        from ..resources import Site
        params = ParamsBuilder.merge({
            "site_id" : site_id,
        }, params)
        method = ApiMethod("put", "/sites/:site_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Site(json, method, client=self.client)
        
    def create(self, params={}, headers={}):
        from ..resources import Site
        method = ApiMethod("post", "/sites", params, headers, self.parent)
        json = self.client.execute(method)
        return Site(json, method, client=self.client)
