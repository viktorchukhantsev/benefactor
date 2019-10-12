from unittest import TestCase

from benefactor.dicts import merge_two_dicts


class TestDicts(TestCase):
    def test_merge_two_dicts(self):
        a = {'x': 1, 'y': 2}
        b = {'y': 3, 'z': 4}
        self.assertEqual(merge_two_dicts(a, b), {'y': 3, 'x': 1, 'z': 4})
