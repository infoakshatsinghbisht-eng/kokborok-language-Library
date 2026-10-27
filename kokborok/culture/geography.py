# -*- coding: utf-8 -*-
"""
Kokborok Sacred Geography, Mountains, Rivers & Historical Landmarks (Haphang).
=============================================================================

Documentation of Tripura's sacred geography, parallel mountain ranges, life-giving rivers,
historical capitals, and ancient rock carvings in indigenous Borok tradition.
"""

from typing import Dict, List, Any, Optional

PLACES: List[Dict[str, Any]] = [
    {
        "id": "jampui_hills",
        "name": "Jampui Hills (Jampui Hachuk)",
        "type": "Mountain Range",
        "elevation": "Around 1,000 meters (Betlingshib peak 930m)",
        "description": "The highest mountain range in Tripura, celebrated as the 'Eternal Spring of the Hills'. Famed for cool temperate climate, orange orchards, and panoramic sunrise vistas across the valleys.",
        "cultural_significance": "Home to the Lushai and Reang communities; heart of the annual Orange and Tourism Festival."
    },
    {
        "id": "longtharai",
        "name": "Longtharai Hills (Longtharai Hachuk)",
        "type": "Mountain Range & Sacred Sanctuary",
        "elevation": "Peak approx 480 meters",
        "description": "A dense, forested mountain range bisecting central Tripura, named after the sacred Shiva deity Longtharai (meaning 'Deep Solitude' in Kokborok).",
        "cultural_significance": "Home to ancient rock shrines and pilgrimage sites visited by devotees crossing between Agartala and northern hills."
    },
    {
        "id": "baramura",
        "name": "Baramura (Hatai Kotor)",
        "type": "Mountain Range & Eco-Park",
        "elevation": "Approx 270 meters",
        "description": "Known as 'Hatai Kotor' (Great Hill Pass) in Kokborok. A magnificent lush ridge known for hornbills, bamboo reserves, and traditional hill roads connecting western plains to interior valleys.",
        "cultural_significance": "Immortalized in early Kokborok folk poetry and historical transit legends."
    },
    {
        "id": "atharamura",
        "name": "Atharamura Range",
        "type": "Mountain Range",
        "elevation": "Approx 480 meters",
        "description": "Literally meaning the 'Eighteen-peaked Ridge', this range features dramatic serpentine passes, deep ravines, and wild bamboo canopies.",
        "cultural_significance": "A strategic natural bulwark historically guarding ancient capitals from western invasions."
    },
    {
        "id": "gomati_river",
        "name": "Gomati River (Twima Gomati)",
        "type": "River",
        "origin": "Confluence of Raima and Sarma rivers at Dumbur",
        "description": "The largest and most sacred river of Tripura. Flows westward past Udaipur (ancient Rangamati) before meandering through lush alluvial plains.",
        "cultural_significance": "Venerated as the life-giving Water Mother (Tuibuma); banks host hundreds of sacred shrines, ancient temples, and pilgrimage sites."
    },
    {
        "id": "howrah_river",
        "name": "Howrah River (Saidra / Saura)",
        "type": "River",
        "origin": "Baramura hill range",
        "description": "Known traditionally in Kokborok as 'Saidra'. Flows right through Agartala city and nurtures the agricultural basin of West Tripura.",
        "cultural_significance": "The sacred immersion of the 14 Gods (Chaturdasha Devata) takes place on the banks of Saidra during Kharchi Puja."
    },
    {
        "id": "dumbur_lake",
        "name": "Dumbur Lake & Falls",
        "type": "Waterbody & Sacred Confluence",
        "description": "A picturesque sprawling waterbody with 48 green islets nestled amidst rolling forest hills, named after the holy tabor-drum shape of the rocky falls.",
        "cultural_significance": "Site of the holy Pous Sankranti Mela (Tirthamukh) where thousands take ritual cleansing baths every January."
    },
    {
        "id": "unakoti",
        "name": "Unakoti Heritage Site (Subrai Khorang)",
        "type": "Ancient Rock Carving & Shavite Sanctuary",
        "description": "A primeval pilgrimage site dating from the 7th-9th centuries featuring colossal bas-relief rock carvings of Lord Shiva (Unakotiswara Kal Bhairava, 30 ft high) and deities carved into vertical cliff walls.",
        "cultural_significance": "Means 'one less than a crore' (99,99,999 carvings). Central to Subrai worship and Ashokastami festival."
    },
    {
        "id": "matabari_udaipur",
        "name": "Tripura Sundari Temple (Matabari, Udaipur)",
        "type": "Ancient Shakti Peetha Temple",
        "description": "One of the 51 holy Shakti Peethas (where Sati's right foot fell), founded in 1501 AD by Maharaja Dhanya Manikya alongside the sacred Kalyan Sagar lake containing giant black softshell turtles.",
        "cultural_significance": "Revered equally by all tribal and non-tribal communities of Tripura."
    },
    {
        "id": "neermahal",
        "name": "Neermahal (Water Palace of Rudrasagar)",
        "type": "Royal Palace Architecture",
        "description": "The largest water palace in Eastern India, constructed in 1930 by Maharaja Bir Bikram Kishore Manikya in the center of picturesque Rudrasagar Lake.",
        "cultural_significance": "A masterpiece blending indigenous Tripuri, Hindu, and Mughal architectural idioms."
    },
    {
        "id": "ujjayanta_palace",
        "name": "Ujjayanta Palace (Nok Kotor, Agartala)",
        "type": "Royal Palace & State Museum",
        "description": "Magnificent neoclassical royal palace built in 1901 by Maharaja Radha Kishore Manikya, featuring Mughal-style formal gardens, tiled fountains, and state heritage archives.",
        "cultural_significance": "Named by Nobel laureate Rabindranath Tagore; houses the premier museum of Northeast Indian tribal heritage."
    },
    {
        "id": "pilak",
        "name": "Pilak Archaeological Site",
        "type": "Ancient Buddhist & Hindu Archaeological Complex",
        "description": "Ancient archaeological site in South Tripura dating from the 8th-12th centuries, yielding colossal terracotta plaques, Avalokiteshvara sculptures, and stone images.",
        "cultural_significance": "Testifies to the peaceful historical coexistence of Hinayana/Mahayana Buddhism and indigenous culture."
    }
]

