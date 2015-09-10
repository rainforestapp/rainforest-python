from ..apibits import *

class GeneratorsEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Generator
        method = ApiMethod("get", "/generators", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Generator, json, method, client=self.client)
        
    def retrieve(self, generator_id, params={}, headers={}):
        from ..resources import Generator
        params = ParamsBuilder.merge({
            "generator_id" : generator_id,
        }, params)
        method = ApiMethod("get", "/generators/:generator_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Generator(json, method, client=self.client)
        
    def delete(self, generator_id, params={}, headers={}):
        from ..resources import Generator
        params = ParamsBuilder.merge({
            "generator_id" : generator_id,
        }, params)
        method = ApiMethod("delete", "/generators/:generator_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Generator(json, method, client=self.client)
        
    def update(self, generator_id, params={}, headers={}):
        from ..resources import Generator
        params = ParamsBuilder.merge({
            "generator_id" : generator_id,
        }, params)
        method = ApiMethod("put", "/generators/:generator_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Generator(json, method, client=self.client)
        
    def create(self, params={}, headers={}):
        from ..resources import Generator
        method = ApiMethod("post", "/generators", params, headers, self.parent)
        json = self.client.execute(method)
        return Generator(json, method, client=self.client)
