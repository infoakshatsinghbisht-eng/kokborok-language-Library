# -*- coding: utf-8 -*-
"""Kokborok Traditional Kinship Roles and Clan Structure."""

from typing import Dict, List, Optional, Any

KINSHIP_TERMS: Dict[str, Dict[str, str]] = {
    "ama": {"kokborok": "Ama", "english": "Mother", "hindi": "माँ", "bengali": "মা", "role": "Matriarch / life-giver"},
    "apha": {"kokborok": "Apha", "english": "Father", "hindi": "पिता", "bengali": "বাবা", "role": "Patriarch / provider"},
    "achu": {"kokborok": "Achu", "english": "Grandfather", "hindi": "दादा / नाना", "bengali": "দাদা / নানা", "role": "Elder patriarch"},
    "aywi": {"kokborok": "Aywi", "english": "Grandmother", "hindi": "दादी / नानी", "bengali": "দাদি / নানি", "role": "Elder matriarch"},
    "atai": {"kokborok": "Atai", "english": "Elder Brother", "hindi": "बड़ा भाई", "bengali": "বড় ভাই", "role": "Senior sibling"},
    "anwi": {"kokborok": "Anwi", "english": "Elder Sister", "hindi": "बड़ी बहन", "bengali": "বড় বোন", "role": "Senior female sibling"},
    "phaywng": {"kokborok": "Phaywng", "english": "Younger Brother", "hindi": "छोटा भाई", "bengali": "ছোট ভাই", "role": "Junior male sibling"},
    "bwby": {"kokborok": "Bwby", "english": "Younger Sister", "hindi": "छोटी बहन", "bengali": "ছোট বোন", "role": "Junior female sibling"},
    "bwsajla": {"kokborok": "Bwsajla", "english": "Son", "hindi": "बेटा / पुत्र", "bengali": "ছেলে / পুত্র", "role": "Offspring (male)"},
    "bwsajwk": {"kokborok": "Bwsajwk", "english": "Daughter", "hindi": "बेटी / पुत्री", "bengali": "মেয়ে / কন্যা", "role": "Offspring (female)"},
    "bwsai": {"kokborok": "Bwsai", "english": "Husband", "hindi": "पति", "bengali": "স্বামী", "role": "Spouse (male)"},
    "bihik": {"kokborok": "Bihik", "english": "Wife", "hindi": "पत्नी", "bengali": "স্ত্রী", "role": "Spouse (female)"}
}

def list_kinship_terms() -> List[Dict[str, str]]:
    return list(KINSHIP_TERMS.values())

def get_kinship_term(key: str) -> Optional[Dict[str, str]]:
    return KINSHIP_TERMS.get(key.lower().strip())
