# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokTopLevel(unittest.TestCase):
    def test_metadata(self):
        self.assertEqual(kokborok.__version__, "1.0.0")
        self.assertEqual(kokborok.ISO_639_3, "trp")
        self.assertEqual(kokborok.NATIVE_NAME, "Kókborok")

    def test_translation(self):
        res = kokborok.translate("How are you?")
        self.assertEqual(res.text, "Nwng bahai tong?")
        self.assertEqual(res.target_lang, "kokborok")

        res_hi = kokborok.translate("नमस्ते")
        self.assertEqual(res_hi.text, "Khulumkha!")

        res_ben = kokborok.translate("ধন্যবাদ")
        self.assertEqual(res_ben.text, "Hambai!")

    def test_numbers(self):
        self.assertEqual(kokborok.num_to_words(1), "sa")
        self.assertEqual(kokborok.num_to_words(2), "nwi")
        self.assertEqual(kokborok.num_to_words(10), "chi")
        self.assertEqual(kokborok.apply_classifier(2, "khorok"), "khorok-nwi")

    def test_dictionary(self):
        entry = kokborok.lookup("khulumkha")
        self.assertIsNotNone(entry)
        self.assertEqual(entry["english"], "Greetings / Hello")

    def test_grammar(self):
        v = kokborok.conjugate("thang", tense="past", subject="ang")
        self.assertEqual(v, "ang thang-kha")
        n = kokborok.decline_noun("borok", "accusative")
        self.assertEqual(n, "borok-no")

    def test_script(self):
        ben = kokborok.roman_to_bengali("borok")
        self.assertIn("ব", ben)

    def test_culture(self):
        f = kokborok.list_festivals()
        self.assertTrue(len(f) >= 5)
        a = kokborok.list_authors()
        self.assertTrue(len(a) >= 4)
