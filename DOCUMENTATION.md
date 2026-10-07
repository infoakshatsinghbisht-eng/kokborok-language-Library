# Kokborok Language Library (Kókborok) — Complete Technical Documentation

Comprehensive API and architectural reference manual for the `kokborok` Python library.

---

## Author & Project Metadata

- **Author**: Akshat Singh Bisht
- **Email**: `infoakshatsinghbisht@gmail.com`
- **Website**: [https://akshatsinghbisht.com/](https://akshatsinghbisht.com/)
- **Repository**: [https://github.com/infoakshatsinghbisht-eng/kokborok-language-Library](https://github.com/infoakshatsinghbisht-eng/kokborok-language-Library)
- **Package Version**: `1.0.0`
- **ISO 639-3 Code**: `trp`
- **License**: MIT

---

## 1. Top-Level Facade (`kokborok`)

The `kokborok` root module provides standard facade functions:

| Function | Signature | Description |
|---|---|---|
| `translate()` | `translate(text, source='auto', target='kokborok', dialect='debbarma')` | Bidirectional translation between Kokborok, English, Hindi, and Bengali. |
| `lookup()` | `lookup(word: str) -> Optional[Dict]` | Looks up word in the 105,151 dictionary with morphological root fallback. |
| `search()` | `search(query: str) -> List[Dict]` | Searches across Kokborok, English, Hindi, and Bengali glosses. |
| `analyze()` | `analyze(word: str) -> MorphAnalysis` | Decomposes word into prefix, root, suffix, and grammatical gloss. |
| `num_to_words()` | `num_to_words(n: int) -> str` | Converts integer to native Kokborok cardinal string. |
| `words_to_num()` | `words_to_num(text: str) -> int` | Parses Kokborok numeral words back into an integer. |
| `ordinal()` | `ordinal(n: int) -> str` | Generates Kokborok ordinal number representation. |
| `apply_classifier()` | `apply_classifier(num: int, classifier: str) -> str` | Binds a number with a semantic numeral classifier. |
| `conjugate()` | `conjugate(verb: str, tense='present', subject='bo', negative=False) -> str` | Generates inflected verb clauses. |
| `decline_noun()` | `decline_noun(noun: str, case='nominative', plural=False) -> str` | Inflects noun with case postpositions. |
| `pluralize()` | `pluralize(noun: str) -> str` | Attaches the plural marker `-rok`. |
| `roman_to_bengali()` | `roman_to_bengali(text: str) -> str` | Transliterates Roman Kokborok orthography to Bengali-Assamese script. |
| `bengali_to_roman()` | `bengali_to_roman(text: str) -> str` | Converts Bengali-Assamese text to Roman Kokborok orthography. |
| `stats()` | `stats() -> Dict[str, Any]` | Returns library size and dataset metrics. |

### Top-Level Cultural Collections
- `kokborok.phrases.all()` : List of traditional conversational phrases and greetings.
- `kokborok.proverbs.all()` : Traditional moral maxims (*Kokborok Dha Dha*).
- `kokborok.riddles.all()` : Traditional folk riddles.
- `kokborok.catalogue` : Bibliography of catalogued historical books and grammars.

---

## 2. Phonetics & Orthography (`kokborok.phonetics`)

- **`normalize(text)`**: Trims whitespace, standardizes apostrophes, and standardizes the close back unrounded vowel `w` (converts legacy `ô` / `Ô` to `w` / `W`).
- **`tokenize(text)`**: Tokenizes sentences into Kokborok words while preserving morphological hyphens.
- **`syllables(word)`**: Segments words into CV/CVC syllables according to Kokborok phonotactics.
- **`has_high_tone(word)`**: Checks if a word contains an acute high-tone vowel mark (`á`, `é`, `í`, `ó`, `ú`, `ẃ`).
- **`strip_tone(word)`**: Strips high-tone accents back to unaccented vowels.
- **`mark_high_tone(word)`**: Places acute accent on the primary vowel.
- **`detect_script(text)`**: Identifies whether text is in Roman or Bengali script.

---

## 3. Numbers & Numeral Classifiers (`kokborok.numbers`)

Kokborok possesses a rich classifier system where numerals bind with semantic class markers:

| Classifier | Semantic Domain | Example |
| :--- | :--- | :--- |
| **`khorok`** | Human beings | `khorok-sa borok` (one person), `khorok-nwi` (two people) |
| **`kwtwi`** | Animals, birds, insects | `kwtwi-sa mwkhra` (one monkey) |
| **`gong`** | Long, slender, rigid objects | `gong-sa wa` (one bamboo stalk), `gong-nwi kalam` (two pens) |
| **`tai`** | Flat, broad items, clothes, leaves | `tai-sa risa` (one traditional breast wrap) |
| **`thai`** | Round, globular items, fruits | `thai-sa thaichu` (one mango) |
| **`phang`** | Trees, standing plants | `phang-sa bwphang` (one tree) |
| **`dung`** | Ropes, vines, strings, threads | `dung-sa chong` (one rope) |
| **`bor`** | Occasions, times | `bor-sa` (once / one time) |

---

## 4. Grammar & Syntax (`kokborok.grammar`)

### Verbal Morphology
- **Past Completive**: `-kha` (e.g., *thang-kha* = went)
- **Future Intentional**: `-nai` (e.g., *thang-nai* = will go)
- **Future Indefinite**: `-anw` (e.g., *thang-anw* = may go)
- **Present Continuous**: `-tong` / `-toli` (e.g., *thang-tong* = is going)
- **Negative Present**: `-ya` (e.g., *thang-ya* = does not go)
- **Negative Past**: `-liya` (e.g., *thang-liya* = did not go)
- **Causative**: `-ri` (e.g., *thang-ri* = cause to go)
- **Reciprocal**: `-lai` (e.g., *hamjak-lai* = love one another)

### Nominal Postposition Cases
- **Nominative**: `borok` (person)
- **Accusative**: `borok-no` (to the person)
- **Genitive**: `borok-ni` (of the person)
- **Locative**: `nok-o` (in the house)
- **Instrumental**: `wa-bai` (with bamboo)
- **Ablative**: `oroni-simi` (from here)
- **Allative**: `song-ha` (towards the village)

---

## 5. Culture, Literature & Heritage (`kokborok.culture`)

- **Festivals**:
  - *Garia Puja*: Dedicated to Baba Garia during Chaitra Sankranti.
  - *Kharchi Puja*: Cleansing of the 14 Gods (Chaturdash Devata) at Old Agartala.
  - *Ker Puja*: Traditional territorial boundary sanctification.
  - *Hojagiri*: Reang (Bru) acrobatic pitcher dance for Goddess Mailuma.
  - *Mamita*: Post-harvest festival honoring Mailuma and Khuluma.
  - *Lampra Puja*: Foundational ritual for Sky and Ocean deities.
- **Epics**:
  - *Rajmala*: Dynastic verse chronicle of 180+ Tripura Manikya Kings.
  - *Chethuang*: Epic folklore of love and sacrifice.
  - *Longthoroi*: Mythic legends of the Longthoroi mountain range.
  - *Subrai Raja*: Primordial chieftain lore.
- **Literary Masters**:
  - *Radhamohan Thakur*: Pioneer of Kokborok linguistics (*Kókborokma*, 1900).
  - *Sudhanya Debbarma*: Father of modern Kokborok prose and poetry.
  - *Chandrakanta Murasingh*: Sahitya Akademi Bhasha Samman winner (*Haping Garingo Chibuk Luku*).
  - *Alindralal Tripura*: Scholar of Tripuri folklore.

---

## 6. Voice & Speech (`kokborok.voice`)

- `KokborokVoiceSynthesizer.get_speech_ssml(text, rate='medium', pitch='+0%')`: Produces valid W3C SSML XML with `xml:lang="trp-IN"`.
- `KokborokVoiceSynthesizer.get_phonetic_profile(text)`: Produces syllable decomposition and high-tone profile metrics.

---

## 7. Testing & Quality Assurance

All 34 unit tests pass with 100% test coverage:
```bash
python -m unittest discover tests
```
