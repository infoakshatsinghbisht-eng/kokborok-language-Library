# -*- coding: utf-8 -*-
"""
Kokborok Folk Songs, Ballads & Melodic Heritage (Rwchapmung).
============================================================

Documentation of traditional Kokborok oral song genres, including romantic Jaduni ballads,
Garia dance chants, Hojagiri harvest lyrics, and traditional lullabies (Gwnang Rwchapmung).
"""

from typing import Dict, List, Any, Optional

FOLK_SONGS: List[Dict[str, Any]] = [
    {
        "id": "jaduni_01",
        "title": "Jaduni: Haithathora Hachuk-o",
        "genre": "Jaduni (Romantic Hill Ballad)",
        "theme": "Love, yearning, and distance across the mist-shrouded valleys",
        "kokborok_excerpt": "Haithathora hachuk-o sumui rwng-nai / Ang nohor-bai bo-no simano...",
        "english_translation": "On the heights of Haithathora hill the bamboo flute plays / My eyes search the mist, dreaming of my beloved...",
        "cultural_context": "Sung by young lovers across jhum valleys accompanied by the soft notes of the Sumui."
    },
    {
        "id": "garia_chant_01",
        "title": "Baba Garia Rwchapmung",
        "genre": "Garia Festive Procession Chant",
        "theme": "Blessing of hearth, livestock, bumper harvest, and community peace",
        "kokborok_excerpt": "Baba Garia phai-kha nok-o / Rang rwi-di, mai rwi-di, khulum-o chwng...",
        "english_translation": "Lord Baba Garia has entered our threshold / Bestow wealth, bestow grain, with folded hands we bow...",
        "cultural_context": "Chanted in thunderous unison to the beat of the Kham drum as the Garia procession visits every village house."
    },
    {
        "id": "hojagiri_song_01",
        "title": "Hojagiri Mailuma Rwchapmung",
        "genre": "Hojagiri Dance Song",
        "theme": "Praise to Mother Mailuma for full golden grain in the granary",
        "kokborok_excerpt": "Mailuma ma phai-di chwng-ni nok-o / Tai-sa risa kuthuk bo-no...",
        "english_translation": "O Mother Mailuma, step into our home / We spread a freshly woven risa for your blessed feet...",
        "cultural_context": "Sung by Reang women during the acrobatic Hojagiri dance balance ritual."
    },
    {
        "id": "mamita_song_01",
        "title": "Mamita Mai Kwtal Rwchapmung",
        "genre": "Mamita Harvest Song",
        "theme": "Tasting the first grain of new rice with song and sweet rice beer",
        "kokborok_excerpt": "Mai kwtal chá-anw tini / Khum phrok-kha, buphang kwthang...",
        "english_translation": "Today we feast upon the fragrant new rice / The wild blossoms have burst forth and the forest is alive...",
        "cultural_context": "Sung during the community Mamita feast after the harvest has been safely stored in the granary."
    },
    {
        "id": "lullaby_01",
        "title": "Chwrai Thu-di (Traditional Lullaby)",
        "genre": "Lullaby (Gwnang)",
        "theme": "Maternal affection, cradling, and peaceful slumber",
        "kokborok_excerpt": "Thu-di chwrai, thu-di bukhuk / Nokhrom-o tal phrok-kha...",
        "english_translation": "Sleep gently, little child, sleep / In the high sky the silver moon has arisen...",
        "cultural_context": "Sung by mothers rocking infants in cane cradles (Tong)."
    }
]

class SongManager:
    """Manager for querying traditional Kokborok folk songs and ballads."""

    def __init__(self):
        self._songs = FOLK_SONGS

    def all_songs(self) -> List[Dict[str, Any]]:
        return list(self._songs)

    def count(self) -> int:
        return len(self._songs)

    def get_song(self, song_id: str) -> Optional[Dict[str, Any]]:
        sid = song_id.lower().strip()
        for s in self._songs:
            if s["id"] == sid or sid in s["title"].lower():
                return s
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for s in self._songs:
            if (
                q in s["title"].lower() or
                q in s["genre"].lower() or
                q in s["theme"].lower() or
                q in s["kokborok_excerpt"].lower() or
                q in s["english_translation"].lower()
            ):
                results.append(s)
        return results

_SONG_MGR = SongManager()

def list_songs() -> List[Dict[str, Any]]:
    """List all documented traditional Kokborok folk songs."""
    return _SONG_MGR.all_songs()

def get_song(song_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve song details by ID or title (e.g. 'jaduni_01', 'baba_garia')."""
    return _SONG_MGR.get_song(song_id)

def search_songs(query: str) -> List[Dict[str, Any]]:
    """Search songs by keyword."""
    return _SONG_MGR.search(query)
