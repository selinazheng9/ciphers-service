from django.test import TestCase
from .ciphers import caesar_encode

class CiphersTest(TestCase):
    def test1(self):
        plainText = "hello"
        shift = 1
        expected = "ifmmp"
        output = caesar_encode(plainText,shift)
        self.assertEqual(expected,output)
    def test2(self):
        plainText = "winter"
        shift = 3
        expected = "zlqwhu"
        output = caesar_encode(plainText,shift)
        self.assertEqual(expected,output)