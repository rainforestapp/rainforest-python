from ..apibits import *
from ..endpoints import SchedulesEndpoint

class Schedule(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().schedules().all(params, headers)
        return res

    @classmethod
    def retrieve(cls, schedule_id, params={}, headers={}):
        res = cls.default_client().schedules().retrieve(schedule_id, params, headers)
        return res

    @classmethod
    def update(cls, schedule_id, params={}, headers={}):
        res = cls.default_client().schedules().update(schedule_id, params, headers)
        return res

    @classmethod
    def create(cls, params={}, headers={}):
        res = cls.default_client().schedules().create(params, headers)
        return res

    def refresh(self, params={}, headers={}):
        res = self.get_client().schedules().retrieve(self.id, params, headers)
        return self.refresh_from(res.json, res.api_method, res.client)

    def delete(self, params={}, headers={}):
        res = self.get_client().schedules().delete(self.id, params, headers)
        return res

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(Schedule, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "schedule")

    _api_attributes = {
        "created_at" : {},
        "filters" : {},
        "id" : {},
        "repeat_rules" : {},
    }
