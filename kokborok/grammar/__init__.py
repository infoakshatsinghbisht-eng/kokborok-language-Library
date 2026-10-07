# -*- coding: utf-8 -*-
from .nouns import KokborokNoun, decline_noun, pluralize
from .verbs import conjugate, extract_root, causative, reciprocal
from .adjectives import make_adjective, make_comparative, make_superlative
from .pronouns import PRONOUN_TABLE, get_pronoun, DEMONSTRATIVES, INTERROGATIVES
from .syntax import build_sentence, interrogate_sentence

__all__ = [
    "KokborokNoun", "decline_noun", "pluralize",
    "conjugate", "extract_root", "causative", "reciprocal",
    "make_adjective", "make_comparative", "make_superlative",
    "PRONOUN_TABLE", "get_pronoun", "DEMONSTRATIVES", "INTERROGATIVES",
    "build_sentence", "interrogate_sentence"
]
