# -*- coding: utf-8 -*-
"""Kokborok Pronouns, Demonstratives, and Interrogatives."""

PRONOUN_TABLE = {
    "1sg": {"kokborok": "ang", "english": "I", "hindi": "मैं", "bengali": "আমি"},
    "1pl": {"kokborok": "chwng", "english": "we", "hindi": "हम", "bengali": "আমরা"},
    "2sg": {"kokborok": "nwng", "english": "you", "hindi": "तू / तुम", "bengali": "তুমি"},
    "2pl": {"kokborok": "norok", "english": "you all", "hindi": "आप सब", "bengali": "তোমরা"},
    "3sg": {"kokborok": "bo", "english": "he / she / it", "hindi": "वह / उसे", "bengali": "সে / তিনি"},
    "3pl": {"kokborok": "borok", "english": "they", "hindi": "वे / उन्हें", "bengali": "তারা"}
}

DEMONSTRATIVES = {
    "this": "abo / ebo",
    "that": "obo",
    "here": "oro",
    "there": "oroni / aro",
    "these": "eborok",
    "those": "oborok"
}

INTERROGATIVES = {
    "who": "sabo",
    "what": "tamo",
    "where": "boro",
    "when": "baphang / baphango",
    "why": "tamoni",
    "how": "bahai / bahaitwi",
    "how_much": "bwsuk"
}

def get_pronoun(code: str) -> str:
    """Get pronoun by person/number code: 1sg, 1pl, 2sg, 2pl, 3sg, 3pl."""
    return PRONOUN_TABLE.get(code, {}).get("kokborok", "bo")
