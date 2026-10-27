# -*- coding: utf-8 -*-
"""
Kokborok Grammar Package.
=========================

Comprehensive grammar subsystem incorporating:
- Classical Grammar Rules Engine & 50+ rules (rules.py)
- Nominal declension, case postpositions, and plurality (nouns.py, postpositions.py)
- Verbal inflection, tense, aspect, causative, reciprocal (verbs.py)
- Adjectival morphology and degrees of comparison (adjectives.py)
- Pronouns and demonstratives (pronouns.py)
- Adverb classification and catalog (adverbs.py)
- Expressives, ideophones, and echo reduplication (echo_words.py)
- Syntax and clause generation (syntax.py)
"""

from .nouns import KokborokNoun, decline_noun, pluralize
from .verbs import conjugate, extract_root, causative, reciprocal
from .adjectives import make_adjective, make_comparative, make_superlative
from .pronouns import PRONOUN_TABLE, get_pronoun, DEMONSTRATIVES, INTERROGATIVES
from .syntax import build_sentence, interrogate_sentence
from .rules import (
    GrammarRule,
    CLASSICAL_GRAMMAR_RULES,
    GrammarRulesEngine,
    get_grammar_rules_engine,
    grammar_rules
)
from .adverbs import list_adverbs, get_adverb, classify_adverb, ADVERBS
from .postpositions import list_postpositions, get_postposition, attach_case, POSTPOSITIONS
from .echo_words import (
    list_expressives,
    get_expressive,
    reduplicate_word,
    find_echo_word,
    EXPRESSIVES,
    ECHO_PATTERNS
)

__all__ = [
    # Nouns & Declension
    "KokborokNoun", "decline_noun", "pluralize",
    # Verbs & Conjugation
    "conjugate", "extract_root", "causative", "reciprocal",
    # Adjectives
    "make_adjective", "make_comparative", "make_superlative",
    # Pronouns
    "PRONOUN_TABLE", "get_pronoun", "DEMONSTRATIVES", "INTERROGATIVES",
    # Syntax
    "build_sentence", "interrogate_sentence",
    # Classical Grammar Rules Engine
    "GrammarRule", "CLASSICAL_GRAMMAR_RULES", "GrammarRulesEngine",
    "get_grammar_rules_engine", "grammar_rules",
    # Adverbs
    "list_adverbs", "get_adverb", "classify_adverb", "ADVERBS",
    # Postpositions
    "list_postpositions", "get_postposition", "attach_case", "POSTPOSITIONS",
    # Expressives & Reduplication
    "list_expressives", "get_expressive", "reduplicate_word", "find_echo_word",
    "EXPRESSIVES", "ECHO_PATTERNS"
]
