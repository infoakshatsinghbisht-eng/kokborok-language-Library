# -*- coding: utf-8 -*-
"""
Kokborok Traditional Attire, Handloom Textiles, and Weaving Heritage.
=====================================================================

Comprehensive documentation of Tripuri traditional garments, loin-loom weaving traditions,
cultural rituals like Risa Sormani, and tribal textile motifs of Tripura.
"""

from typing import Dict, List, Any, Optional

TRADITIONAL_GARMENTS: List[Dict[str, Any]] = [
    {
        "id": "rignai",
        "name": "Rignai (Rigwani)",
        "english_name": "Traditional Wrap-Around Lower Skirt",
        "gender": "female",
        "category": "garment",
        "type": "lower_wear",
        "materials": ["Locally spun cotton", "Natural dyed silk", "Acrylic thread"],
        "description": "The quintessential traditional lower garment of Tripuri women. A handwoven rectangular piece of fabric wrapped snugly around the waist down to the ankles.",
        "cultural_significance": "A woman's clan, lineage, and artistic mastery were historically recognized immediately by the unique patterns and borders of her Rignai.",
        "occasions": ["Daily wear", "Weddings", "Garia Puja", "Kharchi Puja", "Kokborok Day celebrations"]
    },
    {
        "id": "risa",
        "name": "Risa",
        "english_name": "Handwoven Upper Bust Wrap / Ceremonial Stole",
        "gender": "unisex",
        "category": "garment",
        "type": "upper_wear / ceremonial stole",
        "materials": ["Indigenous cotton", "Multi-colored silk threads"],
        "description": "A narrow, finely patterned handwoven cloth used by women as an upper bust cover, and by men as a ceremonial turban, waist sash, or honorary muffler.",
        "cultural_significance": "Central to the 'Risa Sormani' adolescent rite of passage where young girls aged 12-14 receive their first Risa. Awarded as the supreme symbol of Tripuri honor.",
        "occasions": ["Risa Sormani ritual", "Garia dance", "Felicitations", "Royal ceremonies", "Weddings"]
    },
    {
        "id": "rikutu",
        "name": "Rikutu (Rituku)",
        "english_name": "Traditional Upper Draping Shawl",
        "gender": "female",
        "category": "garment",
        "type": "upper_drape",
        "materials": ["Cotton", "Warm eri silk / wool mix"],
        "description": "A broader handwoven shawl draped gracefully across the upper body, over the shoulders and head, worn over the Risa for warmth and modest elegance.",
        "cultural_significance": "Worn by married women during visits to elder kin, sacred temples, and formal gatherings as a mark of respect and dignity.",
        "occasions": ["Formal visits", "Temple worship at Matabari", "Winter wear", "Wedding ceremonies"]
    },
    {
        "id": "kamchwlwi",
        "name": "Kamchwlwi borok",
        "english_name": "Men's Traditional Loin Wrap & Dhoti",
        "gender": "male",
        "category": "garment",
        "type": "lower_wear",
        "materials": ["Pure white or off-white coarse cotton"],
        "description": "Traditional lower loin cloth or short dhoti worn by Tripuri men, folded comfortably above the knees for agile mountain work and dance.",
        "cultural_significance": "Represents the agility and agrarian pride of jhum cultivators and dancers during the Garia festival.",
        "occasions": ["Garia festival dance", "Harvesting", "Jhum field cultivation", "Community gatherings"]
    },
    {
        "id": "takborok",
        "name": "Takborok (Khabang)",
        "english_name": "Traditional Headgear / Turban",
        "gender": "male",
        "category": "headwear",
        "type": "ceremonial",
        "materials": ["Handwoven cotton / Risa fabric"],
        "description": "A colorful handwoven cloth skillfully tied into a turban around the head, often adorned with cock feathers or wild flowers during festive dances.",
        "cultural_significance": "Worn by village chiefs (Choudhury), priests (Ochai), and dancers leading the Garia procession.",
        "occasions": ["Garia Puja", "Chukbar marriage rites", "Council meetings"]
    }
]

WEAVING_MOTIFS: List[Dict[str, Any]] = [
    {
        "name": "Chamathwi Bar",
        "english_meaning": "White base with red/maroon floral border",
        "symbolism": "Purity, royal ancestry, and fertility; the most prestigious motif in Tripuri weaving.",
        "used_in": ["Rignai Chamathwi", "Wedding attire", "Garia celebration wraps"]
    },
    {
        "name": "Kumpilak Bar",
        "english_meaning": "Butterfly wing geometry",
        "symbolism": "Grace, joyful movement, and feminine beauty in the spring bloom.",
        "used_in": ["Risa borders", "Festival shawls"]
    },
    {
        "name": "Thaichu Bar",
        "english_meaning": "Mango blossom and sprout design",
        "symbolism": "Abundant harvest, sweet fortune, and prosperous home life.",
        "used_in": ["Rignai patterns", "Gift stoles"]
    },
    {
        "name": "Takhor",
        "english_meaning": "Traditional loin-loom (backstrap loom)",
        "symbolism": "The wooden loin-loom found in every traditional Tripuri home where women practice indigenous weaving art.",
        "used_in": ["Domestic textile craft"]
    }
]

class AttireManager:
    """Manager for querying and searching Kokborok traditional garments and textile heritage."""

    def __init__(self):
        self._garments = TRADITIONAL_GARMENTS
        self._motifs = WEAVING_MOTIFS

    def all_garments(self) -> List[Dict[str, Any]]:
        return list(self._garments)

    def all_motifs(self) -> List[Dict[str, Any]]:
        return list(self._motifs)

    def get_garment(self, garment_id: str) -> Optional[Dict[str, Any]]:
        gid = garment_id.lower().strip()
        for g in self._garments:
            if g["id"] == gid or g["name"].lower().startswith(gid):
                return g
        return None

    def by_gender(self, gender: str) -> List[Dict[str, Any]]:
        g_low = gender.lower().strip()
        return [g for g in self._garments if g["gender"] == g_low or g["gender"] == "unisex"]

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for g in self._garments:
            if (
                q in g["name"].lower() or
                q in g["english_name"].lower() or
                q in g["description"].lower() or
                q in g["cultural_significance"].lower()
            ):
                results.append(g)
        return results

_ATTIRE_MGR = AttireManager()

def list_attire() -> List[Dict[str, Any]]:
    """List all documented traditional Tripuri garments."""
    return _ATTIRE_MGR.all_garments()

def get_attire(garment_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve garment details by ID or name (e.g. 'rignai', 'risa', 'rikutu')."""
    return _ATTIRE_MGR.get_garment(garment_id)

def list_motifs() -> List[Dict[str, Any]]:
    """List traditional Tripuri handloom weaving motifs."""
    return _ATTIRE_MGR.all_motifs()
