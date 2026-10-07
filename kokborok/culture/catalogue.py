# -*- coding: utf-8 -*-
"""Master Bibliography Catalogue for Kokborok Language & Literature."""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional

DATA_FILE = Path(__file__).resolve().parent / "data" / "kokborok_bibliography.json"

class KokborokCatalogue:
    def __init__(self):
        self._items = []
        if DATA_FILE.exists():
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self._items = json.load(f)

    def all(self) -> List[Dict[str, Any]]:
        return self._items

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        return [i for i in self._items if q in i.get("title", "").lower() or q in i.get("author", "").lower()]

    def by_type(self, item_type: str) -> List[Dict[str, Any]]:
        t = item_type.lower().strip()
        return [i for i in self._items if t in i.get("type", "").lower()]

    def count(self) -> int:
        return len(self._items)
