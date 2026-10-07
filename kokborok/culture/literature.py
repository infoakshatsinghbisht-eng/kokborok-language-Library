# -*- coding: utf-8 -*-
"""Canonical Kokborok Literary Figures, Epics, and Traditional Folklore."""

from typing import Dict, List, Any

AUTHORS: List[Dict[str, Any]] = [
    {
        "name": "Radhamohan Thakur",
        "era": "Late 19th - Early 20th Century",
        "title": "Pioneer of Kokborok Linguistics",
        "notable_works": ["Kokborok Grammar (Kókborokma, 1900)"],
        "contribution": "Compiled the earliest formal descriptive grammar of the Kokborok language under royal patronage."
    },
    {
        "name": "Doulot Ahmad",
        "era": "1897",
        "title": "Co-compiler of Kokborokma",
        "notable_works": ["Kokborokma (1897)"],
        "contribution": "Collaborated with Radhamohan Thakur to document Tripuri grammar and vocabulary."
    },
    {
        "name": "Sudhanya Debbarma",
        "era": "20th Century",
        "title": "Father of Modern Kokborok Literature",
        "notable_works": ["Kókborok Rwbwchap (Folk Songs)", "Kokborok Prose"],
        "contribution": "Pioneered creative writing, education, and social awareness in Kokborok."
    },
    {
        "name": "Chandrakanta Murasingh",
        "era": "1961 - 2023",
        "title": "Sahitya Akademi Bhasha Samman Awardee",
        "notable_works": ["Haping Garingo Chibuk Luku (Snake on the Hill)", "Pinchiring", "Holi"],
        "contribution": "Brought modern Kokborok poetry to national and international prominence."
    },
    {
        "name": "Alindralal Tripura",
        "era": "20th Century",
        "title": "Folklorist & Scholar",
        "notable_works": ["Tripura Folk Tales", "Chumrai"],
        "contribution": "Preserved oral literature, clan histories, and traditional tales."
    },
    {
        "name": "Bikashrai Debbarma",
        "era": "Modern Era",
        "title": "Poet and Cultural Historian",
        "notable_works": ["Twima", "Kokborok Sahitya Charcha"],
        "contribution": "Champion of contemporary Kokborok essays, research, and lexicon development."
    }
]

EPICS: List[Dict[str, Any]] = [
    {
        "title": "Rajmala (Tripura Raj Ratnakar)",
        "native": "Bubagra-ni Charit",
        "type": "Dynastic Royal Chronicle",
        "theme": "The epic verse chronicle recounting the genealogy of 180+ Tripura Manikya Kings tracing back to Druhyu and the lunar dynasty."
    },
    {
        "title": "Chethuang",
        "native": "Chethuang-ni Kothoma",
        "type": "Tragic Romantic Folk Epic",
        "theme": "The beloved folklore of intense devotion, societal struggle, and sacrifice in the lush hills of Tripura."
    },
    {
        "title": "Longthoroi",
        "native": "Hachuk Longthoroi",
        "type": "Sacred Mountain & River Legend",
        "theme": "The mythic origins of the Longthoroi mountain ranges, sacred springs, and guardian deities."
    },
    {
        "title": "Subrai Raja",
        "native": "Subrai-ni Phunukma",
        "type": "Heroic Myth",
        "theme": "The primordial chieftain who established customs, shifting cultivation (Jhum), and sacred laws."
    }
]

def list_authors() -> List[Dict[str, Any]]:
    return AUTHORS

def list_epics() -> List[Dict[str, Any]]:
    return EPICS
