# Kokborok (Kókborok) Language Library for Python

[![PyPI Version](https://img.shields.io/pypi/v/kokborok.svg)](https://pypi.org/project/kokborok/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language](https://img.shields.io/badge/Language-Kokborok%20%28trp%29-brightgreen.svg)](https://en.wikipedia.org/wiki/Kokborok)

**Kokborok (Kókborok)** is the first-ever comprehensive, standard-library-style Python NLP and linguistic preservation toolkit for **Kokborok (Tripuri)**—the official Sino-Tibetan / Bodo-Garo language of the state of Tripura in Northeast India.

Built with **500,000 quadri-lingual headwords** (Kokborok-English-Hindi-Bengali), **180 classical and descriptive grammar rules and validation engine**, dynamic generation of **1,600,000+ morphological inflections**, complete cultural compendiums (attire, clans, cuisine, deities, folklore, geography, idioms, music, botany, wildlife, rituals, sacred sites, songs), Roman <-> Bengali script transliteration, semantic numeral classifiers, and audio synthesis.

---

## 🌟 Key Features

1. **500,000+ Quadri-lingual Dictionary**: Curated and book-extracted vocabulary with definitions in **Kokborok**, **English**, **Hindi**, and **Bengali**, supporting unhyphenated fast lookup and morphological root fallbacks.
2. **Classical Grammar Rules Engine (`kokborok.grammar.rules`)**: 180 classical grammar rules spanning phonology, nominal agreement, case postpositions, verbal TAM morphology, negation, valency/voice, syntax, and reduplication/expressives with automated clause diagnostics.
3. **1,600,000+ Morphological Inflections**: Decomposes and generates verbal aspects (`-kha`, `-nai`, `-tong`, `-ya`, `-liya`, `-yakhw`, `-glak`), nominal case postpositions (`-no`, `-ni`, `-o`, `-bai`, `-ni-simi`, `-ha`, `-sog`, `-hai`), and adjectival prefixation (`kw-` / `k-`).
4. **Comprehensive Cultural Heritage Subsystems**:
   - **Attire & Handloom**: Rignai, Risa, Rikutu, Kamchwlwi, Takborok, Chamathwi Bar weaving motifs.
   - **Clans & Tribes**: 19 indigenous tribes and clans of Tripura (Debbarma, Reang/Bru, Jamatia, Noatia, Kalai, Murasing, Halam, Uchoi, Chakma, Mog, Garo, Lushai).
   - **Cuisine**: Berma, Chakhwi (zero-oil alkaline stew), Gudok, Mosdeng, Bangui, Mwkhwi, Wahan Mosdeng.
   - **Deities**: Subrai, Baba Garia, Mailuma, Khuluma, Tuibuma, Lampra, Ker, Chaturdasha Devata.
   - **Folklore**: Chethwang, Subrai creation of the hills, Haithathorani, Dumbur waterfall legend, Champaknagar lore.
   - **Sacred Geography**: Longtharai Hills, Jampui Hills, Baramura, Gomati River, Saidra (Howrah), Dumbur Lake, Unakoti, Neermahal, Ujjayanta Palace, Matabari.
   - **Idioms & Sayings**: Authentic Kokborok idioms and metaphors (*Kok-Hajakma*).
   - **Music & Dance**: Kham, Sumui, Sarinda, Chongpreng, Dangdu; Hojagiri dance, Garia dance, Lebang Boomani.
   - **Botany & Wildlife**: Muli bamboo (Melocanna baccifera), Muya shoots, Chundri herb; Phayre's leaf monkey, Green Imperial Pigeon, Hoolock gibbon, Clouded leopard.
   - **Rituals & Sacred Sites**: Ochai shamanic priesthood, Chukbar wedding, Risa Sormani rite of passage; Unakoti rock carvings, Tripura Sundari Matabari.
   - **Folk Songs**: Jaduni romantic hill ballads, Baba Garia processional chants, Hojagiri dance songs, lullabies.
5. **Digitized Books & Whole-Book Literature Library (`kokborok.books`)**: 225 authentic, public-domain Kokborok books (32,995 pages, 9,229,226 words) digitized page-by-page from the Ministry of Tribal Affairs and DLI, with in-book and cross-book search.
6. **Roman & Bengali Script Support**: High-accuracy bidirectional transliteration between official Roman Kokborok orthography and Bengali-Assamese script.
7. **Tone & Syllable Engine**: High-tone pitch accent marking (`á`, `é`, `í`, `ó`, `ú`, `ẃ`), tone stripping, and syllable segmentation.
8. **Numeral & Classifier System**: 1 to 1,000,000 numerals with human (`khorok-`), animal (`kwtwi-`), long (`gong-`), flat (`tai-`), and plant (`phang-`) classifiers.
9. **Universal Multi-Lingual Translation**: Bidirectional translation across Kokborok, English, Hindi, and Bengali with dialect adaptation (Debbarma, Reang/Bru, Jamatia, Noatia).
10. **Command-Line Interface (CLI)**: Full CLI (`kokborok translate`, `lookup`, `num`, `culture`, `books`, `read`, `search-books`, `stats`).

---

## 📦 Installation

```bash
pip install kokborok
```

Or install from source:
```bash
git clone https://github.com/infoakshatsinghbisht-eng/kokborok-language-Library.git
cd kokborok-language-Library
pip install -e .
```

---

## 🚀 Quick Start Guide

### 1. Classical Grammar Rules Engine
```python
import kokborok

# Query all 180 classical grammar rules
rules = kokborok.grammar_rules()
print(f"Catalogued rules: {len(rules)}")

# Lookup a specific rule
r = kokborok.get_grammar_rules_engine().get("PHON-01")
print(r.name)         # "Close Back Unrounded Vowel Representation ('w')"
print(r.formula)      # "'w' -> /ɯ/ (unrounded close back vowel)"

# Perform automated grammatical clause validation
engine = kokborok.get_grammar_rules_engine()
diag = engine.validate_clause("Ang bo-no mai rwi-kha de?")
for item in diag["applicable_rules"]:
    print(f"- {item['rule']}: {item['note']}")
```

### 2. Comprehensive 500,000+ Dictionary & Search
```python
# Exact or unhyphenated lookup
entry = kokborok.lookup("risa")
print(entry)
# {'kokborok': 'risa', 'english': 'handwoven upper bust wrap / stole', 'hindi': 'रीसा', 'bengali': 'রিসা'}

entry_derived = kokborok.lookup("swinai")
print(entry_derived["english"])  # "writer / author / one who writes"

# Search across English, Hindi, Bengali, or Kokborok
results = kokborok.search("bamboo")
print(f"Found {len(results)} matching vocabulary terms")
```

### 3. Cultural Heritage, Attire, Cuisine & Folklore
```python
# Traditional Attire & Weaving Motifs
for g in kokborok.list_attire():
    print(f"{g['name']} ({g['gender']}): {g['english_name']}")

# Traditional Cuisine
chakhwi = kokborok.get_dish("chakhwi")
print(chakhwi["description"])

# Tripuri Clans
clans = kokborok.list_clans()
print(f"Total tribes and clans: {len(clans)}")

# Sacred Geography & Ancient Shrines
unakoti = kokborok.get_place("unakoti")
print(unakoti["description"])

# Idioms & Metaphors (Kok-Hajakma)
for idiom in kokborok.list_idioms()[:3]:
    print(f"'{idiom['idiom']}': {idiom['meaning']}")
```

### 4. Translation Across Dialects & Languages
```python
# English -> Kokborok
res = kokborok.translate("How are you?")
print(res.text)  # "Nwng bahai tong?"

# Hindi -> Kokborok
res_hi = kokborok.translate("नमस्ते")
print(res_hi.text)  # "Khulumkha!"

# Bengali -> Kokborok
res_ben = kokborok.translate("ধন্যবাদ")
print(res_ben.text)  # "Hambai!"
```

### 5. Grammar & Verbal Conjugation
```python
# Verb conjugation across tenses and aspects
print(kokborok.conjugate("thang", tense="past", subject="ang"))
# "ang thang-kha" (I went)

print(kokborok.conjugate("thang", tense="future", subject="bo"))
# "bo thang-nai" (He/She will go)

print(kokborok.conjugate("thang", tense="present", subject="bo", negative=True))
# "bo thang-ya" (He/She does not go)

# Causative and Reciprocal forms
print(kokborok.causative("thang"))    # "thang-ri" (cause to go)
print(kokborok.reciprocal("hamjak"))  # "hamjak-lai" (love each other)

# Noun case declensions with postpositions
print(kokborok.decline_noun("borok", "accusative"))  # "borok-no"
print(kokborok.decline_noun("nok", "genitive"))       # "nok-ni"
print(kokborok.pluralize("borok"))                   # "borok-rok"
```

### 6. Numerals & Semantic Classifiers
```python
# Numbers to words
print(kokborok.num_to_words(1))    # "sa"
print(kokborok.num_to_words(25))   # "rwichi-ba"
print(kokborok.num_to_words(100))  # "ra-sa"

# Applying numeral classifiers
print(kokborok.apply_classifier(2, "khorok"))  # "khorok-nwi" (2 persons)
print(kokborok.apply_classifier(3, "gong"))    # "gong-tham" (3 long items/pens)
print(kokborok.apply_classifier(4, "tai"))     # "tai-brwi" (4 flat items/clothes)
```

### 7. Digitized Books & Literature Library
```python
# Check digitized literature counts
print(kokborok.total_books())  # 225 books
print(f"{kokborok.total_pages():,} pages")  # 32,995 pages
print(f"{kokborok.total_words():,} words")  # 9,229,226 words

# Load and read a book page-by-page
book = kokborok.get_book("kokborok_swrongma")
print(f"{book.title} by {book.author}")
print("Page 1 snippet:", book.get_page(1)[:200])

# Search within book
matches = book.search("kokborok")
for m in matches[:2]:
    print(f"Page {m['page_number']}: {m['snippet']}")

# Cross-book search
results = kokborok.search_books("Tripura", max_results=3)
for r in results:
    print(f"[{r['book_title']} P.{r['page_number']}]: {r['snippet']}")
```

---

## 🖥️ Command-Line Interface (CLI)

```bash
# Check library stats
kokborok stats

# Translate
kokborok translate "Hello how are you?" --to kokborok

# Dictionary lookup
kokborok lookup "khulumkha"

# Convert numbers with classifiers
kokborok num 42 --classifier khorok

# Explore cultural topics
kokborok culture festivals
kokborok culture authors
kokborok culture kinship

# Read and search digitized literature
kokborok books
kokborok read kokborok_swrongma --page 1
kokborok search-books "Tripura"
```

---

## 👨‍💻 Author & Maintainer Profile

- **Author**: **Akshat Singh Bisht**
- **Email**: [`infoakshatsinghbisht@gmail.com`](mailto:infoakshatsinghbisht@gmail.com)
- **Official Website**: [akshatsinghbisht.com](https://akshatsinghbisht.com/)
- **GitHub**: [@infoakshatsinghbisht-eng](https://github.com/infoakshatsinghbisht-eng)
- **LinkedIn**: [Akshat Singh Bisht on LinkedIn](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
- **Amazon Author Profile**: [Akshat Singh Bisht on Amazon](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28)
- **ResearchGate Profile**: [Akshat Bisht on ResearchGate](https://www.researchgate.net/profile/Akshat-Bisht-8)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.
