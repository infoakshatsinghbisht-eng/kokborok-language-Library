# -*- coding: utf-8 -*-
"""Kokborok Noun Morphology, Pluralization (-rok), and Case Postpositions."""

from typing import Dict, Any

class KokborokNoun:
    def __init__(self, lemma: str, english: str, hindi: str, bengali: str):
        self.lemma = lemma
        self.english = english
        self.hindi = hindi
        self.bengali = bengali

    @property
    def plural(self) -> str:
        return f"{self.lemma}-rok"

    def declensions(self) -> Dict[str, str]:
        """Generate case inflections with postpositions."""
        return {
            "nominative_sg": self.lemma,
            "nominative_pl": f"{self.lemma}-rok",
            "accusative_sg": f"{self.lemma}-no",
            "accusative_pl": f"{self.lemma}-rok-no",
            "genitive_sg": f"{self.lemma}-ni",
            "genitive_pl": f"{self.lemma}-rok-ni",
            "locative_sg": f"{self.lemma}-o",
            "locative_pl": f"{self.lemma}-rok-o",
            "instrumental_sg": f"{self.lemma}-bai",
            "instrumental_pl": f"{self.lemma}-rok-bai",
            "ablative_sg": f"{self.lemma}-ni-simi",
            "ablative_pl": f"{self.lemma}-rok-ni-simi",
            "allative_sg": f"{self.lemma}-ha",
            "allative_pl": f"{self.lemma}-rok-ha"
        }

def pluralize(noun: str) -> str:
    """Pluralize a Kokborok noun with -rok."""
    n = noun.strip()
    return f"{n}-rok" if not n.endswith("-rok") else n

def decline_noun(noun: str, case: str, plural: bool = False) -> str:
    """Decline a noun into specified case (accusative, genitive, locative, instrumental, etc.)."""
    base = pluralize(noun) if plural else noun
    case_map = {
        "nominative": "",
        "accusative": "-no",
        "genitive": "-ni",
        "locative": "-o",
        "instrumental": "-bai",
        "ablative": "-ni-simi",
        "allative": "-ha"
    }
    suffix = case_map.get(case.lower(), "")
    return f"{base}{suffix}"
