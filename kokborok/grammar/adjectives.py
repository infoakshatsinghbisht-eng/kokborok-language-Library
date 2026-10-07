# -*- coding: utf-8 -*-
"""Kokborok Adjectives, kw- Prefixation, and Degree System."""

def make_adjective(root: str) -> str:
    """Form canonical Kokborok adjective using kw- prefix."""
    r = root.strip().lower()
    if r.startswith("kw-") or r.startswith("k-") or r.startswith("ku-"):
        return r
    if r[0] in "bcdfghjklmnpqrstvwxyz":
        return f"kw{r}"
    return f"k-{r}"

def make_comparative(adj: str) -> str:
    """Form comparative degree ('kham-')."""
    return f"{adj}-kham"

def make_superlative(adj: str) -> str:
    """Form superlative degree ('jotoni khuk-')."""
    return f"jotoni {adj}-khuk"
