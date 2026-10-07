# -*- coding: utf-8 -*-
"""Kokborok Verbal Inflection, Aspect Markers, and Affixes."""

from typing import Dict, Any, Optional

def extract_root(verb: str) -> str:
    """Extract verbal root by stripping tense, aspect, and negative suffixes."""
    v = verb.strip().lower()
    suffixes = [
        "-baikha", "-khaba", "-toli", "-tong", "-nai", "-anw", 
        "-kha", "-ya", "-liya", "-lai", "-ri"
    ]
    for suf in suffixes:
        if v.endswith(suf):
            return v[:-len(suf)].rstrip("-")
    prefixes = ["da-", "ta-", "ri-", "phwng-"]
    for pref in prefixes:
        if v.startswith(pref):
            return v[len(pref):].lstrip("-")
    return v

def conjugate(verb: str, tense: str = "present", subject: str = "bo", negative: bool = False) -> str:
    """
    Conjugate Kokborok verb.
    Past: -kha
    Future: -nai / -anw
    Present: root (or -o)
    Present Continuous: -tong / -toli
    Negative: -ya / -liya
    """
    root = extract_root(verb)
    if negative:
        if tense in ("past", "completed"):
            return f"{subject} {root}-liya"
        return f"{subject} {root}-ya"

    if tense in ("past", "completed"):
        return f"{subject} {root}-kha"
    elif tense in ("future", "intentional"):
        return f"{subject} {root}-nai"
    elif tense in ("present_continuous", "continuous"):
        return f"{subject} {root}-tong"
    elif tense in ("perfect",):
        return f"{subject} {root}-baikha"
    return f"{subject} {root}"

def causative(verb: str) -> str:
    """Create causative verb form (ri- / -ri)."""
    root = extract_root(verb)
    return f"{root}-ri"

def reciprocal(verb: str) -> str:
    """Create reciprocal mutual action form (-lai)."""
    root = extract_root(verb)
    return f"{root}-lai"
