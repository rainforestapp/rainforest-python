class ApiEndpoint(object):
	client = None
	parent = None

	def __init__(self, client, parent=None):
		self.client = client
		self.parent = parent
