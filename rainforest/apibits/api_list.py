from .api_resource import ApiResource

class ApiList(ApiResource):
    _api_attributes = {}
    data = []
    klass = None
    client = None

    def refresh_from(self, json, api_method=None, client=None):
        if not isinstance(json, dict):
            json = { 'data': json }

        self.clear_api_attributes()
        self.api_method = api_method
        self.data = []
        self.json = json
        self.client = client

        for key, value in json.items():
            if key == 'data':
                if isinstance(value, list):
                    setattr(self, key, [self.klass(elem) for elem in value])
                else:
                    setattr(self, key, value or [])
            elif key in self.__class__.api_attribute_names():
                setattr(self, key, self.determine_api_attribute_value(key, value))

        return self

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        for item in self.data:
            yield item

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return "<rainforest.apibits.ApiList object (class %s): %s>" % (self.klass.__name__, self.data.__repr__())

    def __init__(self, klass, json={}, api_method=None, client=None):
        self.klass = klass

        super(ApiList, self).__init__()

        self.refresh_from(json, api_method, client)
