import os
import unittest

from otxb_core_utils.tests import TestUtils

from api import api

ROOT_PATH = os.path.dirname(__file__)


class TestCase(unittest.TestCase):
    def setUp(self):
        resources = os.path.join(ROOT_PATH, "resources")
        TestUtils.set_test_resource_directory(resources)
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls).setUpClass()

    def test_health_check(self):
        rv = self.app.get('/health')
        self.assertEqual(b'so healthy it hurts',
                         rv.data,
                         "Health check did not return right")
        self.assertEqual(200,
                         rv.status_code,
                         "Did not get expected response code")
