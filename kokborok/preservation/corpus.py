# -*- coding: utf-8 -*-
"""Kokborok Digital Corpus and Cultural Preservation Engine."""

from typing import Dict, List, Any

class PreservationRecord:
    def __init__(self, title: str, author: str, year: str, source: str, pages: int = 0):
        self.title = title
        self.author = author
        self.year = year
        self.source = source
        self.pages = pages

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "source": self.source,
            "pages": self.pages
        }

class CorpusManager:
    def __init__(self):
        self.records: List[PreservationRecord] = []

    def add_record(self, record: PreservationRecord):
        self.records.append(record)

    def list_records(self) -> List[Dict[str, Any]]:
        return [r.to_dict() for r in self.records]
