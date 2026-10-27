# -*- coding: utf-8 -*-
"""
Tripuri Spiritual Pantheon, Indigenous Deities & Sacred Lore (Mwtai).
====================================================================

Comprehensive documentation of the indigenous Tripuri deities, animistic nature gods,
ancestral guardians, and the Chaturdasha Devata (14 Gods) pantheon.
"""

from typing import Dict, List, Any, Optional

DEITIES: List[Dict[str, Any]] = [
    {
        "name": "Subrai (Shibrai / Burasa)",
        "id": "subrai",
        "realm": "Supreme Patriarch / Cosmos & Forest",
        "description": "The supreme primordial god and patriarch of Tripuri cosmology. Associated with cosmic creation, the high mountains, and wisdom; syncretized as Lord Shiva in the 14 Gods.",
        "sacred_symbols": ["Bamboo Wathop altar", "Forest hills", "Sacred fire"],
        "festival": "Kharchi Puja, Shivaratri"
    },
    {
        "name": "Baba Garia (Goria)",
        "id": "garia",
        "realm": "Lord of Livestock, Harvest, Fertility & Peace",
        "description": "The most beloved guardian deity of the Tripuri people. Celebrated during the grand seven-day Garia festival marking the beginning of the jhum cultivation cycle.",
        "sacred_symbols": ["Garia bamboo pole tied with thread, cotton, and rooster feathers", "Sacred pitcher"],
        "festival": "Garia Puja (Chaitra Sankranti / April)"
    },
    {
        "name": "Mailuma",
        "id": "mailuma",
        "realm": "Goddess of Corn, Agriculture & Harvest",
        "description": "The benevolent goddess personifying rice, paddy, and harvest abundance. Revering her ensures that granaries remain overflowing throughout the year.",
        "sacred_symbols": ["Earthen pot filled with newly harvested rice grain", "Cotton ears"],
        "festival": "Hojagiri, Mamita harvest feast, Mailuma Puja"
    },
    {
        "name": "Khuluma",
        "id": "khuluma",
        "realm": "Goddess of Cotton & Handloom Weaving",
        "description": "The sister goddess to Mailuma, embodying cotton fiber, spinning, and textile protection. Honored by Tripuri women before beginning intricate loom weaving.",
        "sacred_symbols": ["White raw cotton balls", "Loin-loom shuttle (Takhor)"],
        "festival": "Khuluma Puja, alongside Mailuma"
    },
    {
        "name": "Tuibuma (Twibukma / Tuima)",
        "id": "tuibuma",
        "realm": "Goddess of Rivers, Waters & Streams",
        "description": "The great Water Mother personifying all rivers, streams, and life-giving waters of Tripura. Propitiated to prevent water-borne sickness and protect fishermen.",
        "sacred_symbols": ["River confluences", "Fresh water stream offerings"],
        "festival": "Twibuma Puja on river banks"
    },
    {
        "name": "Lampra (Lampra Wathop)",
        "id": "lampra",
        "realm": "Guardian of Heaven & Earth / Household Threshold",
        "description": "A dual deity embodying Akasa (Sky) and Prithvi (Earth). Lampra is obligatorily the very first god propitiated at the start of any lifecycle rite, birth, or wedding.",
        "sacred_symbols": ["Double bamboo altar (Wathop)", "Betel leaf and nut offerings"],
        "festival": "Lampra Puja (preceding all major pujas)"
    },
    {
        "name": "Ker (Vastu Ker)",
        "id": "ker",
        "realm": "Guardian of Territorial Boundary & Calamity Protection",
        "description": "The fierce protective deity worshipped during Ker Puja to seal the village or royal boundaries against epidemics, earthquakes, and invading evil.",
        "sacred_symbols": ["Ker bamboo framework", "Strict 30-hour spatial boundary cordon"],
        "festival": "Ker Puja (two weeks after Kharchi Puja)"
    },
    {
        "name": "Sangrongma",
        "id": "sangrongma",
        "realm": "Goddess of Mountain Passes & Road Protection",
        "description": "Guardian of travelers, mountain pathways, and deep forest treks, protecting voyagers from wild predators and forest spirits.",
        "sacred_symbols": ["Roadside bamboo altars", "Wild flowers"],
        "festival": "Sangrongma Puja"
    },
    {
        "name": "Chaturdasha Devata (14 Royal Gods)",
        "id": "chaturdasha_devata",
        "realm": "The Supreme Royal Pantheon of Tripura",
        "description": "The 14 guardian deities of the Royal Manikya dynasty and all Borok people: Shiva, Durga, Vishnu, Lakshmi, Saraswati, Kartikeya, Ganesha, Brahma, Earth, Water, Fire, Wind, Sky, and Himalaya.",
        "sacred_symbols": ["14 sacred metal heads installed at Old Agartala temple"],
        "festival": "Kharchi Puja (July)"
    }
]

class DeityManager:
    """Manager for querying Tripuri deities, pantheon, and spiritual realms."""

    def __init__(self):
        self._deities = DEITIES
        self._by_id = {d["id"]: d for d in self._deities}

    def all_deities(self) -> List[Dict[str, Any]]:
        return list(self._deities)

    def count(self) -> int:
        return len(self._deities)

    def get_deity(self, deity_id: str) -> Optional[Dict[str, Any]]:
        did = deity_id.lower().strip()
        for d in self._deities:
            if d["id"] == did or did in d["name"].lower():
                return d
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for d in self._deities:
            if (
                q in d["name"].lower() or
                q in d["realm"].lower() or
                q in d["description"].lower() or
                q in d["festival"].lower()
            ):
                results.append(d)
        return results

_DEITY_MGR = DeityManager()

def list_deities() -> List[Dict[str, Any]]:
    """List all documented indigenous Tripuri deities."""
    return _DEITY_MGR.all_deities()

def get_deity(deity_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve deity details by ID or name (e.g. 'subrai', 'garia', 'mailuma', 'lampra')."""
    return _DEITY_MGR.get_deity(deity_id)

def search_deities(query: str) -> List[Dict[str, Any]]:
    """Search deities by keyword."""
    return _DEITY_MGR.search(query)
