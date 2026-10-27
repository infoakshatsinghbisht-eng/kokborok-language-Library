# -*- coding: utf-8 -*-
"""
Kokborok Traditional Culinary Art, Food Culture & Kitchen Heritage (Mui Borok).
================================================================================

Comprehensive documentation of authentic Tripuri gastronomy, indigenous fermentation (Berma),
bamboo shoot preparations, hill ingredients, and oil-free herbal cooking methods.
"""

from typing import Dict, List, Any, Optional

DISHES: List[Dict[str, Any]] = [
    {
        "name": "Chakhwi",
        "category": "Zero-Oil Alkaline Stew",
        "ingredients": "Bamboo shoots (muya), green papaya, jackfruit seeds, pork or freshwater fish, Khar (alkaline ash extract from banana skin / bamboo), Berma, ginger, fiery green chilies, rice paste",
        "description": "The national culinary soul of the Tripuri people. A gentle, oil-free stew thickened with rice flour and balanced with natural alkaline Khar and pungent Berma.",
        "cultural_context": "Centerpiece of family meals, harvest feasts, and community gatherings across all 19 tribes."
    },
    {
        "name": "Muya Awandru",
        "category": "Bamboo Shoot Rice Broth",
        "ingredients": "Tender young bamboo shoots (muya), smooth rice flour batter, Berma, green chillies, wild mountain coriander / sweet basil leaves, salt",
        "description": "A comforting, velvet-smooth broth made by simmering tender bamboo shoots in a silky rice-flour soup flavored with savory Berma and aromatic forest herbs.",
        "cultural_context": "Staple comfort food during monsoon season when bamboo shoots emerge abundantly in the hills."
    },
    {
        "name": "Gudok",
        "category": "Bamboo-Steamed Mashed Stew",
        "ingredients": "Fermented fish (Berma), bamboo shoots, yardlong beans, potatoes, jackfruit seeds, green chilies, garlic cloves",
        "description": "Traditionally cooked inside a fresh, sealed green bamboo stem (wa) directly over an open wood fire, then pounded into a rustic, fragrant mash using a bamboo stick.",
        "cultural_context": "Ancient jhum field delicacy; the green bamboo imparts a distinctive sweet woody aroma found nowhere else."
    },
    {
        "name": "Mosdeng (Mosdeng Serma)",
        "category": "Spicy Pounded Chutney",
        "ingredients": "Charcoal-roasted Berma, roasted fiery bird's eye chilies, shallots, garlic, salt",
        "description": "An intense, spicy chutney made by pounding roasted fermented fish with fiery mountain chilies and sweet shallots in a wooden mortar.",
        "cultural_context": "The indispensable daily condiment served alongside steaming plates of hot hill rice (mairong)."
    },
    {
        "name": "Wahan Mosdeng",
        "category": "Meat Salad / Side Dish",
        "ingredients": "Boiled tender pork with rind, roasted green chilies, thinly sliced ginger slivers, chopped onions, salt, fresh mountain coriander",
        "description": "A celebrated pork salad made by tossing succulent boiled pork with roasted fiery chilies, ginger, and fresh herbs without a single drop of cooking oil.",
        "cultural_context": "Festive delicacy served during Garia Puja, Buisu, weddings, and winter feasts."
    },
    {
        "name": "Tokhan Mosdeng",
        "category": "Country Chicken Mash",
        "ingredients": "Charcoal-grilled country chicken, pounded green chilies, garlic, roasted Berma, onion slivers",
        "description": "Rustic shredded country chicken pounded with smoky roasted chilies and aromatic herbs.",
        "cultural_context": "Served to honored guests during village visits and ancestral ceremonies."
    },
    {
        "name": "Bangui (Awan Bangui)",
        "category": "Steamed Sticky Rice Cake",
        "ingredients": "Indigenous sticky hill rice (Goria or Binni rice), light ginger, chopped pork belly or cashews, wrapped tightly in wild Lairu leaves",
        "description": "A fragrant, cylindrical steamed cake made by packing sticky glutinous rice and ginger into fresh wild leaves, bound with cane strips, and boiled until tender.",
        "cultural_context": "Traditional food packed by hunters and farmers traveling into deep forests; popular during festivals."
    },
    {
        "name": "Mwkhwi",
        "category": "Sour Fruit Delicacy / Relish",
        "ingredients": "Green mango (thaichu) or olive (belpho), crushed Berma, red chili powder, salt, mustard seed",
        "description": "A tangy, mouth-watering sour fruit relish prepared to cleanse the palate after heavy meals.",
        "cultural_context": "Eaten during the hot summer months across Tripura villages."
    },
    {
        "name": "Berma",
        "category": "Fermented Fish Foundation",
        "ingredients": "Small freshwater fish (puthi), stored in earthen jars and fermented for months with salt",
        "description": "The foundational umami cornerstone of Kokborok cuisine. Dried, salted, and naturally fermented in airtight terracotta pots until pungent and savory.",
        "cultural_context": "Essential in almost every authentic Kokborok dish, imparting deep flavor and natural probiotics."
    }
]

class CuisineManager:
    """Manager for querying Kokborok culinary heritage and traditional dishes."""

    def __init__(self):
        self._dishes = DISHES

    def all_dishes(self) -> List[Dict[str, Any]]:
        return list(self._dishes)

    def count(self) -> int:
        return len(self._dishes)

    def get_dish(self, name: str) -> Optional[Dict[str, Any]]:
        n_low = name.lower().strip()
        for d in self._dishes:
            if d["name"].lower().startswith(n_low) or n_low in d["name"].lower():
                return d
        return None

    def by_category(self, category: str) -> List[Dict[str, Any]]:
        c_low = category.lower().strip()
        return [d for d in self._dishes if c_low in d["category"].lower()]

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for d in self._dishes:
            if (
                q in d["name"].lower() or
                q in d["ingredients"].lower() or
                q in d["description"].lower() or
                q in d["cultural_context"].lower()
            ):
                results.append(d)
        return results

_CUISINE_MGR = CuisineManager()

def list_cuisine() -> List[Dict[str, Any]]:
    """List all documented traditional Kokborok dishes."""
    return _CUISINE_MGR.all_dishes()

def get_dish(name: str) -> Optional[Dict[str, Any]]:
    """Retrieve dish details by name (e.g. 'chakhwi', 'gudok', 'mosdeng', 'bangui')."""
    return _CUISINE_MGR.get_dish(name)

def search_cuisine(query: str) -> List[Dict[str, Any]]:
    """Search dishes by ingredient or keyword."""
    return _CUISINE_MGR.search(query)
