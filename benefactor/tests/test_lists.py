from unittest import TestCase
from math import floor

from benefactor.lists import all_unique, transpose, deep_flatten, difference, difference_by, has_duplicates, \
    to_dictionary, most_frequent, spread


class TestLists(TestCase):
    def test_all_unique(self):
        x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
        y = [1, 2, 3, 4, 5]
        self.assertFalse(all_unique(x))
        self.assertTrue(all_unique(y))

    def test_transpose(self):
        a = [['a', 'b'], ['c', 'd'], ['e', 'f']]
        self.assertEqual(transpose(a), [('a', 'c', 'e'), ('b', 'd', 'f')])

    def test_deep_flatten(self):
        self.assertEqual(deep_flatten([1, [2], [[3], 4], 5]), [1, 2, 3, 4, 5])

    def test_difference(self):
        self.assertEqual(difference([1, 2, 3], [1, 2, 4]), [3])

    def test_difference_by(self):
        self.assertEqual(difference_by([2.1, 1.2], [2.3, 3.4], floor), [1.2])
        self.assertEqual(difference_by([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x']), [{'x': 2}])

    def test_has_duplicates(self):
        x = [1, 2, 3, 4, 5, 5]
        y = [1, 2, 3, 4, 5]
        self.assertTrue(has_duplicates(x))
        self.assertFalse(has_duplicates(y))

    def test_to_dictionary(self):
        keys = ["a", "b", "c"]
        values = [2, 3, 4]
        self.assertEqual(to_dictionary(keys, values), {'a': 2, 'c': 4, 'b': 3})

    def test_most_frequent(self):
        numbers = [1, 2, 1, 2, 3, 2, 1, 4, 2]
        self.assertEqual(most_frequent(numbers), 2)

    def test_spread(self):
        self.assertEqual(spread([1, 2, 3, [4, 5, 6], [7], 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
