# -*- coding: utf-8 -*-
"""Kokborok Cardinal & Ordinal Numeral Converter."""

ONES = {
    1: "sa", 2: "nwi", 3: "tham", 4: "brwi", 5: "ba",
    6: "dok", 7: "sni", 8: "char", 9: "chuku"
}

TEENS = {
    10: "chi", 11: "chisa", 12: "chinwi", 13: "chitham", 14: "chibrwi",
    15: "chiba", 16: "chidok", 17: "chisni", 18: "chichar", 19: "chichuku"
}

TENS = {
    20: "rwichi", 30: "kholchi", 40: "brwichi", 50: "bachi",
    60: "dokchi", 70: "snichi", 80: "charchi", 90: "chukuchi"
}

def num_to_words(n: int) -> str:
    """Convert integer to Kokborok words up to 1,000,000."""
    if n == 0:
        return "yasi"
    if n < 0:
        return "mwsung " + num_to_words(-n)

    if n in ONES:
        return ONES[n]
    if n in TEENS:
        return TEENS[n]
    if n in TENS:
        return TENS[n]

    if 21 <= n <= 99:
        tens_val = (n // 10) * 10
        rem = n % 10
        return f"{TENS[tens_val]} {ONES[rem]}"

    if 100 <= n <= 999:
        hundreds = n // 100
        rem = n % 100
        h_str = "ra-sa" if hundreds == 1 else f"ra-{ONES[hundreds]}"
        if rem == 0:
            return h_str
        return f"{h_str} {num_to_words(rem)}"

    if 1000 <= n <= 99999:
        thousands = n // 1000
        rem = n % 1000
        t_str = "sai-sa" if thousands == 1 else f"sai-{num_to_words(thousands)}"
        if rem == 0:
            return t_str
        return f"{t_str} {num_to_words(rem)}"

    if n >= 100000:
        lakhs = n // 100000
        rem = n % 100000
        l_str = "lak-sa" if lakhs == 1 else f"lak-{num_to_words(lakhs)}"
        if rem == 0:
            return l_str
        return f"{l_str} {num_to_words(rem)}"

    return str(n)

def words_to_num(text: str) -> int:
    """Convert Kokborok numeral words back to integer."""
    clean = text.lower().strip()
    words = clean.replace("-", " ").split()
    total = 0
    current = 0
    for w in words:
        for k, v in ONES.items():
            if w == v:
                current += k
        for k, v in TEENS.items():
            if w == v:
                current += k
        for k, v in TENS.items():
            if w == v:
                current += k
        if w in ["ra", "rasa"]:
            current = (current if current else 1) * 100
            total += current
            current = 0
        elif w in ["sai", "saisa"]:
            current = (current if current else 1) * 1000
            total += current
            current = 0
        elif w in ["lak", "laksa"]:
            current = (current if current else 1) * 100000
            total += current
            current = 0
    return total + current

def ordinal(n: int) -> str:
    """Convert number to Kokborok ordinal form."""
    if n == 1:
        return "bwngkhrw / achuk"
    return f"{num_to_words(n)}-ni"
