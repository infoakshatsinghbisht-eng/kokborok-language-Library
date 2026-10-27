# -*- coding: utf-8 -*-
"""
Kokborok Postpositions and Relational Case Postposition Engine.
==============================================================

Provides programmatic attachment, parsing, and query for Kokborok postpositions
and case markers (-no, -ni, -o, -bai, -simi, -ha, -sog, -bagwi, -twi).
"""

from typing import Dict, List, Any, Optional

POSTPOSITIONS: List[Dict[str, Any]] = [
    {
        "marker": "-no",
        "case": "accusative_dative",
        "english": "to / for / [direct/indirect object]",
        "function": "Marks definite patients, recipients, and beneficiaries.",
        "example": "bo-no (to him / her)"
    },
    {
        "marker": "-ni",
        "case": "genitive",
        "english": "of / 's [possessive]",
        "function": "Indicates possession, association, or provenance.",
        "example": "nok-ni (of the house)"
    },
    {
        "marker": "-o",
        "case": "locative",
        "english": "in / at / on",
        "function": "Specifies spatial location or point in time.",
        "example": "hachuk-o (on the mountain)"
    },
    {
        "marker": "-bai",
        "case": "instrumental_comitative",
        "english": "with / by means of / alongside",
        "function": "Denotes instrument of action or personal accompaniment.",
        "example": "seng-bai (with a dao/knife)"
    },
    {
        "marker": "-simi",
        "case": "ablative",
        "english": "from / since",
        "function": "Marks point of spatial or temporal departure.",
        "example": "oro-ni-simi (from here)"
    },
    {
        "marker": "-ha",
        "case": "allative",
        "english": "towards / unto",
        "function": "Specifies direction or target destination.",
        "example": "song-ha (towards the village)"
    },
    {
        "marker": "-sog",
        "case": "terminative",
        "english": "up to / as far as / until",
        "function": "Denotes boundary or physical limit.",
        "example": "nok-sog (as far as the house)"
    },
    {
        "marker": "-bagwi",
        "case": "benefactive",
        "english": "for / because of / for the sake of",
        "function": "Expresses purpose, intention, or underlying cause.",
        "example": "ani bagwi (for me / on my behalf)"
    },
    {
        "marker": "-twi",
        "case": "manner_instrumental",
        "english": "through / according to / in the manner of",
        "function": "Indicates manner, trajectory, or custom.",
        "example": "kokborok-twi (in the Kokborok way / according to Kokborok)"
    }
]

def list_postpositions() -> List[Dict[str, Any]]:
    """List all Kokborok postpositions and relational case markers."""
    return list(POSTPOSITIONS)

def get_postposition(marker: str) -> Optional[Dict[str, Any]]:
    """Retrieve postposition metadata by marker (e.g. '-no', '-ni', '-bai')."""
    m = marker.strip().lower()
    if not m.startswith("-") and not m.startswith("b"):
        m = "-" + m
    for p in POSTPOSITIONS:
        if p["marker"] == m or p["case"] == m.lstrip("-"):
            return p
    return None

def attach_case(noun: str, case: str) -> str:
    """Attach a specific case postposition to a noun stem."""
    n = noun.strip()
    c = case.strip().lower()

    if c in ("nominative", "nom"):
        return n
    elif c in ("accusative", "dative", "acc", "dat"):
        return f"{n}-no"
    elif c in ("genitive", "possessive", "gen"):
        return f"{n}-ni"
    elif c in ("locative", "loc"):
        # If ends in vowel, often -yo or -o
        if n and n[-1] in "aeiouw":
            return f"{n}-o"
        return f"{n}-o"
    elif c in ("instrumental", "comitative", "inst", "com"):
        return f"{n}-bai"
    elif c in ("ablative", "abl"):
        return f"{n}-ni-simi"
    elif c in ("allative", "all"):
        return f"{n}-ha"
    elif c in ("terminative", "term"):
        return f"{n}-sog"
    elif c in ("benefactive", "ben"):
        return f"{n}-ni bagwi"
    elif c in ("manner", "modal"):
        return f"{n}-twi"
    else:
        return f"{n}-{case}"
