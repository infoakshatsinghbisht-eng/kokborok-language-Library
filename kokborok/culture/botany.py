# -*- coding: utf-8 -*-
"""
Kokborok Indigenous Botany, Forest Flora & Bamboo Culture (Bwphang & Wa).
=========================================================================

Comprehensive documentation of Tripura's rich botanical heritage, indigenous bamboo varieties,
edible wild shoots (Muya), sacred trees, and traditional ethnomedicinal herbs.
"""

from typing import Dict, List, Any, Optional

PLANTS: List[Dict[str, Any]] = [
    {
        "id": "muli_bamboo",
        "kokborok_name": "Muli Wa (Wathwi)",
        "scientific_name": "Melocanna baccifera",
        "category": "Bamboo Species",
        "description": "The dominant, most economically and culturally vital bamboo of Tripura. Features long, smooth, thin-walled culms and large edible berry-like fruits.",
        "traditional_uses": "House construction, wall mats (Dhari), weaving baskets, flute making (Sumui), and culinary shoot extraction (Muya)."
    },
    {
        "id": "barak_bamboo",
        "kokborok_name": "Barak Wa",
        "scientific_name": "Bambusa balcooa",
        "category": "Bamboo Species",
        "description": "A very sturdy, thick-walled, heavy giant bamboo species capable of enduring heavy structural loads.",
        "traditional_uses": "Scaffolding, roof beams, bridge piling over hill streams, heavy boundary palisades."
    },
    {
        "id": "muya",
        "kokborok_name": "Muya (Bwkhwk)",
        "scientific_name": "Tender bamboo shoot",
        "category": "Edible Forest Produce",
        "description": "Young tender bamboo shoots harvested from hill slopes at the onset of monsoon rains.",
        "traditional_uses": "Culinary staple used in Chakhwi, Gudok, and Muya Awandru; deeply rich in dietary fiber and essential minerals."
    },
    {
        "id": "gamari_tree",
        "kokborok_name": "Gamari Bwphang",
        "scientific_name": "Gmelina arborea",
        "category": "Sacred Forest Tree",
        "description": "Prized indigenous hardwood tree with golden-yellow timber that resists rot and insect attack.",
        "traditional_uses": "Carving the Kham drum body, ceremonial altars (Wathop), royal furniture, and temple pillars."
    },
    {
        "id": "agarwood",
        "kokborok_name": "Agar Bwphang",
        "scientific_name": "Aquilaria malaccensis",
        "category": "Precious Aromatic Flora",
        "description": "Tripura's legendary 'Liquid Gold' aromatic tree. Undergoes natural resinous heartwood formation producing the world's finest agar oil and oud incense.",
        "traditional_uses": "Traditional perfumery, spiritual purification, ancient medicine, and royal trade."
    },
    {
        "id": "chundri",
        "kokborok_name": "Chundri Bwphang",
        "scientific_name": "Clerodendrum colebrookianum",
        "category": "Ethnomedicinal Herb",
        "description": "Indigenous wild shrub known for broad pungent leaves celebrated in Tripuri ethnomedicine.",
        "traditional_uses": "Boiled leaves eaten to naturally regulate high blood pressure and soothe gastrointestinal ailments."
    },
    {
        "id": "lairu_leaf",
        "kokborok_name": "Lairu Lai",
        "scientific_name": "Phrynium pubinerve",
        "category": "Wrapping Leaf Flora",
        "description": "Large, pliable, fragrant wild forest leaves harvested from moist shaded stream valleys.",
        "traditional_uses": "Wrapping sticky rice for Awan Bangui cakes, packing food for forest journeys, and eco-friendly feast platters."
    }
]

class BotanyManager:
    """Manager for querying indigenous Tripuri botanical species and flora."""

    def __init__(self):
        self._plants = PLANTS

    def all_plants(self) -> List[Dict[str, Any]]:
        return list(self._plants)

    def count(self) -> int:
        return len(self._plants)

    def get_plant(self, plant_id: str) -> Optional[Dict[str, Any]]:
        pid = plant_id.lower().strip()
        for p in self._plants:
            if p["id"] == pid or pid in p["kokborok_name"].lower() or pid in p["scientific_name"].lower():
                return p
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for p in self._plants:
            if (
                q in p["kokborok_name"].lower() or
                q in p["scientific_name"].lower() or
                q in p["category"].lower() or
                q in p["description"].lower() or
                q in p["traditional_uses"].lower()
            ):
                results.append(p)
        return results

_BOTANY_MGR = BotanyManager()

def list_plants() -> List[Dict[str, Any]]:
    """List all documented indigenous Tripuri botanical species."""
    return _BOTANY_MGR.all_plants()

def get_plant(plant_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve botanical information by ID or Kokborok name (e.g. 'muli_bamboo', 'muya', 'agarwood')."""
    return _BOTANY_MGR.get_plant(plant_id)

def search_plants(query: str) -> List[Dict[str, Any]]:
    """Search flora by keyword."""
    return _BOTANY_MGR.search(query)
