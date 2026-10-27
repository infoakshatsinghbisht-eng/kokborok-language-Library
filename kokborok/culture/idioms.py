# -*- coding: utf-8 -*-
"""
Kokborok Idioms, Metaphorical Expressions & Cultural Wisdom (Kok-Hajakma).
========================================================================

Collection of classical and conversational Kokborok idioms derived from daily
agrarian life, hill navigation, and human nature.
"""

from typing import Dict, List, Any, Optional

IDIOMS: List[Dict[str, Any]] = [
    {
        "idiom": "Dangai pho bokha bising kabo",
        "literal": "Even while bearing pain, the inner heart weeps",
        "meaning": "True sufferers deeply empathize with and realize the silent sorrows of others.",
        "usage": "Invoked when someone demonstrates profound compassion during bereavement."
    },
    {
        "idiom": "Beng-nog beng nango",
        "literal": "The one who digs a pit gets caught in it",
        "meaning": "He who plots malicious traps or deception for others inevitably falls into his own snare.",
        "usage": "Warns against plotting deceit or betrayal."
    },
    {
        "idiom": "Siyari bai twima ongia",
        "literal": "A great flowing river cannot be constructed from mere morning fog",
        "meaning": "Substance and genuine character matter over hollow talk; superficial words cannot accomplish great deeds.",
        "usage": "Reminding boastful people that actions speak louder than empty promises."
    },
    {
        "idiom": "Sa haya hai bithi rukh",
        "literal": "Administering herbal medicine strictly matching the specific illness",
        "meaning": "Delivering precisely the right remedy or decisive solution to solve a complex dilemma.",
        "usage": "Praising a wise judge or mediator for an exact resolution."
    },
    {
        "idiom": "Khorok-o thung-o",
        "literal": "Walking with the head held stubbornly high in the clouds",
        "meaning": "Excessively proud, arrogant, haughty, or stubborn; refusing wise counsel.",
        "usage": "Describing someone whose arrogance alienates neighbors."
    },
    {
        "idiom": "Mwsakhoro bwkhorok",
        "literal": "Having a hornet's nest in the head",
        "meaning": "Extremely short-tempered, irritable, quick to flare up in uncontrollable anger.",
        "usage": "Advising others to approach an angry individual with caution."
    },
    {
        "idiom": "Kok lam rwngya",
        "literal": "Not knowing the pathway of words",
        "meaning": "Speechless with astonishment, stunned into silence, or lacking conversational tact.",
        "usage": "Expressing utter shock or surprise upon hearing extraordinary news."
    },
    {
        "idiom": "Bukha kwrwi borok",
        "literal": "A person devoid of a heart",
        "meaning": "Cruel, cold-hearted, or completely insensitive to communal suffering.",
        "usage": "Condemning ruthless or merciless behavior."
    },
    {
        "idiom": "Hachuk son-wi mai chá",
        "literal": "Clearing the high mountain before tasting rice",
        "meaning": "No achievement comes without persistent, arduous labor; success demands sweat.",
        "usage": "Encouraging young students and farmers to endure initial hardships."
    },
    {
        "idiom": "Twima bai khak-laiya",
        "literal": "Unseverable like the flowing waters of a river",
        "meaning": "Indissoluble bond of friendship, clan solidarity, or true marital love.",
        "usage": "Celebrating lifetime loyalty between kindred families."
    }
]

class IdiomManager:
    """Manager for querying and searching Kokborok idioms and cultural sayings."""

    def __init__(self):
        self._idioms = IDIOMS

    def all_idioms(self) -> List[Dict[str, Any]]:
        return list(self._idioms)

    def count(self) -> int:
        return len(self._idioms)

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for i in self._idioms:
            if (
                q in i["idiom"].lower() or
                q in i["literal"].lower() or
                q in i["meaning"].lower() or
                q in i["usage"].lower()
            ):
                results.append(i)
        return results

_IDIOM_MGR = IdiomManager()

def list_idioms() -> List[Dict[str, Any]]:
    """List all documented Kokborok idioms."""
    return _IDIOM_MGR.all_idioms()

def search_idioms(query: str) -> List[Dict[str, Any]]:
    """Search idioms by keyword."""
    return _IDIOM_MGR.search(query)
