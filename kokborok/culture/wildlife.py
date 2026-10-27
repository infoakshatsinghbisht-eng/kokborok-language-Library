# -*- coding: utf-8 -*-
"""
Kokborok Indigenous Fauna & Wildlife Heritage (Kwtwi-rok).
=========================================================

Documentation of Tripura's native wildlife, state symbols, mountain mammals,
birds, and river fish with their authentic Kokborok zoological names.
"""

from typing import Dict, List, Any, Optional

FAUNA: List[Dict[str, Any]] = [
    {
        "id": "phayres_langur",
        "kokborok_name": "Chashma Mwkhra",
        "english_name": "Phayre's Leaf Monkey (Spectacled Langur)",
        "scientific_name": "Trachypithecus phayrei",
        "category": "State Animal of Tripura",
        "description": "An endangered arboreal primate distinguished by prominent white ring patches around the dark eyes resembling spectacles. Inhabits mixed primary evergreen and bamboo forests of Sepahijala and Trishna.",
        "cultural_significance": "Revered in folk tales for intelligence and playful canopy movement."
    },
    {
        "id": "green_imperial_pigeon",
        "kokborok_name": "Dukung (Daokhung)",
        "english_name": "Green Imperial Pigeon",
        "scientific_name": "Ducula aenea",
        "category": "State Bird of Tripura",
        "description": "A magnificent large forest pigeon with iridescent emerald-green plumage, pearl-grey breast, and a deep booming call reverberating through primary canopies.",
        "cultural_significance": "Its deep call signals the changing of seasons in high hill villages."
    },
    {
        "id": "hoolock_gibbon",
        "kokborok_name": "Hulok Mwkhra",
        "english_name": "Western Hoolock Gibbon",
        "scientific_name": "Hoolock hoolock",
        "category": "Ape / Primate",
        "description": "India's only native ape species, famed for loud territorial duets echoing across the morning mist in Gumti and Sepahijala Wildlife Sanctuaries.",
        "cultural_significance": "A symbol of pristine old-growth rainforests in tribal folklore."
    },
    {
        "id": "clouded_leopard",
        "kokborok_name": "Mwsakhoro (Mwsa)",
        "english_name": "Clouded Leopard",
        "scientific_name": "Neofelis nebulosa",
        "category": "Big Cat / Predator",
        "description": "A secretive, master arboreal feline with beautiful cloud-like rosettes and disproportionately long canines roaming the forested ridges of Clouded Leopard National Park.",
        "cultural_significance": "Regarded as the stealthiest hunter of the mountain forests; invoked in heroic proverbs."
    },
    {
        "id": "bison_gaur",
        "kokborok_name": "Mwsal (Mwsai)",
        "english_name": "Indian Bison (Gaur)",
        "scientific_name": "Bos gaurus",
        "category": "Herbivore",
        "description": "The largest extant bovine species in the world, thriving in large herds inside Trishna Wildlife Sanctuary in South Tripura.",
        "cultural_significance": "A symbol of immense physical strength and quiet dignity."
    },
    {
        "id": "puthi_fish",
        "kokborok_name": "Punti A (A-sa)",
        "english_name": "Spotted Barb / Freshwater Puthi",
        "scientific_name": "Puntius sophore",
        "category": "Freshwater Fish",
        "description": "Abundant small silver freshwater fish harvested from clean hill streams and rivers.",
        "cultural_significance": "The primary fish species salted, sun-dried, and traditionally fermented in earthen vats to create Berma."
    }
]

class WildlifeManager:
    """Manager for querying indigenous Tripuri fauna and native animals."""

    def __init__(self):
        self._fauna = FAUNA

    def all_fauna(self) -> List[Dict[str, Any]]:
        return list(self._fauna)

    def count(self) -> int:
        return len(self._fauna)

    def get_animal(self, animal_id: str) -> Optional[Dict[str, Any]]:
        aid = animal_id.lower().strip()
        for a in self._fauna:
            if a["id"] == aid or aid in a["kokborok_name"].lower() or aid in a["english_name"].lower():
                return a
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for a in self._fauna:
            if (
                q in a["kokborok_name"].lower() or
                q in a["english_name"].lower() or
                q in a["scientific_name"].lower() or
                q in a["category"].lower() or
                q in a["description"].lower()
            ):
                results.append(a)
        return results

_WILDLIFE_MGR = WildlifeManager()

def list_wildlife() -> List[Dict[str, Any]]:
    """List all documented native fauna of Tripura."""
    return _WILDLIFE_MGR.all_fauna()

def get_wildlife(animal_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve fauna details by ID or name (e.g. 'phayres_langur', 'green_imperial_pigeon')."""
    return _WILDLIFE_MGR.get_animal(animal_id)

def search_wildlife(query: str) -> List[Dict[str, Any]]:
    """Search wildlife by keyword."""
    return _WILDLIFE_MGR.search(query)
