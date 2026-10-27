# -*- coding: utf-8 -*-
"""
Kokborok Digitized Books & Literature Library Module.
=====================================================

Exposes the full digitized book library across `kokborok.books`.
Provides page-by-page text navigation, cover-to-cover text reading,
and cross-book keyword search for all public domain Kokborok literature.
"""

from .culture.books import (
    BookPage,
    KokborokBook,
    Book,
    BooksManager,
    list_books,
    get_book,
    get_book_full_text,
    search_books,
    total_books,
    total_pages,
    total_words,
    books,
)

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
