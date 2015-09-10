import rainforest

class ParamsBuilder(object):
	@classmethod
	def merge(cls, *args):
		params = {}
		for other_dict in args:
			params.update(other_dict)
		return params

	@classmethod
	def default_params(cls):
		return {
        }

	@classmethod
	def build(cls, params):
		""" Class currently does nothing, but was created to conform to spec."""
		return cls.merge(cls.default_params(), params)
