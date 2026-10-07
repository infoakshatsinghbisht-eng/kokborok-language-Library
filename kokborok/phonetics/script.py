# -*- coding: utf-8 -*-
"""Transliteration between Roman (Official Kokborok) and Bengali-Assamese Scripts."""

import re

ROMAN_TO_BEN = [
    ("ch", "চ"), ("kh", "খ"), ("ph", "ফ"), ("th", "থ"), ("ng", "ঙ"),
    ("b", "ব"), ("d", "দ"), ("g", "গ"), ("h", "হ"), ("j", "জ"),
    ("k", "ক"), ("l", "ল"), ("m", "ম"), ("n", "ন"), ("p", "প"),
    ("r", "র"), ("s", "স"), ("t", "ত"), ("y", "য়"),
    ("ai", "াই"), ("ui", "ুই"), ("oi", "ই"), ("wi", "ৈ"), ("au", "াউ"),
    ("a", "া"), ("i", "ি"), ("u", "ু"), ("e", "ে"), ("o", "ো"), ("w", "্ব")
]

BEN_TO_ROMAN = [
    ("চ", "ch"), ("খ", "kh"), ("ফ", "ph"), ("থ", "th"), ("ঙ", "ng"),
    ("ব", "b"), ("দ", "d"), ("গ", "g"), ("হ", "h"), ("জ", "j"),
    ("ক", "k"), ("ল", "l"), ("ম", "m"), ("ন", "n"), ("প", "p"),
    ("র", "r"), ("স", "s"), ("ত", "t"), ("য়", "y"),
    ("াই", "ai"), ("ুই", "ui"), ("াউ", "au"),
    ("া", "a"), ("ি", "i"), ("ু", "u"), ("ে", "e"), ("ো", "o"), ("্ব", "w")
]

def roman_to_bengali(text: str) -> str:
    """Convert Roman Kokborok orthography to Bengali-Assamese script."""
    res = text.lower()
    for rom, ben in ROMAN_TO_BEN:
        res = res.replace(rom, ben)
    return res

def bengali_to_roman(text: str) -> str:
    """Convert Bengali-Assamese Kokborok text to Roman orthography."""
    res = text
    for ben, rom in BEN_TO_ROMAN:
        res = res.replace(ben, rom)
    return res

def detect_script(text: str) -> str:
    """Detect whether text is in Latin (Roman) or Bengali script."""
    has_bengali = any('\u0980' <= c <= '\u09FF' for c in text)
    if has_bengali:
        return "bengali"
    return "roman"
