# -*- coding: utf-8 -*-
"""Kokborok Tone and Pitch Accent Management."""

HIGH_TONE_MAP = {
    "a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "w": "ẃ"
}
REVERSE_TONE_MAP = {v: k for k, v in HIGH_TONE_MAP.items()}

def has_high_tone(word: str) -> bool:
    """Check if word has a marked high tone accent."""
    return any(c in REVERSE_TONE_MAP for c in word)

def strip_tone(word: str) -> str:
    """Remove acute high-tone accents from vowels."""
    res = []
    for c in word:
        res.append(REVERSE_TONE_MAP.get(c, c))
    return "".join(res)

def mark_high_tone(word: str) -> str:
    """Mark high tone on the primary vowel of a monosyllabic or root word."""
    for i, c in enumerate(word):
        if c.lower() in HIGH_TONE_MAP:
            return word[:i] + HIGH_TONE_MAP[c.lower()] + word[i+1:]
    return word
