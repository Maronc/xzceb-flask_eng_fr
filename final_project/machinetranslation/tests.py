import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(englishToFrench('Null'), 'Null')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
        self.assertNotEqual(englishToFrench('Hello'), 'Bonjours')

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(englishToFrench('Null'), 'Null')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(englishToFrench('Bonjour'), 'Hellos')

unittest.main()
