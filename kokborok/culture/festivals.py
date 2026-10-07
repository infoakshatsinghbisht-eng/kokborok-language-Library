# -*- coding: utf-8 -*-
"""Traditional Kokborok / Tripuri Festivals and Sacred Rituals."""

from typing import Dict, List, Optional, Any

KOKBOROK_FESTIVALS: List[Dict[str, Any]] = [
    {
        "name": "Garia Puja",
        "native": "Baba Garia Puja",
        "season": "Chaitra Sankranti / Baisakh",
        "description": "The supreme agricultural and prosperity festival dedicated to Baba Garia. Marked by the holy Garia bamboo pole, communal dancing, and sacrifice for bumper crops and peace.",
        "category": "major_ritual"
    },
    {
        "name": "Kharchi Puja",
        "native": "Chaturdash Devata Puja",
        "season": "Ashadha (July)",
        "description": "The sacred cleansing and purification of the 14 Gods (Chaturdash Devata) at Old Agartala. Symbolizes the purification of Mother Earth (Ama Twima / Basumati) following the monsoon.",
        "category": "state_heritage"
    },
    {
        "name": "Ker Puja",
        "native": "Ker Puja",
        "season": "August (Fortnight after Kharchi)",
        "description": "Strict boundary-locking ritual performed for communal defense, protection from calamity, and state sanctification.",
        "category": "sacred_boundary"
    },
    {
        "name": "Hojagiri",
        "native": "Hojagiri Sal",
        "season": "Laxmi Puja (Ashvin)",
        "description": "Celebrated by the Reang (Bru) community honoring Goddess Mailuma. Acclaimed worldwide for its stunning acrobatic balancing dances upon earthen pitchers with lit lamps.",
        "category": "dance_harvest"
    },
    {
        "name": "Mamita",
        "native": "Mamita Phunukma",
        "season": "Post-Harvest (Kartika / Agrahayana)",
        "description": "Traditional new-harvest festival with feasting on fresh rice, folk songs (Koktwma), and thanksgiving to Mailuma (Goddess of Grain) and Khuluma (Goddess of Cotton).",
        "category": "harvest"
    },
    {
        "name": "Lampra Puja",
        "native": "Lampra Wathop",
        "season": "All auspicious occasions",
        "description": "Foundational ritual propitiating the twin deities of Sky and Ocean before initiating marriages, journeys, and agriculture.",
        "category": "foundational"
    }
]

def list_festivals() -> List[Dict[str, Any]]:
    return KOKBOROK_FESTIVALS

def get_festival(name: str) -> Optional[Dict[str, Any]]:
    n = name.lower().strip()
    for f in KOKBOROK_FESTIVALS:
        if n in f["name"].lower() or n in f["native"].lower():
            return f
    return None
