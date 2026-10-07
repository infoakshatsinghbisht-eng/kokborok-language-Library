# -*- coding: utf-8 -*-
from .engine import translate, TranslationResult
from .dialects import apply_dialect, DIALECT_MAP
from .pivot import pivot_translate

__all__ = ["translate", "TranslationResult", "apply_dialect", "DIALECT_MAP", "pivot_translate"]
