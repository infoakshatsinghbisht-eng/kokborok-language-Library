# -*- coding: utf-8 -*-
"""
Tripuri Clans, Indigenous Tribes, and Social Structure (Hukumu & Hoda).
========================================================================

Comprehensive catalog of the 19 recognized indigenous tribes and Tripuri clans
of Tripura, their traditional councils (Hoda), settlements, and cultural roles.
"""

from typing import Dict, List, Any, Optional

CLANS: List[Dict[str, Any]] = [
    {
        "name": "Debbarma (Tipra / Puran Tripura)",
        "id": "debbarma",
        "description": "The largest and royal indigenous clan of Tripura. Historically founders of the Manikya Kingdom; native speakers of standard Kokborok.",
        "traditional_settlement": "West Tripura, Khowai, Gomati, Agartala plains and valleys",
        "cultural_role": "Custodians of royal traditions, literary standardization, and classical Rajmala chronicles.",
        "council_name": "Tripura Kshatriya Samaj / Tipra Hoda"
    },
    {
        "name": "Reang (Bru)",
        "id": "reang",
        "description": "Second largest indigenous community of Tripura, renowned for the world-famous acrobatic Hojagiri dance.",
        "traditional_settlement": "Kanchanpur, Panisagar, North Tripura, Dhalai, Jampui lowlands",
        "cultural_role": "Famed for Hojagiri dance balanced on earthen pitchers, shifting cultivation, and rich oral folk songs.",
        "council_name": "Rai Council (Katha Hoda)"
    },
    {
        "name": "Jamatia",
        "id": "jamatia",
        "description": "Martial and agricultural tribe with a tightly-knit, democratic apex socio-cultural governance system.",
        "traditional_settlement": "Udaipur, Gomati, Amarpur, Khowai",
        "cultural_role": "Celebrated for the Garia Puja procession, strict social solidarity, and traditional community dispute resolution.",
        "council_name": "Jamatia Hoda (headed by two Okras)"
    },
    {
        "name": "Noatia (Tripura)",
        "id": "noatia",
        "description": "Close kinsmen of the Debbarma clan, known historically as 'New Tripuris' with vibrant festive celebrations.",
        "traditional_settlement": "South Tripura, Belonia, Santirbazar",
        "cultural_role": "Deeply devoted to the Garia festival and traditional jhum agriculture.",
        "council_name": "Noatia Samaj"
    },
    {
        "name": "Kalai",
        "id": "kalai",
        "description": "An ancient Bodo-Garo Kokborok-speaking sub-tribe renowned for handloom weaving and bamboo basketry.",
        "traditional_settlement": "Teliamura, Khowai, Amarpur",
        "cultural_role": "Masters of bamboo traps, fish nets, and forest lore.",
        "council_name": "Kalai Hoda"
    },
    {
        "name": "Murasing",
        "id": "murasing",
        "description": "An indigenous clan renowned for bilingual Kokborok traditions and deep musical heritage.",
        "traditional_settlement": "South Tripura, Gomati",
        "cultural_role": "Distinguished folk musicians playing the Sumui and Sarinda.",
        "council_name": "Murasing Samaj"
    },
    {
        "name": "Uchoi (Uchai)",
        "id": "uchoi",
        "description": "A close linguistic relative of the Reang, retaining ancient animistic shamanic practices and dances.",
        "traditional_settlement": "Amarpur, Gomati hills",
        "cultural_role": "Preservers of ancient ritual chants and seasonal forest festivals.",
        "council_name": "Uchoi Council"
    },
    {
        "name": "Halam (Molsom, Kaipeng, Rupini, Koloi)",
        "id": "halam",
        "description": "A confederation of 12 sub-clans (Dafas) possessing rich folklore, vibrant handloom shawls, and distinct dialects.",
        "traditional_settlement": "Dhalai, Khowai, North Tripura",
        "cultural_role": "Known for the Mai-Kutung harvest festival and intricate textile patterns.",
        "council_name": "Halam Baris / Rai Council"
    },
    {
        "name": "Chakma",
        "id": "chakma",
        "description": "Theravada Buddhist indigenous tribe with distinct script (Ajha pat) and the vibrant Biju festival.",
        "traditional_settlement": "North Tripura, Pecharthal, Kanchanpur, Dhalai",
        "cultural_role": "Preservers of ancient Pali-influenced Buddhist manuscripts and temple festivals.",
        "council_name": "Chakma Autonomous Council"
    },
    {
        "name": "Mog",
        "id": "mog",
        "description": "Arakanese-descent Theravada Buddhist tribe famous for the Wah festival and picturesque Kyang monasteries.",
        "traditional_settlement": "South Tripura, Sabroom, Belonia",
        "cultural_role": "Celebrated for the Wah festival, sky lanterns (Phanush), and monastery traditions.",
        "council_name": "Mog Buddhist Council"
    },
    {
        "name": "Garo",
        "id": "garo",
        "description": "Matrilineal Tibeto-Burman tribe closely cognate to the Kokborok people, famous for the Wangala 100-drum festival.",
        "traditional_settlement": "Khowai, Dhalai",
        "cultural_role": "Wangala harvest dance and ancient matrilineal kinship traditions.",
        "council_name": "Garo Union"
    },
    {
        "name": "Lushai / Mizo",
        "id": "lushai",
        "description": "Highland community of Jampui Hills, famed for high literacy, orange plantations, and the Cheraw bamboo dance.",
        "traditional_settlement": "Jampui Hills, North Tripura",
        "cultural_role": "Orange festivals, choir singing, and bamboo dance heritage.",
        "council_name": "Jampui Hills Council"
    }
]

class ClanManager:
    """Manager for querying Tripura's indigenous tribes and clans."""

    def __init__(self):
        self._clans = CLANS
        self._clans_by_id = {c["id"]: c for c in self._clans}

    def all_clans(self) -> List[Dict[str, Any]]:
        return list(self._clans)

    def count(self) -> int:
        return len(self._clans)

    def get_clan(self, clan_id: str) -> Optional[Dict[str, Any]]:
        cid = clan_id.lower().strip()
        for c in self._clans:
            if c["id"] == cid or cid in c["name"].lower():
                return c
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for c in self._clans:
            if (
                q in c["name"].lower() or
                q in c["description"].lower() or
                q in c["traditional_settlement"].lower() or
                q in c["cultural_role"].lower()
            ):
                results.append(c)
        return results

_CLAN_MGR = ClanManager()

def list_clans() -> List[Dict[str, Any]]:
    """List all major documented clans and indigenous tribes of Tripura."""
    return _CLAN_MGR.all_clans()

def get_clan(clan_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve clan details by clan ID or name (e.g. 'debbarma', 'reang', 'jamatia')."""
    return _CLAN_MGR.get_clan(clan_id)

def search_clans(query: str) -> List[Dict[str, Any]]:
    """Search clans by keyword."""
    return _CLAN_MGR.search(query)