class GeographyManager:
    """Manager for querying Tripura's sacred geography and heritage landmarks."""

    def __init__(self):
        self._places = PLACES

    def all_places(self) -> List[Dict[str, Any]]:
        return list(self._places)

    def count(self) -> int:
        return len(self._places)

    def get_place(self, place_id: str) -> Optional[Dict[str, Any]]:
        pid = place_id.lower().strip()
        for p in self._places:
            if p["id"] == pid or pid in p["name"].lower():
                return p
        return None

    def by_type(self, place_type: str) -> List[Dict[str, Any]]:
        t_low = place_type.lower().strip()
        return [p for p in self._places if t_low in p["type"].lower()]

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for p in self._places:
            if (
                q in p["name"].lower() or
                q in p["type"].lower() or
                q in p["description"].lower() or
                q in p["cultural_significance"].lower()
            ):
                results.append(p)
        return results

_GEO_MGR = GeographyManager()

def list_geography() -> List[Dict[str, Any]]:
    """List all documented sacred geography landmarks of Tripura."""
    return _GEO_MGR.all_places()

def get_place(place_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve geography details by ID or name (e.g. 'unakoti', 'longtharai', 'gomati_river')."""
    return _GEO_MGR.get_place(place_id)

def search_geography(query: str) -> List[Dict[str, Any]]:
    """Search geographical landmarks by keyword."""
    return _GEO_MGR.search(query)
