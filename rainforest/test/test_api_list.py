import rainforest
import unittest

class TestApiList(unittest.TestCase):
    def setUp(self):
        self.fake_resource = {"data" : "fake-data"}
        self.apilist = rainforest.apibits.ApiList(rainforest.apibits.ApiResource, [self.fake_resource])

    def test_setting_klass(self):
        self.assertEqual(rainforest.apibits.ApiResource, self.apilist.klass)

    def test_convert_data_to_klass_instances(self):
        self.assertIsInstance(self.apilist[0], rainforest.apibits.ApiResource)
        self.assertEqual(self.fake_resource, self.apilist[0].json)

