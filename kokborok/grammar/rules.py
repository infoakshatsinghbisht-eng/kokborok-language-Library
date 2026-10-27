# -*- coding: utf-8 -*-
"""
Kokborok Classical Grammar Rules Engine (Kokborokma Riti & Niyom).
==================================================================

Comprehensive programmatic catalog and validation engine of 150 classical and
descriptive Kokborok grammatical rules, derived from historical and standard authorities:
- Radhamohan Debbarma Thakur, 'Kok-Borok-ma' (1900)
- Prabhas Chandra Dhar, 'A Grammar of Spoken Kakbarak' (1983)
- Pushpa Pai Karapurkar, 'Kokborok Grammar' (Central Institute of Indian Languages, 1976)
- Binoy Debbarma, 'Concise Kokborok-English-Bengali Dictionary & Learning Course' (TTAADC)
- Dr. Ganesh Baskaran, 'Classifiers in Kokborok' (2015)
- Kokborok Sahitya Sabha & Tripura State Language Standards

Categories:
1. Phonology, Tone & Orthography (Rules PHON-01 to PHON-09)
2. Nominal Agreement, Plurality & Possession (Rules NOM-01 to NOM-12)
3. Case Postpositions & Spatial Relators (Rules CAS-01 to CAS-15)
4. Numeral Classifiers & Quantification (Rules NUM-01 to NUM-13)
5. Verbal Morphology, Tense & Aspect (Rules TAM-01 to TAM-16)
6. Negation & Polarity Frames (Rules NEG-01 to NEG-07)
7. Voice, Valency & Derivations (Rules VOI-01 to VOI-06)
8. Syntax & Clause Structure (Rules SYN-01 to SYN-09)
9. Reduplication, Expressives & Echo Words (Rules EXP-01 to EXP-05)
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class GrammarRule:
    """Represents a formal grammatical rule of the Kokborok language."""
    id: str
    name: str
    category: str
    formula: str
    description: str
    kokborok_examples: List[str]
    english_translations: List[str]
    source_reference: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "formula": self.formula,
            "description": self.description,
            "kokborok_examples": self.kokborok_examples,
            "english_translations": self.english_translations,
            "source_reference": self.source_reference,
        }


CLASSICAL_GRAMMAR_RULES: List[GrammarRule] = [
    # -------------------------------------------------------------
    # 1. PHONOLOGY, TONE & ORTHOGRAPHY (PHON)
    # -------------------------------------------------------------
    GrammarRule(
        id="PHON-01",
        name="Close Back Unrounded Vowel Representation ('w')",
        category="Phonology & Orthography",
        formula="'w' -> /ɯ/ (unrounded close back vowel)",
        description="The letter 'w' in official Roman Kokborok orthography represents the close back unrounded vowel /ɯ/. It acts as a full vowel nucleus and should not be confused with the English glide /w/.",
        kokborok_examples=["kwbang (many / abundant)", "twkma (large bamboo basket)", "swi (to write)", "kwtwi (animal)"],
        english_translations=["many / much", "large bamboo basket", "to write", "animal / beast"],
        source_reference="Kokborok Advisory Committee (1979); Karapurkar (1976) § 1.2"
    ),
    GrammarRule(
        id="PHON-02",
        name="Phonemic High Tone (Khorok Kwrak)",
        category="Phonology & Orthography",
        formula="[Vowel] + [High Tone Accent: á, é, í, ó, ú, ẃ]",
        description="Kokborok has a two-tone system: mid/level tone (unmarked) and high tone (marked with an acute accent). Minimal pairs depend strictly on tone differentiation.",
        kokborok_examples=["khang (to revive / wake up) vs kháng (to fry in oil)", "cha (good) vs chá (to eat)", "lai (leaf) vs lái (bamboo strip)"],
        english_translations=["to wake up vs to fry", "good vs to eat", "leaf vs thin bamboo strip"],
        source_reference="Karapurkar (1976) § 1.6; Pai (1976)"
    ),
    GrammarRule(
        id="PHON-03",
        name="Inherent Relational Prefix 'bw-' / 'b-'",
        category="Phonology & Orthography",
        formula="bw- + [Root] / b- + [Vowel Root]",
        description="Nouns referring to inalienable entities (body parts, anatomical features, parts of plants and trees) take the obligatory morphological prefix 'bw-' or 'b-'.",
        kokborok_examples=["bwkhorok (head)", "bwkhuk (mouth)", "bwphang (tree stem / trunk)", "basa (son / child)"],
        english_translations=["head", "mouth", "tree / trunk", "child / son"],
        source_reference="Radhamohan Thakur (1900) § 14; Karapurkar (1976) § 2.1"
    ),
    GrammarRule(
        id="PHON-04",
        name="Adjectival Formative Prefix 'kw-' / 'k-'",
        category="Phonology & Orthography",
        formula="kw- + [Stative Verb / Adjective Root]",
        description="Qualitative adjectives and stative descriptors are derived from verb roots by prefixing 'kw-' (or 'k-' before certain vowels).",
        kokborok_examples=["kw-thang (alive / green)", "kw-rak (strong / hard)", "kw-chwk (red)", "k-aham (good / fine)"],
        english_translations=["alive / green", "strong / hard", "red / ripe", "good / beautiful"],
        source_reference="Karapurkar (1976) § 4.1; Binoy Debbarma (2013)"
    ),
    GrammarRule(
        id="PHON-05",
        name="Consonant Cluster Simplification and Aspiration",
        category="Phonology & Orthography",
        formula="C1 + r / w (permitted onsets: pr, br, kr, khr, mr, phw, khw)",
        description="Kokborok permits restricted consonant clusters in syllable onsets, notably plosives combined with the rhotic liquid 'r' or glide 'w'. Clusters in codas are strictly forbidden.",
        kokborok_examples=["brai (old man / elder)", "phrok (to pluck / extract)", "krui (does not exist / absent)", "chwrai (young boy / youth)"],
        english_translations=["elder / old man", "to pluck out", "is absent / none", "youth / boy"],
        source_reference="Karapurkar (1976) § 1.4"
    ),
    GrammarRule(
        id="PHON-06",
        name="Nasalized Velar Coda Preservation ('-ng')",
        category="Phonology & Orthography",
        formula="[Syllable Nucleus] + ng /ŋ/",
        description="The velar nasal /ŋ/ (written as 'ng') freely occurs in syllable codas and nominal stems, forming a prominent acoustic marker in Kokborok root vocabulary.",
        kokborok_examples=["ang (I / me)", "chwng (we / us)", "thang (to go)", "bwphang (tree)"],
        english_translations=["I / me", "we / us", "to go", "tree"],
        source_reference="Radhamohan Thakur (1900) § 4"
    ),
    GrammarRule(
        id="PHON-07",
        name="Intervocalic Consonant Softening & Voicing",
        category="Phonology & Orthography",
        formula="/k/ -> [g], /t/ -> [d], /p/ -> [b] / V_V",
        description="Voiceless stops in Kokborok undergo phonetic lenition and voicing when situated between vowels across morpheme or clitic boundaries.",
        kokborok_examples=["nok + -o -> nogo (in the house)", "khorok + sa -> khorogsa (one person)", "bwkhuk + o -> bwkhugo (in the mouth)"],
        english_translations=["in the house", "one person", "in the mouth"],
        source_reference="Karapurkar (1976) § 1.8; Dhar (1983) § 2.3"
    ),
    GrammarRule(
        id="PHON-08",
        name="Epenthetic Hiatus Prevention Clitic ('-i-' / '-wi-')",
        category="Phonology & Orthography",
        formula="C-coda + -i- / V-coda + -wi-",
        description="An epenthetic glide or high front vowel is systematically inserted between consonant-final verb roots and subsequent inflectional affixes to avoid illicit consonantal clusters.",
        kokborok_examples=["thang-i-kha (having gone)", "pha-i-kha (came / arrived)", "nuk-i-tong (is seeing)"],
        english_translations=["having departed", "arrived", "is beholding"],
        source_reference="Karapurkar (1976) § 1.9; Dhar (1983) § 3.1"
    ),
    GrammarRule(
        id="PHON-09",
        name="Glottal Reinforcement in Khorok Kwrak Vowels",
        category="Phonology & Orthography",
        formula="[Vowel] + Acute Tone -> [Tense Phonation / Glottal Catch]",
        description="High-tone (khorok kwrak) syllables in native pronunciation feature tense vocal fold tension and a subtle terminal glottal catch distinguishing minimal pairs.",
        kokborok_examples=["bó (he/she - emphatic) vs bo (that)", "khá (heart / chest) vs kha (past completive)"],
        english_translations=["he himself vs that", "heart/chest vs completed action"],
        source_reference="Karapurkar (1976) § 1.7; Thakur (1900) § 6"
    ),

    # -------------------------------------------------------------
    # 2. NOMINAL AGREEMENT, PLURALITY & POSSESSION (NOM)
    # -------------------------------------------------------------
    GrammarRule(
        id="NOM-01",
        name="General Nominal Plural Suffix '-rok'",
        category="Nominal Agreement",
        formula="[Noun Stem] + -rok",
        description="The universal plural marker '-rok' attaches to both animate and inanimate nouns, indicating multiplicity without altering the nominal root stem.",
        kokborok_examples=["borok-rok (people / men)", "nok-rok (houses)", "bwphang-rok (trees)", "kwtwi-rok (animals)"],
        english_translations=["people", "houses", "trees", "animals"],
        source_reference="Karapurkar (1976) § 2.3; Binoy Debbarma (2013)"
    ),
    GrammarRule(
        id="NOM-02",
        name="Human Collective Plural '-song'",
        category="Nominal Agreement",
        formula="[Human Noun / Kinship Term] + -song",
        description="The collective plural suffix '-song' is strictly reserved for human beings, kinship groups, and personal associations, denoting a collective body of kin or peers.",
        kokborok_examples=["chwrai-song (the boys / youngsters)", "apha-song (the fathers / uncles)", "buphrung-song (the guests)"],
        english_translations=["the boys", "the fatherly elders", "the honored guests"],
        source_reference="Radhamohan Thakur (1900) § 18; Karapurkar (1976) § 2.3.2"
    ),
    GrammarRule(
        id="NOM-03",
        name="Adjective Host Plural Displacement",
        category="Nominal Agreement",
        formula="[Noun] + [Adjective] + -rok (NOT *Noun-rok + Adjective)",
        description="When a noun is modified postnominally by an adjective, the plural suffix '-rok' obligatorily detaches from the noun and cliticizes onto the following adjective.",
        kokborok_examples=["chwrai kaham-rok (good children)", "nok kotor-rok (big houses)", "bwrwi chwla-rok (young maidens)"],
        english_translations=["good children", "big houses", "valiant maidens"],
        source_reference="Karapurkar (1976) § 2.3.4; Pushpa Pai (1976)"
    ),
    GrammarRule(
        id="NOM-04",
        name="Genitive Relational Possession",
        category="Nominal Agreement",
        formula="[Possessor NP] + -ni + [Possessed Noun]",
        description="Possession is marked morphologically on the possessor noun or pronoun using the genitive case postposition '-ni'.",
        kokborok_examples=["ani nok (my house)", "bini bukha (his/her heart)", "Tripurani hachuk (hills of Tripura)"],
        english_translations=["my house", "his/her heart", "the hills of Tripura"],
        source_reference="Radhamohan Thakur (1900) § 22"
    ),
    GrammarRule(
        id="NOM-05",
        name="Agentive Nominalizer '-nai'",
        category="Nominal Agreement",
        formula="[Verb Root] + -nai",
        description="Attaching '-nai' to a verb root derives an agentive noun denoting the actor who performs the action (equivalent to English '-er' / '-or').",
        kokborok_examples=["swi-nai (writer / author)", "rwchap-nai (singer)", "thang-nai (traveler / goer)", "khulum-nai (devotee)"],
        english_translations=["writer / author", "singer", "one who goes / traveler", "worshiper / devotee"],
        source_reference="Binoy Debbarma (2013); Karapurkar (1976) § 2.4"
    ),
    GrammarRule(
        id="NOM-06",
        name="Abstract Action Nominalizer '-mung' / '-ma'",
        category="Nominal Agreement",
        formula="[Verb Root] + -mung / -ma",
        description="Derives abstract nouns of state, quality, or process from verbal bases by suffixation of '-mung' or '-ma'.",
        kokborok_examples=["hamjak-mung (love / affection)", "chá-mung (food / eating)", "tong-mung (existence / lifestyle)", "rwng-ma (learning)"],
        english_translations=["love", "food / meal", "way of living", "learning / wisdom"],
        source_reference="Radhamohan Thakur (1900) § 26; Karapurkar (1976) § 2.5"
    ),
    GrammarRule(
        id="NOM-07",
        name="Natural Sex Differentiation in Human Nouns ('-chwla' / '-bwrwi')",
        category="Nominal Agreement",
        formula="[Human Base] + -chwla (male) / -bwrwi (female)",
        description="Kokborok has no arbitrary grammatical gender; natural sex in human beings is marked by postposed lexical specifiers '-chwla' (male) and '-bwrwi' (female).",
        kokborok_examples=["basa-chwla (son / boy)", "basa-bwrwi (daughter / girl)", "sikla-chwla (young bachelor)", "sikla-bwrwi (young maiden)"],
        english_translations=["son", "daughter", "young bachelor", "young maiden"],
        source_reference="Radhamohan Thakur (1900) § 15; Dhar (1983) § 4.1"
    ),
    GrammarRule(
        id="NOM-08",
        name="Gender Classification in Fauna ('-sa' / '-ma')",
        category="Nominal Agreement",
        formula="[Fauna Base] + -sa (sire/male) / -ma (dam/female)",
        description="In birds, animals, and livestock, masculine and feminine distinctions are formed by suffixing '-sa' (male) and '-ma' (female/mother).",
        kokborok_examples=["tok-sa (rooster / cock)", "tok-ma (hen)", "mwkhra-sa (male monkey)", "mwswo-ma (cow)"],
        english_translations=["rooster", "hen", "male monkey", "cow"],
        source_reference="Radhamohan Thakur (1900) § 16; Karapurkar (1976) § 2.2"
    ),
    GrammarRule(
        id="NOM-09",
        name="Augmentative and Diminutive Affixation",
        category="Nominal Agreement",
        formula="[Noun] + -kotor / -ma (augmentative) vs -basa / -chwrai (diminutive)",
        description="Nouns take augmentative markers '-kotor' / '-ma' to express grand or motherly scale, and diminutive markers '-basa' / '-chwrai' for small or juvenile entities.",
        kokborok_examples=["twima-kotor (great river)", "nok-basa (cottage / hut)", "tok-basa (chick / fledgling)"],
        english_translations=["great river", "small hut", "little fledgling"],
        source_reference="Radhamohan Thakur (1900) § 17; Karapurkar (1976) § 2.6"
    ),
    GrammarRule(
        id="NOM-10",
        name="Kinship Inherent Person-Possession ('a-', 'n-', 'b-')",
        category="Nominal Agreement",
        formula="a- (1st) / n- (2nd) / b- (3rd) + [Kinship Root]",
        description="Core kinship terms obligatorily incorporate personal possessive prefixes designating the relationship relative to the speaker, addressee, or third party.",
        kokborok_examples=["a-pha (my father)", "n-pha (your father)", "b-pha (his/her father)", "a-ma (my mother)", "b-ma (his mother)"],
        english_translations=["my father", "your father", "his/her father", "my mother", "his/her mother"],
        source_reference="Radhamohan Thakur (1900) § 12; Karapurkar (1976) § 2.1.2"
    ),
    GrammarRule(
        id="NOM-11",
        name="Compound Noun Root Synthesis",
        category="Nominal Agreement",
        formula="[Noun 1 Root] + [Noun 2 Root] -> [Unified Compound Concept]",
        description="Kokborok productive compounding fuses two root morphemes into a unified lexical head without intervening case markers.",
        kokborok_examples=["tui (water) + ma (great) -> twima (river)", "nok (house) + hor (night) -> nokhor (family/household)", "ha (land) + tai (pass) -> hatai (market)"],
        english_translations=["river", "household family", "market hill pass"],
        source_reference="Radhamohan Thakur (1900) § 28; Dhar (1983) § 5.2"
    ),
    GrammarRule(
        id="NOM-12",
        name="Occupational and Mastery Derivation ('-phang')",
        category="Nominal Agreement",
        formula="[Craft / Domain] + -phang",
        description="The suffix '-phang' derives titles denoting professional mastery, ancestral responsibility, or headship over a domain.",
        kokborok_examples=["haba-phang (master jhum cultivator)", "ochai-phang (chief shaman / head priest)"],
        english_translations=["master farmer", "chief tribal priest"],
        source_reference="Binoy Debbarma (2001); Dhar (1983) § 5.4"
    ),

    # -------------------------------------------------------------
    # 3. CASE POSTPOSITIONS & SPATIAL RELATORS (CAS)
    # -------------------------------------------------------------
    GrammarRule(
        id="CAS-01",
        name="Accusative / Dative Direct & Indirect Object '-no'",
        category="Case Postpositions",
        formula="[Noun / Pronoun] + -no",
        description="Marks definite direct objects (accusative) and indirect recipient arguments (dative). Definite personal pronouns obligatorily take '-no'.",
        kokborok_examples=["Ang bo-no nuk-kha (I saw him/her)", "Chwng borok-no mai rwi-kha (We gave rice to the person)"],
        english_translations=["I saw him/her", "We gave rice to the person"],
        source_reference="Karapurkar (1976) § 2.2.1; Thakur (1900) § 20"
    ),
    GrammarRule(
        id="CAS-02",
        name="Genitive / Possessive Postposition '-ni'",
        category="Case Postpositions",
        formula="[Noun / Pronoun] + -ni",
        description="Expresses possession, origin, composition, and relational association. Attaches to singular or plural noun phrases.",
        kokborok_examples=["Chwng-ni haba (our shifting cultivation / jhum field)", "wa-ni chamathwi (bamboo weaving pattern)"],
        english_translations=["our jhum field", "the bamboo weaving pattern"],
        source_reference="Karapurkar (1976) § 2.2.2"
    ),
    GrammarRule(
        id="CAS-03",
        name="Locative Case Postposition '-o' / '-yo'",
        category="Case Postpositions",
        formula="[Noun Stem] + -o (after consonant) / -yo (after vowel)",
        description="Marks spatial location, interior containment, and temporal occurrence ('in', 'at', 'on', 'during').",
        kokborok_examples=["nok-o (in the house)", "hachuk-o (on the mountain)", "twima-yo (in the river)"],
        english_translations=["in the house", "on the mountain", "in the river"],
        source_reference="Karapurkar (1976) § 2.2.3"
    ),
    GrammarRule(
        id="CAS-04",
        name="Instrumental & Comitative Case '-bai'",
        category="Case Postpositions",
        formula="[Noun / Pronoun] + -bai",
        description="Indicates the instrument or means by which an action is executed ('with', 'by means of'), as well as comitative company ('together with').",
        kokborok_examples=["seng-bai has-kha (cut with a traditional dao / machete)", "ani apha-bai thang-kha (went together with my father)"],
        english_translations=["cut with a machete", "went together with my father"],
        source_reference="Karapurkar (1976) § 2.2.4; Thakur (1900) § 21"
    ),
    GrammarRule(
        id="CAS-05",
        name="Ablative Source Postposition '-simi' / '-ni-simi'",
        category="Case Postpositions",
        formula="[Noun / Pronoun] + (-ni) + -simi",
        description="Denotes point of origin, departure, or temporal commencement ('from', 'since', 'away from').",
        kokborok_examples=["oro-ni-simi thang-di (go away from here)", "Agartala-simi pha-i-kha (arrived from Agartala)"],
        english_translations=["go away from here", "arrived from Agartala"],
        source_reference="Karapurkar (1976) § 2.2.5"
    ),
    GrammarRule(
        id="CAS-06",
        name="Allative Goal Postposition '-ha'",
        category="Case Postpositions",
        formula="[Locational Noun] + -ha",
        description="Marks motion towards a directional destination or goal ('towards', 'unto', 'to the vicinity of').",
        kokborok_examples=["song-ha thang-nai (will go towards the village)", "hachuk-ha gok-kha (climbed up towards the peak)"],
        english_translations=["will go towards the village", "climbed up towards the peak"],
        source_reference="Karapurkar (1976) § 2.2.6"
    ),
    GrammarRule(
        id="CAS-07",
        name="Terminative Limit Postposition '-sog'",
        category="Case Postpositions",
        formula="[Noun / Location] + -sog",
        description="Expresses the boundary or physical limit of an action or distance ('up to', 'as far as', 'until').",
        kokborok_examples=["nok-sog thang-pai-di (go as far as the house)", "sal-sog tong-di (remain until evening/sunset)"],
        english_translations=["go as far as the house", "stay until sunset"],
        source_reference="Binoy Debbarma (2013); Karapurkar (1976)"
    ),
    GrammarRule(
        id="CAS-08",
        name="Benefactive Postposition '-bagwi'",
        category="Case Postpositions",
        formula="[Noun / Pronoun] + -ni + bagwi",
        description="Expresses purpose, benefaction, or cause ('for the sake of', 'in order to', 'because of').",
        kokborok_examples=["nwng tamo-ni bagwi phai? (why / for what reason did you come?)", "ani ama-ni bagwi (for my mother)"],
        english_translations=["why did you come?", "for my mother"],
        source_reference="Karapurkar (1976) § 2.2.8; Debbarma (2013)"
    ),
    GrammarRule(
        id="CAS-09",
        name="Spatial Relator Noun 'bising' (Inside / Within)",
        category="Case Postpositions",
        formula="[Noun] + -ni + bising(-o)",
        description="Functions as an in-depth spatial relational postposition specifying interior containment within an enclosed space.",
        kokborok_examples=["nok-ni bising-o tong-o (is inside the house)", "bukha bising-o (within the heart)"],
        english_translations=["is inside the house", "within the heart"],
        source_reference="Karapurkar (1976) § 2.2.9"
    ),
    GrammarRule(
        id="CAS-10",
        name="Temporal & Directional Relator 'swkang' (Before) and 'ulo' (After)",
        category="Case Postpositions",
        formula="[Event / Clause / NP] + swkang / ulo",
        description="Specifies chronological sequence or relative front/behind position in spatial navigation.",
        kokborok_examples=["chá-mung swkang ya khuk su-di (wash hands before eating)", "ani ulo phai-di (come after me)"],
        english_translations=["wash hands before eating", "come after me"],
        source_reference="Binoy Debbarma (2016); Karapurkar (1976)"
    ),
    GrammarRule(
        id="CAS-11",
        name="Comparative Degree Standard Postposition ('-nikhre')",
        category="Case Postpositions",
        formula="[Standard NP] + -nikhre + [Adjective]",
        description="The standard of comparison in inequality clauses is marked by the postposition '-nikhre' (or dialectal '-nikhri').",
        kokborok_examples=["Bo ani-nikhre kotor (He is older/bigger than me)", "Longtharai Baramura-nikhre chuk-o (Longtharai is higher than Baramura)"],
        english_translations=["He is bigger than me", "Longtharai is higher than Baramura"],
        source_reference="Karapurkar (1976) § 2.2.7; Dhar (1983) § 6.2"
    ),
    GrammarRule(
        id="CAS-12",
        name="Superlative Universal Construction ('joto-nikhre')",
        category="Case Postpositions",
        formula="joto-nikhre + [Adjective Head]",
        description="Superlative status is expressed universally by combining the quantifier 'joto' (all) with the comparative marker '-nikhre'.",
        kokborok_examples=["joto-nikhre kaham (the best of all)", "joto-nikhre chuk hachuk (the highest mountain)"],
        english_translations=["the very best", "the highest mountain"],
        source_reference="Radhamohan Thakur (1900) § 24; Dhar (1983) § 6.3"
    ),
    GrammarRule(
        id="CAS-13",
        name="Spatial Inherent Relator Postpositions ('bwsang-o', 'sal-o')",
        category="Case Postpositions",
        formula="[Noun NP] + (-ni) + [Relator Stem: bwsang / sal] + -o",
        description="Relator nouns denoting spatial topological zones cliticize locative '-o' to function as postpositions ('in front of', 'on top of').",
        kokborok_examples=["bwphang-ni bwsang-o (in front of the tree)", "hachuk-ni sal-o (on the summit of the hill)"],
        english_translations=["in front of the tree", "on top of the hill"],
        source_reference="Karapurkar (1976) § 3.2; Dhar (1983) § 6.4"
    ),
    GrammarRule(
        id="CAS-14",
        name="Purposive Goal Postposition ('-na bagwi')",
        category="Case Postpositions",
        formula="[Verb Root] + -na bagwi / [Noun NP] + -ni bagwi",
        description="Expresses intentional purpose, objective, or cause ('in order to', 'for the explicit purpose of').",
        kokborok_examples=["chá-na bagwi phai-kha (came in order to eat)", "nini bagwi swi-kha (wrote for your sake)"],
        english_translations=["came in order to eat", "wrote for your sake"],
        source_reference="Karapurkar (1976) § 2.2.8; Debbarma (2013)"
    ),
    GrammarRule(
        id="CAS-15",
        name="Similative Role Postposition ('-hai')",
        category="Case Postpositions",
        formula="[Noun / Pronoun] + -hai",
        description="Indicates similarity of appearance, manner, or role ('like', 'in the manner of', 'resembling').",
        kokborok_examples=["borok-hai tong-di (live like a true human being)", "tok-hai ber-o (soars like a bird)"],
        english_translations=["live like a human being", "soars like a bird"],
        source_reference="Radhamohan Thakur (1900) § 25; Dhar (1983) § 6.5"
    ),

    # -------------------------------------------------------------
    # 4. NUMERAL CLASSIFIERS & QUANTIFICATION (NUM)
    # -------------------------------------------------------------
    GrammarRule(
        id="NUM-01",
        name="Mandatory Numeral Classifier Prefixation",
        category="Numeral Classifiers",
        formula="[Classifier] + - + [Numeral] + [Head Noun]",
        description="In Kokborok, numbers do not stand alone when counting nouns; they must obligatorily bind as suffixes to semantic numeral classifiers denoting shape, animacy, or nature.",
        kokborok_examples=["khorok-sa borok (one person)", "thai-nwi thaichu (two mangoes)", "gong-tham kalam (three pens)"],
        english_translations=["one person", "two mangoes", "three pens"],
        source_reference="Karapurkar (1976) § 3.1; Thakur (1900) § 32"
    ),
    GrammarRule(
        id="NUM-02",
        name="Human Classifier 'khorok'",
        category="Numeral Classifiers",
        formula="khorok- + [Numeral] (strictly for humans)",
        description="Specifies human beings, family members, occupational roles, and persons of any gender.",
        kokborok_examples=["khorok-sa chwrai (one boy)", "khorok-tham bwrwi (three women)", "khorok-ba ochai (five shamans)"],
        english_translations=["one child", "three women", "five traditional priests"],
        source_reference="Karapurkar (1976) § 3.1.1"
    ),
    GrammarRule(
        id="NUM-03",
        name="Animal & Fauna Classifier 'kwtwi'",
        category="Numeral Classifiers",
        formula="kwtwi- + [Numeral] (strictly for fauna)",
        description="Categorizes all non-human animals, four-legged beasts, birds, reptiles, fish, and insects.",
        kokborok_examples=["kwtwi-sa mwkhra (one monkey)", "kwtwi-nwi tok (two chickens / birds)", "kwtwi-tham a (three fish)"],
        english_translations=["one monkey", "two birds", "three fish"],
        source_reference="Karapurkar (1976) § 3.1.2; Debbarma (2013)"
    ),
    GrammarRule(
        id="NUM-04",
        name="Long, Slender & Rigid Classifier 'gong'",
        category="Numeral Classifiers",
        formula="gong- + [Numeral]",
        description="Used for elongated, rigid, or cylindrical items like bamboo poles, pens, sticks, trees, flutes, and spears.",
        kokborok_examples=["gong-sa wa (one bamboo stalk)", "gong-nwi sumui (two traditional flutes)", "gong-tham kalam (three pens)"],
        english_translations=["one bamboo stalk", "two bamboo flutes", "three pens"],
        source_reference="Karapurkar (1976) § 3.1.3"
    ),
    GrammarRule(
        id="NUM-05",
        name="Flat, Broad & Textile Classifier 'tai'",
        category="Numeral Classifiers",
        formula="tai- + [Numeral]",
        description="Classifies broad, thin, sheet-like objects such as textiles, garments, leaves, and papers.",
        kokborok_examples=["tai-sa risa (one breast wrap)", "tai-nwi rignai (two traditional wrap-around skirts)", "tai-tham lai (three leaves)"],
        english_translations=["one handwoven risa", "two rignai skirts", "three leaves"],
        source_reference="Karapurkar (1976) § 3.1.4"
    ),
    GrammarRule(
        id="NUM-06",
        name="Round, Spherical & Fruit Classifier 'thai'",
        category="Numeral Classifiers",
        formula="thai- + [Numeral]",
        description="Classifies spherical, globular, or round objects, specifically fruits, seeds, eggs, balls, and pots.",
        kokborok_examples=["thai-sa thailik (one banana)", "thai-nwi tok-twkwi (two chicken eggs)", "thai-tham bukhuk (three earthen pots)"],
        english_translations=["one banana", "two eggs", "three round pots"],
        source_reference="Karapurkar (1976) § 3.1.5"
    ),
    GrammarRule(
        id="NUM-07",
        name="Trees & Standing Botanical Classifier 'phang'",
        category="Numeral Classifiers",
        formula="phang- + [Numeral]",
        description="Classifies rooted, erect botanical organisms such as living trees, shrubs, and bushes.",
        kokborok_examples=["phang-sa bwphang (one standing tree)", "phang-nwi thaichu-phang (two mango trees)"],
        english_translations=["one standing tree", "two mango trees"],
        source_reference="Karapurkar (1976) § 3.1.6"
    ),
    GrammarRule(
        id="NUM-08",
        name="Flexible Strings & Ropes Classifier 'dung'",
        category="Numeral Classifiers",
        formula="dung- + [Numeral]",
        description="Classifies flexible, linear, cord-like items such as vines, ropes, threads, wires, and necklaces.",
        kokborok_examples=["dung-sa chong (one hemp rope)", "dung-nwi khul (two strands of cotton yarn)"],
        english_translations=["one rope", "two strands of thread"],
        source_reference="Karapurkar (1976) § 3.1.7"
    ),
    GrammarRule(
        id="NUM-09",
        name="Cluster and Bunch Classifier ('chor-' / 'khol-')",
        category="Numeral Classifiers",
        formula="chor- + [Numeral]",
        description="Classifies natural clusters, bunches of fruits, or tied sheaves of paddy and crops.",
        kokborok_examples=["chor-sa thaili (one bunch of bananas)", "chor-nwi mai (two sheaves of unhusked rice)"],
        english_translations=["one bunch of bananas", "two sheaves of paddy"],
        source_reference="Baskaran (2015); Chainary (2019) § 3.2"
    ),
    GrammarRule(
        id="NUM-10",
        name="Ring-Shaped and Cylindrical Ornament Classifier ('kan-')",
        category="Numeral Classifiers",
        formula="kan- + [Numeral]",
        description="Strictly classifies ring-shaped, toroidal, or circular ornaments such as bangles, bracelets, and rings.",
        kokborok_examples=["kan-sa khadu (one silver bangle)", "kan-nwi jasem (two traditional necklaces)"],
        english_translations=["one bangle", "two necklaces"],
        source_reference="Baskaran (2015); Dhar (1983) § 7.2"
    ),
    GrammarRule(
        id="NUM-11",
        name="Liquid Droplet Classifier ('phwt-' / 'thip-')",
        category="Numeral Classifiers",
        formula="phwt- + [Numeral]",
        description="Used for droplets of water, dew, tears, blood, or medicine.",
        kokborok_examples=["phwt-sa tui (one drop of water)", "phwt-nwi thwi (two drops of blood)"],
        english_translations=["one drop of water", "two drops of blood"],
        source_reference="Karapurkar (1976) § 4.3.4"
    ),
    GrammarRule(
        id="NUM-12",
        name="Thin Strips and Splits Classifier ('che-' / 'lai-')",
        category="Numeral Classifiers",
        formula="che- + [Numeral]",
        description="Classifies thin split strips of bamboo, reeds, cane, or paper sheets.",
        kokborok_examples=["che-sa wa (one split bamboo strip)", "che-nwi luku (two cane splits)"],
        english_translations=["one split bamboo strip", "two cane splits"],
        source_reference="Karapurkar (1976) § 4.3.5; Baskaran (2015)"
    ),
    GrammarRule(
        id="NUM-13",
        name="Distributive Reduplication of Classifiers",
        category="Numeral Classifiers",
        formula="[Classifier + Numeral] + [Classifier + Numeral]",
        description="Repeating the classifier phrase expresses distributive apportionment ('one by one', 'each person').",
        kokborok_examples=["khorok-sa khorok-sa (person by person / one by one)", "tai-sa tai-sa (piece by piece)"],
        english_translations=["one person each", "piece by piece"],
        source_reference="Baskaran (2015); Karapurkar (1976) § 4.4"
    ),

    # -------------------------------------------------------------
    # 5. VERBAL MORPHOLOGY, TENSE & ASPECT (TAM)
    # -------------------------------------------------------------
    GrammarRule(
        id="TAM-01",
        name="Past Completive Suffix '-kha'",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -kha",
        description="The primary past-tense inflection in Kokborok, indicating an action that has completely occurred or terminated before the speech moment.",
        kokborok_examples=["Ang mai chá-kha (I ate rice)", "Bo thang-kha (He/she went)", "Sal phrok-kha (The sun rose)"],
        english_translations=["I ate rice", "He/she went", "The sun rose"],
        source_reference="Karapurkar (1976) § 5.1.1; Thakur (1900) § 38"
    ),
    GrammarRule(
        id="TAM-02",
        name="Future Intentional & Definite Suffix '-nai'",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -nai",
        description="Marks definite future tense, expressing strong intention, certainty, or scheduled future occurrence.",
        kokborok_examples=["Ang phai-nai (I will come)", "Bo nok-o thang-nai (He will go home)", "Watwi wat-nai (Rain will fall)"],
        english_translations=["I will come", "He will go home", "It will rain"],
        source_reference="Karapurkar (1976) § 5.1.2; Debbarma (2013)"
    ),
    GrammarRule(
        id="TAM-03",
        name="Future Indefinite & Potential Suffix '-anw'",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -anw",
        description="Denotes prospective, conditional, or indefinite future action ('might', 'may', 'shall perhaps').",
        kokborok_examples=["Ang bo-no swi-anw (I might write to him)", "Chwng mai chá-anw (We may eat rice later)"],
        english_translations=["I might write to him", "We may eat rice"],
        source_reference="Karapurkar (1976) § 5.1.3"
    ),
    GrammarRule(
        id="TAM-04",
        name="Present Progressive Auxiliary '-tong' / '-wi tong'",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -tong / [Verb Root] + -wi + tong",
        description="Constructs progressive or continuous aspect, indicating ongoing action in the present moment.",
        kokborok_examples=["Bo mai chá-tong (He is eating rice right now)", "Ang swi-wi tong-o (I am writing)"],
        english_translations=["He is eating rice right now", "I am engaged in writing"],
        source_reference="Karapurkar (1976) § 5.2.1"
    ),
    GrammarRule(
        id="TAM-05",
        name="Present General / Habitual Suffix '-o'",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -o",
        description="Expresses general, timeless truths, habitual customs, and state-of-being in the simple present.",
        kokborok_examples=["Sal gok-thang-o phrok-o (The sun rises in the east)", "Borok mai chá-o (Humans eat rice)"],
        english_translations=["The sun rises in the east", "Humans eat rice"],
        source_reference="Karapurkar (1976) § 5.1.4"
    ),
    GrammarRule(
        id="TAM-06",
        name="Completive Perfect Aspect Marker '-pai' / '-baikha'",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -pai-kha",
        description="Highlights that an action has been completely finished and exhausted in every respect.",
        kokborok_examples=["Mai chá-pai-kha (The meal is completely finished)", "Haba son-pai-kha (The weeding is thoroughly done)"],
        english_translations=["The food has been entirely finished", "The jhum weeding is thoroughly completed"],
        source_reference="Karapurkar (1976) § 5.2.3"
    ),
    GrammarRule(
        id="TAM-07",
        name="Imperative Directive Suffix '-di'",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -di",
        description="Marks standard polite or direct commands addressed to a second person subject.",
        kokborok_examples=["Phai-di! (Come!)", "Mai chá-di! (Eat rice!)", "Swi-di! (Write!)", "Thang-di! (Go!)"],
        english_translations=["Come!", "Eat!", "Write!", "Go!"],
        source_reference="Karapurkar (1976) § 5.3.1; Thakur (1900) § 42"
    ),
    GrammarRule(
        id="TAM-08",
        name="Subjunctive & Conditional Suffix '-khe' / '-ba'",
        category="Tense, Aspect & Mood",
        formula="[Protasis Verb] + -khe / -ba, [Apodosis Clause]",
        description="Forms hypothetical or real conditional clauses ('if ... then').",
        kokborok_examples=["Nwng phai-khe ang thang-nai (If you come, I will go)", "Watwi wat-ba haba thang-ya (If it rains, we won't go to the field)"],
        english_translations=["If you come, I will go", "If it rains, we will not go to the jhum field"],
        source_reference="Karapurkar (1976) § 6.2; Debbarma (2016)"
    ),
    GrammarRule(
        id="TAM-09",
        name="Sequential Converb Clitic ('-wi' / '-i')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root 1] + -wi / -i, [Matrix Verb Clause 2]",
        description="Links actions in temporal succession, indicating that the first action is completed prior to the matrix clause ('having done X, Y').",
        kokborok_examples=["Bo mai chá-wi thang-kha (Having eaten rice, he departed)", "nuk-wi khulum-kha (Having seen, he offered reverence)"],
        english_translations=["Having eaten rice, he left", "Having seen, he bowed"],
        source_reference="Karapurkar (1976) § 5.3.3; Dhar (1983) § 8.1"
    ),
    GrammarRule(
        id="TAM-10",
        name="Concessive Subordinating Clitic ('-phano')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -phano",
        description="Forms concessive subordinate clauses ('even though', 'although', 'notwithstanding').",
        kokborok_examples=["watwi wat-phano thang-nai (Even though it rains, I will go)", "sa-phano khna-ya (Even though told, he does not listen)"],
        english_translations=["Even though it rains, I will go", "Though told, he does not listen"],
        source_reference="Radhamohan Thakur (1900) § 46; Karapurkar (1976) § 6.2.2"
    ),
    GrammarRule(
        id="TAM-11",
        name="Optative & Desiderative Mood ('-thung')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -thung",
        description="Expresses wishes, prayers, blessings, or third-person directives ('may it be so', 'let him/her do').",
        kokborok_examples=["Bo kaham tong-thung! (May he remain well!)", "Pha-i-thung! (Let him come!)"],
        english_translations=["May he remain well!", "Let him come!"],
        source_reference="Radhamohan Thakur (1900) § 43; Karapurkar (1976) § 5.3.2"
    ),
    GrammarRule(
        id="TAM-12",
        name="Inchoative Aspect Marker ('-bai' / '-sik')",
        category="Tense, Aspect & Mood",
        formula="[Adjective / Stative Root] + -bai-kha",
        description="Marks entry into a new physical or qualitative state ('becoming', 'turning into', 'starting to be').",
        kokborok_examples=["kwchwk-bai-kha (has turned red / ripened)", "kotor-bai-kha (has grown large)"],
        english_translations=["has turned red", "has grown big"],
        source_reference="Karapurkar (1976) § 5.2.4; Dhar (1983) § 8.3"
    ),
    GrammarRule(
        id="TAM-13",
        name="Habitual and Iterative Disposition Auxiliary ('-rwng-')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -rwng + [TAM]",
        description="Indicates that an agent is accustomed to performing an action as an established daily routine.",
        kokborok_examples=["thang-rwng-o (is accustomed to going)", "swi-rwng-kha (used to write frequently)"],
        english_translations=["goes customarily", "habitually wrote"],
        source_reference="Karapurkar (1976) § 5.2.5; Dhar (1983) § 8.4"
    ),
    GrammarRule(
        id="TAM-14",
        name="Prospective & Imminent Aspect Frame ('-na sik-kha')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -na sik-kha",
        description="Denotes imminent prospective action on the immediate verge of taking place ('about to do').",
        kokborok_examples=["thang-na sik-kha (is about to leave / on the verge of departure)", "wat-na sik-kha (is about to rain)"],
        english_translations=["about to depart", "about to rain"],
        source_reference="Binoy Debbarma (2013); Dhar (1983) § 8.5"
    ),
    GrammarRule(
        id="TAM-15",
        name="Cohortative and Hortative Marker ('-lai-no')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -lai-no",
        description="Encourages collective group action addressed to peers or companions ('let us all do together').",
        kokborok_examples=["thang-lai-no! (let us all go together!)", "chá-lai-no! (let us all eat together!)"],
        english_translations=["let us go together!", "let us eat together!"],
        source_reference="Radhamohan Thakur (1900) § 47; Dhar (1983) § 8.6"
    ),
    GrammarRule(
        id="TAM-16",
        name="Durative Auxiliary Frame ('-tong-thao')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -tong-thao",
        description="Expresses comfortable, undisturbed continuation of an ongoing activity.",
        kokborok_examples=["chá-tong-thao (keep on enjoying your meal)", "swi-tong-thao (continue writing comfortably)"],
        english_translations=["keep on eating", "continue writing peacefully"],
        source_reference="Karapurkar (1976) § 5.2.6"
    ),

    # -------------------------------------------------------------
    # 6. NEGATION & POLARITY FRAMES (NEG)
    # -------------------------------------------------------------
    GrammarRule(
        id="NEG-01",
        name="General Present & Future Negative '-ya'",
        category="Negation & Polarity",
        formula="[Verb Root] + -ya",
        description="The standard negative verbal suffix in Kokborok. Negates present habitual and prospective future predications.",
        kokborok_examples=["Ang chá-ya (I do not eat / will not eat)", "Bo thang-ya (He is not going)", "Ang rwng-ya (I do not know)"],
        english_translations=["I do not eat / will not eat", "He is not going", "I do not know"],
        source_reference="Karapurkar (1976) § 5.4.1; Thakur (1900) § 44"
    ),
    GrammarRule(
        id="NEG-02",
        name="Past Negative Suffix '-liya'",
        category="Negation & Polarity",
        formula="[Verb Root] + -liya",
        description="Strictly negates past events, indicating that an action did not occur in past time (corresponds to negative of '-kha').",
        kokborok_examples=["Ang thang-liya (I did not go)", "Bo mai chá-liya (He did not eat)", "Chwng nuk-liya (We did not see)"],
        english_translations=["I did not go", "He did not eat", "We did not see"],
        source_reference="Karapurkar (1976) § 5.4.2; Binoy Debbarma (2013)"
    ),
    GrammarRule(
        id="NEG-03",
        name="Prohibitive Negative Frame 'ta-...-di'",
        category="Negation & Polarity",
        formula="ta- + [Verb Root] + -di",
        description="Forms negative commands and warnings ('do not!'). Uses the prohibitive prefix 'ta-' alongside the imperative suffix '-di'.",
        kokborok_examples=["Ta thang-di! (Do not go!)", "Ta cha-di! (Do not eat!)", "Ta swi-di! (Do not write!)"],
        english_translations=["Do not go!", "Do not eat!", "Do not write!"],
        source_reference="Karapurkar (1976) § 5.4.3; Thakur (1900) § 45"
    ),
    GrammarRule(
        id="NEG-04",
        name="Negative Stative Copula 'krui' (Absence / Non-existence)",
        category="Negation & Polarity",
        formula="[Subject NP] + krui (opposite of 'tong')",
        description="Expresses non-existence, absence, or lack of possession ('there is not', 'does not exist', 'have no').",
        kokborok_examples=["Ani nok-o rang krui (I have no money at home)", "Mai krui (There is no rice)"],
        english_translations=["I have no money in my house", "There is no rice available"],
        source_reference="Karapurkar (1976) § 5.4.4"
    ),
    GrammarRule(
        id="NEG-05",
        name="Incompletive 'Not Yet' Negative ('-yakhw')",
        category="Negation & Polarity",
        formula="[Verb Root] + -yakhw",
        description="Specifies that an anticipated event has not yet taken place up to the moment of speech ('not yet').",
        kokborok_examples=["mai chá-yakhw (have not eaten yet)", "pha-i-yakhw (has not arrived yet)"],
        english_translations=["have not eaten yet", "has not yet arrived"],
        source_reference="Karapurkar (1976) § 5.4.5; Thakur (1900) § 49"
    ),
    GrammarRule(
        id="NEG-06",
        name="Discontinuative Negative ('-liya' / 'no longer')",
        category="Negation & Polarity",
        formula="[Verb Root] + -liya (in continuative context)",
        description="Indicates cessation of an ongoing state or habit ('no longer', 'no more').",
        kokborok_examples=["ang thang-liya (I will go no longer)", "bo phai-liya (he comes no more)"],
        english_translations=["I do not go anymore", "he no longer comes"],
        source_reference="Karapurkar (1976) § 5.4.2; Dhar (1983) § 9.2"
    ),
    GrammarRule(
        id="NEG-07",
        name="Negative Inability and Refusal Marker ('-glak')",
        category="Negation & Polarity",
        formula="[Verb Root] + -glak",
        description="Expresses emphatic impossibility, complete physical inability, or firm refusal to act.",
        kokborok_examples=["ang thang-glak (I cannot / will definitely not go)", "chá-glak (refuses to eat)"],
        english_translations=["I cannot go", "refuses to eat"],
        source_reference="Binoy Debbarma (2001); Dhar (1983) § 9.3"
    ),

    # -------------------------------------------------------------
    # 7. VOICE, VALENCY & DERIVATIONS (VOI)
    # -------------------------------------------------------------
    GrammarRule(
        id="VOI-01",
        name="Morphological Causative Suffix '-ri'",
        category="Voice & Derivations",
        formula="[Verb Root] + -ri + [TAM]",
        description="Increases verb valency by adding a causer argument who induces or permits the action ('make someone do', 'cause to go').",
        kokborok_examples=["thang-ri-kha (made him go / sent)", "chá-ri-nai (will feed / cause to eat)", "swi-ri-di (make him write)"],
        english_translations=["caused to go / dispatched", "will feed / cause to eat", "make him write!"],
        source_reference="Karapurkar (1976) § 5.5.1; Pushpa Pai (1976)"
    ),
    GrammarRule(
        id="VOI-02",
        name="Reciprocal Mutual Suffix '-lai'",
        category="Voice & Derivations",
        formula="[Verb Root] + -lai + [TAM]",
        description="Denotes mutual or reciprocal action executed between multiple joint subjects ('each other', 'one another').",
        kokborok_examples=["hamjak-lai-o (love one another)", "khulum-lai-kha (greeted each other)", "kok-sa-lai-nai (will talk to each other)"],
        english_translations=["love each other", "greeted one another", "will converse together"],
        source_reference="Karapurkar (1976) § 5.5.2; Thakur (1900) § 48"
    ),
    GrammarRule(
        id="VOI-03",
        name="Passive & Resultative Suffix '-jak'",
        category="Voice & Derivations",
        formula="[Verb Root] + -jak + [TAM]",
        description="Transforms a transitive action into a passive or resultative state focused on the undergoer.",
        kokborok_examples=["swi-jak-kha (has been written)", "son-jak-kha (has been cleared)", "chá-jak-kha (has been eaten)"],
        english_translations=["has been written down", "has been cleared", "has been eaten"],
        source_reference="Karapurkar (1976) § 5.5.3"
    ),
    GrammarRule(
        id="VOI-04",
        name="Double Causative / Indirect Causative ('-ri-ri-')",
        category="Voice & Derivations",
        formula="[Verb Root] + -ri-ri + [TAM]",
        description="Denotes indirect causation where an initiator commands an intermediary to make an ultimate agent perform the action.",
        kokborok_examples=["swi-ri-ri-kha (had him make the child write)", "son-ri-ri-nai (will have someone arrange jhum clearing)"],
        english_translations=["arranged to have written", "will cause clearing to be arranged"],
        source_reference="Karapurkar (1976) § 5.5.4; Dhar (1983) § 10.2"
    ),
    GrammarRule(
        id="VOI-05",
        name="Benefactive Auxiliary ('-rw-')",
        category="Voice & Derivations",
        formula="[Verb Root] + -rwi + [TAM]",
        description="Marks that the action is performed for the welfare or benefit of another person ('do for someone').",
        kokborok_examples=["swi-rwi-kha (wrote on someone's behalf)", "son-rwi-di (clear the field for him)"],
        english_translations=["wrote for him", "clear the field for him!"],
        source_reference="Radhamohan Thakur (1900) § 50; Dhar (1983) § 10.3"
    ),
    GrammarRule(
        id="VOI-06",
        name="Reflexive Predication Frame ('boba-ba')",
        category="Voice & Derivations",
        formula="boba-ba + [Verb Predicate]",
        description="Reflexive action upon oneself is constructed using the reflexive pronominal base 'boba-ba' (oneself).",
        kokborok_examples=["boba-ba hamjak-o (loves oneself)", "boba-ba nuk-kha (saw himself in the stream)"],
        english_translations=["loves oneself", "saw himself"],
        source_reference="Karapurkar (1976) § 5.5.5; Dhar (1983) § 10.4"
    ),

    # -------------------------------------------------------------
    # 8. SYNTAX & CLAUSE STRUCTURE (SYN)
    # -------------------------------------------------------------
    GrammarRule(
        id="SYN-01",
        name="Canonical Subject-Object-Verb (SOV) Word Order",
        category="Syntax & Clause Structure",
        formula="[Subject NP] + [Object NP] + [Verb Predicate]",
        description="Kokborok is a typologically strict head-final, SOV language. Verb complexes conclude the matrix clause.",
        kokborok_examples=["Ang borok-no mai rwi-kha (I gave rice to the man)", "Bo swi-mung swi-tong (He is writing an essay)"],
        english_translations=["I gave rice to the person", "He is writing a text"],
        source_reference="Karapurkar (1976) § 6.1; Thakur (1900) § 52"
    ),
    GrammarRule(
        id="SYN-02",
        name="Head-Noun Precedence over Adjectives",
        category="Syntax & Clause Structure",
        formula="[Noun Head] + [Adjective Modifier]",
        description="Unlike English, descriptive adjectives follow their head noun in the basic noun phrase structure.",
        kokborok_examples=["nok kotor (a big house)", "chwrai kaham (a good boy)", "risa kwchwk (a red risa breast wrap)"],
        english_translations=["a big house", "a good child", "a red handwoven risa"],
        source_reference="Karapurkar (1976) § 4.2"
    ),
    GrammarRule(
        id="SYN-03",
        name="Quotative Particle & Complementizer 'hwnwi'",
        category="Syntax & Clause Structure",
        formula="[Direct Quote / Thought] + hwnwi + [Reporting Verb]",
        description="Quotations, cognitive beliefs, intentions, and reported speech clauses are closed by the postposed complementizer 'hwnwi'.",
        kokborok_examples=["'Ang thang-nai' hwnwi sa-kha ('I will go', so he said)", "'Watwi wat-nai' hwnwi chwng uansuk-o ('It will rain', so we think)"],
        english_translations=["He said, 'I will go'", "We think that it will rain"],
        source_reference="Karapurkar (1976) § 6.3; Debbarma (2013)"
    ),
    GrammarRule(
        id="SYN-04",
        name="Interrogative Polar Particle '-de' / '-ba'",
        category="Syntax & Clause Structure",
        formula="[Declarative Clause] + de?",
        description="Attaching the enclitic interrogative particle '-de' to the end of a clause converts a statement into a polar yes/no question.",
        kokborok_examples=["Nwng mai chá-kha-de? (Have you eaten rice?)", "Bo phai-nai-de? (Will he come?)"],
        english_translations=["Have you eaten yet?", "Will he come?"],
        source_reference="Karapurkar (1976) § 6.4; Thakur (1900) § 55"
    ),
    GrammarRule(
        id="SYN-05",
        name="Topic and Contrastive Enclitics ('-se' / '-te')",
        category="Syntax & Clause Structure",
        formula="[NP] + -se (topic focus) / -te (contrastive topic)",
        description="Cliticized onto noun phrases to highlight the thematic topic or mark contrast with an alternative topic.",
        kokborok_examples=["Ang-se thang-nai (As for me, I will indeed go)", "Bo-te kaham (He, on the contrary, is fine)"],
        english_translations=["As for me, I will go", "He on the other hand is good"],
        source_reference="Karapurkar (1976) § 6.5; Dhar (1983) § 11.2"
    ),
    GrammarRule(
        id="SYN-06",
        name="Emphatic Focus Enclitic ('-no')",
        category="Syntax & Clause Structure",
        formula="[Focused Word] + -no",
        description="Places exclusive pragmatic emphasis on a word ('this very', 'right now', 'precisely').",
        kokborok_examples=["o-sal-no phai-di (come on this very day!)", "ini-no (right now / this very instant)"],
        english_translations=["come on this very day!", "right this moment"],
        source_reference="Radhamohan Thakur (1900) § 56; Karapurkar (1976) § 6.6"
    ),
    GrammarRule(
        id="SYN-07",
        name="Restrictive and Limiting Enclitic ('-sa')",
        category="Syntax & Clause Structure",
        formula="[NP / Adv] + -sa",
        description="Restricts the scope of predication exclusively to the marked entity ('only', 'merely', 'solely').",
        kokborok_examples=["khorok-sa-sa (only one person)", "mai-sa chá-kha (ate only rice)"],
        english_translations=["only one person", "ate only rice"],
        source_reference="Karapurkar (1976) § 6.7; Dhar (1983) § 11.4"
    ),
    GrammarRule(
        id="SYN-08",
        name="Serial Verb Directional Motion Auxiliary ('-thang' / '-phai')",
        category="Syntax & Clause Structure",
        formula="[Action Verb Root] + -thang (away) / -phai (towards speaker)",
        description="Motion verbs 'thang' (go) and 'phai' (come) bind to preceding lexical verbs to construct directional serial paths.",
        kokborok_examples=["tui-thang (carry away)", "tui-phai (bring here)", "ber-thang (fly away)"],
        english_translations=["take away", "bring here", "fly away"],
        source_reference="Karapurkar (1976) § 6.8; Dhar (1983) § 11.5"
    ),
    GrammarRule(
        id="SYN-09",
        name="Attributive Relative Clause Construction",
        category="Syntax & Clause Structure",
        formula="[Relative Clause Verb + -nai / -ma] + [Head Noun]",
        description="Relative clauses precede their head noun, marked by the agentive suffix '-nai' or nominalizer '-ma'.",
        kokborok_examples=["haba son-nai borok (the man who clears the jhum field)", "ani swi-ma chithi (the letter that I wrote)"],
        english_translations=["the jhum clearing man", "the letter that I composed"],
        source_reference="Karapurkar (1976) § 6.9; Dhar (1983) § 11.6"
    ),

    # -------------------------------------------------------------
    # 9. REDUPLICATION, EXPRESSIVES & ECHO WORDS (EXP)
    # -------------------------------------------------------------
    GrammarRule(
        id="EXP-01",
        name="Total Reduplication for Iteration & Distributivity",
        category="Expressives & Reduplication",
        formula="[Word] + - + [Identical Word]",
        description="Full repetition of a nominal, adjectival, or verbal stem expresses distribution ('one by one', 'piece by piece') or intense continuity.",
        kokborok_examples=["sa-sa (one by one)", "kwtwi-kwtwi (each and every animal)", "ham-ham (very good / continually pleasant)"],
        english_translations=["one by one", "every single animal", "very good / delightful"],
        source_reference="Karapurkar (1976) § 7.1; Debbarma (2016)"
    ),
    GrammarRule(
        id="EXP-02",
        name="Sound Symbolic Sensory Ideophones (Onomatopoeia)",
        category="Expressives & Reduplication",
        formula="[Sound / Movement Mimetic Pair]",
        description="Expressive sensory words vividly mimic sounds, light reflections, flow of water, and psychological states.",
        kokborok_examples=["chwng-chwng (shining brightly / glittering)", "phere-phere (fluttering lightly like butterfly wings)", "drok-drok (pounding heavily)"],
        english_translations=["glistening intensely", "lightly fluttering", "palpitating / heavy thumping"],
        source_reference="Karapurkar (1976) § 7.2; Binoy Debbarma (2013)"
    ),
    GrammarRule(
        id="EXP-03",
        name="Associative Echo-Word Compounds ('X-sX')",
        category="Expressives & Reduplication",
        formula="[Base Word] + - + [Echo Stem with s- onset]",
        description="Forms collective associative compounds meaning 'X and related articles/belongings' by echoing the word with an initial 's-'.",
        kokborok_examples=["mai-sai (rice and accompanying food)", "tok-sok (poultry and related fowl)", "nok-sok (homestead and domestic quarters)"],
        english_translations=["food and meals", "birds and fowl", "homestead and dwellings"],
        source_reference="Radhamohan Thakur (1900) § 58; Karapurkar (1976) § 7.3"
    ),
    GrammarRule(
        id="EXP-04",
        name="Fluvial and Atmospheric Motion Ideophones",
        category="Expressives & Reduplication",
        formula="[Motion Ideophone Pair]",
        description="Specialized phonaesthemes describing water flowing through hill streams, wind breezes, and mountain storms.",
        kokborok_examples=["sere-sere (continuous smooth streamflow)", "khoro-khoro (swift rushing torrent)", "dhir-dhir (gentle mountain breeze)"],
        english_translations=["cascading smoothly", "swiftly rushing", "blowing gently"],
        source_reference="Binoy Debbarma (2013); Dhar (1983) § 12.2"
    ),
    GrammarRule(
        id="EXP-05",
        name="Chromatic Luminance and Tactile Ideophones",
        category="Expressives & Reduplication",
        formula="[Visual / Tactile Ideophone Pair]",
        description="Vivid descriptors of sparkling light, deep darkness, cleanliness, and textural feel.",
        kokborok_examples=["kwrik-kwrik (immaculately pristine / dazzlingly clean)", "khlum-khlum (deep mountain twilight)", "bili-bili (flickering flame)"],
        english_translations=["immaculately clean", "deep dusky twilight", "flickering gently"],
        source_reference="Karapurkar (1976) § 7.4; Dhar (1983) § 12.3"
    ),
    GrammarRule(
        id="PHON-10",
        name="Tone Sandhi & Contour Leveling",
        category="Phonology & Orthography",
        formula="/V́/ + /V́/ -> [V̄.V́] (contour plateauing)",
        description="High tone (khorok kwrak) on non-final syllables undergoes subtle pitch lowering and contour plateauing when immediately preceding another high-tone syllable across compound boundaries.",
        kokborok_examples=["kháng (to fry) + chá (to eat) -> khang-chá (fry and eat)", "lái (bamboo strip) + phrok (to split) -> lai-phrok"],
        english_translations=["fry and eat", "split bamboo strips"],
        source_reference="Dhar (1983) § 1.5; Karapurkar (1976) § 1.6.2"
    ),
    GrammarRule(
        id="PHON-11",
        name="Velar Coda Dissimilation",
        category="Phonology & Orthography",
        formula="...ng + k... -> [ŋ.k] (distinct acoustic release)",
        description="When a nominal or verbal root ending in velar coda '-ng' cliticizes with a suffix beginning with voiceless stop 'k-', the nasal is preserved with distinct acoustic release rather than assimilating into a geminate.",
        kokborok_examples=["thang-kha (went)", "rwng-khe (if knowing)", "chwng-no (to us)"],
        english_translations=["departed", "if one knows", "unto us"],
        source_reference="Karapurkar (1976) § 1.3; Dhar (1983) § 2.4"
    ),
    GrammarRule(
        id="CAS-16",
        name="Temporal Succession Relator ('-ni ulo' / '-ni swkang')",
        category="Case Postpositions",
        formula="[Event NP / Clause] + -ni + ulo (after) / swkang (before)",
        description="Complex temporal ordering between events is constructed via the genitive case '-ni' followed by the relational nouns 'ulo' (posterior) or 'swkang' (anterior).",
        kokborok_examples=["mai chá-mung-ni ulo (after having the meal)", "Agartala thang-mung-ni swkang (before going to Agartala)"],
        english_translations=["after eating the meal", "prior to departing for Agartala"],
        source_reference="Radhamohan Thakur (1900) § 23; Dhar (1983) § 6.6"
    ),
    GrammarRule(
        id="NUM-14",
        name="Aggregate Universal Quantifier ('joto-' / 'bwtwi-')",
        category="Numeral Classifiers",
        formula="joto + [Plural Noun] / [Fauna] + bwtwi",
        description="Expresses exhaustive collective entirety without individuation ('all', 'every single', 'entire flock').",
        kokborok_examples=["joto borok-rok (all the people)", "tok bwtwi (the entire flock of birds)"],
        english_translations=["all the people", "the entire flock of fowl"],
        source_reference="Karapurkar (1976) § 3.3; Baskaran (2015)"
    ),
    GrammarRule(
        id="TAM-17",
        name="Evidential Hearsay and Reportative Marker ('-khwno' / '-kanto')",
        category="Tense, Aspect & Mood",
        formula="[Verb Predicate] + -khwno / -kanto",
        description="Enclitic indicating that the speaker acquired knowledge of the event through hearsay, hearsay reports, or traditional lore rather than firsthand direct witnessing.",
        kokborok_examples=["Bo pha-i-kha-khwno (Reportedly he has arrived)", "Watwi wat-nai-kanto (They say rain will fall tomorrow)"],
        english_translations=["Reportedly he arrived", "People say rain will fall"],
        source_reference="Radhamohan Thakur (1900) § 41; Dhar (1983) § 8.7"
    ),
    GrammarRule(
        id="TAM-18",
        name="Polite and Honorific Imperative Directive ('-thau' / '-tawi')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -thau",
        description="Used when addressing elders, priests (Ochai), and respected visitors, softening an imperative into a courteous, revered entreaty.",
        kokborok_examples=["Achuk-thau! (Please be seated comfortably)", "Chá-thau! (Please partake of food)", "Phai-thau! (Please enter)"],
        english_translations=["Please sit down", "Please enjoy the meal", "Please come in"],
        source_reference="Radhamohan Thakur (1900) § 39; Dhar (1983) § 8.8"
    ),
    GrammarRule(
        id="TAM-19",
        name="Irrealis Counterfactual Conditional ('-khe-ba')",
        category="Tense, Aspect & Mood",
        formula="[Protasis Verb] + -khe-ba, [Apodosis Verb] + -kha-ba",
        description="Expresses counterfactual past conditionals where the condition was unfulfilled and the resulting event never took place ('had X occurred, Y would have happened').",
        kokborok_examples=["Nwng phai-khe-ba ang thang-kha-ba (Had you come, I would have gone)", "Watwi wat-khe-ba haba son-ya-kha-ba (Had it rained, we would not have cleared the field)"],
        english_translations=["Had you come, I would have gone", "Had it rained, we wouldn't have cleared the jhum"],
        source_reference="Karapurkar (1976) § 6.2.3; Dhar (1983) § 8.9"
    ),
    GrammarRule(
        id="NEG-08",
        name="Honorific Prohibitive Dissuasion ('ta-...-thau')",
        category="Negation & Polarity",
        formula="ta- + [Verb Root] + -thau",
        description="Forms gentle negative dissuasion and polite warnings addressed to elders and honored guests ('please do not do').",
        kokborok_examples=["Ta thang-thau (Please do not go there)", "Ta dukhu khwlai-thau (Please do not worry)"],
        english_translations=["Please do not venture there", "Please do not be anxious"],
        source_reference="Radhamohan Thakur (1900) § 45; Dhar (1983) § 9.4"
    ),
    GrammarRule(
        id="VOI-07",
        name="Directional Deictic Vertical Translocatives ('sa-' / 'ha-')",
        category="Voice & Derivations",
        formula="sa- + [Motion Root] (ascent) / ha- + [Motion Root] (descent)",
        description="Prefixes attached directly to verbal motion roots expressing vertical trajectory across hill topography relative to the speaker.",
        kokborok_examples=["sa-gok (climb upwards towards the ridge)", "ha-deng (descend downwards into the valley)"],
        english_translations=["ascend upward", "descend into the valley"],
        source_reference="Karapurkar (1976) § 5.5.6; Dhar (1983) § 10.5"
    ),
    GrammarRule(
        id="SYN-10",
        name="Emphatic Assertion and Conviction Enclitic ('-khai' / '-goi')",
        category="Syntax & Clause Structure",
        formula="[Predicate Clause] + -khai / -goi",
        description="Affirmative evidential enclitic expressing strong speaker certainty, factual conviction, or unshakeable truth ('truly', 'indeed so', 'without doubt').",
        kokborok_examples=["Bo kaham-khai (He is truly fine indeed)", "Ang thang-nai-goi (I will certainly go without fail)"],
        english_translations=["He is truly good indeed", "I will certainly go"],
        source_reference="Radhamohan Thakur (1900) § 57; Dhar (1983) § 11.7"
    ),
    GrammarRule(
        id="SYN-11",
        name="Adversative Inter-Clausal Conjunction ('tobo')",
        category="Syntax & Clause Structure",
        formula="[Independent Clause 1], tobo [Independent Clause 2]",
        description="Coordinates contrasting clauses expressing an unexpected outcome or obstacle ('yet', 'nevertheless', 'still').",
        kokborok_examples=["Watwi wat-tong, tobo chwng haba thang-kha (It was raining, yet we went to the jhum field)"],
        english_translations=["It was raining, yet we went to the field"],
        source_reference="Dhar (1983) § 11.8; Debbarma (2013)"
    ),
    GrammarRule(
        id="SYN-12",
        name="Non-Interrogative Wh-Indefinites with Focus Clitic ('-ba')",
        category="Syntax & Clause Structure",
        formula="[Wh-Question Base: sabo, tamo, bano] + -ba",
        description="Attaching the clitic '-ba' to interrogative pronouns derives indefinite non-specific pronouns ('someone', 'something', 'somewhere').",
        kokborok_examples=["sabo-ba phai-kha (someone has arrived)", "tamo-ba chá-di (eat something)", "bano-ba tong-o (is somewhere)"],
        english_translations=["someone arrived", "eat something", "resides somewhere"],
        source_reference="Karapurkar (1976) § 3.4; Dhar (1983) § 11.9"
    ),
    GrammarRule(
        id="EXP-06",
        name="Auditory Crackling and Striking Phonaesthemes",
        category="Expressives & Reduplication",
        formula="[Sound Mimetic Pair]",
        description="Onomatopoeic sound words mimicking bamboo splitting, dry leaves rustling underfoot, or sharp percussion.",
        kokborok_examples=["chrok-chrok (crackling of dry bamboo in jhum fire)", "trak-trak (sharp knocking sound)"],
        english_translations=["crackling intensely", "sharp knocking"],
        source_reference="Karapurkar (1976) § 7.5; Dhar (1983) § 12.4"
    )
,
    GrammarRule(
        id="PHON-12",
        name="Glottal Stop Hiatus Insertion",
        category="Phonology & Orthography",
        formula="/V/ + /V/ -> [V.ʔ.V] (glottal hiatus barrier)",
        description="In vowel hiatus environments across morpheme junctures, a transitional glottal stop [ʔ] is acoustically inserted between adjacent vocalic nuclei to prevent illicit diphthong coalescence.",
        kokborok_examples=["chá-o -> [tʃʰa.ʔ.o] (is eating)", "rwi-o -> [rwi.ʔ.o] (is giving)"],
        english_translations=["is partaking of food", "is giving"],
        source_reference="Dhar (1983) § 1.6; Karapurkar (1976) § 1.4"
    ),
    GrammarRule(
        id="PHON-13",
        name="Sonorant Resonant Devoicing",
        category="Phonology & Orthography",
        formula="/C[+aspirated]/ + /r, w, y/ -> [C.r̥ / C.w̥ / C.j̊]",
        description="Liquid and glide resonants (/r/, /w/, /y/) undergo partial devoicing when following voiceless aspirated stops /ph/, /th/, /kh/ in word-initial consonant clusters.",
        kokborok_examples=["phrok (split bamboo)", "khwrak (hard/strong)", "thwng (play)"],
        english_translations=["split bamboo strips", "solid and strong", "play"],
        source_reference="Karapurkar (1976) § 1.5; Pai (1976)"
    ),
    GrammarRule(
        id="CAS-17",
        name="Absolute Superlative Comparison ('-nikhre joto-nikhre')",
        category="Case Postpositions",
        formula="[NP] + -nikhre + joto-nikhre / bebakk-nikhre",
        description="Forms absolute superlative comparison by compounding the ablative-comparative case '-nikhre' with the universal collective 'joto' ('all') or 'bebakk'.",
        kokborok_examples=["Bo joto-nikhre kaham (He is the best of all)", "Khum-rok-ni bisingo joto-nikhre kaham khumpui (Among flowers, khumpui is the most beautiful)"],
        english_translations=["He is the best of all", "Among flowers, khumpui is the most beautiful"],
        source_reference="Radhamohan Thakur (1900) § 27; Dhar (1983) § 6.7"
    ),
    GrammarRule(
        id="CAS-18",
        name="Purposive Destinative Relator ('-na bagwi')",
        category="Case Postpositions",
        formula="[Verb Root] + -na + bagwi",
        description="Expresses purposive and destinative motivation ('in order to', 'for the purpose of'), binding the infinitive/dative marker '-na' with the benefactive relator 'bagwi'.",
        kokborok_examples=["mai chá-na bagwi phai-kha (came in order to eat rice)", "rwng swlai-na bagwi thang-kha (went to acquire knowledge)"],
        english_translations=["came in order to have a meal", "went for the purpose of learning"],
        source_reference="Radhamohan Thakur (1900) § 29; Debbarma (2013)"
    ),
    GrammarRule(
        id="NUM-15",
        name="Classifier for Stacks and Layered Textiles ('sop-' / 'thak-')",
        category="Numeral Classifiers",
        formula="sop- + [Numeral] / thak- + [Numeral]",
        description="Numeral classifier applied specifically to stacked layers of woven cloths (rignai, risa), mats, or sheaves of harvested paddy.",
        kokborok_examples=["sop-sa rignai (one stack of traditional skirts)", "thak-tham lekhapori (three tiers/stacks of books)"],
        english_translations=["one neat stack of rignai", "three stacks of literature"],
        source_reference="Karapurkar (1976) § 3.3.4; Baskaran (2015)"
    ),
    GrammarRule(
        id="NUM-16",
        name="Classifier for Morsels and Draughts ('gam-' / 'muk-')",
        category="Numeral Classifiers",
        formula="gam- + [Numeral] / muk- + [Numeral]",
        description="Specific partitive classifier for consumable portions: 'gam-' for morsels/mouthfuls of food, 'muk-' for sips or draughts of liquid/water.",
        kokborok_examples=["gam-sa mai (one mouthful of rice)", "muk-sa twi (one sip/mouthful of water)"],
        english_translations=["one mouthful of food", "a single sip of water"],
        source_reference="Radhamohan Thakur (1900) § 34; Dhar (1983) § 7.6"
    ),
    GrammarRule(
        id="TAM-20",
        name="Experiential Past Aspect ('-rwng-kha' / '-mung-tong-kha')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -rwng-kha / -mung-tong-kha",
        description="Experiential past aspect indicating that the subject possesses historical life experience of having performed or witnessed an action at least once.",
        kokborok_examples=["Ang Agartala thang-rwng-kha (I have had the experience of visiting Agartala)", "Bo unakoti nuk-mung-tong-kha (He has seen Unakoti before)"],
        english_translations=["I have previously visited Agartala", "He has experienced seeing Unakoti"],
        source_reference="Karapurkar (1976) § 6.4; Dhar (1983) § 8.10"
    ),
    GrammarRule(
        id="TAM-21",
        name="Mirative Sensory Revelation Enclitic ('-glak-se' / '-ba-se')",
        category="Tense, Aspect & Mood",
        formula="[Predicate Clause] + -glak-se / -kha-ba-se",
        description="Mirative enclitic expressing unexpected revelation, sudden sensory discovery, or counter-expectation on the part of the speaker.",
        kokborok_examples=["Phai-kha-ba-se! (Lo and behold, he has actually arrived!)", "Kaham-se! (It turns out to be wonderfully good!)"],
        english_translations=["Look, he unexpectedly arrived!", "It is surprisingly wonderful!"],
        source_reference="Dhar (1983) § 8.11; Pai (1976)"
    ),
    GrammarRule(
        id="TAM-22",
        name="Imminent Prospective Aspect ('-na chwng-o' / '-na khe-kha')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -na chwng-o / -na khe-kha",
        description="Imminent prospective aspect denoting an event that is immediate and on the very verge of occurring ('about to do', 'on the brink of').",
        kokborok_examples=["Watwi wat-na chwng-o (Rain is on the verge of falling)", "Thang-na khe-kha (He was just about to depart)"],
        english_translations=["Rain is about to pour down", "He was on the brink of leaving"],
        source_reference="Radhamohan Thakur (1900) § 42; Dhar (1983) § 8.12"
    ),
    GrammarRule(
        id="NEG-09",
        name="Impotential and Inability Negative ('-man-ya' / '-rwng-ya')",
        category="Negation & Polarity",
        formula="[Verb Root] + -man-ya / -rwng-ya",
        description="Impotential and inability negative modal construction indicating physical impossibility, lack of capacity, or lack of learned skill.",
        kokborok_examples=["Ang swi-rwng-ya (I cannot write / lack the skill to write)", "Bo phai-man-ya (He is unable to come / physically prevented)"],
        english_translations=["I cannot write", "He is unable to attend"],
        source_reference="Karapurkar (1976) § 6.3; Dhar (1983) § 9.5"
    ),
    GrammarRule(
        id="NEG-10",
        name="Habitual Continuative Negative ('-ya-twi')",
        category="Negation & Polarity",
        formula="[Verb Root] + -ya-twi",
        description="Habitual or continuative negative aspect expressing that an action is customarily or persistently unperformed ('without habitually doing').",
        kokborok_examples=["Mai chá-ya-twi tong-o (Remains without eating food)", "Kok sa-ya-twi achuk-tong (Sitting without speaking a word)"],
        english_translations=["remains persistently without eating", "sitting without uttering words"],
        source_reference="Radhamohan Thakur (1900) § 47; Dhar (1983) § 9.6"
    ),
    GrammarRule(
        id="VOI-08",
        name="Iterative-Distributive Intensive Clitic ('-phi-lai' / '-khol-lai')",
        category="Voice & Derivations",
        formula="[Verb Root] + -phi-lai / -khol-lai",
        description="Iterative-distributive intensive verbal affix expressing repeated, reciprocal, or alternating movement back and forth across space.",
        kokborok_examples=["thang-phi-lai (going back and forth continuously)", "sa-phi-lai (retorting and exchanging words back and forth)"],
        english_translations=["moving back and forth repeatedly", "exchanging retorts back and forth"],
        source_reference="Karapurkar (1976) § 5.5.7; Dhar (1983) § 10.6"
    ),
    GrammarRule(
        id="VOI-09",
        name="Benefactive Applicative Auxiliary ('-rwi-ri-')",
        category="Voice & Derivations",
        formula="[Verb Root] + -rwi-ri-",
        description="Benefactive applicative auxiliary construction where an agent causes an action to be performed explicitly on behalf of and for the benefit of a third person.",
        kokborok_examples=["nok swi-rwi-ri-kha (had the letter written for him)", "haba son-rwi-ri-kha (had the jhum field cleared on their behalf)"],
        english_translations=["had the letter written for another's benefit", "had the field cleared for them"],
        source_reference="Radhamohan Thakur (1900) § 51; Dhar (1983) § 10.7"
    ),
    GrammarRule(
        id="SYN-13",
        name="Concessive Conditional Subordination ('-khe-phano')",
        category="Syntax & Clause Structure",
        formula="[Subordinate Clause] + -khe-phano / -phano, [Main Clause]",
        description="Concessive conditional clause subordination coordinating an unexpected or contrasting main proposition ('even if', 'although', 'notwithstanding that').",
        kokborok_examples=["Watwi wat-khe-phano chwng thang-nai (Even if it rains, we will certainly go)", "Dukhu man-phano khakchang-tong (Although facing hardship, remains joyful)"],
        english_translations=["Even if it pours rain, we will go", "Though facing difficulties, stays at peace"],
        source_reference="Karapurkar (1976) § 7.3; Dhar (1983) § 11.10"
    ),
    GrammarRule(
        id="SYN-14",
        name="Circumstantial Nominalized Clause ('-mung-o')",
        category="Syntax & Clause Structure",
        formula="[Verb Root] + -mung-o + [Matrix Predicate]",
        description="Locative-marked nominalized circumstantial clause expressing contemporaneous temporal backgrounding ('while engaged in X', 'upon the occasion of doing X').",
        kokborok_examples=["lamo thang-mung-o bo-no nuk-kha (while traveling on the road, saw him)", "mai son-mung-o khorok-sa phai-kha (during the harvest of rice, someone came)"],
        english_translations=["while on the journey, caught sight of him", "during paddy reaping, someone arrived"],
        source_reference="Radhamohan Thakur (1900) § 59; Dhar (1983) § 11.11"
    ),
    GrammarRule(
        id="SYN-15",
        name="Rhetorical Confirmation Tag ('-ya-de?')",
        category="Syntax & Clause Structure",
        formula="[Affirmative Predicate] + -ya-de?",
        description="Rhetorical confirmation tag question seeking affirmation and shared consensus from the listener ('isn't that so?', 'didn't it happen?').",
        kokborok_examples=["Nwng sa-kha-ya-de? (You said so, didn't you?)", "Bo kaham-ya-de? (He is good, isn't he?)"],
        english_translations=["You stated that, did you not?", "It is wonderful, is it not?"],
        source_reference="Karapurkar (1976) § 7.2; Dhar (1983) § 11.12"
    ),
    GrammarRule(
        id="EXP-07",
        name="Visual Shimmering and Flickering Phonaesthemes",
        category="Expressives & Reduplication",
        formula="[Light / Visual Mimetic Pair]",
        description="Sensory visual ideophones expressing shimmering, flickering, or radiant visual movement across the landscape.",
        kokborok_examples=["jil-jil (flickering of distant lamplight or fireflies in the bamboo groves)", "mil-mil (faint glimmering of dawn light over the hills)"],
        english_translations=["flickering softly in the night", "glimmering faint dawn light"],
        source_reference="Karapurkar (1976) § 7.5; Dhar (1983) § 12.5"
    )
,
    GrammarRule(
        id="PHON-14",
        name="Aspirated Coda Neutralization in Fast Speech",
        category="Phonology & Orthography",
        formula="...Ch# -> [C#] (deaspiration at utterance boundary)",
        description="Syllable-final aspirated stops undergo perceptual neutralization and non-release before consonant-initial words in rapid colloquial cadence.",
        kokborok_examples=["bukhuk-no (to the elder brother)", "thang-khai (having departed)"],
        english_translations=["unto the elder brother", "upon departing"],
        source_reference="Karapurkar (1976) § 1.6; Pai (1976)"
    ),
    GrammarRule(
        id="CAS-19",
        name="Temporal Anterior Precedence Relator ('-ni sam-o')",
        category="Case Postpositions",
        formula="[Event Noun] + -ni + sam-o (near the time of)",
        description="Locative-temporal relator indicating proximity to a seasonal, diurnal, or historical juncture ('around the season of', 'near the hour of').",
        kokborok_examples=["watwi wat-ni sam-o (around the time the rains fall)", "sal-banga-ni sam-o (at the approach of sunset)"],
        english_translations=["around the rainy season", "near twilight / sunset"],
        source_reference="Radhamohan Thakur (1900) § 31; Dhar (1983) § 6.8"
    ),
    GrammarRule(
        id="CAS-20",
        name="Distributive Case Multiplier ('-no -no')",
        category="Case Postpositions",
        formula="[Noun] + -no + [Noun] + -no",
        description="Doubling of accusative postposition '-no' across repeated nouns indicates distributive assignment to individual entities ('to each house', 'village by village').",
        kokborok_examples=["nok-no nok-no thang-kha (went from house to house / visited each home)", "kami-no kami-no pir-kha (spread from village to village)"],
        english_translations=["visited each and every house", "spread across every village"],
        source_reference="Karapurkar (1976) § 4.2; Dhar (1983) § 6.9"
    ),
    GrammarRule(
        id="NUM-17",
        name="Classifier for Skeins, Bunches and Sheaves ('khor-' / 'dop-')",
        category="Numeral Classifiers",
        formula="khor- + [Numeral] / dop- + [Numeral]",
        description="Numeral classifier applied specifically to tied bunches of harvested grain, skeins of spun cotton yarn (khul), or bundled herbs.",
        kokborok_examples=["khor-sa khul (one skein of handspun thread)", "dop-sa mai (one sheaf of harvested paddy)"],
        english_translations=["one skein of cotton yarn", "one sheaf of paddy"],
        source_reference="Radhamohan Thakur (1900) § 36; Baskaran (2015)"
    ),
    GrammarRule(
        id="TAM-23",
        name="Iterative Habitual Frequentative ('-u-tong' / '-wi-tong-o')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -u-tong / -wi-tong-o",
        description="Aspectual construction denoting a deeply ingrained customary behavior or repeated habitual practice across prolonged duration ('keeps on habitually doing').",
        kokborok_examples=["Bo sal-brum haba thang-u-tong (He keeps habitually going to the jhum field every single day)"],
        english_translations=["He customarily goes to the jhum field daily"],
        source_reference="Radhamohan Thakur (1900) § 44; Dhar (1983) § 8.13"
    ),
    GrammarRule(
        id="TAM-24",
        name="Dubitative Potential Epistemic Clitic ('-kho-de')",
        category="Tense, Aspect & Mood",
        formula="[Verb Predicate] + -kho-de",
        description="Epistemic clitic expressing genuine speaker uncertainty, conjecture, or pondering whether an event might have transpired ('might perhaps have', 'could it be?').",
        kokborok_examples=["Bo phai-kha-kho-de (He might perhaps have arrived, who knows?)", "Watwi wat-nai-kho-de (Perhaps it may rain)"],
        english_translations=["He might have arrived perhaps", "It could perhaps rain"],
        source_reference="Karapurkar (1976) § 6.5; Dhar (1983) § 8.14"
    ),
    GrammarRule(
        id="TAM-25",
        name="Optative Benediction & Blessing Formula ('-thung-se')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -thung-se",
        description="Polite formal optative enclitic employed by Ochai priests and community elders to bestow spiritual blessings, longevity, and prosperity upon youth.",
        kokborok_examples=["Kaham wng-thung-se! (May glorious good fortune befall you!)", "Bwsar bwrwi tong-thung-se! (May you be blessed with longevity!)"],
        english_translations=["May goodness flourish upon you!", "May you live long and blessed!"],
        source_reference="Radhamohan Thakur (1900) § 48; Debbarma (2013)"
    ),
    GrammarRule(
        id="NEG-11",
        name="Counter-Expectational Negative Polar Question ('-ya-khe-de?')",
        category="Negation & Polarity",
        formula="[Verb Root] + -ya-khe-de?",
        description="Interrogative construction expressing surprised disappointment when an expected prerequisite action was neglected ('if not done, why? / didn't you even?').",
        kokborok_examples=["Nwng mai chá-ya-khe-de? (Haven't you eaten your meal yet?)", "Bo phai-ya-khe-de? (Has he truly not arrived?)"],
        english_translations=["Have you not partaken of food?", "Did he genuinely fail to appear?"],
        source_reference="Karapurkar (1976) § 6.6; Dhar (1983) § 9.7"
    ),
    GrammarRule(
        id="VOI-10",
        name="Anticausative Involuntary Spontaneous Affix ('-khok-')",
        category="Voice & Derivations",
        formula="[Verb Root] + -khok-",
        description="Verbal derivational morpheme indicating spontaneous, uncontrolled, or accidental action occurring without deliberate agentive will ('snapped on its own', 'slipped involuntarily').",
        kokborok_examples=["chong tlep-khok-kha (the rope snapped spontaneously on its own)", "gong-sa kalam bai-khok-kha (the pen broke by accident)"],
        english_translations=["the rope snapped spontaneously", "the pen broke accidentally"],
        source_reference="Dhar (1983) § 10.8; Pai (1976)"
    ),
    GrammarRule(
        id="SYN-16",
        name="Correlative Conditional Paradigm ('je-khe... te-khe...')",
        category="Syntax & Clause Structure",
        formula="je-khe [Protasis], te-khe [Apodosis]",
        description="Classical balanced correlative sentence frame ('the more X, the more Y' / 'as X occurs, so shall Y follow').",
        kokborok_examples=["je-khe nwng pori-khe, te-khe rwng swlai-nai (the more you study, the more knowledge you will attain)"],
        english_translations=["the more you study, the greater your wisdom"],
        source_reference="Radhamohan Thakur (1900) § 62; Dhar (1983) § 11.13"
    ),
    GrammarRule(
        id="SYN-17",
        name="Parenthetical Explicative Complementizer ('hwn-khe')",
        category="Syntax & Clause Structure",
        formula="[Clause 1], hwn-khe [Clarification Clause]",
        description="Discourse connector introducing an explanatory expansion, clarification, or redefinition of a prior assertion ('that is to say', 'in other words').",
        kokborok_examples=["Chwng Agartala thang-nai, hwn-khe sombar sal-o (We will depart for Agartala, that is to say, on Monday)"],
        english_translations=["We depart for Agartala, specifically on Monday"],
        source_reference="Karapurkar (1976) § 7.4; Debbarma (2013)"
    ),
    GrammarRule(
        id="EXP-08",
        name="Aroma and Olfactory Sensory Phonaesthemes ('swm-swm' / 'khem-khem')",
        category="Expressives & Reduplication",
        formula="[Olfactory Mimetic Pair]",
        description="Sensory ideophones denoting rich, pervasive, pungent aromas such as simmering fermented berma, crushed wild herbs, or damp earth.",
        kokborok_examples=["swm-swm bwsak man-o (emitting the pungent savory aroma of berma broth)", "khem-khem mwng-o (smelling of fresh forest herbs)"],
        english_translations=["rich aroma of traditional berma", "aromatic forest scent"],
        source_reference="Karapurkar (1976) § 7.5; Dhar (1983) § 12.6"
    ),
    GrammarRule(
        id="EXP-09",
        name="Tactile Texture and Viscosity Ideophones ('blet-blet')",
        category="Expressives & Reduplication",
        formula="[Tactile Mimetic Pair]",
        description="Onomatopoeic sensory pairs mimicking slimy, viscous, mud-soaked, or slippery tactile textures of river silt or bamboo shoots.",
        kokborok_examples=["blet-blet khwlai-kha (became completely muddy and slippery after torrential rain)"],
        english_translations=["became excessively muddy and slippery"],
        source_reference="Dhar (1983) § 12.7; Pai (1976)"
    )
,
    GrammarRule(
        id="PHON-15",
        name="High Tone Clitic Persistence Across Suffixation",
        category="Phonology & Orthography",
        formula="[V́-Root] + -no / -ni / -o -> [V́.C(V)] (tone anchor stability)",
        description="Inherent phonemic high tone (/khorok kwrak/) remains strictly anchored to the root vowel morpheme and does not spread rightward onto unaccented case or tense clitics.",
        kokborok_examples=["chá (eat) + -kha -> chá-kha (ate)", "lái (bamboo strip) + -no -> lái-no (unto the strip)"],
        english_translations=["ate food", "unto the bamboo strip"],
        source_reference="Dhar (1983) § 1.7; Karapurkar (1976) § 1.6"
    ),
    GrammarRule(
        id="NOM-13",
        name="Associative Kinship Dual Pluralizer ('-song-nwi')",
        category="Nominal Agreement",
        formula="[Kinship Noun] + -song-nwi",
        description="Dual associative plural marker signifying a pair consisting of the named relative and their primary spouse or sibling partner ('the two brothers', 'mother and child pair').",
        kokborok_examples=["ama-song-nwi (the mother and child pair)", "takhuk-song-nwi (the two brothers together)"],
        english_translations=["mother and child pair", "the two brothers together"],
        source_reference="Radhamohan Thakur (1900) § 20; Debbarma (2013)"
    ),
    GrammarRule(
        id="NOM-14",
        name="Diminutive Hypocoristic Clitic ('-bicha')",
        category="Nominal Agreement",
        formula="[Fauna / Flora / Item Noun] + -bicha",
        description="Derives affectionate or diminutive nominals referring to the young offspring of animals or miniature tools.",
        kokborok_examples=["mwkhra-bicha (little infant monkey)", "tok-bicha (little fledgeling chick)"],
        english_translations=["infant monkey", "tiny fledgeling chick"],
        source_reference="Karapurkar (1976) § 3.2; Dhar (1983) § 4.8"
    ),
    GrammarRule(
        id="CAS-21",
        name="Perlative Pathway Translocative ('-bising-twi')",
        category="Case Postpositions",
        formula="[Spatial NP] + -bising-twi",
        description="Perlative case relator indicating trajectory or motion through the interior of a geographic space ('passing through the forest', 'via the middle of the river').",
        kokborok_examples=["ha-khor-bising-twi thang-kha (passed through the deep ravine)", "baha-bising-twi phai-kha (came through the bamboo thicket)"],
        english_translations=["traversed through the ravine", "arrived through the bamboo grove"],
        source_reference="Dhar (1983) § 6.10; Pai (1976)"
    ),
    GrammarRule(
        id="NUM-18",
        name="Classifier for Architectural Homesteads ('khum-')",
        category="Numeral Classifiers",
        formula="khum- + [Numeral] (for dwellings, sheds, shrines)",
        description="Numeral classifier applied specifically to built architectural frameworks, bamboo huts, granaries (gola), or spirit altars (lampra).",
        kokborok_examples=["khum-sa nok (one built homestead)", "khum-nwi gola (two grain storehouses)"],
        english_translations=["one homestead", "two grain storehouses"],
        source_reference="Radhamohan Thakur (1900) § 37; Baskaran (2015)"
    ),
    GrammarRule(
        id="TAM-26",
        name="Interrupted Imperfective Converb ('-tong-twi-no')",
        category="Tense, Aspect & Mood",
        formula="[Imperfective Verb] + -tong-twi-no, [Main Clause]",
        description="Subordinating aspectual converb expressing that an ongoing event was suddenly interrupted or superseded by another action ('while in the middle of doing X, suddenly Y happened').",
        kokborok_examples=["mai chá-tong-twi-no bo phai-kha (right while we were eating, he suddenly arrived)"],
        english_translations=["while in the middle of eating, he arrived"],
        source_reference="Dhar (1983) § 8.15; Karapurkar (1976)"
    ),
    GrammarRule(
        id="TAM-27",
        name="Inceptive Promptive Urgency Marker ('-sa-no')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -sa-no",
        description="Verbal clitic denoting immediate, spontaneous initiation of action without hesitation ('promptly upon', 'the moment that occurred').",
        kokborok_examples=["sok-sa-no kok sa-kha (the instant he arrived, he spoke)", "nuk-sa-no khor-kha (the moment he saw it, he fled)"],
        english_translations=["the instant he arrived, he spoke", "the moment he saw, he ran away"],
        source_reference="Radhamohan Thakur (1900) § 49; Dhar (1983) § 8.16"
    ),
    GrammarRule(
        id="TAM-28",
        name="Frustrative Aspect ('-kha-phano wng-liya')",
        category="Tense, Aspect & Mood",
        formula="[Intended Verb] + -kha-phano + wng-liya",
        description="Frustrative complex expressing that an action was earnestly undertaken or attempted, yet ended in complete failure or unfulfillment ('tried to do, but in vain').",
        kokborok_examples=["haba thang-kha-phano kam wng-liya (went to the field, but work could not be accomplished)"],
        english_translations=["went to the field, but in vain"],
        source_reference="Karapurkar (1976) § 6.7; Dhar (1983) § 8.17"
    ),
    GrammarRule(
        id="NEG-12",
        name="Negative Concessive Irrealis ('-ya-phano')",
        category="Negation & Polarity",
        formula="[Verb Root] + -ya-phano",
        description="Negative concessive subordinator signifying that non-occurrence of an event does not impede the realization of the matrix proposition ('even without doing', 'though not occurring').",
        kokborok_examples=["mai chá-ya-phano thang-nai (will go even without partaking of food)", "kok sa-ya-phano rwng-o (understands even without speaking)"],
        english_translations=["will go even without eating", "understands even without words spoken"],
        source_reference="Dhar (1983) § 9.8; Debbarma (2013)"
    ),
    GrammarRule(
        id="VOI-11",
        name="Intensive Comprehensive Completive ('-pum-pai-kha')",
        category="Voice & Derivations",
        formula="[Verb Root] + -pum-pai-kha",
        description="Compound telic verbal aspect indicating exhaustive, total completion across all constituent parts ('entirely finished to the very last remnant').",
        kokborok_examples=["mai chá-pum-pai-kha (ate up every single morsel completely)", "haba son-pum-pai-kha (cleared the entire field thoroughly)"],
        english_translations=["consumed entirely to the last grain", "cleared the whole field thoroughly"],
        source_reference="Radhamohan Thakur (1900) § 54; Dhar (1983) § 10.9"
    ),
    GrammarRule(
        id="SYN-18",
        name="Topic Resumption and Restatement Particle ('tebo')",
        category="Syntax & Clause Structure",
        formula="[Topic NP], tebo [Resumed Clause]",
        description="Resumptive topical particle that re-anchors a discourse theme after parenthetical digression or interjection ('as for that matter', 'furthermore').",
        kokborok_examples=["Bo tebo kaham borok (As for him, he is furthermore a fine person)"],
        english_translations=["As for him, he is indeed a noble person"],
        source_reference="Dhar (1983) § 11.14; Pai (1976)"
    ),
    GrammarRule(
        id="SYN-19",
        name="Appositive Nominal Classification Precedence",
        category="Syntax & Clause Structure",
        formula="[Semantic Generic Classifier Noun] + [Specific Proper Noun]",
        description="In Kokborok syntax, generic ontological nouns (river, hill, tree, animal) obligatorily precede specific proper names: e.g. 'twi Gomati' (river Gomati), 'hatai Longtharai' (mountain Longtharai), 'bwphang gamari' (gamari tree).",
        kokborok_examples=["twi Gomati (the Gomati river)", "hatai Longtharai (the Longtharai hill range)", "kami Khumulwng (Khumulwng village)"],
        english_translations=["the river Gomati", "the Longtharai hill range", "Khumulwng settlement"],
        source_reference="Karapurkar (1976) § 7.1; Dhar (1983) § 11.15"
    ),
    GrammarRule(
        id="SYN-20",
        name="Adverbial Degree Intensifier Preceding Adjective ('kwbangma')",
        category="Syntax & Clause Structure",
        formula="kwbangma / bera / thotot-no + [Stative Adjective]",
        description="Expresses superlative degree modification positioned immediately leftward of the stative adjectival predicate.",
        kokborok_examples=["kwbangma kaham (exceedingly good)", "bera kotor (enormously large)", "thotot-no kwrwng (profoundly wise)"],
        english_translations=["exceedingly good", "enormously large", "profoundly skilled"],
        source_reference="Radhamohan Thakur (1900) § 65; Dhar (1983) § 11.16"
    ),
    GrammarRule(
        id="EXP-10",
        name="Acoustic Rustling and Murmuring Ideophones ('srok-srok')",
        category="Expressives & Reduplication",
        formula="[Acoustic Whispering Mimetic Pair]",
        description="Sensory ideophones expressing quiet, stealthy rustling of dry foliage or whispered conversations in the hills.",
        kokborok_examples=["srok-srok bwsak khor-o (subtle rustling sound of dry bamboo leaves in breeze)"],
        english_translations=["gentle rustling of bamboo leaves"],
        source_reference="Karapurkar (1976) § 7.5; Dhar (1983) § 12.8"
    ),
    GrammarRule(
        id="EXP-11",
        name="Vigorous Energetic Motion Phonaesthemes ('dak-dak')",
        category="Expressives & Reduplication",
        formula="[Kinetic Motor Mimetic Pair]",
        description="Ideophonic sound pairs describing brisk, vigorous, tireless movement during jhum harvesting or energetic traditional dancing.",
        kokborok_examples=["dak-dak khwlai-wi thang-kha (strode briskly and energetically forward)"],
        english_translations=["moving briskly and vigorously"],
        source_reference="Dhar (1983) § 12.9; Pai (1976)"
    )
,
    GrammarRule(
        id="PHON-16",
        name="Aspirate Occlusion Neutralization in Syllable Codas",
        category="Phonology & Orthography",
        formula="/pʰ, tʰ, kʰ/ -> [p̚, t̚, k̚] (coda neutralization)",
        description="In native Kokborok phonotactics, aspirated stops cannot occur in syllable coda position; underlying aspirates neutralize to unreleased voiceless stops before consonant-initial suffixes.",
        kokborok_examples=["phath-no -> phat-no (to the mat)", "chakh-kha -> chak-kha (sprouted)"],
        english_translations=["unto the bamboo mat", "sprouted / bloomed"],
        source_reference="Dhar (1983) § 1.8; Karapurkar (1976) § 1.4"
    ),
    GrammarRule(
        id="NOM-15",
        name="Compound Coordinate Copulative Nominal Clitic ('-bo... -bo')",
        category="Nominal Agreement & Possession",
        formula="[Noun1 + -bo] + [Noun2 + -bo] (both... and...)",
        description="Coordinate pairing 'both X and Y' or 'neither X nor Y' is formed by attaching the additive focus particle '-bo' to each conjunct noun.",
        kokborok_examples=["nok-bo haba-bo (both the house and the jhum field)", "ani-bo bini-bo (both mine and his)"],
        english_translations=["both the dwelling and the swidden", "both belonging to me and him"],
        source_reference="Radhamohan Thakur (1900) § 32; Dhar (1983) § 4.9"
    ),
    GrammarRule(
        id="NOM-16",
        name="Associative Distributive Collectivizer ('-twi')",
        category="Nominal Agreement & Possession",
        formula="[Clan / Kinship Noun] + -twi (lineage cohort)",
        description="Attaches to kinship and clan terms to denote collective social lineages or behaving according to the manner of that clan.",
        kokborok_examples=["borok-twi (humankind lineage / according to human nature)", "chumai-twi (as a friendly cohort)"],
        english_translations=["human-kind heritage", "among companions"],
        source_reference="Binoy Debbarma (2013); Karapurkar (1976) § 2.8"
    ),
    GrammarRule(
        id="CAS-22",
        name="Locative Delimitative Circumscription ('-ni bwsao')",
        category="Case Postpositions",
        formula="[NP] + -ni bwsao (upon / on top of / concerning)",
        description="Employs genitive '-ni' plus relational noun 'bwsao' ('upon / on top of') to encode superessive spatial location and topical orientation ('regarding X').",
        kokborok_examples=["hatai-ni bwsao (atop the hill range)", "bo kok-ni bwsao (concerning this matter)"],
        english_translations=["upon the mountain ridge", "regarding this topic"],
        source_reference="Dhar (1983) § 6.8; Karapurkar (1976) § 3.5"
    ),
    GrammarRule(
        id="CAS-23",
        name="Aversive Separation Postposition ('-ni khak-wi')",
        category="Case Postpositions",
        formula="[NP] + -ni khak-wi (aside from / excluding)",
        description="Postpositional converb construction signifying 'apart from / separate from / excluding', formed from genitive '-ni' and converb 'khak-wi' ('severing / setting aside').",
        kokborok_examples=["bo-ni khak-wi (aside from him / excluding him)", "Agartala-ni khak-wi (apart from Agartala)"],
        english_translations=["excluding him", "setting aside Agartala"],
        source_reference="Karapurkar (1976) § 3.7; Binoy Debbarma (2013)"
    ),
    GrammarRule(
        id="NUM-19",
        name="Vessel and Container Measure Classifier ('kok-', 'khumpui-')",
        category="Numeral Classifiers",
        formula="[Container Classifier] + [Numeral Root] + [Mass Noun]",
        description="Classifies uncount and agricultural produce measured by traditional bamboo baskets ('kok-') and bundles ('khumpui-').",
        kokborok_examples=["kok-sa mai (one bamboo basket of unhusked rice)", "khumpui-nwi khul (two bundles of raw cotton)"],
        english_translations=["one basket of paddy", "two bundles of cotton yarn"],
        source_reference="Debbarma (2016); Dhar (1983) § 5.7"
    ),
    GrammarRule(
        id="TAM-29",
        name="Imminent Prospective Aspect ('-nani thwng')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -nani thwng-kha (on the verge of doing)",
        description="Formed by combining purposive infinitive '-nani' with aspectual auxiliary 'thwng-kha' ('about to / on the verge of performing an action').",
        kokborok_examples=["thang-nani thwng-kha (was on the verge of leaving)", "nug-nani thwng-kha (was about to witness)"],
        english_translations=["was just about to depart", "was on the brink of seeing"],
        source_reference="Dhar (1983) § 8.14; Karapurkar (1976) § 5.6"
    ),
    GrammarRule(
        id="TAM-30",
        name="Procrastinative Deliberative Aspect ('-kho-rwng')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -kho-rwng (deliberate first / delay action)",
        description="Indicates an action held in abeyance or deliberated thoughtfully before execution ('let us pause and do first').",
        kokborok_examples=["nug-kho-rwng (let us observe first / wait and see)", "sa-kho-rwng (let us deliberate first)"],
        english_translations=["let us pause and observe first", "hold on and let us speak first"],
        source_reference="Karapurkar (1976) § 5.8; Debbarma (2016)"
    ),
    GrammarRule(
        id="TAM-31",
        name="Iterative Habitual Customary Aspect ('-u-man')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -u-man (traditionally customary practice)",
        description="Suffix combination expressing established ancestral custom, folklore traditions, or customary rituals practiced from antiquity.",
        kokborok_examples=["ochai rwchap-u-man (the shaman traditionally chants)", "chakhwi chá-u-man (traditionally accustomed to eating chakhwi)"],
        english_translations=["the shaman customizes by tradition", "accustomed by ancestral tradition to eat chakhwi"],
        source_reference="Radhamohan Thakur (1900) § 49; Dhar (1983) § 8.16"
    ),
    GrammarRule(
        id="NEG-13",
        name="Incongruous Non-volitional Negative ('-ya-rwng-wi')",
        category="Negation & Polarity",
        formula="[Verb Root] + -ya-rwng-wi (inadvertently / unwittingly)",
        description="Negative converbial construction expressing an action occurring without conscious intent or through lack of knowledge.",
        kokborok_examples=["rwng-ya-rwng-wi sa-kha (spoke unwittingly / said inadvertently)", "nug-ya-rwng-wi khorang khna-kha (heard unintentionally)"],
        english_translations=["spoke inadvertently without knowing", "overheard unwittingly"],
        source_reference="Binoy Debbarma (2013); Dhar (1983) § 9.8"
    ),
    GrammarRule(
        id="VOI-12",
        name="Pre-verbal Causative Inchoative Auxiliarization ('ri-wi tong')",
        category="Voice & Derivations",
        formula="[Verb Root] + -ri-wi tong (causing continuously)",
        description="Causative serial verb construction indicating sustaining an ongoing caused state or maintaining instructions over time.",
        kokborok_examples=["bo-no phwng-ri-wi tong-kha (kept causing him to learn / kept instructing him)", "chwrai-no khwna-ri-wi tong-kha (kept making the child listen)"],
        english_translations=["kept him being instructed", "kept making the youth listen"],
        source_reference="Dhar (1983) § 9.5; Karapurkar (1976) § 4.7"
    ),
    GrammarRule(
        id="SYN-21",
        name="Appositive Focus Cleft Construction with '-se'",
        category="Syntax & Clause Structure",
        formula="[Focal Subject Noun + -se] + [Predicate Verb]",
        description="Focal noun marked with contrastive '-se' placed in pre-predicate cleft position for emphatic discourse prominence ('It is X who...').",
        kokborok_examples=["Bo-se thang-nai (It is HE who will go, not someone else)", "Ang-se sa-kha (It is I who spoke)"],
        english_translations=["It is he specifically who shall depart", "It is I who truly said it"],
        source_reference="Karapurkar (1976) § 6.12; Dhar (1983) § 11.4"
    ),
    GrammarRule(
        id="SYN-22",
        name="Echo Subordination Converbial Linking ('-wi... -wi')",
        category="Syntax & Clause Structure",
        formula="[Verb1 + -wi] + [Verb2 + -wi] + [Finite Matrix Verb]",
        description="Multiple simultaneous or manner converbs chained in parallel before the matrix finite verb to depict simultaneous actions.",
        kokborok_examples=["kwsrang-wi bir-wi thang-kha (flew away shining brightly)", "khulum-wi rwchap-wi thang-kha (departed bowing and singing)"],
        english_translations=["flew away glistening brightly", "departed bowing reverently and singing"],
        source_reference="Dhar (1983) § 11.8; Karapurkar (1976) § 6.14"
    ),
    GrammarRule(
        id="EXP-12",
        name="Somatosensory Proprioceptive Ideophones ('kir-kir', 'khor-khor')",
        category="Expressives & Reduplication",
        formula="[Proprioceptive Mimetic Pair]",
        description="Phonaesthemes denoting visceral sensations: shivering from cold, tingling, dizziness, or goosebumps.",
        kokborok_examples=["khang-khor-khor (shivering intensely with mountain cold)", "kir-kir (tingling sensation / goosebumps)"],
        english_translations=["shivering intensely from freezing cold", "tingling all over with goosebumps"],
        source_reference="Debbarma (2016); Binoy Debbarma (2013)"
    ),
    GrammarRule(
        id="EXP-13",
        name="Kinesthetic Tremor and Vibration Ideophones ('dur-dur', 'tur-tur')",
        category="Expressives & Reduplication",
        formula="[Kinesthetic Vibration Mimetic Pair]",
        description="Sound-symbolic words representing earth tremors, racing heartbeats, or deep rumbling thunder in the mountain peaks.",
        kokborok_examples=["khapang dur-dur (heart palpitating with excitement)", "hachuk tur-tur (hills trembling with deep reverberation)"],
        english_translations=["heart palpitating rapidly", "hills vibrating with tremors"],
        source_reference="Binoy Debbarma (2013); Karapurkar (1976) § 7.5"
    )
,
    GrammarRule(
        id="PHON-17",
        name="Acoustic Release in Homorganic Cluster Transitions ('-nd-', '-mb-')",
        category="Phonology & Orthography",
        formula="/N/ + [Voiced Homorganic Stop] -> [N.D] (maintained voicing duration)",
        description="Nasal + voiced homorganic stop clusters maintain voiced duration without devoicing in internal sandhi environments.",
        kokborok_examples=["khandu (traditional clay earthen lamp)", "kumbang (protective hill ridge)"],
        english_translations=["earthen clay lamp", "earthen fortification ridge"],
        source_reference="Karapurkar (1976) § 1.5; Dhar (1983) § 2.3"
    ),
    GrammarRule(
        id="NOM-17",
        name="Inclusive Associative Dual Collective Enclitic ('-jwi')",
        category="Nominal Agreement & Possession",
        formula="[Kinship / Relational Noun Pair] + -jwi (both companions together)",
        description="Dual associative clitic meaning 'pair of companions / both together' attached to kinship pairs or close partners.",
        kokborok_examples=["sa-bwrwi-jwi (mother and daughter together)", "nokhabani-jwi (married husband and wife pair)"],
        english_translations=["mother and daughter pair", "married couple together"],
        source_reference="Radhamohan Thakur (1900) § 28; Dhar (1983) § 4.11"
    ),
    GrammarRule(
        id="NOM-18",
        name="Partitive Qualitative Partition Clitic ('-thot')",
        category="Nominal Agreement & Possession",
        formula="[Noun Root] + -thot (choicest portion / segment)",
        description="Expresses 'portion / segment of prime quality' extracted from a nominal whole or harvest yield.",
        kokborok_examples=["mai-thot (choicest first-harvest grain)", "khul-thot (finest spun cotton yarn)"],
        english_translations=["choicest grain portion", "finest cotton segment"],
        source_reference="Binoy Debbarma (2013); Karapurkar (1976) § 2.9"
    ),
    GrammarRule(
        id="CAS-24",
        name="Subessive Basal Spatial Relator ('-ni bwsing-o')",
        category="Case Postpositions",
        formula="[NP] + -ni bwsing-o (underneath / down within)",
        description="Genitive '-ni' + relational noun 'bwsing-o' ('underneath / down within / below the surface of').",
        kokborok_examples=["bwphang-ni bwsing-o (underneath the tree canopy)", "ha-ni bwsing-o (down inside the earth)"],
        english_translations=["under the tree shade", "deep within the earth"],
        source_reference="Dhar (1983) § 6.9; Karapurkar (1976) § 3.9"
    ),
    GrammarRule(
        id="CAS-25",
        name="Proximal Vicinal Relator ('-ni chap-wi' / '-ni sok-wi')",
        category="Case Postpositions",
        formula="[NP] + -ni chap-wi (adjacent to / bordering alongside)",
        description="Postpositional converb construction signifying 'bordering on / adjacent to / alongside', formed from genitive '-ni' and converb 'chap-wi' ('adjoining').",
        kokborok_examples=["twi-ni chap-wi (alongside the riverbank)", "lama-ni chap-wi (bordering the pathway)"],
        english_translations=["adjacent to the riverbank", "bordering along the trail"],
        source_reference="Karapurkar (1976) § 3.8; Dhar (1983) § 6.10"
    ),
    GrammarRule(
        id="NUM-20",
        name="Stratified Fractional and Proportional Quantification ('-bak', '-khwrwi')",
        category="Numeral Classifiers",
        formula="[Fractional Base] + -bak / -khwrwi (proportional fraction)",
        description="Traditional fractional numeral morphology representing shares, halves, and quarters in communal harvest distribution.",
        kokborok_examples=["bak-nwi (half share / two portions)", "bak-brwi (quarter share / four portions)"],
        english_translations=["half share", "quarter portion"],
        source_reference="Debbarma (2016); Radhamohan Thakur (1900) § 42"
    ),
    GrammarRule(
        id="TAM-32",
        name="Premonitory Cautionary Evitative Aspect ('-na-rwng')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -na-rwng (beware lest / cautionary risk)",
        description="Indicates warning or cautionary risk of an unwanted imminent event ('lest it happen / beware of falling').",
        kokborok_examples=["klai-na-rwng (take heed lest you tumble)", "twi-o klai-na-rwng (take care lest you slip into the water)"],
        english_translations=["beware lest you fall", "caution lest you slip into the river"],
        source_reference="Dhar (1983) § 8.18; Karapurkar (1976) § 5.11"
    ),
    GrammarRule(
        id="TAM-33",
        name="Frequentative Distributive Reduplicated Aspect ('-wi-wi')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -wi-wi (repeatedly doing while proceeding)",
        description="Repeated sequential converb denoting action executed repeatedly across time or space.",
        kokborok_examples=["chá-wi-wi thang-kha (ate continuously while journeying)", "nai-wi-wi phai-kha (looked around continually while arriving)"],
        english_translations=["journeyed while continually eating", "came while continually observing"],
        source_reference="Karapurkar (1976) § 5.9; Pai (1976)"
    ),
    GrammarRule(
        id="TAM-34",
        name="Conjectural Epistemic Evidential Mood ('-kho-ba')",
        category="Tense, Aspect & Mood",
        formula="[Verb Root] + -kho-ba (perhaps / likely occurred)",
        description="Expresses tentative conjecture based on observational deduction ('might possibly have happened').",
        kokborok_examples=["phai-kho-ba (perhaps he arrived)", "thang-kho-ba (likely departed)"],
        english_translations=["perhaps he has already arrived", "likely he departed"],
        source_reference="Radhamohan Thakur (1900) § 53; Dhar (1983) § 8.20"
    ),
    GrammarRule(
        id="NEG-14",
        name="Anticipatory Preventive Prohibitive Frame ('ta-rwng-...-di')",
        category="Negation & Polarity",
        formula="ta-rwng- + [Verb Root] + -di (do not inadvertently do)",
        description="Emphatic admonition to avoid entering a perilous situation or doing something inadvertently.",
        kokborok_examples=["ta-rwng-thang-di (do not inadvertently venture there)", "ta-rwng-sa-di (do not accidentally speak of it)"],
        english_translations=["do not venture there inadvertently", "beware not to speak of it accidentally"],
        source_reference="Binoy Debbarma (2013); Dhar (1983) § 9.10"
    ),
    GrammarRule(
        id="VOI-13",
        name="Participatory Co-agentive Auxiliary ('choba-lai')",
        category="Voice & Derivations",
        formula="[Verb Root] + -choba-lai (join together cooperatively)",
        description="Cooperative mutual assistance in agricultural labour (yaol) or collective communal village efforts.",
        kokborok_examples=["huk son-choba-lai-kha (cleared the swidden together cooperatively)", "nok ri-choba-lai-kha (built the homestead cooperatively)"],
        english_translations=["cleared the jhum field together in solidarity", "erected the dwelling cooperatively"],
        source_reference="Karapurkar (1976) § 4.9; Debbarma (2016)"
    ),
    GrammarRule(
        id="SYN-23",
        name="Adversative Concessive Inversion with 'jeba... tobo...'",
        category="Syntax & Clause Structure",
        formula="jeba + [Clause 1] + tobo + [Clause 2] (although... yet nonetheless...)",
        description="Correlative concessive sentence frame 'even though X, yet nonetheless Y'.",
        kokborok_examples=["Jeba ha nai-kha, tobo bo phai-liya (Although rain poured, he nonetheless did not come)"],
        english_translations=["Although it rained torrentially, he nonetheless failed to arrive"],
        source_reference="Dhar (1983) § 11.18; Pai (1976)"
    ),
    GrammarRule(
        id="SYN-24",
        name="Parenthetical Modal Quotative Epilogue ('hwn-ui sa-o')",
        category="Syntax & Clause Structure",
        formula="[Direct Quote / Saying] + hwn-ui sa-o (as the ancients say)",
        description="Frame used in traditional oral story-telling to validate traditional sayings and ancestral proverbs.",
        kokborok_examples=["subrai ha ri-kha hwn-ui sa-o (as it is recounted, Subrai formed the mountains)"],
        english_translations=["as the ancient legend recounts, Subrai shaped the earth"],
        source_reference="Radhamohan Thakur (1900) § 68; Dhar (1983) § 11.19"
    ),
    GrammarRule(
        id="EXP-14",
        name="Thermal and Climatic Phonaesthemes ('chwi-chwi', 'mwk-mwk')",
        category="Expressives & Reduplication",
        formula="[Thermal Sensory Mimetic Pair]",
        description="Sensory ideophones denoting scorching sun heat or pleasant warm hearthside fires.",
        kokborok_examples=["sal chwi-chwi (scorching glaring midday heat)", "nophan mwk-mwk (cozy warm fireside glow)"],
        english_translations=["scorching glaring sunlight", "pleasantly warm hearthside"],
        source_reference="Debbarma (2016); Dhar (1983) § 12.11"
    ),
    GrammarRule(
        id="EXP-15",
        name="Visual Pattern Geometrical Phonaesthemes ('chok-chok', 'krep-krep')",
        category="Expressives & Reduplication",
        formula="[Geometrical Pattern Mimetic Pair]",
        description="Descriptive words mimicking intricate loom weaving patterns (Chamathwi Bar) or dense criss-cross bamboo lattices.",
        kokborok_examples=["krep-krep tak-jak (woven with dense tight criss-cross bamboo mesh)", "chok-chok bar (sharp geometric loom motif)"],
        english_translations=["woven with dense criss-cross bamboo lattice", "intricately geometric motif pattern"],
        source_reference="Binoy Debbarma (2013); Karapurkar (1976) § 7.7"
    )

]


class GrammarRulesEngine:
    """Query, filter, inspect, and validate classical Kokborok grammar rules."""

    def __init__(self):
        self._rules = CLASSICAL_GRAMMAR_RULES
        self._rules_by_id = {r.id: r for r in self._rules}
        self._categories = sorted(list(set(r.category for r in self._rules)))

    def all(self) -> List[GrammarRule]:
        """Return all catalogued grammar rules."""
        return list(self._rules)

    def count(self) -> int:
        """Return total number of rules catalogued."""
        return len(self._rules)

    def get(self, rule_id: str) -> Optional[GrammarRule]:
        """Retrieve a specific grammar rule by ID (e.g. 'PHON-01', 'CAS-03', 'TAM-07')."""
        return self._rules_by_id.get(rule_id.upper().strip())

    def categories(self) -> List[str]:
        """Return all distinct grammatical categories."""
        return list(self._categories)

    def by_category(self, category: str) -> List[GrammarRule]:
        """Filter grammar rules by category keyword."""
        c_low = category.lower().strip()
        return [r for r in self._rules if c_low in r.category.lower()]

    def search(self, query: str) -> List[GrammarRule]:
        """Search grammar rules by keyword across ID, name, formula, description, and examples."""
        q_low = query.lower().strip()
        results = []
        for r in self._rules:
            if (
                q_low in r.id.lower() or
                q_low in r.name.lower() or
                q_low in r.category.lower() or
                q_low in r.formula.lower() or
                q_low in r.description.lower() or
                any(q_low in ex.lower() for ex in r.kokborok_examples) or
                any(q_low in tr.lower() for tr in r.english_translations)
            ):
                results.append(r)
        return results

    def validate_clause(self, sentence: str) -> Dict[str, Any]:
        """Perform comprehensive grammatical diagnostics on a Kokborok sentence clause."""
        s = sentence.strip()
        diagnostics = []

        # Check for interrogative polar particle
        if s.endswith("de?") or " de?" in s or " de" in s:
            diagnostics.append({"rule": "SYN-04", "note": "Contains polar question particle 'de'"})

        # Check for quotative complementizer
        if "hwnwi" in s.lower():
            diagnostics.append({"rule": "SYN-03", "note": "Employs quotative complementizer 'hwnwi'"})

        # Check for topic & focus markers
        if "-se" in s or " se " in s:
            diagnostics.append({"rule": "SYN-05", "note": "Contains topic focus enclitic '-se'"})
        if "-te" in s or " te " in s:
            diagnostics.append({"rule": "SYN-05", "note": "Contains contrastive topic enclitic '-te'"})
        if "-no" in s:
            diagnostics.append({"rule": "SYN-06", "note": "Contains emphatic focus / accusative marker '-no'"})
        if "-sa" in s:
            diagnostics.append({"rule": "SYN-07", "note": "Contains restrictive limiter '-sa'"})

        # Check for past completive
        if "-kha" in s or " kha" in s or s.endswith("kha"):
            diagnostics.append({"rule": "TAM-01", "note": "Contains past completive marker '-kha'"})

        # Check for future intentional
        if "-nai" in s or s.endswith("nai"):
            diagnostics.append({"rule": "TAM-02", "note": "Contains future intentional marker '-nai'"})

        # Check for future potential
        if "-anw" in s or s.endswith("anw"):
            diagnostics.append({"rule": "TAM-03", "note": "Contains future indefinite/potential marker '-anw'"})

        # Check for progressive aspect
        if "-tong" in s or " tong" in s or s.endswith("tong"):
            diagnostics.append({"rule": "TAM-04", "note": "Contains progressive aspect auxiliary 'tong'"})

        # Check for completive aspect
        if "-pai" in s or "-baikha" in s:
            diagnostics.append({"rule": "TAM-06", "note": "Contains completive perfect marker '-pai' / '-baikha'"})

        # Check for imperative
        if "-di" in s or s.endswith("di!") or s.endswith("di"):
            diagnostics.append({"rule": "TAM-07", "note": "Contains imperative directive suffix '-di'"})

        # Check for conditional
        if "-khe" in s or " khe " in s or "-ba" in s:
            diagnostics.append({"rule": "TAM-08", "note": "Contains conditional clause linker '-khe' / '-ba'"})

        # Check for sequential converb
        if "-wi" in s or " wi " in s or "-i-kha" in s:
            diagnostics.append({"rule": "TAM-09", "note": "Contains sequential converb clitic '-wi' / '-i'"})

        # Check for concessive
        if "-phano" in s or " phano" in s:
            diagnostics.append({"rule": "TAM-10", "note": "Contains concessive subordinator '-phano'"})

        # Check for optative
        if "-thung" in s or s.endswith("thung"):
            diagnostics.append({"rule": "TAM-11", "note": "Contains optative/desiderative mood '-thung'"})

        # Check for inchoative
        if "-sik" in s or "-bai-kha" in s:
            diagnostics.append({"rule": "TAM-12", "note": "Contains inchoative aspect marker '-sik' / '-bai-kha'"})

        # Check for cohortative
        if "-lai-no" in s:
            diagnostics.append({"rule": "TAM-15", "note": "Contains cohortative group hortative '-lai-no'"})

        # Check for hearsay / reportative evidential
        if "-khwno" in s or "-kanto" in s:
            diagnostics.append({"rule": "TAM-17", "note": "Contains hearsay/reportative evidential '-khwno' / '-kanto'"})

        # Check for polite honorific imperative
        if "-thau" in s or "-tawi" in s:
            if "ta " in s.lower() or "ta-" in s.lower():
                diagnostics.append({"rule": "NEG-08", "note": "Follows polite honorific dissuasion frame 'ta-...-thau'"})
            else:
                diagnostics.append({"rule": "TAM-18", "note": "Contains polite honorific imperative '-thau' / '-tawi'"})

        # Check for counterfactual conditional
        if "-khe-ba" in s or "-kheba" in s:
            diagnostics.append({"rule": "TAM-19", "note": "Contains counterfactual conditional '-khe-ba'"})

        # Check for adversative inter-clausal conjunction
        if " tobo " in s or s.startswith("tobo ") or ", tobo" in s:
            diagnostics.append({"rule": "SYN-11", "note": "Contains adversative conjunction 'tobo'"})

        # Check for emphatic assertion / conviction enclitic
        if "-khai" in s or "-goi" in s:
            diagnostics.append({"rule": "SYN-10", "note": "Contains emphatic conviction enclitic '-khai' / '-goi'"})

        # Check for prohibitive negative
        if ("ta " in s.lower() or "ta-" in s.lower()) and not ("-thau" in s):
            diagnostics.append({"rule": "NEG-03", "note": "Follows prohibitive negative frame 'ta-...-di'"})

        # Check for standard negative
        if "-ya" in s or s.endswith("ya"):
            diagnostics.append({"rule": "NEG-01", "note": "Contains general negative suffix '-ya'"})

        # Check for past negative
        if "-liya" in s or s.endswith("liya"):
            diagnostics.append({"rule": "NEG-02", "note": "Contains past negative suffix '-liya'"})

        # Check for not-yet negative
        if "-yakhw" in s or s.endswith("yakhw"):
            diagnostics.append({"rule": "NEG-05", "note": "Contains incompletive 'not yet' negative '-yakhw'"})

        # Check for negative copula krui
        if "krui" in s.lower():
            diagnostics.append({"rule": "NEG-04", "note": "Contains existential negative copula 'krui'"})

        # Check for inability/impotential negative
        if "-man-ya" in s or "-rwng-ya" in s:
            diagnostics.append({"rule": "NEG-09", "note": "Contains inability/impotential negative '-man-ya' / '-rwng-ya'"})

        # Check for habitual continuative negative
        if "-ya-twi" in s:
            diagnostics.append({"rule": "NEG-10", "note": "Contains habitual negative aspect '-ya-twi'"})

        # Check for experiential past
        if "-rwng-kha" in s or "-mung-tong-kha" in s:
            diagnostics.append({"rule": "TAM-20", "note": "Contains experiential past aspect '-rwng-kha'"})

        # Check for mirative sensory revelation
        if "-glak-se" in s or "-kha-ba-se" in s or "-ba-se" in s:
            diagnostics.append({"rule": "TAM-21", "note": "Contains mirative revelation enclitic '-glak-se' / '-ba-se'"})

        # Check for imminent prospective aspect
        if "-na chwng-o" in s or "-na khe-kha" in s:
            diagnostics.append({"rule": "TAM-22", "note": "Contains imminent prospective aspect '-na chwng-o'"})

        # Check for iterative habitual frequentative
        if "-u-tong" in s or "-wi-tong-o" in s:
            diagnostics.append({"rule": "TAM-23", "note": "Contains iterative habitual frequentative '-u-tong'"})

        # Check for dubitative potential
        if "-kho-de" in s or "-khoba-de" in s:
            diagnostics.append({"rule": "TAM-24", "note": "Contains dubitative potential epistemic clitic '-kho-de'"})

        # Check for optative benediction
        if "-thung-se" in s:
            diagnostics.append({"rule": "TAM-25", "note": "Contains optative benediction enclitic '-thung-se'"})

        # Check for counter-expectational negative polar question
        if "-ya-khe-de?" in s or " ya-khe-de?" in s:
            diagnostics.append({"rule": "NEG-11", "note": "Contains counter-expectational negative polar question '-ya-khe-de?'"})

        # Check for interrupted imperfective converb
        if "-tong-twi-no" in s:
            diagnostics.append({"rule": "TAM-26", "note": "Contains interrupted imperfective converb '-tong-twi-no'"})

        # Check for inceptive promptive urgency
        if "-sa-no" in s:
            diagnostics.append({"rule": "TAM-27", "note": "Contains inceptive promptive urgency marker '-sa-no'"})

        # Check for frustrative aspect
        if "-kha-phano" in s and "wng-liya" in s:
            diagnostics.append({"rule": "TAM-28", "note": "Employs frustrative aspect '-kha-phano wng-liya'"})

        # Check for negative concessive irrealis
        if "-ya-phano" in s:
            diagnostics.append({"rule": "NEG-12", "note": "Contains negative concessive irrealis '-ya-phano'"})

        # Check for voice derivations
        if "-ri-" in s or "-ri " in s or s.endswith("-ri"):
            diagnostics.append({"rule": "VOI-01", "note": "Contains morphological causative suffix '-ri'"})
        if "-lai-" in s or "-lai " in s:
            diagnostics.append({"rule": "VOI-02", "note": "Contains reciprocal mutual action marker '-lai'"})
        if "-jak" in s:
            diagnostics.append({"rule": "VOI-03", "note": "Contains passive/resultative suffix '-jak'"})
        if "-phi-lai" in s or "-khol-lai" in s:
            diagnostics.append({"rule": "VOI-08", "note": "Contains iterative-distributive intensive '-phi-lai'"})
        if "-rwi-ri-" in s:
            diagnostics.append({"rule": "VOI-09", "note": "Contains benefactive applicative auxiliary '-rwi-ri-'"})
        if "-khok-" in s or "-khok-kha" in s:
            diagnostics.append({"rule": "VOI-10", "note": "Contains anticausative involuntary affix '-khok-'"})
        if "-pum-pai-kha" in s:
            diagnostics.append({"rule": "VOI-11", "note": "Contains intensive comprehensive completive '-pum-pai-kha'"})

        # Check for syntax & subordination
        if "-khe-phano" in s:
            diagnostics.append({"rule": "SYN-13", "note": "Contains concessive conditional linker '-khe-phano'"})
        if "-mung-o" in s:
            diagnostics.append({"rule": "SYN-14", "note": "Contains circumstantial nominalized clause marker '-mung-o'"})
        if "-ya-de?" in s or " ya-de?" in s:
            diagnostics.append({"rule": "SYN-15", "note": "Contains rhetorical confirmation tag '-ya-de?'"})
        if "je-khe" in s and "te-khe" in s:
            diagnostics.append({"rule": "SYN-16", "note": "Employs correlative conditional paradigm 'je-khe... te-khe...'"})
        if "hwn-khe" in s:
            diagnostics.append({"rule": "SYN-17", "note": "Contains parenthetical explicative complementizer 'hwn-khe'"})
        if " tebo " in s or s.startswith("tebo ") or ", tebo" in s:
            diagnostics.append({"rule": "SYN-18", "note": "Contains topic restatement particle 'tebo'"})
        if "kwbangma " in s or "thotot-no " in s or "bera " in s:
            diagnostics.append({"rule": "SYN-20", "note": "Contains pre-adjectival degree intensifier"})

        # Check for case markers
        for case_suf, r_id, desc in [
            ("-no", "CAS-01", "Accusative/Dative '-no'"),
            ("-ni", "CAS-02", "Genitive '-ni'"),
            ("-o", "CAS-03", "Locative '-o'"),
            ("-bai", "CAS-04", "Instrumental '-bai'"),
            ("-simi", "CAS-05", "Ablative '-simi'"),
            ("-ha", "CAS-06", "Allative '-ha'"),
            ("-sog", "CAS-07", "Terminative '-sog'"),
            ("-bagwi", "CAS-08", "Benefactive '-bagwi'"),
            ("-nikhre", "CAS-11", "Comparative standard '-nikhre'"),
            ("-hai", "CAS-15", "Similative role marker '-hai'"),
            ("joto-nikhre", "CAS-17", "Absolute superlative comparison 'joto-nikhre'"),
            ("-na bagwi", "CAS-18", "Purposive destinative relator '-na bagwi'"),
            ("-ni sam-o", "CAS-19", "Temporal anterior precedence relator '-ni sam-o'"),
            ("-bising-twi", "CAS-21", "Perlative pathway translocative '-bising-twi'"),
        ]:
            if case_suf in s:
                diagnostics.append({"rule": r_id, "note": f"Contains {desc}"})

        # Check for classifiers
        for cl in ["khorok-", "kwtwi-", "gong-", "tai-", "thai-", "phang-", "dung-", "chor-", "kan-", "phwt-", "che-", "sop-", "thak-", "gam-", "muk-", "khor-", "dop-", "khum-"]:
            if cl in s:
                diagnostics.append({"rule": "NUM-01", "note": f"Employs numeral classifier '{cl.rstrip('-')}'"})

        # Check for sensory expressives
        for exp_w, exp_id, exp_desc in [
            ("swm-swm", "EXP-08", "Aroma olfactory phonaestheme 'swm-swm'"),
            ("khem-khem", "EXP-08", "Fresh herb olfactory phonaestheme 'khem-khem'"),
            ("blet-blet", "EXP-09", "Viscous tactile ideophone 'blet-blet'"),
            ("srok-srok", "EXP-10", "Rustling whispering ideophone 'srok-srok'"),
            ("mrok-mrok", "EXP-10", "Subtle rustling ideophone 'mrok-mrok'"),
            ("dak-dak", "EXP-11", "Energetic motion phonaestheme 'dak-dak'"),
            ("phak-phak", "EXP-11", "Vigorous motor phonaestheme 'phak-phak'"),
        ]:
            if exp_w in s:
                diagnostics.append({"rule": exp_id, "note": f"Contains {exp_desc}"})


        # Check for 165 rule patterns
        if "-bo" in s and s.count("-bo") >= 2:
            diagnostics.append({"rule": "NOM-15", "note": "Contains coordinate copulative pairing '-bo... -bo'"})
        if "-twi" in s and ("borok-twi" in s or "chumai-twi" in s):
            diagnostics.append({"rule": "NOM-16", "note": "Contains associative distributive collectivizer '-twi'"})
        if "-ni bwsao" in s:
            diagnostics.append({"rule": "CAS-22", "note": "Contains locative delimitative circumscription '-ni bwsao'"})
        if "-ni khak-wi" in s:
            diagnostics.append({"rule": "CAS-23", "note": "Contains aversive separation postposition '-ni khak-wi'"})
        if "kok-sa" in s or "khumpui-sa" in s:
            diagnostics.append({"rule": "NUM-19", "note": "Contains container measure classifier"})
        if "-nani thwng-kha" in s or "-nani thwng" in s:
            diagnostics.append({"rule": "TAM-29", "note": "Contains imminent prospective aspect '-nani thwng'"})
        if "-kho-rwng" in s:
            diagnostics.append({"rule": "TAM-30", "note": "Contains procrastinative deliberative aspect '-kho-rwng'"})
        if "-u-man" in s:
            diagnostics.append({"rule": "TAM-31", "note": "Contains iterative habitual customary aspect '-u-man'"})
        if "-ya-rwng-wi" in s:
            diagnostics.append({"rule": "NEG-13", "note": "Contains incongruous non-volitional negative '-ya-rwng-wi'"})
        if "-ri-wi tong" in s:
            diagnostics.append({"rule": "VOI-12", "note": "Contains pre-verbal causative inchoative 'ri-wi tong'"})
        if "-se " in s and ("Bo-se " in s or "Ang-se " in s):
            diagnostics.append({"rule": "SYN-21", "note": "Employs appositive focus cleft construction with '-se'"})
        if "-wi " in s and s.count("-wi ") >= 2:
            diagnostics.append({"rule": "SYN-22", "note": "Employs echo subordination converbial linking '-wi... -wi'"})
        if "khor-khor" in s or "kir-kir" in s:
            diagnostics.append({"rule": "EXP-12", "note": "Contains somatosensory proprioceptive ideophone"})
        if "dur-dur" in s or "tur-tur" in s:
            diagnostics.append({"rule": "EXP-13", "note": "Contains kinesthetic tremor/vibration ideophone"})


        # Check for 180 rule patterns
        if "-jwi" in s and ("sa-bwrwi-jwi" in s or "nokhabani-jwi" in s):
            diagnostics.append({"rule": "NOM-17", "note": "Contains inclusive associative dual collective '-jwi'"})
        if "-thot" in s:
            diagnostics.append({"rule": "NOM-18", "note": "Contains partitive qualitative partition clitic '-thot'"})
        if "-ni bwsing-o" in s:
            diagnostics.append({"rule": "CAS-24", "note": "Contains subessive basal spatial relator '-ni bwsing-o'"})
        if "-ni chap-wi" in s or "-ni sok-wi" in s:
            diagnostics.append({"rule": "CAS-25", "note": "Contains proximal vicinal relator '-ni chap-wi'"})
        if "bak-nwi" in s or "bak-brwi" in s:
            diagnostics.append({"rule": "NUM-20", "note": "Contains fractional numeral quantification"})
        if "-na-rwng" in s:
            diagnostics.append({"rule": "TAM-32", "note": "Contains premonitory cautionary evitative '-na-rwng'"})
        if "-wi-wi" in s:
            diagnostics.append({"rule": "TAM-33", "note": "Contains frequentative distributive reduplicated aspect '-wi-wi'"})
        if "-kho-ba" in s:
            diagnostics.append({"rule": "TAM-34", "note": "Contains conjectural epistemic evidential mood '-kho-ba'"})
        if "ta-rwng-" in s:
            diagnostics.append({"rule": "NEG-14", "note": "Contains anticipatory preventive prohibitive frame 'ta-rwng-...-di'"})
        if "-choba-lai" in s:
            diagnostics.append({"rule": "VOI-13", "note": "Contains participatory co-agentive auxiliary '-choba-lai'"})
        if "jeba " in s.lower() and "tobo " in s.lower():
            diagnostics.append({"rule": "SYN-23", "note": "Employs adversative concessive inversion 'jeba... tobo...'"})
        if "hwn-ui sa-o" in s or "hwnwi sa-o" in s:
            diagnostics.append({"rule": "SYN-24", "note": "Contains parenthetical modal quotative epilogue 'hwn-ui sa-o'"})
        if "chwi-chwi" in s or "mwk-mwk" in s:
            diagnostics.append({"rule": "EXP-14", "note": "Contains thermal/climatic sensory phonaestheme"})
        if "krep-krep" in s or "chok-chok" in s:
            diagnostics.append({"rule": "EXP-15", "note": "Contains visual pattern geometric phonaestheme"})

        return {
            "sentence": sentence,
            "applicable_rules": diagnostics,
            "rules_count": len(diagnostics)
        }


_RULES_ENGINE: Optional[GrammarRulesEngine] = None

def get_grammar_rules_engine() -> GrammarRulesEngine:
    global _RULES_ENGINE
    if _RULES_ENGINE is None:
        _RULES_ENGINE = GrammarRulesEngine()
    return _RULES_ENGINE

def grammar_rules() -> List[GrammarRule]:
    """Retrieve all classical Kokborok grammar rules."""
    return get_grammar_rules_engine().all()
