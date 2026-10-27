# -*- coding: utf-8 -*-
"""
Kokborok Cultural Heritage, Traditions, Folklore & Arts Subsystem.
==================================================================

Comprehensive cultural knowledge subsystem providing programmatic access to:
- Traditional Calendar (months, days, seasons)
- Festivals and sacred ceremonies
- Classical literature, epics, and authors
- Kinship structure and relational terminology
- Traditional attire, handloom garments, and weaving motifs
- Indigenous clans and tribes of Tripura
- Traditional cuisine and culinary heritage
- Spiritual pantheon and deities (Mwtai)
- Folklore, creation myths, and oral tales
- Sacred geography, mountains, and rivers
- Idioms and metaphorical expressions (Kok-Hajakma)
- Traditional musical instruments and folk dances
- Indigenous botany, bamboo species, and wild flora
- Native wildlife and fauna
- Lifecycle rituals, Ochai rites, and weddings
- Sacred pilgrimage sites and ancient temples
- Folk songs, Jaduni ballads, and lullabies
- Historical bibliography and literature catalogue
"""

from .calendar import get_months, get_days, get_seasons
from .festivals import list_festivals, get_festival, KOKBOROK_FESTIVALS
from .literature import list_authors, list_epics, AUTHORS, EPICS
from .kinship import list_kinship_terms, get_kinship_term, KINSHIP_TERMS
from .catalogue import KokborokCatalogue
from .attire import (
    list_attire, get_attire, list_motifs,
    TRADITIONAL_GARMENTS, WEAVING_MOTIFS, AttireManager
)
from .clans import list_clans, get_clan, search_clans, CLANS, ClanManager
from .cuisine import list_cuisine, get_dish, search_cuisine, DISHES, CuisineManager
from .deities import list_deities, get_deity, search_deities, DEITIES, DeityManager
from .folklore import list_folklore, get_story, search_folklore, STORIES, FolkloreManager
from .geography import list_geography, get_place, search_geography, PLACES, GeographyManager
from .idioms import list_idioms, search_idioms, IDIOMS, IdiomManager
from .music import (
    list_instruments, get_instrument, list_dances,
    INSTRUMENTS, DANCE_FORMS, MusicManager
)
from .botany import list_plants, get_plant, search_plants, PLANTS, BotanyManager
from .wildlife import list_wildlife, get_wildlife, search_wildlife, FAUNA, WildlifeManager
from .rituals import list_rituals, get_ritual, search_rituals, RITUALS, RitualManager
from .sacred_sites import (
    list_sacred_sites, get_sacred_site, search_sacred_sites,
    SACRED_SITES, SacredSiteManager
)
from .songs import list_songs, get_song, search_songs, FOLK_SONGS, SongManager
from .books import (
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

catalogue = KokborokCatalogue()

__all__ = [
    # Calendar & Festivals
    "get_months", "get_days", "get_seasons",
    "list_festivals", "get_festival", "KOKBOROK_FESTIVALS",
    # Literature & Kinship
    "list_authors", "list_epics", "AUTHORS", "EPICS",
    "list_kinship_terms", "get_kinship_term", "KINSHIP_TERMS",
    "catalogue", "KokborokCatalogue",
    # Attire & Textiles
    "list_attire", "get_attire", "list_motifs",
    "TRADITIONAL_GARMENTS", "WEAVING_MOTIFS", "AttireManager",
    # Clans & Tribes
    "list_clans", "get_clan", "search_clans", "CLANS", "ClanManager",
    # Cuisine
    "list_cuisine", "get_dish", "search_cuisine", "DISHES", "CuisineManager",
    # Deities
    "list_deities", "get_deity", "search_deities", "DEITIES", "DeityManager",
    # Folklore & Legends
    "list_folklore", "get_story", "search_folklore", "STORIES", "FolkloreManager",
    # Sacred Geography
    "list_geography", "get_place", "search_geography", "PLACES", "GeographyManager",
    # Idioms & Sayings
    "list_idioms", "search_idioms", "IDIOMS", "IdiomManager",
    # Music & Dance
    "list_instruments", "get_instrument", "list_dances",
    "INSTRUMENTS", "DANCE_FORMS", "MusicManager",
    # Botany & Wildlife
    "list_plants", "get_plant", "search_plants", "PLANTS", "BotanyManager",
    "list_wildlife", "get_wildlife", "search_wildlife", "FAUNA", "WildlifeManager",
    # Rituals & Sacred Sites
    "list_rituals", "get_ritual", "search_rituals", "RITUALS", "RitualManager",
    "list_sacred_sites", "get_sacred_site", "search_sacred_sites",
    "SACRED_SITES", "SacredSiteManager",
    # Songs & Melodies
    "list_songs", "get_song", "search_songs", "FOLK_SONGS", "SongManager",
    # Digitized Books & Literature
    "BookPage", "KokborokBook", "Book", "BooksManager",
    "list_books", "get_book", "get_book_full_text", "search_books",
    "total_books", "total_pages", "total_words", "books"
]
