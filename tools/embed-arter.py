#!/usr/bin/env python3
"""Bak arter.json inn i index.html.

Fuglevinduet er én HTML-fil, så artsdataene må ligge inne i dokumentet
(en fetch av arter.json virker ikke når filen åpnes rett fra disk).
arter.json i repoet er kilden. Kjør dette etter hver redigering:

    python3 tools/embed-arter.py

Skriptet er et redigeringsverktøy, ikke et byggesteg: index.html er
komplett og kjørbar uten at det noen gang kjøres.
"""
import json, re, sys, pathlib

rot = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((rot / "arter.json").read_text(encoding="utf-8"))
html = (rot / "index.html").read_text(encoding="utf-8")

blokk = json.dumps(data, ensure_ascii=False, indent=1)
# </script> inne i en JSON-streng ville avsluttet taggen for tidlig
blokk = blokk.replace("</", "<\\/")

ny, n = re.subn(
    r'(<script id="arter-data" type="application/json">\n).*?(\n</script>)',
    lambda m: m.group(1) + blokk + m.group(2),
    html, flags=re.S)

if n != 1:
    sys.exit("Fant ikke arter-data-blokken i index.html (traff %d ganger)" % n)

(rot / "index.html").write_text(ny, encoding="utf-8")
print("Bakte inn %d arter i index.html" % len(data))
