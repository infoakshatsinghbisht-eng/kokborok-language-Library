# -*- coding: utf-8 -*-
"""Kokborok Orthographic Normalization and Tokenizer."""

import re
from typing import List

VALID_CHARS = set("abcdefghijklmnopqrstuvwxyzáéíóúẃwô'-")

def normalize(text: str) -> str:
    """Normalize Kokborok text: trim, standardize apostrophes and w/ô vowels."""
    if not text:
        return ""
    t = text.strip()
    t = t.replace("’", "'").replace("‘", "'").replace("`", "'")
    t = t.replace("ô", "w").replace("Ô", "W")
    t = re.sub(r"\s+", " ", t)
    return t

def tokenize(text: str) -> List[str]:
    """Tokenize text into Kokborok words, preserving hyphens for compounds and suffixes."""
    norm = normalize(text)
    tokens = re.findall(r"[\w'áéíóúẃ-]+|[^\w\s]", norm, re.UNICODE)
    return [t for t in tokens if t.strip()]

def syllables(word: str) -> List[str]:
    """Segment a Kokborok word into syllables based on CV/CVC patterns."""
    w = normalize(word).lower()
    if not w:
        return []
    subwords = w.split("-")
    result = []
    vowels = "aeiouwáéíóúẃ"
    for sw in subwords:
        if not sw:
            continue
        cur = ""
        for i, ch in enumerate(sw):
            cur += ch
            if ch in vowels:
                if i + 1 < len(sw) and sw[i+1] not in vowels:
                    if i + 2 < len(sw) and sw[i+2] in vowels:
                        result.append(cur)
                        cur = ""
                    elif i + 2 < len(sw) and sw[i+1:i+3] in ["ng", "ch", "kh", "ph", "th"]:
                        result.append(cur)
                        cur = ""
                    else:
                        cur += sw[i+1]
                        result.append(cur)
                        cur = ""
        if cur:
            if result and len(cur) == 1 and cur not in vowels:
                result[-1] += cur
            else:
                result.append(cur)
    return result if result else [word]

PUNCT_CHARS = ".,!?;:'\"()[]{}"

def is_kokborok_word(word: str) -> bool:
    """Check if a word follows valid Kokborok phonotactics and orthography."""
    w = normalize(word).lower().strip(PUNCT_CHARS)
    if not w or len(w) > 35:
        return False
    return bool(re.match(r"^[abdeghijklmnoprstuwyaeiouwáéíóúẃ'-]+$", w))
