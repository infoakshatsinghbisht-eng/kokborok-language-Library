# -*- coding: utf-8 -*-
"""
Kokborok Digitized Books & Literature Library Module (Kokborok Thiar).
======================================================================

Comprehensive whole-book access (all pages, chapters, and metadata)
for authentic Kokborok literature, primers, folklore, and historical chronicles.

Key Features:
- Page-by-page text navigation (`book.get_page(page_number)`)
- Full concatenated book text access (`book.full_text`)
- In-book search across pages with text snippets (`book.search("...")`)
- Universal full-text search across all digitized books (`search_books("...")`)
- Rich metadata: Title, native title, author, year, genre, chapters, total words
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union

_BOOKS_DATA_DIR = Path(__file__).resolve().parent / "data" / "books"
_INDEX_PATH = _BOOKS_DATA_DIR / "books_index.json"

_BOOKS_INDEX_CACHE: Optional[List[Dict[str, Any]]] = None
_BOOK_CACHE: Dict[str, "KokborokBook"] = {}


@dataclass
class BookPage:
    """Represents a single page in a Kokborok book."""
    page_number: int
    text: str
    word_count: int

    def contains(self, query: str, case_sensitive: bool = False) -> bool:
        """Check if query is in this page's text."""
        if case_sensitive:
            return query in self.text
        return query.lower() in self.text.lower()


