# -*- coding: utf-8 -*-
"""
Kokborok Musical Instruments, Folk Music & Dance Heritage (Rwchapmung & Mwsamung).
===================================================================================

Documentation of traditional Tripuri musical instruments (Kham, Sumui, Sarinda, Chongpreng, Dangdu)
and world-renowned indigenous folk dance forms like Hojagiri, Garia, and Lebang Boomani.
"""

from typing import Dict, List, Any, Optional

INSTRUMENTS: List[Dict[str, Any]] = [
    {
        "id": "kham",
        "name": "Kham (Kham Kotor)",
        "type": "Membranophone (Double-headed Barrel Drum)",
        "materials": ["Hollowed timber (Gamari or jackfruit wood)", "Tightly stretched cow or goat hide", "Cane lacings"],
        "description": "The heartbeat of Tripuri rhythm. A double-headed cylindrical wooden drum slung over the shoulder and beaten with hands or bamboo drumsticks to produce thunderous bass and sharp treble tones.",
        "cultural_context": "Drives the rhythm of Garia Puja processions, Hojagiri dance, and community festive dances."
    },
    {
        "id": "sumui",
        "name": "Sumui",
        "type": "Aerophone (Side-blown Bamboo Flute)",
        "materials": ["Fine, mature thin-walled bamboo (Muli bamboo)", "Seven finger holes"],
        "description": "The iconic traditional bamboo flute of Tripura, celebrated for its sweet, evocative, melancholic tone that carries across mountain ridges.",
        "cultural_context": "Associated with romantic pastoral melodies, Jaduni folk ballads, and evening relaxation around the hearth."
    },
    {
        "id": "sarinda",
        "name": "Sarinda",
        "type": "Chordophone (Bowed Folk Lute / Fiddle)",
        "materials": ["Carved hardwood soundbox with hollowed lower waist", "Parchment skin belly", "Three gut/steel strings", "Horsehair bow"],
        "description": "A traditional bowed string instrument producing an extraordinarily soulful, expressive, human-voice-like resonance.",
        "cultural_context": "Accompanies wandering balladeers, village storytellers, and classical wedding ceremonies."
    },
    {
        "id": "chongpreng",
        "name": "Chongpreng",
        "type": "Chordophone (Plucked Folk Lute)",
        "materials": ["Hollow seasoned bamboo tube or gourd resonator", "Two or three strings", "Bone or wooden bridge"],
        "description": "An ancient plucked chordophone related to the dotara/ektara, played with rhythmic plucking strokes to maintain melodic tempo.",
        "cultural_context": "Played by elders singing oral histories, humorous ballads, and festive social gatherings."
    },
    {
        "id": "dangdu",
        "name": "Dangdu",
        "type": "Idiophone (Bamboo Jew's Harp / Mouth Harp)",
        "materials": ["A single piece of flexible split bamboo with carved vibrating reed tongue"],
        "description": "Held between the teeth or lips while plucking the protruding bamboo tongue; the oral cavity acts as a variable resonator producing pulsating, twanging sounds.",
        "cultural_context": "Intimate personal music played in the quiet of the jhum field watchtower (Tong-Ghar)."
    }
]

DANCE_FORMS: List[Dict[str, Any]] = [
    {
        "name": "Hojagiri Dance",
        "community": "Reang (Bru) community",
        "description": "World-famous acrobatic folk dance where female dancers perform mesmerizing movements of the lower body while balancing pitchers on their heads and lighted lamps on bottles.",
        "festival": "Mailuma / Laxmi Puja harvest season"
    },
    {
        "name": "Garia Dance",
        "community": "All Tripuri clans (Debbarma, Jamatia, Reang, Noatia, Kalai)",
        "description": "Vibrant, ecstatic community dance led by youth chanting and drumming in praise of Baba Garia, moving rhythmically from house to house across the entire village.",
        "festival": "Garia Puja (April)"
    },
    {
        "name": "Lebang Boomani Dance",
        "community": "Tripuri hill farmers",
        "description": "Harvest dance depicting the joyful catching of green 'Lebang' insects (crickets) that flock to jhum fields during monsoon, using two clacking bamboo sticks.",
        "festival": "Monsoon cultivation season"
    },
    {
        "name": "Mamita Dance",
        "community": "Tripuri community",
        "description": "Celebratory harvest dance honoring the new crop of rice, accompanied by the Kham, Sumui, and singing.",
        "festival": "Mamita festival"
    }
]

class MusicManager:
    """Manager for querying traditional Kokborok musical instruments and dance forms."""

    def __init__(self):
        self._instruments = INSTRUMENTS
        self._dances = DANCE_FORMS

    def all_instruments(self) -> List[Dict[str, Any]]:
        return list(self._instruments)

    def all_dances(self) -> List[Dict[str, Any]]:
        return list(self._dances)

    def get_instrument(self, inst_id: str) -> Optional[Dict[str, Any]]:
        iid = inst_id.lower().strip()
        for i in self._instruments:
            if i["id"] == iid or iid in i["name"].lower():
                return i
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for i in self._instruments:
            if (
                q in i["name"].lower() or
                q in i["type"].lower() or
                q in i["materials"] or
                q in i["description"].lower() or
                q in i["cultural_context"].lower()
            ):
                results.append(i)
        return results

_MUSIC_MGR = MusicManager()

def list_instruments() -> List[Dict[str, Any]]:
    """List all documented traditional Kokborok musical instruments."""
    return _MUSIC_MGR.all_instruments()

def get_instrument(inst_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve musical instrument details by ID or name (e.g. 'kham', 'sumui', 'sarinda')."""
    return _MUSIC_MGR.get_instrument(inst_id)

def list_dances() -> List[Dict[str, Any]]:
    """List traditional Tripuri folk dance forms."""
    return _MUSIC_MGR.all_dances()
