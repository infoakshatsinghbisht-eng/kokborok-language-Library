# Kokborok Language Library Documentation

Full architectural specification and API reference for `kokborok`.

## 1. Top-Level Facade (`kokborok`)
- `translate(text, source='auto', target='kokborok', dialect='debbarma')`: Bidirectional translation.
- `lookup(word)`: Look up a word in the 105,000+ dictionary with morphological fallback.
- `search(query)`: Search across Kokborok, English, Hindi, and Bengali.
- `analyze(word)`: Morphological decomposition into prefix, root, suffix, and gloss.
- `num_to_words(n)`: Convert integer to Kokborok words.
- `words_to_num(text)`: Convert Kokborok words back to integer.
- `apply_classifier(num, classifier)`: Bind a number with a numeral classifier (`khorok-`, `kwtwi-`, `gong-`, `tai-`).
- `conjugate(verb, tense='present', subject='bo', negative=False)`: Conjugate Kokborok verbs.
- `decline_noun(noun, case='nominative', plural=False)`: Case inflections with postpositions.
- `roman_to_bengali(text)`: Convert Roman Kokborok orthography to Bengali-Assamese script.
- `bengali_to_roman(text)`: Convert Bengali script to Roman Kokborok orthography.
- `list_festivals()`: Documentation of Garia Puja, Kharchi Puja, Ker Puja, Hojagiri, Mamita, Lampra.
- `list_authors()`: Biographies of Radhamohan Thakur, Sudhanya Debbarma, Chandrakanta Murasingh, etc.
- `list_epics()`: Rajmala, Chethuang, Longthoroi, Subrai Raja.
- `stats()`: Package summary metrics.
