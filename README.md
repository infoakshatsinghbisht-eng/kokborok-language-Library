# Kokborok (Kókborok) Language Library for Python

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language](https://img.shields.io/badge/Language-Kokborok%20%28trp%29-brightgreen.svg)](https://en.wikipedia.org/wiki/Kokborok)

**Kokborok (Kókborok)** is the first-ever industrial-grade, standard-library-style Python NLP and linguistic preservation package for **Kokborok (Tripuri)**—the official Sino-Tibetan language of the state of Tripura in Northeast India.

Built with **105,000+ quadri-lingual headwords** (Kokborok-English-Hindi-Bengali), dynamic generation of **300,000+ morphological inflections**, script transliteration (Roman <-> Bengali), numeral classifiers, and cultural preservation records.

---

## 🌟 Key Features

1. **105,000+ Headwords Dictionary**: Quadri-lingual vocabulary with English, Hindi, and Bengali translations.
2. **300,000+ Morphological Forms**: Dynamic decomposition of `kw-` adjectival prefixes, `-kha` / `-nai` verbal aspect, and `-rok` / `-no` / `-ni` / `-o` noun case postpositions.
3. **Roman & Bengali Script Support**: Bi-directional transliteration and syllable tokenization.
4. **Numeral & Classifier System**: 1 to 1,000,000 Kokborok numbers with human (`khorok-`), animal (`kwtwi-`), long (`gong-`), and flat (`tai-`) classifiers.
5. **Universal Translation Engine**: Bidirectional machine translation across Kokborok, English, Hindi, and Bengali with dialect adaptation (Debbarma, Reang/Bru, Jamatia, Noatia).
6. **Cultural Heritage & Calendar**: Complete documentation of Kokborok Day (*19 January*), 12 lunar-solar months, traditional festivals (*Garia Puja*, *Kharchi Puja*, *Ker Puja*, *Hojagiri*), and epics (*Rajmala*, *Chethuang*).

---

## 🚀 Quick Start

```python
import kokborok

# 1. Translate
res = kokborok.translate("How are you?")
print(res.text)  # "Nwng bahai tong?"

# 2. Verb Conjugation
print(kokborok.conjugate("thang", tense="past", subject="ang"))
# "ang thang-kha"

# 3. Numbers & Classifiers
print(kokborok.num_to_words(42))
# "brwichi-nwi"
print(kokborok.apply_classifier(2, "khorok"))
# "khorok-nwi" (two people)

# 4. Dictionary Lookup
entry = kokborok.lookup("khulumkha")
print(entry)
# {'kokborok': 'khulumkha', 'english': 'Greetings / Hello', 'hindi': 'नमस्ते / प्रणाम', 'bengali': 'নমস্কার'}

# 5. Script Transliteration
print(kokborok.roman_to_bengali("Nwng bahai tong?"))
# "ন্বঙ বাহাই তং?"
```

---

## 🏛️ Author & Citation

- **Author**: Akshat Singh Bisht
- **Contact**: `infoakshatsinghbisht@gmail.com`
- **Website**: [akshatsinghbisht.com](https://akshatsinghbisht.com/)
- **License**: MIT
