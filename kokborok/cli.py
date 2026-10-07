# -*- coding: utf-8 -*-
"""Kokborok Command-Line Interface (CLI)."""

import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(
        prog="kokborok",
        description="Kokborok Language Processing and Cultural Heritage Toolkit"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    p_trans = subparsers.add_parser("translate", help="Translate to/from Kokborok")
    p_trans.add_argument("text", help="Text to translate")
    p_trans.add_argument("--to", default="kokborok", help="Target language (kokborok, en, hi, bengali)")
    p_trans.add_argument("--dialect", default="debbarma", help="Dialect (debbarma, reang, jamatia, noatia)")

    p_look = subparsers.add_parser("lookup", help="Look up Kokborok word")
    p_look.add_argument("word", help="Word to look up")

    p_num = subparsers.add_parser("num", help="Convert numbers to Kokborok")
    p_num.add_argument("number", type=int, help="Integer to convert")
    p_num.add_argument("--classifier", default=None, help="Numeral classifier (e.g., khorok, gong, tai)")

    subparsers.add_parser("stats", help="Display library statistics")

    p_cult = subparsers.add_parser("culture", help="View cultural information")
    p_cult.add_argument("topic", choices=["festivals", "authors", "epics", "kinship", "months", "days"], help="Topic to display")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    import kokborok

    if args.command == "translate":
        res = kokborok.translate(args.text, target=args.to, dialect=args.dialect)
        print(f"[{res.source_lang} -> {res.target_lang}] ({res.dialect}, conf={res.confidence}):")
        print(res.text)

    elif args.command == "lookup":
        entry = kokborok.lookup(args.word)
        if entry:
            print(json.dumps(entry, ensure_ascii=False, indent=2))
        else:
            print(f"Word '{args.word}' not found in dictionary.")

    elif args.command == "num":
        words = kokborok.num_to_words(args.number)
        if args.classifier:
            cls_form = kokborok.apply_classifier(args.number, args.classifier)
            print(f"{args.number} -> {words} (With classifier: {cls_form})")
        else:
            print(f"{args.number} -> {words}")

    elif args.command == "stats":
        st = kokborok.stats()
        print("=== KOKBOROK LANGUAGE LIBRARY STATISTICS ===")
        for k, v in st.items():
            print(f"  {k}: {v}")

    elif args.command == "culture":
        if args.topic == "festivals":
            for f in kokborok.list_festivals():
                print(f"- {f['name']} ({f['native']}): {f['season']}")
        elif args.topic == "authors":
            for a in kokborok.list_authors():
                print(f"- {a['name']} ({a['title']}): {a['notable_works']}")
        elif args.topic == "epics":
            for e in kokborok.list_epics():
                print(f"- {e['title']} ({e['type']})")
        elif args.topic == "kinship":
            for k in kokborok.list_kinship_terms():
                print(f"- {k['kokborok']} = {k['english']} ({k['role']})")
        elif args.topic == "months":
            for m in kokborok.get_months():
                print(f"- {m['kokborok']}: {m['english']} ({m['meaning']})")
        elif args.topic == "days":
            for d in kokborok.get_days():
                print(f"- {d['kokborok']}: {d['english']}")

if __name__ == "__main__":
    main()
