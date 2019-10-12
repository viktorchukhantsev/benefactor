from unittest import TestCase

from benefactor.numbers import digitize


class TestNumbers(TestCase):
    def test_anagram(self):
        self.assertEqual(digitize(12345), [1, 2, 3, 4, 5])
