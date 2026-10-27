# -*- coding: utf-8 -*-
"""
Kokborok Reduplication, Ideophones, and Expressives Engine.
==========================================================

Kokborok possesses an exceptionally rich inventory of phonaesthetic expressives,
echo words, onomatopoeic ideophones, and total/partial reduplication patterns.
Based on Karapurkar (1976), Pushpa Pai (1976), and Binoy Debbarma (2013).
"""

from typing import Dict, List, Any, Optional

EXPRESSIVES: List[Dict[str, Any]] = [
    {
        "word": "chwng-chwng",
        "type": "ideophone_visual",
        "meaning": "brightly shining, gleaming, sparkling like clear water or clean jewelry",
        "example": "Watwi pai-khe sal chwng-chwng phrok-o (After the rain, the sun shines glistening bright)"
    },
    {
        "word": "phere-phere",
        "type": "ideophone_motion",
        "meaning": "light fluttering motion, like butterfly wings or a light cloth in the breeze",
        "example": "Kumpilak phere-phere bi-o (The butterfly flutters lightly)"
    },
    {
        "word": "drok-drok",
        "type": "ideophone_acoustic",
        "meaning": "deep rhythmic thumping, heavy heartbeat or rapid drum pulsation",
        "example": "Ani bukha drok-drok thum-o (My heart pounds heavily)"
    },
    {
        "word": "bili-bili",
        "type": "ideophone_tactile",
        "meaning": "extremely smooth, soft, silky texture of cloth or bamboo skin",
        "example": "Abo risa bili-bili man-o (That risa feels silky smooth)"
    },
    {
        "word": "ghwr-ghwr",
        "type": "ideophone_acoustic",
        "meaning": "continuous low rumble of thunder or flowing mountain stream",
        "example": "Nokhrom-o ghwr-ghwr watwi wat-o (Thunder rumbles low across the sky)"
    },
    {
        "word": "thok-thok",
        "type": "ideophone_acoustic",
        "meaning": "sharp knocking, tapping on dry bamboo or hollow wood",
        "example": "Wa thok-thok dok-di (Knock sharply on the bamboo)"
    },
    {
        "word": "plang-plang",
        "type": "ideophone_visual",
        "meaning": "wide open, unobstructed vista, clear cloudless sky",
        "example": "Nokhrom plang-plang kwrang-kha (The sky has cleared wide open)"
    },
    {
        "word": "sir-sir",
        "type": "ideophone_motion",
        "meaning": "gentle rustling of dry leaves under foot or gentle mountain breeze",
        "example": "Nohor sir-sir nawi tong-o (A gentle breeze blows rustling through)"
    },
    {
        "word": "muk-muk",
        "type": "ideophone_sensory",
        "meaning": "fragrant and appetizing smell of boiling fresh jhum rice",
        "example": "Mairong muk-muk khup-o (The sweet aroma of fresh rice wafts up)"
    },
    {
        "word": "khrang-khrang",
        "type": "ideophone_state",
        "meaning": "crisp, bone-dry, well-sunned harvest or firewood",
        "example": "Buphang khrang-khrang ran-kha (The wood is dried crisp and ready)"
    }
]

ECHO_PATTERNS: Dict[str, str] = {
    "mai": "mai-sai (rice and foodstuffs generally)",
    "nok": "nok-sok (houses and settlements)",
    "borok": "borok-sorok (people and community folks)",
    "wa": "wa-sa (bamboos and cane sticks)",
    "tui": "tui-sui (water and drinking liquids)",
    "chá": "chá-sá (eating and feasting)",
    "kok": "kok-sok (talks, gossip, conversations)",
    "risa": "risa-sisa (traditional stoles and wraps)"
}

def list_expressives(expressive_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return all catalogued ideophones and expressives, optionally filtered by type."""
    if expressive_type:
        t_low = expressive_type.lower().strip()
        return [e for e in EXPRESSIVES if t_low in e["type"].lower()]
    return list(EXPRESSIVES)

def get_expressive(word: str) -> Optional[Dict[str, Any]]:
    """Retrieve an expressive or ideophone by word."""
    w = word.strip().lower()
    for e in EXPRESSIVES:
        if e["word"].lower() == w or e["word"].replace("-", " ") == w:
            return e
    return None

def reduplicate_word(word: str, delimiter: str = "-") -> str:
    """Perform total reduplication on a word (e.g. 'sa' -> 'sa-sa')."""
    w = word.strip()
    return f"{w}{delimiter}{w}"

def find_echo_word(word: str) -> Optional[str]:
    """Retrieve traditional associative echo compound for a root word (e.g. 'mai' -> 'mai-sai')."""
    return ECHO_PATTERNS.get(word.strip().lower())
