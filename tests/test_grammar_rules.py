# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokGrammarRules(unittest.TestCase):
    def setUp(self):
        self.engine = kokborok.get_grammar_rules_engine()

    def test_rules_catalog_count(self):
        rules = kokborok.grammar_rules()
        self.assertGreaterEqual(len(rules), 170)
        self.assertEqual(len(rules), 180)
        self.assertEqual(self.engine.count(), len(rules))

    def test_rules_categories(self):
        cats = self.engine.categories()
        self.assertTrue(len(cats) >= 6)
        phon_rules = self.engine.by_category("Phonology")
        self.assertTrue(len(phon_rules) >= 6)
        tam_rules = self.engine.by_category("Tense")
        self.assertTrue(len(tam_rules) >= 10)
        self.assertIsNotNone(self.engine.get("TAM-09"))
        self.assertIsNotNone(self.engine.get("CAS-11"))
        self.assertIsNotNone(self.engine.get("NOM-07"))
        self.assertIsNotNone(self.engine.get("EXP-03"))

    def test_rule_lookup_by_id(self):
        r1 = self.engine.get("PHON-01")
        self.assertIsNotNone(r1)
        self.assertIn("Unrounded", r1.name)
        self.assertIn("/ɯ/", r1.formula)

        r_tam = self.engine.get("TAM-01")
        self.assertIsNotNone(r_tam)
        self.assertIn("-kha", r_tam.formula)

    def test_rules_search(self):
        res = self.engine.search("classifier")
        self.assertTrue(len(res) >= 5)
        res_tone = self.engine.search("tone")
        self.assertTrue(len(res_tone) >= 1)

    def test_clause_validation(self):
        diag = self.engine.validate_clause("Ang bo-no mai rwi-kha de?")
        rules_found = [d["rule"] for d in diag["applicable_rules"]]
        self.assertIn("TAM-01", rules_found)  # -kha
        self.assertIn("CAS-01", rules_found)  # -no
        self.assertIn("SYN-04", rules_found)  # de?

    def test_adverbs(self):
        advs = kokborok.list_adverbs()
        self.assertGreaterEqual(len(advs), 15)
        tini = kokborok.get_adverb("tini")
        self.assertIsNotNone(tini)
        self.assertEqual(tini["english"], "today")
        self.assertEqual(kokborok.classify_adverb("tini"), "time")
        self.assertEqual(kokborok.classify_adverb("oro"), "place")

    def test_postpositions(self):
        postpositions = kokborok.list_postpositions()
        self.assertGreaterEqual(len(postpositions), 8)
        self.assertEqual(kokborok.attach_case("nok", "locative"), "nok-o")
        self.assertEqual(kokborok.attach_case("borok", "accusative"), "borok-no")
        self.assertEqual(kokborok.attach_case("seng", "instrumental"), "seng-bai")
        self.assertEqual(kokborok.attach_case("oro", "ablative"), "oro-ni-simi")

    def test_expressives_and_echo_words(self):
        exp = kokborok.list_expressives()
        self.assertGreaterEqual(len(exp), 8)
        chwng = kokborok.get_expressive("chwng-chwng")
        self.assertIsNotNone(chwng)
        self.assertIn("shining", chwng["meaning"])

        echo = kokborok.find_echo_word("mai")
        self.assertIsNotNone(echo)
        self.assertIn("mai-sai", echo)

        red = kokborok.reduplicate_word("sa")
        self.assertEqual(red, "sa-sa")

if __name__ == "__main__":
    unittest.main()
