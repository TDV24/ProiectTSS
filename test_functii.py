import unittest
from functii import mutatie_animale


class Teste(unittest.TestCase):
    #functional
    def test_functional_true(self):
        self.assertEqual(mutatie_animale("elefant", "antilopa"), "elefantilopa")
    def test_functional_false(self):
        self.assertNotEqual(mutatie_animale("capra", "rata"), "caprarata")
    #structural
    def test_int_data_type_left(self):
        self.assertFalse(mutatie_animale(7, "pisica"))
    def test_int_data_type_right(self):
        self.assertFalse(mutatie_animale("caine", 7))
    def test_list_data_type_for_both(self):
        self.assertNotEqual(mutatie_animale(["elefant", "capra", 6], ["rata"]), True)
    def test_list_data_type_for_left(self):
        self.assertEqual(type(mutatie_animale(["elefant", "capra", 8], "rata")), type(["cuvant", "litera"]))
    def test_list_data_type_for_right(self):
        self.assertNotEqual(mutatie_animale("papagal", ["albatros", "albina", 3]), [])
