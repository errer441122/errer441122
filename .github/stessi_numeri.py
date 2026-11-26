"""I numeri del profilo devono essere gli stessi in README.md (inglese) e README.it.md (italiano).

Si contano solo i numeri staccati dalle lettere (non n8n, GA4, B2B). I link non contano.
Inglese: 48,000 e 26.1; italiano: 48.000 e 26,1. Una versione come 2.48.7 resta com'è.
"""
import re
import sys
from collections import Counter

NUMERO = re.compile(r"(?<![\w.,])\d+(?:[.,]\d+)*(?![\w])")


def numeri(testo, lingua):
    testo = re.sub(r"\]\([^)]*\)|https?://\S+|<!--.*?-->", " ", testo, flags=re.S)
    trovati = Counter()
    for n in NUMERO.findall(testo):
        n = n.rstrip(".,")
        migliaia, decimali = (",", ".") if lingua == "en" else (".", ",")
        if re.fullmatch(r"\d{1,3}(?:" + re.escape(migliaia) + r"\d{3})+", n):
            n = n.replace(migliaia, "")
        elif n.count(decimali) == 1 and migliaia not in n:
            n = n.replace(decimali, ".")
        trovati[n] += 1
    return trovati


def main(inglese, italiano):
    en = numeri(open(inglese, encoding="utf-8").read(), "en")
    it = numeri(open(italiano, encoding="utf-8").read(), "it")
    solo_en, solo_it = en - it, it - en
    for nome, diff in ((inglese, solo_en), (italiano, solo_it)):
        for n, volte in sorted(diff.items()):
            print(f"Solo in {nome}: {n}" + (f" ({volte} volte)" if volte > 1 else ""))
    if solo_en or solo_it:
        print("I numeri delle due versioni non coincidono: aggiorna quella rimasta indietro.")
        return 1
    print(f"Stessi numeri nelle due versioni ({sum(en.values())}).")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
