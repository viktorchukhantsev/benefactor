from unittest import TestCase

from benefactor.strings import anagram, byte_size, get_vowels, decapitalize, palindrome


class TestStrings(TestCase):
    def test_anagram(self):
        self.assertTrue(anagram("abcd3", "3acdb"))

    def test_byte_size(self):
        self.assertEqual(byte_size('Hello World'), 11)

    def test_get_vowels(self):
        self.assertEqual(get_vowels('foobar'), ['o', 'o', 'a'])
        self.assertEqual(get_vowels('gym'), [])

    def test_decapitalize(self):
        self.assertEqual(decapitalize("HelloWorld"), "helloWorld")

    def test_palindrome(self):
        self.assertTrue(palindrome('mom'))
        self.assertFalse(palindrome('monday'))
