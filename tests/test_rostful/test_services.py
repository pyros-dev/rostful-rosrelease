from __future__ import absolute_import

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import mock
import unittest

import pyros
from rostful import create_app, set_pyros_client, ServiceNotFound


class TestServicesNoPyros(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        app.testing = True  # required to check for exceptions
        self.client = app.test_client()

    def tearDown(self):
        pass


class TestServicesPyros(TestServicesNoPyros):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # overloading run to instantiate the pyros context manager
    # this will call setup and teardown
    def run(self, result=None):
        # argv is rosargs but these have no effect on client, so no need to pass anything here
        with pyros.pyros_ctx(name='rostful', argv=[], mock_client=True, base_path=os.path.join(os.path.dirname(__file__), '..', '..', '..')) as node_ctx:
            self.node_ctx = node_ctx
            set_pyros_client(self.node_ctx.client)
            super(TestServicesPyros, self).run(result)

    def setUp(self):
        super(TestServicesPyros, self).setUp()

    def tearDown(self):
        super(TestServicesPyros, self).tearDown()

if __name__ == '__main__':

    import nose
    nose.runmodule()
