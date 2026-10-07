# -*- coding: utf-8 -*-
"""Kokborok SOV (Subject - Object - Verb) Syntax Engine."""

from .verbs import conjugate
from .nouns import decline_noun

def build_sentence(subject: str, direct_object: str, verb: str, tense: str = "present") -> str:
    """Construct a canonical Kokborok SOV sentence."""
    obj_case = decline_noun(direct_object, "accusative") if direct_object else ""
    v_conj = conjugate(verb, tense=tense, subject="").strip()
    parts = [p for p in [subject, obj_case, v_conj] if p]
    return " ".join(parts)

def interrogate_sentence(sentence: str) -> str:
    """Convert affirmative sentence into interrogative question by attaching -de particle."""
    s = sentence.strip()
    if s.endswith("?"):
        return s
    return f"{s} de?"
