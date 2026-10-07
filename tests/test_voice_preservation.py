# -*- coding: utf-8 -*-
import unittest
import kokborok

class TestKokborokVoiceAndPreservation(unittest.TestCase):
    def test_ssml_synthesis(self):
        ssml = kokborok.KokborokVoiceSynthesizer.get_speech_ssml("Khulumkha")
        self.assertIn("<speak", ssml)
        self.assertIn('xml:lang="trp-IN"', ssml)
        self.assertIn("Khulumkha", ssml)

    def test_phonetic_profile(self):
        prof = kokborok.KokborokVoiceSynthesizer.get_phonetic_profile("Nwng bahai tong?")
        self.assertGreaterEqual(prof["total_syllables"], 3)

    def test_preservation(self):
        mgr = kokborok.CorpusManager()
        rec = kokborok.PreservationRecord("Kókborokma", "Radhamohan Thakur", "1900", "State Press")
        mgr.add_record(rec)
        self.assertEqual(len(mgr.list_records()), 1)
