# -*- coding: utf-8 -*-
"""Kokborok Numeral Classifier System."""

from typing import Dict, List

CLASSIFIER_TABLE: Dict[str, Dict[str, str]] = {
    "khorok": {"meaning": "human beings", "example": "khorok-sa borok (one person)"},
    "kwtwi": {"meaning": "animals, birds, insects", "example": "kwtwi-sa mwkhra (one monkey)"},
    "gong": {"meaning": "long, slender, rigid objects (sticks, pens, bamboos)", "example": "gong-sa wa (one bamboo)"},
    "tai": {"meaning": "flat, broad objects, leaves, clothes", "example": "tai-sa risa (one traditional cloth)"},
    "thai": {"meaning": "round, globular objects, fruits", "example": "thai-sa thaichu (one mango)"},
    "phang": {"meaning": "trees, standing plants", "example": "phang-sa bwphang (one tree)"},
    "dung": {"meaning": "ropes, strings, threads, vines", "example": "dung-sa chong (one rope)"},
    "bor": {"meaning": "times, occurrences, occasions", "example": "bor-sa (one time / once)"},
    "khang": {"meaning": "heaps, piles of agricultural produce", "example": "khang-sa mai (one pile of paddy)"},
    "bak": {"meaning": "bundles, sheaves", "example": "bak-sa bol (one bundle of firewood)"}
}

def apply_classifier(num: int, classifier: str) -> str:
    """Bind a number with a classifier: e.g., 2 + 'khorok' -> 'khorok-nwi'."""
    from .numerals import num_to_words
    num_str = num_to_words(num)
    return f"{classifier}-{num_str}"

def list_classifiers() -> List[Dict[str, str]]:
    """Return all documented numeral classifiers."""
    return [{"classifier": k, **v} for k, v in CLASSIFIER_TABLE.items()]
