from __future__ import absolute_import, division, unicode_literals
import decimal
import unittest
from warnings import warn

import jsonpickle
from jsonpickle import compat
from jsonpickle.compat import PY2
from jsonpickle.compat import PY3

from helper import SkippableTest


class Thing(object):

    def __init__(self, name):
        self.name = name
        self.child = None


SAMPLE_DATA = {'things': [Thing('data')]}


class BackendBase(SkippableTest):

    def _is_installed(self, backend):
        if not jsonpickle.util.is_installed(backend):
            return self.skip('%s not available; please install' % backend)

    def set_backend(self, *args):
        backend = args[0]

        self._is_installed(backend)

        jsonpickle.load_backend(*args)
        jsonpickle.set_preferred_backend(backend)

    def set_preferred_backend(self, backend):
        self._is_installed(backend)
        jsonpickle.set_preferred_backend(backend)

    def tearDown(self):
        # always reset to default backend
        jsonpickle.set_preferred_backend('json')

    def assertEncodeDecode(self, json_input):
        expect = SAMPLE_DATA
        actual = jsonpickle.decode(json_input)
        self.assertEqual(expect['things'][0].name, actual['things'][0].name)
        self.assertEqual(expect['things'][0].child, actual['things'][0].child)

        pickled = jsonpickle.encode(SAMPLE_DATA)
        actual = jsonpickle.decode(pickled)
        self.assertEqual(expect['things'][0].name, actual['things'][0].name)
        self.assertEqual(expect['things'][0].child, actual['things'][0].child)

    def test_None_dict_key(self):
        """Ensure that backends produce the same result for None dict keys"""
        data = {None: None}
        expect = {'null': None}
        pickle = jsonpickle.encode(data)
        actual = jsonpickle.decode(pickle)
        self.assertEqual(expect, actual)


class JsonTestCase(BackendBase):
    def setUp(self):
        self.set_preferred_backend('json')

    def test_backend(self):
        expected_pickled = (
            '{"things": [{'
            '"py/object": "backend_test.Thing", '
            '"name": "data", '
            '"child": null} '
            ']}')
        self.assertEncodeDecode(expected_pickled)


def has_module(module):
    try:
        __import__(module)
    except ImportError:
        warn(module + ' module not available for testing, '
             'consider installing')
        return False
    return True


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(JsonTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
