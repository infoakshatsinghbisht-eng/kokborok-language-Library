# -*- coding: utf-8 -*-
"""
Kokborok Language Constants, Alphabets, Scripts, Dialects, and Metadata.
"""

from enum import Enum
from typing import Dict, List

ISO_639_3 = "trp"
ISO_639_NAME = "Kokborok"
NATIVE_NAME = "Kókborok"
LANGUAGE_FAMILY = "Sino-Tibetan > Tibeto-Burman > Sal > Bodo-Garo > Kokborok"
OFFICIAL_STATUS = "Official Language of Tripura (Recognized 19 January 1979)"
KOKBOROK_DAY = "19 January (Kokborok Sal)"

# Traditional Scripts
SCRIPTS = ["Latin (Official Roman)", "Bengali-Assamese", "Koloma (Historic)"]

# Kokborok Latin Alphabet
# Vowels: a, i, u, e, o, w (where w represents the close back unrounded vowel [ɯ])
KOKBOROK_VOWELS = ["a", "i", "u", "e", "o", "w"]
KOKBOROK_DIPHTHONGS = ["ai", "ui", "oi", "wi", "au"]

# Consonants
KOKBOROK_CONSONANTS = [
    "b", "ch", "d", "g", "h", "j", "k", "kh", "l", "m", 
    "n", "ng", "p", "ph", "r", "s", "t", "th", "w", "y"
]

KOKBOROK_ALPHABET = [
    "a", "b", "ch", "d", "e", "g", "h", "i", "j", "k", 
    "kh", "l", "m", "n", "ng", "o", "p", "ph", "r", "s", 
    "t", "th", "u", "w", "y"
]

class Dialect(str, Enum):
    DEBBARMA = "debbarma"       # Standard / Puran Tripura
    REANG = "reang"             # Bru
    JAMATIA = "jamatia"         # Jamatia dialect
    NOATIA = "noatia"           # Noatia dialect
    KALAI = "kalai"             # Kalai
    RUPINI = "rupini"           # Rupini
    MURASING = "murasing"       # Murasing
    UCHAI = "uchai"             # Uchai

KOKBOROK_DIALECTS = [d.value for d in Dialect]

class PartOfSpeech(str, Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PRONOUN = "pronoun"
    POSTPOSITION = "postposition"
    CONJUNCTION = "conjunction"
    INTERJECTION = "interjection"
    CLASSIFIER = "classifier"
    PARTICLE = "particle"
    NUMBER = "number"

class Tense(str, Enum):
    PRESENT = "present"
    PAST = "past"
    FUTURE = "future"
    PRESENT_CONTINUOUS = "present_continuous"
    PAST_CONTINUOUS = "past_continuous"
    PERFECT = "perfect"

# Traditional 12 Months
KOKBOROK_MONTHS: List[Dict[str, str]] = [
    {"kokborok": "Tal-sa", "english": "Baisakh (April-May)", "bengali": "বৈশাখ", "meaning": "First month, harvest renewal"},
    {"kokborok": "Tal-nwi", "english": "Jaistha (May-June)", "bengali": "জ্যৈষ্ঠ", "meaning": "Second month, summer rains begin"},
    {"kokborok": "Tal-tham", "english": "Ashadha (June-July)", "bengali": "আষাঢ়", "meaning": "Third month, Kharchi Puja season"},
    {"kokborok": "Tal-brwi", "english": "Shravana (July-August)", "bengali": "শ্রাবণ", "meaning": "Fourth month, high monsoon"},
    {"kokborok": "Tal-ba", "english": "Bhadra (August-September)", "bengali": "ভাদ্র", "meaning": "Fifth month, late monsoon"},
    {"kokborok": "Tal-dok", "english": "Ashvina (September-October)", "bengali": "আশ্বিন", "meaning": "Sixth month, autumn festivals"},
    {"kokborok": "Tal-sni", "english": "Kartika (October-November)", "bengali": "কার্তিক", "meaning": "Seventh month, harvest preparations"},
    {"kokborok": "Tal-char", "english": "Agrahayana (November-December)", "bengali": "অগ্রহায়ণ", "meaning": "Eighth month, winter harvest"},
    {"kokborok": "Tal-chuku", "english": "Pausha (December-January)", "bengali": "পৌষ", "meaning": "Ninth month, winter chill"},
    {"kokborok": "Tal-chi", "english": "Magha (January-February)", "bengali": "মাঘ", "meaning": "Tenth month, Kokborok Day month"},
    {"kokborok": "Tal-chisa", "english": "Phalguna (February-March)", "bengali": "ফাল্গুন", "meaning": "Eleventh month, spring bloom"},
    {"kokborok": "Tal-chinwi", "english": "Chaitra (March-April)", "bengali": "চৈত্র", "meaning": "Twelfth month, Garia Puja preparation"}
]

# Traditional 7 Days of the Week
DAYS_OF_WEEK: List[Dict[str, str]] = [
    {"kokborok": "Sal-sa", "english": "Sunday", "bengali": "রবিবার", "hindi": "रविवार"},
    {"kokborok": "Sal-nwi", "english": "Monday", "bengali": "সোমবার", "hindi": "सोमवार"},
    {"kokborok": "Sal-tham", "english": "Tuesday", "bengali": "মঙ্গলবার", "hindi": "मंगलवार"},
    {"kokborok": "Sal-brwi", "english": "Wednesday", "bengali": "বুধবার", "hindi": "बुधवार"},
    {"kokborok": "Sal-ba", "english": "Thursday", "bengali": "বৃহস্পতিবার", "hindi": "गुरुवार"},
    {"kokborok": "Sal-dok", "english": "Friday", "bengali": "শুক্রবার", "hindi": "शुक्रवार"},
    {"kokborok": "Sal-sni", "english": "Saturday", "bengali": "শনিবার", "hindi": "शनिवार"}
]

# Traditional Seasons
SEASONS: List[Dict[str, str]] = [
    {"kokborok": "Maikhung", "english": "Winter", "bengali": "শীতকাল", "hindi": "शीत ऋतु"},
    {"kokborok": "Kuthung", "english": "Summer", "bengali": "গ্রীষ্মকাল", "hindi": "ग्रीष्म ऋतु"},
    {"kokborok": "Watwi", "english": "Monsoon / Rainy Season", "bengali": "বর্ষাকাল", "hindi": "वर्षा ऋतु"},
    {"kokborok": "Gwbwi", "english": "Autumn / Harvest Season", "bengali": "শরৎকাল", "hindi": "शरद ऋतु"}
]
