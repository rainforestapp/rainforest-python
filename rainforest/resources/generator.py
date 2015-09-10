from ..apibits import *
from ..endpoints import GeneratorsEndpoint
from ..endpoints import GeneratorRowsEndpoint

class Generator(ApiResource):

    @classmethod
    def all(cls, params={}, headers={}):
        res = cls.default_client().generators().all(params, headers)
        return res

    @classmethod
    def retrieve(cls, generator_id, params={}, headers={}):
        res = cls.default_client().generators().retrieve(generator_id, params, headers)
        return res

    @classmethod
    def update(cls, generator_id, params={}, headers={}):
        res = cls.default_client().generators().update(generator_id, params, headers)
        return res

    @classmethod
    def create(cls, params={}, headers={}):
        res = cls.default_client().generators().create(params, headers)
        return res

    def refresh(self, params={}, headers={}):
        res = self.get_client().generators().retrieve(self.id, params, headers)
        return self.refresh_from(res.json, res.api_method, res.client)

    def delete(self, params={}, headers={}):
        res = self.get_client().generators().delete(self.id, params, headers)
        return res

    def rows(self):
        from ..endpoints import GeneratorRowsEndpoint
        return GeneratorRowsEndpoint(self.client, self)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	  super(Generator, self).__init__(*args, **kwargs)
    	  ApiResource.register_api_subclass(self, "generator")

    _api_attributes = {
        "columns" : {},
        "created_at" : {},
        "data" : {},
        "description" : {},
        "generator_type" : {},
        "id" : {},
        "name" : {},
        "row_count" : {},
    }
