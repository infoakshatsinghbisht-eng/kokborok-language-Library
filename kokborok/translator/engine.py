# -*- coding: utf-8 -*-
"""Kokborok Translation Engine."""

import re
from typing import NamedTuple, Optional

class TranslationResult(NamedTuple):
    text: str
    source_lang: str
    target_lang: str
    confidence: float
    dialect: str

    def __repr__(self) -> str:
        return f"<TranslationResult text='{self.text}' dialect='{self.dialect}' conf={self.confidence:.2f}>"

CONVERSATIONAL_EN_KOK = [
    (r"\bhow are you\b", "Nwng bahai tong?"),
    (r"\b(hello|hi|greetings|welcome)\b", "Khulumkha!"),
    (r"\b(i am fine|i am good)\b", "Ang kaham tong."),
    (r"\b(thank you|thanks)\b", "Hambai!"),
    (r"\bwhat is your name\b", "Nini mung tamo?"),
    (r"\bmy name is\s+(.*)", r"Ani mung \1."),
    (r"\bgood morning\b", "Kaham sal!"),
    (r"\bgood night\b", "Kaham hor!"),
    (r"\bwhere are you going\b", "Nwng boro thangnai?"),
    (r"\bi love you\b", "Ang nungno hamjakgo."),
    (r"\bcome here\b", "Oro phai."),
    (r"\bgo there\b", "Aro thang."),
    (r"\bwhat are you doing\b", "Nwng tamo khwlaio?"),
    (r"\bi am eating rice\b", "Ang mai chaotong.")
]

CONVERSATIONAL_HI_KOK = [
    (r"(नमस्ते|नमस्कार|प्रणाम)", "Khulumkha!"),
    (r"(आप कैसे हैं|तुम कैसे हो)", "Nwng bahai tong?"),
    (r"(मैं ठीक हूँ|मैं अच्छा हूँ)", "Ang kaham tong."),
    (r"(धन्यवाद|शुक्रिया)", "Hambai!"),
    (r"(आपका नाम क्या है|तुम्हारा नाम क्या है)", "Nini mung tamo?"),
    (r"(सुप्रभात|शुभ प्रभात)", "Kaham sal!"),
    (r"(शुभ रात्रि)", "Kaham hor!"),
    (r"(तुम कहाँ जा रहे हो|आप कहाँ जा रहे हैं)", "Nwng boro thangnai?"),
    (r"(मैं तुमसे प्यार करता हूँ|मुझे तुमसे प्यार है)", "Ang nungno hamjakgo.")
]

CONVERSATIONAL_BEN_KOK = [
    (r"(নমস্কার|সালাম|হ্যালো)", "Khulumkha!"),
    (r"(আপনি কেমন আছেন|তুমি কেমন আছো)", "Nwng bahai tong?"),
    (r"(আমি ভালো আছি)", "Ang kaham tong."),
    (r"(ধন্যবাদ)", "Hambai!"),
    (r"(আপনার নাম কি|তোমার নাম কি)", "Nini mung tamo?"),
    (r"(শুভ সকাল)", "Kaham sal!"),
    (r"(শুভ রাত্রি)", "Kaham hor!"),
    (r"(তুমি কোথায় যাচ্ছো|আপনি কোথায় যাচ্ছেন)", "Nwng boro thangnai?"),
    (r"(আমি তোমাকে ভালোবাসি)", "Ang nungno hamjakgo.")
]

CONVERSATIONAL_KOK_EN = [
    (r"\bkhulumkha\b", "Greetings / Hello!"),
    (r"\bhambai\b", "Thank you!"),
    (r"\bnwng bahai tong\b", "How are you?"),
    (r"\bang kaham tong\b", "I am fine."),
    (r"\bnini mung tamo\b", "What is your name?"),
    (r"\bang nungno hamjakgo\b", "I love you.")
]

def translate(
    text: str,
    source: str = "auto",
    target: str = "kokborok",
    dialect: str = "debbarma"
) -> TranslationResult:
    """Translate text bidirectionally between Kokborok, English, Hindi, and Bengali."""
    clean = text.strip()
    if not clean:
        return TranslationResult("", source, target, 1.0, dialect)
    clean_low = clean.lower()
    clean_no_punct = re.sub(r"[^\w\s]", "", clean_low).strip()

    from .dialects import apply_dialect

    # Kokborok -> English
    if target.lower() in ("en", "english"):
        for pat, en_tgt in CONVERSATIONAL_KOK_EN:
            if re.search(pat, clean_low) or re.search(pat, clean_no_punct):
                return TranslationResult(en_tgt, "kokborok", "en", 0.98, dialect)
        try:
            from ..lexicon.dictionary import get_dictionary
            d = get_dictionary()
            tokens = clean.split()
            res = []
            f_count = 0
            for t in tokens:
                cl = t.strip(".,!?:;\"'()[]")
                entry = d.lookup(cl)
                if entry and entry.get("english"):
                    res.append(entry["english"].split("/")[0].strip())
                    f_count += 1
                else:
                    res.append(t)
            if f_count > 0:
                return TranslationResult(" ".join(res), "kokborok", "en", max(round(f_count / len(tokens), 2), 0.60), dialect)
        except Exception:
            pass
        return TranslationResult(clean, "kokborok", "en", 0.40, dialect)

    # English -> Kokborok
    for pat, kok_tgt in CONVERSATIONAL_EN_KOK:
        if re.search(pat, clean_low) or re.search(pat, clean_no_punct):
            matched = re.sub(pat, kok_tgt, clean_no_punct) if "\\1" in kok_tgt else kok_tgt
            return TranslationResult(apply_dialect(matched, dialect), "en", target, 0.98, dialect)

    # Hindi -> Kokborok
    for pat, kok_tgt in CONVERSATIONAL_HI_KOK:
        if re.search(pat, clean) or re.search(pat, clean_no_punct):
            return TranslationResult(apply_dialect(kok_tgt, dialect), "hi", target, 0.98, dialect)

    # Bengali -> Kokborok
    for pat, kok_tgt in CONVERSATIONAL_BEN_KOK:
        if re.search(pat, clean) or re.search(pat, clean_no_punct):
            return TranslationResult(apply_dialect(kok_tgt, dialect), "bengali", target, 0.98, dialect)

    # Word lookup fallback
    try:
        from ..lexicon.dictionary import get_dictionary
        d = get_dictionary()
        tokens = clean.split()
        res = []
        f_count = 0
        for t in tokens:
            cl = t.strip(".,!?:;\"'()[]")
            entries = d.search(cl)
            if entries:
                res.append(entries[0]["kokborok"])
                f_count += 1
            else:
                res.append(t)
        if f_count > 0:
            composed = " ".join(res)
            return TranslationResult(apply_dialect(composed, dialect), source, target, max(round(f_count / len(tokens), 2), 0.60), dialect)
    except Exception:
        pass

    return TranslationResult(clean, source, target, 0.50, dialect)
