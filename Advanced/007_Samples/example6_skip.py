import datetime
import sys
import unittest.mock


# python -m unittest example6_skip.py

class UserTestCase(unittest.TestCase):

    @unittest.skip('Test Skip')
    def test_just_skip(self):
        self.fail('Does not run')

    @unittest.skipIf(datetime.datetime.now().hour in [10, 11, 12, 13, 14], 'too late')
    def test_just_skip_if(self):
        self.fail('Does not run')

    @unittest.skipUnless(sys.platform.startswith('darwin'), 'MacOs required')
    def test_only_mac(self):
        self.assertEqual(1, 1)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2)


@unittest.skip('showing class skipping')
class SkipTestCase(unittest.TestCase):
    def test_test(self):
        self.fail('error')
