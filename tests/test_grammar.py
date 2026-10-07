# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokGrammar(unittest.TestCase):
    def test_verb_conjugation(self):
        self.assertEqual(kokborok.conjugate("cha", tense="past", subject="bo"), "bo cha-kha")
        self.assertEqual(kokborok.conjugate("cha", tense="future", subject="bo"), "bo cha-nai")
        self.assertEqual(kokborok.conjugate("cha", tense="present", subject="bo", negative=True), "bo cha-ya")

    def test_noun_declensions(self):
        self.assertEqual(kokborok.decline_noun("nok", "genitive"), "nok-ni")
        self.assertEqual(kokborok.decline_noun("nok", "locative"), "nok-o")
        self.assertEqual(kokborok.pluralize("borok"), "borok-rok")

    def test_adjective_degrees(self):
        self.assertEqual(kokborok.make_adjective("ham"), "kwham")
        self.assertEqual(kokborok.make_comparative("kaham"), "kaham-kham")
