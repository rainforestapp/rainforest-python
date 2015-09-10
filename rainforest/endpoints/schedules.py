from ..apibits import *

class SchedulesEndpoint(ApiEndpoint):
    
    def all(self, params={}, headers={}):
        from ..resources import Schedule
        method = ApiMethod("get", "/schedules", params, headers, self.parent)
        json = self.client.execute(method)
        return ApiList(Schedule, json, method, client=self.client)
        
    def retrieve(self, schedule_id, params={}, headers={}):
        from ..resources import Schedule
        params = ParamsBuilder.merge({
            "schedule_id" : schedule_id,
        }, params)
        method = ApiMethod("get", "/schedules/:schedule_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Schedule(json, method, client=self.client)
        
    def delete(self, schedule_id, params={}, headers={}):
        from ..resources import Schedule
        params = ParamsBuilder.merge({
            "schedule_id" : schedule_id,
        }, params)
        method = ApiMethod("delete", "/schedules/:schedule_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Schedule(json, method, client=self.client)
        
    def update(self, schedule_id, params={}, headers={}):
        from ..resources import Schedule
        params = ParamsBuilder.merge({
            "schedule_id" : schedule_id,
        }, params)
        method = ApiMethod("put", "/schedules/:schedule_id", params, headers, self.parent)
        json = self.client.execute(method)
        return Schedule(json, method, client=self.client)
        
    def create(self, params={}, headers={}):
        from ..resources import Schedule
        method = ApiMethod("post", "/schedules", params, headers, self.parent)
        json = self.client.execute(method)
        return Schedule(json, method, client=self.client)
