# -*- coding: utf-8 -*-
"""
Kokborok Rituals, Lifecycle Rites, and Shamanic Traditions (Hukumu & Ochai).
============================================================================

Documentation of traditional Tripuri lifecycle ceremonies, shamanic priesthood (Ochai),
purification rites (Katharak), weddings (Chukbar), and ancestral ceremonies.
"""

from typing import Dict, List, Any, Optional

RITUALS: List[Dict[str, Any]] = [
    {
        "id": "ochai_priesthood",
        "name": "Ochai Shamanic Rites",
        "category": "Priesthood & Spiritual Mediation",
        "officiant": "Ochai (Traditional High Priest / Shaman)",
        "description": "The Ochai is the spiritual mediator between the human community, ancestral spirits, and nature deities. Using sacred chants, divination with eggshells or split bamboo, the Ochai diagnoses illnesses and performs purification rites.",
        "cultural_significance": "Essential in conducting all 14 Gods rituals, Garia worship, and lifecycle purifications."
    },
    {
        "id": "chukbar",
        "name": "Chukbar (Traditional Wedding Ceremony)",
        "category": "Lifecycle / Marriage",
        "officiant": "Ochai and Clan Elders (Choudhury)",
        "description": "The sacred marriage ceremony of the Tripuri people. Involves invoking Lampra, circumambulating the sacred water pot, tying the Risa around the couple's shoulders, and an exchange of betel leaves.",
        "cultural_significance": "Binds not merely two individuals, but creates an enduring bond of alliance between the two clans."
    },
    {
        "id": "risa_sormani",
        "name": "Risa Sormani (Coming of Age Rite)",
        "category": "Lifecycle / Rite of Passage",
        "officiant": "Mother, Paternal Aunt, and Elder Matriarchs",
        "description": "A joyous rite of passage where an adolescent girl aged 12-14 is formally gifted and draped in her first handwoven Risa, marking her transition into womanhood and community responsibility.",
        "cultural_significance": "Celebrates female dignity, handloom skill, and social maturity in Tripuri culture."
    },
    {
        "id": "katharak",
        "name": "Katharak (Purification Ceremony)",
        "category": "Cleansing & Consecration",
        "officiant": "Ochai",
        "description": "A sacred cleansing ritual using water sprinkled with basil (Tulsi) leaves and fresh mango twigs to purify a household after childbirth, recovery from severe illness, or before consecrating a new home (Nok-Kwtal).",
        "cultural_significance": "Restores spiritual harmony and banishes lingering negative energies from the living space."
    },
    {
        "id": "simang_sokma",
        "name": "Simang Sokma (Funeral & Ancestral Remembrance)",
        "category": "Lifecycle / Mortuary Rites",
        "officiant": "Ochai and Clan Kinsmen",
        "description": "Traditional cremation rites performed on the bank of a hill stream or river, followed by immersing bones in the Gomati river or local stream and offering sacred food to guide the soul (Simang) to the realm of ancestors.",
        "cultural_significance": "Honors the departed ancestors and ensures their protective blessing upon the living lineage."
    }
]

class RitualManager:
    """Manager for querying traditional Kokborok rituals and lifecycle rites."""

    def __init__(self):
        self._rituals = RITUALS

    def all_rituals(self) -> List[Dict[str, Any]]:
        return list(self._rituals)

    def count(self) -> int:
        return len(self._rituals)

    def get_ritual(self, ritual_id: str) -> Optional[Dict[str, Any]]:
        rid = ritual_id.lower().strip()
        for r in self._rituals:
            if r["id"] == rid or rid in r["name"].lower():
                return r
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for r in self._rituals:
            if (
                q in r["name"].lower() or
                q in r["category"].lower() or
                q in r["officiant"].lower() or
                q in r["description"].lower() or
                q in r["cultural_significance"].lower()
            ):
                results.append(r)
        return results

_RITUAL_MGR = RitualManager()

def list_rituals() -> List[Dict[str, Any]]:
    """List all documented traditional Kokborok rituals."""
    return _RITUAL_MGR.all_rituals()

def get_ritual(ritual_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve ritual details by ID or name (e.g. 'chukbar', 'risa_sormani', 'ochai_priesthood')."""
    return _RITUAL_MGR.get_ritual(ritual_id)

def search_rituals(query: str) -> List[Dict[str, Any]]:
    """Search rituals by keyword."""
    return _RITUAL_MGR.search(query)
