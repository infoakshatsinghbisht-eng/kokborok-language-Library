# -*- coding: utf-8 -*-
"""
Kokborok Folklore, Mythological Narratives & Oral Traditions (Kothoma).
======================================================================

Documentation of foundational Tripuri folk legends, creation myths, oral epics,
and ancestral tales passed down across generations of the Borok community.
"""

from typing import Dict, List, Any, Optional

STORIES: List[Dict[str, Any]] = [
    {
        "id": "chethwang",
        "title": "Chethwang and the Royal Falcon",
        "category": "Heroic Epic / Folk Legend",
        "characters": ["Chethwang", "Royal Falcon", "Tribal Princess", "Forest Spirits"],
        "synopsis": "The epic tale of Chethwang, a valiant Borok youth renowned for bravery, hunter agility, and loyalty to his clan. Through courage and the guidance of an enchanted forest falcon, Chethwang overcomes insurmountable perils in the deep mountain gorges of the Baramura range to deliver his community from famine and darkness.",
        "moral": "Courage, righteousness, and living in spiritual harmony with nature and creatures of the forest overcome all hardship."
    },
    {
        "id": "subrai_creation",
        "title": "Subrai and the Creation of the Hills",
        "category": "Cosmological Creation Myth",
        "characters": ["Subrai (Lord Shiva)", "Ama (Mother Earth)", "Early Borok ancestors"],
        "synopsis": "In the primeval era when waters covered the earth, Subrai commanded the great subterranean creatures to heave the earth upwards, sculpting the six parallel mountain ranges of Tripura (Jampui, Sakhan, Longtharai, Atharamura, Baramura, and Deotamura). He gifted the Borok ancestors fire, the bamboo stalk, and the knowledge of jhum agriculture.",
        "moral": "Respect the mountain ranges as living beings and treat the soil with reverence through cyclical fallow."
    },
    {
        "id": "haithathorani",
        "title": "Haithathorani (The Mountain Maiden of the Passes)",
        "category": "Romantic Folk Lore",
        "characters": ["Haitha", "Young Flute Player", "Clan Elders"],
        "synopsis": "A touching romantic legend set in the high windswept pass of Haithathora. A young maiden falls in love with a shepherd whose haunting Sumui (bamboo flute) melodies echo through the misty valleys. Their enduring devotion became immortalized in countless Jaduni folk ballads sung by young lovers during the harvest moon.",
        "moral": "True love transcends mortal boundaries and endures forever in folk melody."
    },
    {
        "id": "dumbur_legend",
        "title": "The Legend of Dumbur Falls and the Sacred Confluence",
        "category": "Sacred Geography Legend",
        "characters": ["River Mother Tuibuma", "Sacred Ox", "Jamatia Pilgrims"],
        "synopsis": "Where the Raima and Sarma mountain streams merge to birth the great Gomati River, the waters churn over rock formations shaped like Lord Shiva's small tabor drum (Dumbur). Legend recounts how an ancient white bull was blessed by the water goddess, creating 48 emerald islets where migratory birds rest during the winter sun.",
        "moral": "Water is sacred; the confluence of life-giving rivers must be preserved with clean worship."
    },
    {
        "id": "champaknagar",
        "title": "The Chronicles of Ancient Champaknagar",
        "category": "Historical Ancestral Lore",
        "characters": ["King Trilochan", "Royal Ministers", "Ochai Shaman"],
        "synopsis": "Recounts the glorious migration of the early Borok tribes from the ancient ancestral capital of Champaknagar to the fertile valleys of Tripura, establishing peace with indigenous clans and building fortified settlements guarded by bamboo stockades.",
        "moral": "Unity among clans forms an unshakeable shield against adversity."
    }
]

class FolkloreManager:
    """Manager for querying and searching Kokborok folklore and traditional legends."""

    def __init__(self):
        self._stories = STORIES
        self._by_id = {s["id"]: s for s in self._stories}

    def all_stories(self) -> List[Dict[str, Any]]:
        return list(self._stories)

    def count(self) -> int:
        return len(self._stories)

    def get_story(self, story_id: str) -> Optional[Dict[str, Any]]:
        sid = story_id.lower().strip()
        for s in self._stories:
            if s["id"] == sid or sid in s["title"].lower():
                return s
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for s in self._stories:
            if (
                q in s["title"].lower() or
                q in s["category"].lower() or
                q in s["synopsis"].lower() or
                q in s["moral"].lower() or
                any(q in c.lower() for c in s["characters"])
            ):
                results.append(s)
        return results

_FOLKLORE_MGR = FolkloreManager()

def list_folklore() -> List[Dict[str, Any]]:
    """List all catalogued Kokborok folk stories and legends."""
    return _FOLKLORE_MGR.all_stories()

def get_story(story_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve story details by ID or title (e.g. 'chethwang', 'dumbur_legend')."""
    return _FOLKLORE_MGR.get_story(story_id)

def search_folklore(query: str) -> List[Dict[str, Any]]:
    """Search folklore by keyword."""
    return _FOLKLORE_MGR.search(query)
