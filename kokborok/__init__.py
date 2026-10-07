# -*- coding: utf-8 -*-
"""
Kokborok (Kókborok) Language Library for Python
===============================================

A standard-library-style Python package for the Kokborok language (Tripura, Northeast India),
providing linguistic primitives, orthography normalization, Roman-to-Bengali transliteration,
grammar parsing, verbal conjugation, 300,000+ morphological inflections, 100,000+ words dictionary,
numeral classifiers, calendar, cultural heritage, and universal multi-lingual translation.
"""

__version__ = "1.0.0"
__author__ = "Akshat Singh Bisht"
__email__ = "infoakshatsinghbisht@gmail.com"
__maintainer__ = "Akshat Singh Bisht"
__website__ = "https://akshatsinghbisht.com/"
__copyright__ = "Copyright (c) 2026 Akshat Singh Bisht"
__license__ = "MIT"

from .constants import (
    ISO_639_3,
    ISO_639_NAME,
    NATIVE_NAME,
    LANGUAGE_FAMILY,
    OFFICIAL_STATUS,
    KOKBOROK_DAY,
    KOKBOROK_ALPHABET,
    KOKBOROK_VOWELS,
    KOKBOROK_CONSONANTS,
    KOKBOROK_DIALECTS,
    Dialect,
    PartOfSpeech,
    Tense,
    KOKBOROK_MONTHS,
    DAYS_OF_WEEK,
    SEASONS,
)

from .phonetics import (
    normalize,
    tokenize,
    syllables,
    is_kokborok_word,
    roman_to_bengali,
    bengali_to_roman,
    detect_script,
    has_high_tone,
    strip_tone,
    mark_high_tone,
)

from .numbers import (
    num_to_words,
    words_to_num,
    ordinal,
    apply_classifier,
    list_classifiers,
)

from .grammar import (
    KokborokNoun,
    decline_noun,
    pluralize,
    conjugate,
    extract_root,
    causative,
    reciprocal,
    make_adjective,
    make_comparative,
    make_superlative,
    PRONOUN_TABLE,
    get_pronoun,
    DEMONSTRATIVES,
    INTERROGATIVES,
    build_sentence,
    interrogate_sentence,
)

from .lexicon import (
    KokborokDictionary,
    get_dictionary,
    KokborokMorphologyEngine,
    get_morphology_engine,
)

from .translator import (
    translate,
    TranslationResult,
    apply_dialect,
    pivot_translate,
)

from .culture import (
    get_months,
    get_days,
    get_seasons,
    list_festivals,
    get_festival,
    list_authors,
    list_epics,
    list_kinship_terms,
    get_kinship_term,
    catalogue,
    KokborokCatalogue,
)

from .voice import KokborokVoiceSynthesizer
from .preservation import CorpusManager, PreservationRecord

_DICT = get_dictionary()
phrases = type("Phrases", (), {"all": _DICT.all_phrases})()
proverbs = type("Proverbs", (), {"all": _DICT.all_proverbs})()
riddles = type("Riddles", (), {"all": _DICT.all_riddles})()

def lookup(word: str):
    return _DICT.lookup(word)

def search(query: str):
    return _DICT.search(query)

def analyze(word: str):
    return get_morphology_engine().analyze(word)

def total_word_forms() -> int:
    return get_morphology_engine().total_forms_count()

def stats():
    return {
        "version": __version__,
        "headwords": _DICT.count(),
        "total_morphological_forms": total_word_forms(),
        "phrases": len(_DICT.all_phrases()),
        "proverbs": len(_DICT.all_proverbs()),
        "riddles": len(_DICT.all_riddles()),
        "dialects": len(KOKBOROK_DIALECTS),
        "catalogued_works": catalogue.count()
    }

__all__ = [
    "translate", "TranslationResult", "pivot_translate",
    "lookup", "search", "analyze", "total_word_forms", "stats",
    "normalize", "tokenize", "syllables", "is_kokborok_word",
    "roman_to_bengali", "bengali_to_roman", "detect_script",
    "num_to_words", "words_to_num", "ordinal", "apply_classifier", "list_classifiers",
    "conjugate", "causative", "reciprocal", "decline_noun", "pluralize",
    "build_sentence", "interrogate_sentence", "make_adjective", "make_comparative", "make_superlative",
    "get_months", "get_days", "get_seasons", "list_festivals", "get_festival",
    "list_authors", "list_epics", "list_kinship_terms", "get_kinship_term",
    "phrases", "proverbs", "riddles", "catalogue", "KokborokCatalogue",
    "KokborokVoiceSynthesizer", "CorpusManager", "PreservationRecord",
    "ISO_639_3", "ISO_639_NAME", "NATIVE_NAME", "LANGUAGE_FAMILY", "OFFICIAL_STATUS", "KOKBOROK_DAY"
]
