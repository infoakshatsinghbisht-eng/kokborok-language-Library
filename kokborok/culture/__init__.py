# -*- coding: utf-8 -*-
from .calendar import get_months, get_days, get_seasons
from .festivals import list_festivals, get_festival, KOKBOROK_FESTIVALS
from .literature import list_authors, list_epics, AUTHORS, EPICS
from .kinship import list_kinship_terms, get_kinship_term, KINSHIP_TERMS
from .catalogue import KokborokCatalogue

catalogue = KokborokCatalogue()

__all__ = [
    "get_months", "get_days", "get_seasons",
    "list_festivals", "get_festival", "KOKBOROK_FESTIVALS",
    "list_authors", "list_epics", "AUTHORS", "EPICS",
    "list_kinship_terms", "get_kinship_term", "KINSHIP_TERMS",
    "catalogue", "KokborokCatalogue"
]
