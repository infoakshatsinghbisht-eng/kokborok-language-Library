# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokLexiconExpanded(unittest.TestCase):
    def test_total_count(self):
        st = kokborok.stats()
        self.assertGreaterEqual(st["headwords"], 490000)
        self.assertEqual(st["headwords"], 500000)
        self.assertGreaterEqual(st["phrases"], 20)
        self.assertGreaterEqual(st["proverbs"], 10)
        self.assertGreaterEqual(st["riddles"], 5)

    def test_word_lookups(self):
        # Traditional and everyday vocabulary lookups
        for word in ["risa", "rignai", "chakhwi", "berma", "sumui", "kham", "mokol", "bwkhorok", "mairong", "habani"]:
            entry = kokborok.lookup(word)
            self.assertIsNotNone(entry, f"Failed lookup for {word}")

    def test_derivational_lookups(self):
        # Lookups of derived forms
        entry_agent = kokborok.lookup("swinai")
        self.assertIsNotNone(entry_agent)
        self.assertIn("writer", entry_agent["english"].lower())

        entry_nominal = kokborok.lookup("hamjakmung")
        self.assertIsNotNone(entry_nominal)
        self.assertIn("love", entry_nominal["english"].lower())

    def test_search(self):
        res = kokborok.search("bamboo")
        self.assertTrue(len(res) > 0)
        res_river = kokborok.search("river")
        self.assertTrue(len(res_river) > 0)

    def test_extracted_book_words(self):
        # Words extracted from the digitized books
        for word in ["takthu", "chethuang", "naithokbi", "takhugonoi", "painalati", "swrongma", "papilik", "kwsrang", "kokbwtwi", "kachangma", "hajlaiti", "uasung"]:
            entry = kokborok.lookup(word)
            self.assertIsNotNone(entry, f"Failed lookup for book word {word}")
            self.assertIn("english", entry)
            self.assertIn("hindi", entry)
            self.assertIn("bengali", entry)

    def test_phrases_proverbs_riddles(self):
        p = kokborok.phrases.all()
        self.assertTrue(len(p) >= 20)
        pr = kokborok.proverbs.all()
        self.assertTrue(len(pr) >= 10)
        r = kokborok.riddles.all()
        self.assertTrue(len(r) >= 5)

if __name__ == "__main__":
    unittest.main()