@dataclass
class KokborokBook:
    """Represents a complete Kokborok book with all its pages, chapters, and metadata."""
    id: str
    title: str
    native_title: str
    author: str
    year: int
    genre: str
    description: str
    total_pages: int
    total_words: int
    chapters: List[str]
    archive_id: str = ""
    pages: List[BookPage] = field(default_factory=list, repr=False)

    @property
    def full_text(self) -> str:
        """Return the entire concatenated text of the book across all pages."""
        return "\n\n".join(p.text for p in self.pages if p.text)

    def get_page(self, page_number: int) -> Optional[str]:
        """Return the text of a specific 1-indexed page."""
        if 1 <= page_number <= len(self.pages):
            return self.pages[page_number - 1].text
        return None

    def get_page_obj(self, page_number: int) -> Optional[BookPage]:
        """Return the BookPage object for a specific 1-indexed page."""
        if 1 <= page_number <= len(self.pages):
            return self.pages[page_number - 1]
        return None

    def read(self, page_number: int = 1) -> Optional[str]:
        """Convenience alias for get_page."""
        return self.get_page(page_number)

    def search(self, query: str, context_chars: int = 150) -> List[Dict[str, Any]]:
        """Search for occurrences of query in this book, returning page matches with snippets."""
        q_low = query.lower().strip()
        matches = []
        for p in self.pages:
            p_text = p.text
            p_low = p_text.lower()
            start = 0
            while True:
                idx = p_low.find(q_low, start)
                if idx == -1:
                    break
                s_start = max(0, idx - context_chars // 2)
                s_end = min(len(p_text), idx + len(query) + context_chars // 2)
                snippet = p_text[s_start:s_end].strip()
                matches.append({
                    "book_id": self.id,
                    "book_title": self.title,
                    "page_number": p.page_number,
                    "snippet": f"...{snippet}..."
                })
                start = idx + len(query)
                if len(matches) >= 30:
                    break
            if len(matches) >= 30:
                break
        return matches

    def to_dict(self) -> Dict[str, Any]:
        """Return summary metadata dict of the book."""
        return {
            "id": self.id,
            "title": self.title,
            "native_title": self.native_title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "description": self.description,
            "total_pages": self.total_pages,
            "total_words": self.total_words,
            "chapters": self.chapters,
            "archive_id": self.archive_id
        }


def _load_index() -> List[Dict[str, Any]]:
    """Load the master index of all digitized books."""
    global _BOOKS_INDEX_CACHE
    if _BOOKS_INDEX_CACHE is not None:
        return _BOOKS_INDEX_CACHE

    if _INDEX_PATH.exists():
        try:
            with open(_INDEX_PATH, "r", encoding="utf-8") as f:
                _BOOKS_INDEX_CACHE = json.load(f)
                return _BOOKS_INDEX_CACHE
        except Exception:
            pass
    _BOOKS_INDEX_CACHE = []
    return _BOOKS_INDEX_CACHE


def list_books() -> List[Dict[str, Any]]:
    """Return summary metadata for all catalogued digitized Kokborok books."""
    return list(_load_index())


def get_book(id_or_title: str) -> Optional[KokborokBook]:
    """Retrieve full KokborokBook instance with all pages by ID or title keyword."""
    target = id_or_title.lower().strip()

    # 1. Check memory cache
    if target in _BOOK_CACHE:
        return _BOOK_CACHE[target]

    # 2. Check index for ID resolution
    index = _load_index()
    matched_id = None
    for entry in index:
        if entry["id"].lower() == target:
            matched_id = entry["id"]
            break
        if target in entry["title"].lower() or target in entry.get("native_title", "").lower():
            matched_id = entry["id"]
            break

    if not matched_id:
        matched_id = target

    # 3. Load from book JSON file
    book_file = _BOOKS_DATA_DIR / f"{matched_id}.json"
    if not book_file.exists():
        # Try matching filename
        for f in _BOOKS_DATA_DIR.glob("*.json"):
            if f.stem != "books_index" and (target in f.stem.lower()):
                book_file = f
                break

    if not book_file.exists():
        return None

    try:
        with open(book_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        pages = [
            BookPage(
                page_number=p["page_number"],
                text=p["text"],
                word_count=p.get("word_count", len(p["text"].split()))
            )
            for p in data.get("pages", [])
        ]

        book = KokborokBook(
            id=data["id"],
            title=data["title"],
            native_title=data.get("native_title", ""),
            author=data.get("author", "Unknown"),
            year=data.get("year", 0),
            genre=data.get("genre", "Literature"),
            description=data.get("description", ""),
            total_pages=data.get("total_pages", len(pages)),
            total_words=data.get("total_words", sum(p.word_count for p in pages)),
            chapters=data.get("chapters", []),
            archive_id=data.get("archive_id", ""),
            pages=pages
        )

        _BOOK_CACHE[target] = book
        _BOOK_CACHE[book.id] = book
        return book
    except Exception as e:
        print(f"Error loading book {book_file}: {e}")
        return None


def get_book_full_text(id_or_title: str) -> Optional[str]:
    """Retrieve complete concatenated text of a book."""
    b = get_book(id_or_title)
    return b.full_text if b else None


def search_books(query: str, max_results: int = 50) -> List[Dict[str, Any]]:
    """Search for a keyword across all digitized Kokborok books."""
    q_low = query.lower().strip()
    results = []

    for item in list_books():
        b = get_book(item["id"])
        if b:
            matches = b.search(q_low)
            results.extend(matches)
            if len(results) >= max_results:
                break

    return results[:max_results]


def total_books() -> int:
    """Return total number of catalogued digitized Kokborok books."""
    return len(_load_index())


def total_pages() -> int:
    """Return total number of digitized pages across all books."""
    return sum(b.get("total_pages", 0) for b in _load_index())


def total_words() -> int:
    """Return total word count across all digitized books."""
    return sum(b.get("total_words", 0) for b in _load_index())


class BooksManager:
    """Object-oriented facade for reading, searching, and inspecting Kokborok books."""

    def __len__(self) -> int:
        return total_books()

    def __iter__(self):
        for b in list_books():
            yield get_book(b["id"])

    def __getitem__(self, item: str) -> Optional[KokborokBook]:
        return get_book(item)

    def all(self) -> List[Dict[str, Any]]:
        """List summary metadata of all books."""
        return list_books()

    def get(self, id_or_title: str) -> Optional[KokborokBook]:
        """Get full book instance by ID or title."""
        return get_book(id_or_title)

    def read(self, id_or_title: str, page_number: int = 1) -> Optional[str]:
        """Read specific page text from a book."""
        b = get_book(id_or_title)
        if b:
            return b.get_page(page_number)
        return None

    def search(self, query: str, max_results: int = 50) -> List[Dict[str, Any]]:
        """Search query across all books."""
        return search_books(query, max_results=max_results)

    def stats(self) -> Dict[str, Any]:
        """Return overall book library statistics."""
        return {
            "total_books": total_books(),
            "total_pages": total_pages(),
            "total_words": total_words()
        }


books = BooksManager()
Book = KokborokBook

__all__ = [
    "BookPage",
    "KokborokBook",
    "Book",
    "BooksManager",
    "list_books",
    "get_book",
    "get_book_full_text",
    "search_books",
    "total_books",
    "total_pages",
    "total_words",
    "books",
]
