# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokLexicon(unittest.TestCase):
    def test_words_count(self):
        st = kokborok.stats()
        self.assertGreaterEqual(st["headwords"], 100000)
        self.assertGreaterEqual(st["total_morphological_forms"], 300000)

    def test_morphology_analysis(self):
        res = kokborok.analyze("thangkha")
        self.assertEqual(res.root, "thang")
        self.assertEqual(res.pos, "verb")

    def test_search(self):
        res = kokborok.search("water")
        self.assertTrue(len(res) > 0)
