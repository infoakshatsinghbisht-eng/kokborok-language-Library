# -*- coding: utf-8 -*-
"""Kokborok Quadri-lingual Dictionary Engine (Kokborok - English - Hindi - Bengali)."""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional

DATA_DIR = Path(__file__).resolve().parent / "data"

class KokborokDictionary:
    def __init__(self):
        self._words: Dict[str, Dict[str, Any]] = {}
        self._phrases: List[Dict[str, Any]] = []
        self._proverbs: List[Dict[str, Any]] = []
        self._riddles: List[Dict[str, Any]] = []
        self._load()

    def _load(self):
        w_file = DATA_DIR / "words.json"
        if w_file.exists():
            with open(w_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self._words[item["kokborok"].lower()] = item

        p_file = DATA_DIR / "phrases.json"
        if p_file.exists():
            with open(p_file, "r", encoding="utf-8") as f:
                self._phrases = json.load(f)

        pr_file = DATA_DIR / "proverbs.json"
        if pr_file.exists():
            with open(pr_file, "r", encoding="utf-8") as f:
                self._proverbs = json.load(f)

        r_file = DATA_DIR / "riddles.json"
        if r_file.exists():
            with open(r_file, "r", encoding="utf-8") as f:
                self._riddles = json.load(f)

    def lookup(self, word: str) -> Optional[Dict[str, Any]]:
        w = word.strip().lower()
        if not w:
            return None
        # 1. Exact match in words
        if w in self._words:
            return self._words[w]
        # 2. Match in phrases
        for p in self._phrases:
            if p["kokborok"].lower().strip(".,!?:") == w:
                return p
        # 3. Morphological root fallback
        from .morphology import get_morphology_engine
        engine = get_morphology_engine()
        analysis = engine.analyze(w)
        if analysis.root in self._words:
            entry = self._words[analysis.root].copy()
            entry["note"] = f"Derived from root '{analysis.root}'"
            entry["root"] = analysis.root
            return entry
        return None
        # Exact match
        if w in self._words:
            return self._words[w]
        # Morphological root fallback
        from .morphology import get_morphology_engine
        engine = get_morphology_engine()
        analysis = engine.analyze(w)
        if analysis.root in self._words:
            entry = self._words[analysis.root].copy()
            entry["note"] = f"Derived from root '{analysis.root}'"
            entry["root"] = analysis.root
            return entry
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for k, item in self._words.items():
            if (
                q in k or
                q in item.get("english", "").lower() or
                q in item.get("hindi", "").lower() or
                q in item.get("bengali", "").lower()
            ):
                results.append(item)
                if len(results) >= 50:
                    break
        return results

    def all_words(self) -> List[Dict[str, Any]]:
        return list(self._words.values())

    def count(self) -> int:
        return len(self._words)

    def all_phrases(self) -> List[Dict[str, Any]]:
        return self._phrases

    def all_proverbs(self) -> List[Dict[str, Any]]:
        return self._proverbs

    def all_riddles(self) -> List[Dict[str, Any]]:
        return self._riddles

_DICT = None

def get_dictionary() -> KokborokDictionary:
    global _DICT
    if _DICT is None:
        _DICT = KokborokDictionary()
    return _DICT
