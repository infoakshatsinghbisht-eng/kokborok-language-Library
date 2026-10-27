# -*- coding: utf-8 -*-
"""
Unit tests for Kokborok Digitized Books & Literature Library Subsystem.
"""

import unittest
import kokborok
from kokborok.books import (
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


class TestKokborokBooks(unittest.TestCase):
    """Test suite for digitized books and page-by-page reader subsystem."""

    def test_total_books_and_stats(self):
        """Verify book counts, page counts, and global library statistics."""
        count = total_books()
        self.assertGreaterEqual(count, 220)
        self.assertEqual(count, 225)
        self.assertEqual(count, len(list_books()))

        pages = total_pages()
        self.assertGreaterEqual(pages, 32000)

        words = total_words()
        self.assertGreaterEqual(words, 9000000)

        st = kokborok.stats()
        self.assertIn("digitized_books", st)
        self.assertIn("total_book_pages", st)
        self.assertIn("total_book_words", st)
        self.assertEqual(st["digitized_books"], count)
        self.assertEqual(st["total_book_pages"], pages)
        self.assertEqual(st["total_book_words"], words)

    def test_list_books_metadata(self):
        """Verify that each listed book has required metadata fields."""
        book_list = list_books()
        self.assertIsInstance(book_list, list)

        for b in book_list:
            self.assertIn("id", b)
            self.assertIn("title", b)
            self.assertIn("author", b)
            self.assertIn("total_pages", b)
            self.assertIn("total_words", b)
            self.assertGreater(b["total_pages"], 0)
            self.assertGreater(b["total_words"], 0)

    def test_get_book_by_id_and_title(self):
        """Verify retrieving books by exact ID, title substring, and case-insensitivity."""
        book = get_book("kokborok_swrongma")
        self.assertIsNotNone(book)
        self.assertEqual(book.id, "kokborok_swrongma")
        self.assertIn("Swrongma", book.title)
        self.assertGreaterEqual(book.total_pages, 80)
        self.assertGreater(book.total_words, 20000)

        # Retrieval by title keyword
        book_by_title = get_book("Primer")
        self.assertIsNotNone(book_by_title)
        self.assertEqual(book_by_title.id, "kokborok_primer")

        # Unknown book returns None
        unknown = get_book("non_existent_book_id_xyz")
        self.assertIsNone(unknown)

    def test_book_page_reading_and_navigation(self):
        """Verify reading specific pages, out-of-range bounds, and full text concatenation."""
        book = get_book("kokborok_swrongma")
        self.assertIsNotNone(book)

        # First page text
        page1 = book.get_page(1)
        self.assertIsInstance(page1, str)
        self.assertGreater(len(page1), 50)

        # Read alias
        self.assertEqual(book.read(1), page1)

        # Out-of-bounds page returns None
        self.assertIsNone(book.get_page(0))
        self.assertIsNone(book.get_page(9999))

        # Page object inspection
        page_obj = book.get_page_obj(1)
        self.assertIsInstance(page_obj, BookPage)
        self.assertEqual(page_obj.page_number, 1)
        self.assertGreater(page_obj.word_count, 10)

        # Full text
        full = book.full_text
        self.assertIsInstance(full, str)
        self.assertIn(page1.strip()[:30], full)
        self.assertGreater(len(full), 10000)

        # Convenience function
        full_text_direct = get_book_full_text("kokborok_swrongma")
        self.assertEqual(full_text_direct, full)

    def test_book_search_and_universal_search(self):
        """Verify keyword search within a book and across all digitized books."""
        book = get_book("kokborok_swrongma")
        self.assertIsNotNone(book)

        # In-book search
        matches = book.search("kokborok")
        self.assertIsInstance(matches, list)
        self.assertGreater(len(matches), 0)
        first_match = matches[0]
        self.assertIn("page_number", first_match)
        self.assertIn("snippet", first_match)
        self.assertEqual(first_match["book_id"], book.id)

        # Universal search across all books
        all_matches = search_books("Tripura", max_results=10)
        self.assertIsInstance(all_matches, list)
        self.assertGreater(len(all_matches), 0)
        for m in all_matches:
            self.assertIn("book_id", m)
            self.assertIn("book_title", m)
            self.assertIn("page_number", m)
            self.assertIn("snippet", m)

    def test_books_manager_facade(self):
        """Verify BooksManager object-oriented facade methods."""
        bm = books
        self.assertEqual(len(bm), total_books())

        # Subscripting
        b = bm["kokborok_dhadha"]
        self.assertIsNotNone(b)
        self.assertEqual(b.id, "kokborok_dhadha")

        # bm.read
        txt = bm.read("kokborok_dhadha", 1)
        self.assertIsNotNone(txt)

        # bm.search
        res = bm.search("Tripura", max_results=5)
        self.assertLessEqual(len(res), 5)

        # bm.stats
        bm_stats = bm.stats()
        self.assertEqual(bm_stats["total_books"], total_books())
        self.assertEqual(bm_stats["total_pages"], total_pages())
        self.assertEqual(bm_stats["total_words"], total_words())

    def test_top_level_exports(self):
        """Verify that all books functions and classes are accessible directly on kokborok."""
        self.assertTrue(hasattr(kokborok, "books"))
        self.assertTrue(hasattr(kokborok, "list_books"))
        self.assertTrue(hasattr(kokborok, "get_book"))
        self.assertTrue(hasattr(kokborok, "get_book_full_text"))
        self.assertTrue(hasattr(kokborok, "search_books"))
        self.assertTrue(hasattr(kokborok, "total_books"))
        self.assertTrue(hasattr(kokborok, "total_pages"))
        self.assertTrue(hasattr(kokborok, "total_words"))
        self.assertTrue(hasattr(kokborok, "KokborokBook"))
        self.assertTrue(hasattr(kokborok, "BookPage"))
        self.assertTrue(hasattr(kokborok, "Book"))
        self.assertTrue(hasattr(kokborok, "BooksManager"))


if __name__ == "__main__":
    unittest.main()
