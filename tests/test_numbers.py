# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokNumbers(unittest.TestCase):
    def test_cardinal_numbers(self):
        self.assertEqual(kokborok.num_to_words(1), "sa")
        self.assertEqual(kokborok.num_to_words(5), "ba")
        self.assertEqual(kokborok.num_to_words(10), "chi")
        self.assertEqual(kokborok.num_to_words(20), "rwichi")
        self.assertEqual(kokborok.num_to_words(30), "kholchi")
        self.assertEqual(kokborok.num_to_words(100), "ra-sa")
        self.assertEqual(kokborok.num_to_words(1000), "sai-sa")

    def test_words_to_num(self):
        self.assertEqual(kokborok.words_to_num("sa"), 1)
        self.assertEqual(kokborok.words_to_num("chi"), 10)
        self.assertEqual(kokborok.words_to_num("rwichi"), 20)

    def test_classifiers(self):
        self.assertEqual(kokborok.apply_classifier(1, "khorok"), "khorok-sa")
        self.assertEqual(kokborok.apply_classifier(3, "gong"), "gong-tham")
        self.assertEqual(kokborok.apply_classifier(4, "tai"), "tai-brwi")
        self.assertEqual(kokborok.apply_classifier(5, "phang"), "phang-ba")
        self.assertEqual(kokborok.apply_classifier(2, "kwtwi"), "kwtwi-nwi")

    def test_list_classifiers(self):
        cls = kokborok.list_classifiers()
        self.assertTrue(len(cls) >= 8)
