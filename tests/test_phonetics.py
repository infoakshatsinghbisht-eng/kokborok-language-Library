# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokPhonetics(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(kokborok.normalize("tôy"), "twy")

    def test_syllables(self):
        s = kokborok.syllables("borok")
        self.assertTrue(len(s) >= 1)

    def test_tone(self):
        self.assertTrue(kokborok.has_high_tone("tẃy"))
        self.assertFalse(kokborok.has_high_tone("twy"))
        self.assertEqual(kokborok.strip_tone("tẃy"), "twy")
