# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokCultureExpanded(unittest.TestCase):
    def test_attire(self):
        garments = kokborok.list_attire()
        self.assertGreaterEqual(len(garments), 5)
        rignai = kokborok.get_attire("rignai")
        self.assertIsNotNone(rignai)
        self.assertIn("Wrap-Around", rignai["english_name"])

        risa = kokborok.get_attire("risa")
        self.assertIsNotNone(risa)
        self.assertIn("Risa", risa["name"])

        motifs = kokborok.list_motifs()
        self.assertGreaterEqual(len(motifs), 4)
        chamathwi = [m for m in motifs if "Chamathwi" in m["name"]]
        self.assertTrue(len(chamathwi) > 0)

    def test_clans(self):
        clans = kokborok.list_clans()
        self.assertGreaterEqual(len(clans), 10)
        debbarma = kokborok.get_clan("debbarma")
        self.assertIsNotNone(debbarma)
        reang = kokborok.get_clan("reang")
        self.assertIsNotNone(reang)
        jamatia = kokborok.get_clan("jamatia")
        self.assertIsNotNone(jamatia)

        search_res = kokborok.search_clans("Hojagiri")
        self.assertTrue(any("Reang" in c["name"] for c in search_res))

    def test_cuisine(self):
        dishes = kokborok.list_cuisine()
        self.assertGreaterEqual(len(dishes), 8)
        chakhwi = kokborok.get_dish("chakhwi")
        self.assertIsNotNone(chakhwi)
        gudok = kokborok.get_dish("gudok")
        self.assertIsNotNone(gudok)
        berma = kokborok.get_dish("berma")
        self.assertIsNotNone(berma)

        bamboo_dishes = kokborok.search_cuisine("bamboo")
        self.assertTrue(len(bamboo_dishes) >= 2)

    def test_deities(self):
        deities = kokborok.list_deities()
        self.assertGreaterEqual(len(deities), 8)
        subrai = kokborok.get_deity("subrai")
        self.assertIsNotNone(subrai)
        mailuma = kokborok.get_deity("mailuma")
        self.assertIsNotNone(mailuma)
        khuluma = kokborok.get_deity("khuluma")
        self.assertIsNotNone(khuluma)
        tuibuma = kokborok.get_deity("tuibuma")
        self.assertIsNotNone(tuibuma)

    def test_folklore(self):
        stories = kokborok.list_folklore()
        self.assertGreaterEqual(len(stories), 5)
        chethwang = kokborok.get_story("chethwang")
        self.assertIsNotNone(chethwang)
        self.assertIn("Falcon", chethwang["title"])

    def test_geography(self):
        places = kokborok.list_geography()
        self.assertGreaterEqual(len(places), 10)
        unakoti = kokborok.get_place("unakoti")
        self.assertIsNotNone(unakoti)
        gomati = kokborok.get_place("gomati_river")
        self.assertIsNotNone(gomati)
        jampui = kokborok.get_place("jampui_hills")
        self.assertIsNotNone(jampui)

    def test_idioms(self):
        idioms = kokborok.list_idioms()
        self.assertGreaterEqual(len(idioms), 8)
        res = kokborok.search_idioms("heart")
        self.assertTrue(len(res) >= 1)

    def test_music(self):
        instruments = kokborok.list_instruments()
        self.assertGreaterEqual(len(instruments), 5)
        kham = kokborok.get_instrument("kham")
        self.assertIsNotNone(kham)
        sumui = kokborok.get_instrument("sumui")
        self.assertIsNotNone(sumui)

        dances = kokborok.list_dances()
        self.assertGreaterEqual(len(dances), 4)

    def test_botany(self):
        plants = kokborok.list_plants()
        self.assertGreaterEqual(len(plants), 6)
        muli = kokborok.get_plant("muli_bamboo")
        self.assertIsNotNone(muli)
        muya = kokborok.get_plant("muya")
        self.assertIsNotNone(muya)

    def test_wildlife(self):
        fauna = kokborok.list_wildlife()
        self.assertGreaterEqual(len(fauna), 5)
        phayre = kokborok.get_wildlife("phayres_langur")
        self.assertIsNotNone(phayre)
        self.assertIn("State Animal", phayre["category"])

    def test_rituals_and_sacred_sites(self):
        rituals = kokborok.list_rituals()
        self.assertGreaterEqual(len(rituals), 5)
        sites = kokborok.list_sacred_sites()
        self.assertGreaterEqual(len(sites), 5)
        matabari = kokborok.get_sacred_site("tripura_sundari")
        self.assertIsNotNone(matabari)

    def test_songs(self):
        songs = kokborok.list_songs()
        self.assertGreaterEqual(len(songs), 5)
        jaduni = kokborok.get_song("jaduni_01")
        self.assertIsNotNone(jaduni)

if __name__ == "__main__":
    unittest.main()
