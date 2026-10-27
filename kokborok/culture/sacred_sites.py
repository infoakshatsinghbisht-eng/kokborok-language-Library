# -*- coding: utf-8 -*-
"""
Kokborok Sacred Sites, Temples & Ancient Shrines (Than & Mwtai Nok).
===================================================================

Documentation of Tripura's sacred pilgrimage shrines, rock-cut bas-relief sanctuaries,
ancient Shakti Peethas, and royal temples of the Manikya Kingdom.
"""

from typing import Dict, List, Any, Optional

SACRED_SITES: List[Dict[str, Any]] = [
    {
        "id": "unakoti_shrine",
        "name": "Unakoti (Subrai Khorang)",
        "location": "Kailashahar, Unakoti District",
        "era": "7th - 9th Century AD",
        "type": "Shaivite Rock-Cut Cliff Sanctuary",
        "description": "Colossal rock bas-reliefs carved directly into the forested hill gorge. Centerpiece is the 30-foot head of Unakotiswara Kal Bhairava, accompanied by Ganga cascading down from Shiva's matted locks.",
        "festival": "Ashokastami Mela in April"
    },
    {
        "id": "tripura_sundari",
        "name": "Tripura Sundari Temple (Matabari)",
        "location": "Udaipur (Ancient Rangamati), Gomati District",
        "era": "1501 AD (founded by Maharaja Dhanya Manikya)",
        "type": "Shakti Peetha Temple",
        "description": "One of the 51 venerable Shakti Peethas where Sati's right foot is believed to have fallen. Built in traditional Bengali 'Charchala' style on a tortoise-shaped hillock beside Kalyan Sagar lake.",
        "festival": "Diwali / Kali Puja grand festival"
    },
    {
        "id": "chaturdasha_devata_temple",
        "name": "Chaturdasha Devata Temple (Fourteen Gods Temple)",
        "location": "Old Agartala (Puran Haveli)",
        "era": "1760 AD (consecrated by Maharaja Krishna Manikya)",
        "type": "Royal Pantheon Temple",
        "description": "The sacred sanctuary housing the 14 royal guardian deities of Tripura. The temple priest (Chantai) is assisted by traditional Ochai shamans.",
        "festival": "Kharchi Puja in July"
    },
    {
        "id": "kasba_kalibari",
        "name": "Kasba Kalibari (Kamalasagar)",
        "location": "Kamalasagar, Sepahijala District, Bangladesh border",
        "era": "15th Century AD (Maharaja Dhanya Manikya)",
        "type": "Hilltop Kali Shrine",
        "description": "Picturesque hilltop temple dedicated to Goddess Mahisamardini (worshiped as Kali) overlooking the vast artificial lake Kamalasagar.",
        "festival": "Navaratri & Chaitra Sankranti Mela"
    },
    {
        "id": "bhubaneswari_temple",
        "name": "Bhubaneswari Temple",
        "location": "Udaipur, Gomati River bank",
        "era": "1660 AD (built by Maharaja Govinda Manikya)",
        "type": "Historic Riverfront Temple",
        "description": "Famous 17th-century brick temple immortalized by Rabindranath Tagore in his celebrated play 'Bisarjan' and novel 'Rajarshi'.",
        "festival": "Durga Puja & Shivaratri"
    },
    {
        "id": "pilak_heritage",
        "name": "Pilak Archaeological Complex",
        "location": "Jolaibari, South Tripura",
        "era": "8th - 12th Century AD",
        "type": "Buddhist & Hindu Archaeological Sanctuary",
        "description": "Sprawling historical site featuring monumental Buddhist stupas, terracotta panels depicting animals and warriors, and rock carvings of Avalokiteshvara.",
        "festival": "State Pilak Festival in December"
    }
]

class SacredSiteManager:
    """Manager for querying Tripura's sacred pilgrimage shrines and heritage temples."""

    def __init__(self):
        self._sites = SACRED_SITES

    def all_sites(self) -> List[Dict[str, Any]]:
        return list(self._sites)

    def count(self) -> int:
        return len(self._sites)

    def get_site(self, site_id: str) -> Optional[Dict[str, Any]]:
        sid = site_id.lower().strip()
        for s in self._sites:
            if s["id"] == sid or sid in s["name"].lower():
                return s
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for s in self._sites:
            if (
                q in s["name"].lower() or
                q in s["location"].lower() or
                q in s["type"].lower() or
                q in s["description"].lower() or
                q in s["festival"].lower()
            ):
                results.append(s)
        return results

_SITE_MGR = SacredSiteManager()

def list_sacred_sites() -> List[Dict[str, Any]]:
    """List all documented sacred shrines and pilgrimage sites in Tripura."""
    return _SITE_MGR.all_sites()

def get_sacred_site(site_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve sacred site details by ID or name (e.g. 'unakoti_shrine', 'tripura_sundari')."""
    return _SITE_MGR.get_site(site_id)

def search_sacred_sites(query: str) -> List[Dict[str, Any]]:
    """Search sacred sites by keyword."""
    return _SITE_MGR.search(query)
