# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokTranslator(unittest.TestCase):
    def test_english_to_kokborok(self):
        self.assertEqual(kokborok.translate("Hello").text, "Khulumkha!")
        self.assertEqual(kokborok.translate("Thank you").text, "Hambai!")
        self.assertEqual(kokborok.translate("Good morning").text, "Kaham sal!")
        self.assertEqual(kokborok.translate("Good night").text, "Kaham hor!")
        self.assertEqual(kokborok.translate("Come here").text, "Oro phai.")
        self.assertEqual(kokborok.translate("Go there").text, "Aro thang.")

    def test_hindi_to_kokborok(self):
        self.assertEqual(kokborok.translate("नमस्ते").text, "Khulumkha!")
        self.assertEqual(kokborok.translate("धन्यवाद").text, "Hambai!")
        self.assertEqual(kokborok.translate("सुप्रभात").text, "Kaham sal!")

    def test_bengali_to_kokborok(self):
        self.assertEqual(kokborok.translate("নমস্কার").text, "Khulumkha!")
        self.assertEqual(kokborok.translate("ধন্যবাদ").text, "Hambai!")
        self.assertEqual(kokborok.translate("শুভ সকাল").text, "Kaham sal!")

    def test_kokborok_to_english(self):
        res = kokborok.translate("Khulumkha", target="en")
        self.assertIn("Hello", res.text)
        res2 = kokborok.translate("Hambai", target="en")
        self.assertIn("Thank you", res2.text)

    def test_dialect_adaptation(self):
        res_reang = kokborok.translate("How are you?", dialect="reang")
        self.assertIsNotNone(res_reang.text)
