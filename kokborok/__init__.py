# -*- coding: utf-8 -*-
"""
Kokborok (Kókborok) Language Library for Python
===============================================

A standard-library-style Python package for the Kokborok language (Tripura, Northeast India),
providing linguistic primitives, orthography normalization, Roman-to-Bengali transliteration,
grammar parsing, verbal conjugation, 300,000+ morphological inflections, 105,000+ words dictionary,
numeral classifiers, calendar, cultural heritage, and universal multi-lingual translation.
"""

__version__ = "1.1.0"
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
    # Classical Grammar Rules Engine
    GrammarRule,
    CLASSICAL_GRAMMAR_RULES,
    GrammarRulesEngine,
    get_grammar_rules_engine,
    grammar_rules,
    # Adverbs, Postpositions, Expressives
    list_adverbs,
    get_adverb,
    classify_adverb,
    ADVERBS,
    list_postpositions,
    get_postposition,
    attach_case,
    POSTPOSITIONS,
    list_expressives,
    get_expressive,
    reduplicate_word,
    find_echo_word,
    EXPRESSIVES,
    ECHO_PATTERNS
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
    KOKBOROK_FESTIVALS,
    list_authors,
    list_epics,
    AUTHORS,
    EPICS,
    list_kinship_terms,
    get_kinship_term,
    KINSHIP_TERMS,
    catalogue,
    KokborokCatalogue,
    # Expanded Cultural Subsystems
    list_attire,
    get_attire,
    list_motifs,
    TRADITIONAL_GARMENTS,
    WEAVING_MOTIFS,
    AttireManager,
    list_clans,
    get_clan,
    search_clans,
    CLANS,
    ClanManager,
    list_cuisine,
    get_dish,
    search_cuisine,
    DISHES,
    CuisineManager,
    list_deities,
    get_deity,
    search_deities,
    DEITIES,
    DeityManager,
    list_folklore,
    get_story,
    search_folklore,
    STORIES,
    FolkloreManager,
    list_geography,
    get_place,
    search_geography,
    PLACES,
    GeographyManager,
    list_idioms,
    search_idioms,
    IDIOMS,
    IdiomManager,
    list_instruments,
    get_instrument,
    list_dances,
    INSTRUMENTS,
    DANCE_FORMS,
    MusicManager,
    list_plants,
    get_plant,
    search_plants,
    PLANTS,
    BotanyManager,
    list_wildlife,
    get_wildlife,
    search_wildlife,
    FAUNA,
    WildlifeManager,
    list_rituals,
    get_ritual,
    search_rituals,
    RITUALS,
    RitualManager,
    list_sacred_sites,
    get_sacred_site,
    search_sacred_sites,
    SACRED_SITES,
    list_songs,
    get_song,
    search_songs,
    FOLK_SONGS,
    SongManager,
    # Digitized Books & Literature
    BookPage,
    KokborokBook,
    Book,
    BooksManager,
    list_books,
    get_book,
    get_book_full_text,
    search_books,
    total_books,
    total_pages,
    total_words,
    books,
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
        "grammar_rules": len(CLASSICAL_GRAMMAR_RULES),
        "traditional_garments": len(TRADITIONAL_GARMENTS),
        "clans": len(CLANS),
        "dishes": len(DISHES),
        "deities": len(DEITIES),
        "folklore_stories": len(STORIES),
        "geographical_landmarks": len(PLACES),
        "idioms": len(IDIOMS),
        "musical_instruments": len(INSTRUMENTS),
        "indigenous_plants": len(PLANTS),
        "wildlife_species": len(FAUNA),
        "rituals": len(RITUALS),
        "sacred_sites": len(SACRED_SITES),
        "folk_songs": len(FOLK_SONGS),
        "dialects": len(KOKBOROK_DIALECTS),
        "catalogued_works": catalogue.count(),
        "digitized_books": total_books(),
        "total_book_pages": total_pages(),
        "total_book_words": total_words(),
    }

