# -*- coding: utf-8 -*-
"""Kokborok Phonetic Synthesis & SSML Audio Profile Generator."""

from ..phonetics.tokenizer import syllables, normalize
from ..phonetics.tones import has_high_tone

class KokborokVoiceSynthesizer:
    @staticmethod
    def get_speech_ssml(text: str, rate: str = "medium", pitch: str = "+0%") -> str:
        clean = normalize(text)
        return (
            f'<speak version="1.0" xml:lang="trp-IN">\n'
            f'  <prosody rate="{rate}" pitch="{pitch}">\n'
            f'    {clean}\n'
            f'  </prosody>\n'
            f'</speak>'
        )

    @staticmethod
    def get_phonetic_profile(text: str) -> dict:
        norm = normalize(text)
        tokens = norm.split()
        profile = []
        for t in tokens:
            syls = syllables(t)
            is_high = has_high_tone(t)
            profile.append({
                "word": t,
                "syllables": syls,
                "syllable_count": len(syls),
                "high_tone": is_high
            })
        return {
            "text": norm,
            "tokens": profile,
            "total_syllables": sum(p["syllable_count"] for p in profile)
        }
