import unittest

class SampleTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2, "Addition test failed.")

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2, "Subtraction test failed.")

    def test_multiplication(self):
        self.assertEqual(3 * 4, 12, "Multiplication test failed.")

    def test_division(self):
        self.assertEqual(10 / 2, 5, "Division test failed.")

    def test_string_concatenation(self):
        self.assertEqual("Hello, " + "World!", "Hello, World!", "String concatenation test failed.")

    def test_list_length(self):
        self.assertEqual(len([1, 2, 3, 4]), 4, "List length test failed.")

    def test_dictionary_key(self):
        sample_dict = {'key1': 'value1', 'key2': 'value2'}
        self.assertIn('key1', sample_dict, "Dictionary key test failed.")

    def test_boolean(self):
        self.assertTrue(3 > 2, "Boolean test failed.")

if __name__ == '__main__':
    unittest.main()
