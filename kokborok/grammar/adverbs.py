# -*- coding: utf-8 -*-
"""
Kokborok Adverbs, Modal Particles, and Temporal Qualifiers.
==========================================================

Categorization, classification, and programmatic manipulation of Kokborok adverbs
based on Pushpa Pai Karapurkar (1976) and Binoy Debbarma (2013).
"""

from typing import Dict, List, Any, Optional

ADVERBS: List[Dict[str, Any]] = [
    # Time (Sal / Somoi)
    {"kokborok": "tini", "english": "today", "hindi": "आज", "bengali": "আজ", "category": "time"},
    {"kokborok": "khorang", "english": "tomorrow", "hindi": "कल (आने वाला)", "bengali": "আগামীকাল", "category": "time"},
    {"kokborok": "mwnak", "english": "yesterday", "hindi": "कल (बीता हुआ)", "bengali": "গতকাল", "category": "time"},
    {"kokborok": "da-phang", "english": "now / immediately", "hindi": "अब / तुरंत", "bengali": "এখন", "category": "time"},
    {"kokborok": "ulo", "english": "afterwards / later", "hindi": "बाद में", "bengali": "পরে", "category": "time"},
    {"kokborok": "swkang", "english": "earlier / beforehand", "hindi": "पहले", "bengali": "আগে", "category": "time"},
    {"kokborok": "sal-brwm", "english": "daily / always", "hindi": "रोज़ / हमेशा", "bengali": "প্রতিদিন", "category": "time"},
    {"kokborok": "ahai-phang", "english": "at that time / then", "hindi": "तब", "bengali": "তখন", "category": "time"},
    {"kokborok": "jora-o", "english": "in due time / punctually", "hindi": "समय पर", "bengali": "সময়ে", "category": "time"},

    # Place & Direction (Haphang)
    {"kokborok": "oro", "english": "here", "hindi": "यहाँ", "bengali": "এখানে", "category": "place"},
    {"kokborok": "aphoro", "english": "there", "hindi": "वहाँ", "bengali": "সেখানে", "category": "place"},
    {"kokborok": "saha", "english": "upwards / above", "hindi": "ऊपर", "bengali": "উপরে", "category": "direction"},
    {"kokborok": "kolo", "english": "downwards / below", "hindi": "नीचे", "bengali": "নিচে", "category": "direction"},
    {"kokborok": "gok-thang", "english": "eastwards (where sun rises)", "hindi": "पूर्व की ओर", "bengali": "পূর্ব দিকে", "category": "direction"},
    {"kokborok": "sal-glaima", "english": "westwards (where sun sets)", "hindi": "पश्चिम की ओर", "bengali": "পশ্চিম দিকে", "category": "direction"},
    {"kokborok": "bising-o", "english": "inside / within", "hindi": "अंदर", "bengali": "ভিতরে", "category": "place"},
    {"kokborok": "hangcho-o", "english": "outside", "hindi": "बाहर", "bengali": "বাইরে", "category": "place"},

    # Manner (Wai)
    {"kokborok": "kaham-twi", "english": "well / properly", "hindi": "अच्छी तरह से", "bengali": "ভালোভাবে", "category": "manner"},
    {"kokborok": "kwrak-twi", "english": "loudly / forcefully", "hindi": "ज़ोर से", "bengali": "জোরে", "category": "manner"},
    {"kokborok": "phwlwng-twi", "english": "swiftly / rapidly", "hindi": "तेज़ी से", "bengali": "দ্রুত", "category": "manner"},
    {"kokborok": "thum-twi", "english": "silently / quietly", "hindi": "शांति से / चुपचाप", "bengali": "চুপচাপ", "category": "manner"},
    {"kokborok": "khajani-twi", "english": "slowly / gently", "hindi": "धीरे-धीरे", "bengali": "আস্তে আস্তে", "category": "manner"},
    {"kokborok": "ahai-hai", "english": "like that / thus", "hindi": "उस प्रकार", "bengali": "সেইভাবে", "category": "manner"},
    {"kokborok": "ihai-hai", "english": "like this / in this way", "hindi": "इस तरह", "bengali": "এইভাবে", "category": "manner"},

    # Degree & Quantity (Swk)
    {"kokborok": "kwbang", "english": "much / greatly / abundantly", "hindi": "बहुत / अधिक", "bengali": "অনেক", "category": "degree"},
    {"kokborok": "twi-sa", "english": "a little bit", "hindi": "थोड़ा सा", "bengali": "একটু", "category": "degree"},
    {"kokborok": "bula", "english": "too much / excessively", "hindi": "अत्यधिक", "bengali": "অতিরিক্ত", "category": "degree"},
    {"kokborok": "belai", "english": "very / extremely", "hindi": "बहुत ही", "bengali": "খুবই", "category": "degree"},
    {"kokborok": "khung-sa", "english": "completely / entirely", "hindi": "पूरी तरह", "bengali": "সম্পূর্ণরূপে", "category": "degree"},
]

def list_adverbs(category: Optional[str] = None) -> List[Dict[str, Any]]:
    """List adverbs, optionally filtered by category ('time', 'place', 'manner', 'degree', 'direction')."""
    if category:
        c_low = category.lower().strip()
        return [a for a in ADVERBS if a["category"] == c_low]
    return list(ADVERBS)

def get_adverb(kokborok_word: str) -> Optional[Dict[str, Any]]:
    """Lookup an adverb by Kokborok text."""
    w = kokborok_word.strip().lower()
    for a in ADVERBS:
        if a["kokborok"].lower() == w:
            return a
    return None

def classify_adverb(kokborok_word: str) -> Optional[str]:
    """Return the semantic classification of an adverb."""
    adv = get_adverb(kokborok_word)
    return adv["category"] if adv else None
