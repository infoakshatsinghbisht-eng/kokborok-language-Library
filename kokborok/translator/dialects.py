# -*- coding: utf-8 -*-
"""Kokborok Dialectal Variation Engine (Debbarma, Reang/Bru, Jamatia, Noatia)."""

from typing import Dict

DIALECT_MAP: Dict[str, Dict[str, str]] = {
    "reang": {
        "chwng": "ching",
        "kaham": "hamya-kaham / kaham",
        "twy": "ti",
        "nok": "nom",
        "borok": "bru"
    },
    "jamatia": {
        "chwng": "chwng",
        "ang": "ang",
        "bo": "bo",
        "kaham": "kaham"
    },
    "noatia": {
        "borok": "borok",
        "twy": "twi"
    }
}

def apply_dialect(text: str, dialect: str = "debbarma") -> str:
    d = dialect.lower().strip()
    if d in ("debbarma", "standard") or d not in DIALECT_MAP:
        return text
    words = text.split()
    mapping = DIALECT_MAP[d]
    res = [mapping.get(w.lower(), w) for w in words]
    return " ".join(res)
