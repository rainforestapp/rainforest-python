from ..apibits import *

class GeneratorRowsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        method = ApiMethod("get", "/generators/:id/rows", params, headers, self.parent)
        json = self.client.execute(method)
        return json
        
    def create(self, params={}, headers={}):
        method = ApiMethod("post", "/generators/:id/rows", params, headers, self.parent)
        json = self.client.execute(method)
        return json