__all__ = [
    # Top-Level Facade & Translation
    "translate", "TranslationResult", "pivot_translate",
    "lookup", "search", "analyze", "total_word_forms", "stats",
    # Phonetics & Script
    "normalize", "tokenize", "syllables", "is_kokborok_word",
    "roman_to_bengali", "bengali_to_roman", "detect_script",
    "has_high_tone", "strip_tone", "mark_high_tone",
    # Numbers & Classifiers
    "num_to_words", "words_to_num", "ordinal", "apply_classifier", "list_classifiers",
    # Grammar & Verb/Noun Morphology
    "conjugate", "causative", "reciprocal", "decline_noun", "pluralize",
    "build_sentence", "interrogate_sentence", "make_adjective", "make_comparative", "make_superlative",
    # Classical Grammar Rules Engine
    "GrammarRule", "CLASSICAL_GRAMMAR_RULES", "GrammarRulesEngine",
    "get_grammar_rules_engine", "grammar_rules",
    # Adverbs, Postpositions & Expressives
    "list_adverbs", "get_adverb", "classify_adverb", "ADVERBS",
    "list_postpositions", "get_postposition", "attach_case", "POSTPOSITIONS",
    "list_expressives", "get_expressive", "reduplicate_word", "find_echo_word",
    "EXPRESSIVES", "ECHO_PATTERNS",
    # Calendar & Festivals
    "get_months", "get_days", "get_seasons", "list_festivals", "get_festival", "KOKBOROK_FESTIVALS",
    # Literature & Kinship
    "list_authors", "list_epics", "AUTHORS", "EPICS",
    "list_kinship_terms", "get_kinship_term", "KINSHIP_TERMS",
    "catalogue", "KokborokCatalogue",
    # Attire & Textiles
    "list_attire", "get_attire", "list_motifs", "TRADITIONAL_GARMENTS", "WEAVING_MOTIFS", "AttireManager",
    # Clans & Tribes
    "list_clans", "get_clan", "search_clans", "CLANS", "ClanManager",
    # Cuisine
    "list_cuisine", "get_dish", "search_cuisine", "DISHES", "CuisineManager",
    # Deities
    "list_deities", "get_deity", "search_deities", "DEITIES", "DeityManager",
    # Folklore & Legends
    "list_folklore", "get_story", "search_folklore", "STORIES", "FolkloreManager",
    # Sacred Geography
    "list_geography", "get_place", "search_geography", "PLACES", "GeographyManager",
    # Idioms & Sayings
    "list_idioms", "search_idioms", "IDIOMS", "IdiomManager",
    # Music & Dance
    "list_instruments", "get_instrument", "list_dances", "INSTRUMENTS", "DANCE_FORMS", "MusicManager",
    # Botany & Wildlife
    "list_plants", "get_plant", "search_plants", "PLANTS", "BotanyManager",
    "list_wildlife", "get_wildlife", "search_wildlife", "FAUNA", "WildlifeManager",
    # Rituals & Sacred Sites
    "list_rituals", "get_ritual", "search_rituals", "RITUALS", "RitualManager",
    "list_sacred_sites", "get_sacred_site", "search_sacred_sites", "SACRED_SITES", "SacredSiteManager",
    # Songs & Melodies
    "list_songs", "get_song", "search_songs", "FOLK_SONGS", "SongManager",
    # Digitized Books & Whole-Book Literature Subsystem
    "BookPage", "KokborokBook", "Book", "BooksManager",
    "list_books", "get_book", "get_book_full_text", "search_books",
    "total_books", "total_pages", "total_words", "books",
    # Collections & Voice/Preservation
    "phrases", "proverbs", "riddles",
    "KokborokVoiceSynthesizer", "CorpusManager", "PreservationRecord",
    # Constants
    "ISO_639_3", "ISO_639_NAME", "NATIVE_NAME", "LANGUAGE_FAMILY", "OFFICIAL_STATUS", "KOKBOROK_DAY",
    "KOKBOROK_ALPHABET", "KOKBOROK_VOWELS", "KOKBOROK_CONSONANTS", "KOKBOROK_DIALECTS"
]
