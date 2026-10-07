# -*- coding: utf-8 -*-
"""Multi-Lingual Pivot Translation for Kokborok."""

from .engine import translate, TranslationResult

def pivot_translate(text: str, source_lang: str = "en", target_lang: str = "kokborok", dialect: str = "debbarma") -> TranslationResult:
    return translate(text, source=source_lang, target=target_lang, dialect=dialect)
