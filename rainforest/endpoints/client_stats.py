from ..apibits import *

class ClientStatsEndpoint(ApiEndpoint):
    
    def retrieve(self, params={}, headers={}):
        from ..resources import ClientStats
        method = ApiMethod("get", "/clients/stats", params, headers, self.parent)
        json = self.client.execute(method)
        return ClientStats(json, method, client=self.client)
