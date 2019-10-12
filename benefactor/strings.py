from collections import Counter


def anagram(first, second):
    return Counter(first) == Counter(second)


def byte_size(string):
    return len(string.encode('utf-8'))


def get_vowels(string):
    return [each for each in string if each in 'aeiou']


def decapitalize(string):
    return string[:1].lower() + string[1:]


def palindrome(a):
    return a == a[::-1]
