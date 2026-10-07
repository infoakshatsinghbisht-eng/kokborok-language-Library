# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokCulture(unittest.TestCase):
    def test_festivals(self):
        festivals = kokborok.list_festivals()
        names = [f["name"] for f in festivals]
        self.assertIn("Garia Puja", names)
        self.assertIn("Kharchi Puja", names)
        self.assertIn("Ker Puja", names)
        self.assertIn("Hojagiri", names)
        self.assertIn("Mamita", names)

    def test_authors(self):
        authors = kokborok.list_authors()
        names = [a["name"] for a in authors]
        self.assertIn("Radhamohan Thakur", names)
        self.assertIn("Sudhanya Debbarma", names)
        self.assertIn("Chandrakanta Murasingh", names)

    def test_epics(self):
        epics = kokborok.list_epics()
        titles = [e["title"] for e in epics]
        self.assertTrue(any("Rajmala" in t for t in titles))
        self.assertTrue(any("Chethuang" in t for t in titles))

    def test_kinship(self):
        terms = kokborok.list_kinship_terms()
        self.assertTrue(len(terms) >= 10)
        ama = kokborok.get_kinship_term("ama")
        self.assertEqual(ama["english"], "Mother")
        apha = kokborok.get_kinship_term("apha")
        self.assertEqual(apha["english"], "Father")

    def test_calendar(self):
        months = kokborok.get_months()
        self.assertEqual(len(months), 12)
        days = kokborok.get_days()
        self.assertEqual(len(days), 7)
        seasons = kokborok.get_seasons()
        self.assertEqual(len(seasons), 4)

    def test_catalogue(self):
        cat = kokborok.catalogue
        self.assertGreaterEqual(cat.count(), 5)
        results = cat.search("Grammar")
        self.assertTrue(len(results) > 0)
