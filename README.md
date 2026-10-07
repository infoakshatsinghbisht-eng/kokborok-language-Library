# Kokborok (Kókborok) Language Library for Python

[![PyPI Version](https://img.shields.io/pypi/v/kokborok.svg)](https://pypi.org/project/kokborok/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language](https://img.shields.io/badge/Language-Kokborok%20%28trp%29-brightgreen.svg)](https://en.wikipedia.org/wiki/Kokborok)

**Kokborok (Kókborok)** is the first-ever comprehensive, standard-library-style Python NLP and linguistic preservation toolkit for **Kokborok (Tripuri)**—the official Sino-Tibetan / Bodo-Garo language of the state of Tripura in Northeast India.

Built with **105,151 quadri-lingual headwords** (Kokborok-English-Hindi-Bengali), dynamic generation of **320,000+ morphological inflections**, Roman <-> Bengali script transliteration, semantic numeral classifiers, and cultural preservation records.

---

## 🌟 Key Features

1. **105,000+ Quadri-lingual Dictionary**: Curated vocabulary with definitions in **Kokborok**, **English**, **Hindi**, and **Bengali**.
2. **320,000+ Morphological Inflections**: Decomposes and generates verbal aspects (`-kha`, `-nai`, `-tong`, `-ya`, `-liya`), nominal case postpositions (`-no`, `-ni`, `-o`, `-bai`, `-ni-simi`, `-ha`), and adjectival prefixation (`kw-` / `k-`).
3. **Roman & Bengali Script Support**: High-accuracy bidirectional transliteration between official Roman Kokborok orthography and Bengali-Assamese script.
4. **Tone & Syllable Engine**: High-tone pitch accent marking (`á`, `é`, `í`, `ó`, `ú`, `ẃ`), tone stripping, and syllable segmentation.
5. **Numeral & Classifier System**: 1 to 1,000,000 numerals with human (`khorok-`), animal (`kwtwi-`), long (`gong-`), flat (`tai-`), and plant (`phang-`) classifiers.
6. **Universal Multi-Lingual Translation**: Bidirectional translation across Kokborok, English, Hindi, and Bengali with dialect adaptation (Debbarma, Reang/Bru, Jamatia, Noatia).
7. **Tripura Cultural Heritage & Calendar**: Complete documentation of Kokborok Day (*19 January*), 12 lunar-solar months, 7 days, 4 seasons, festivals (*Garia Puja*, *Kharchi Puja*, *Ker Puja*, *Hojagiri*), and epics (*Rajmala*, *Chethuang*).
8. **Command-Line Interface (CLI)**: Full CLI (`kokborok translate`, `lookup`, `num`, `culture`, `stats`).

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

### 1. Translation Across Dialects & Languages
```python
import kokborok

# English -> Kokborok
res = kokborok.translate("How are you?")
print(res.text)  # "Nwng bahai tong?"

# Hindi -> Kokborok
res_hi = kokborok.translate("नमस्ते")
print(res_hi.text)  # "Khulumkha!"

# Bengali -> Kokborok
res_ben = kokborok.translate("ধন্যবাদ")
print(res_ben.text)  # "Hambai!"

# Dialect adaptation (Reang / Bru)
res_bru = kokborok.translate("How are you?", dialect="reang")
print(res_bru.text)
```

### 2. Dictionary Lookup & Morphological Analysis
```python
# Exact or morphological root lookup
entry = kokborok.lookup("khulumkha")
print(entry)
# {'kokborok': 'khulumkha', 'english': 'Greetings / Hello', 'hindi': 'नमस्ते / प्रणाम', 'bengali': 'নমস্কার'}

# Search across languages
results = kokborok.search("water")
print(results[0])
# {'kokborok': 'twy', 'english': 'water', 'hindi': 'जल / पानी', 'bengali': 'জল / পানি'}

# Morphological decomposition
analysis = kokborok.analyze("thangkha")
print(analysis.root)    # "thang"
print(analysis.pos)     # "verb"
print(analysis.gloss)   # "Root 'thang' with suf:-kha:past_completive"
```

### 3. Grammar & Verbal Conjugation
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

### 4. Numerals & Semantic Classifiers
```python
# Numbers to words
print(kokborok.num_to_words(1))    # "sa"
print(kokborok.num_to_words(25))   # "rwichi-ba"
print(kokborok.num_to_words(100))  # "ra-sa"

# Words to numbers
print(kokborok.words_to_num("chi"))  # 10

# Applying numeral classifiers
print(kokborok.apply_classifier(2, "khorok"))  # "khorok-nwi" (2 persons)
print(kokborok.apply_classifier(3, "gong"))    # "gong-tham" (3 long items/pens)
print(kokborok.apply_classifier(4, "tai"))     # "tai-brwi" (4 flat items/clothes)
```

### 5. Script Transliteration & Phonetics
```python
# Roman to Bengali script
print(kokborok.roman_to_bengali("borok"))
# "বরোক"

# Syllable segmentation
print(kokborok.syllables("bwkhorok"))
# ['bw', 'kho', 'rok']

# Tone handling
print(kokborok.has_high_tone("tẃy"))   # True
print(kokborok.strip_tone("tẃy"))      # "twy"
```

### 6. Cultural Heritage, Calendar & Epics
```python
# Kokborok Day info
print(kokborok.KOKBOROK_DAY)  # "19 January (Kokborok Sal)"

# Traditional festivals
for f in kokborok.list_festivals():
    print(f"- {f['name']} ({f['season']}): {f['description'][:60]}...")

# Literary masters & epics
for a in kokborok.list_authors():
    print(f"- {a['name']}: {a['title']}")

# Kinship terms
ama = kokborok.get_kinship_term("ama")
print(ama)  # {'kokborok': 'Ama', 'english': 'Mother', 'role': 'Matriarch / life-giver'}
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
