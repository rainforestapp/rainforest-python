from ..apibits import *

class UsersEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import User
        method = ApiMethod("get", "/users", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(User, json, method, client=self.client)
        
    def retrieve(self, user_id, params={}, headers={}):
        from ..resources import User
        params = ParamsBuilder.merge({
            "user_id" : user_id,
        }, params)
        method = ApiMethod("get", "/users/:user_id", params, headers, self.parent)
        json = self.client.execute(method)
        return User(json, method, client=self.client)
        
    def update(self, user_id, params={}, headers={}):
        from ..resources import User
        params = ParamsBuilder.merge({
            "user_id" : user_id,
        }, params)
        method = ApiMethod("put", "/users/:user_id", params, headers, self.parent)
        json = self.client.execute(method)
        return User(json, method, client=self.client)
        
    def create(self, params={}, headers={}):
        from ..resources import User
        method = ApiMethod("post", "/users", params, headers, self.parent)
        json = self.client.execute(method)
        return User(json, method, client=self.client)
        
    def reset_password(self, email, params={}, headers={}):
        params = ParamsBuilder.merge({
            "email" : email,
        }, params)
        method = ApiMethod("post", "/users/reset_password", params, headers, self.parent)
        json = self.client.execute(method)
        return json
