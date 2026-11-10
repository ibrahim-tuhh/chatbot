# build_index.py
import json
from pypdf import PdfReader

PROGRAMME = {  # Dateiname: (Partei, Jahr, URL)
    "spd_2025.pdf": ("SPD", 2025, "https://..."),
    "cdu_2025.pdf": ("CDU", 2025, "https://..."),
    "gruene_2025.pdf": ("Grüne", 2025, "https://..."),
    "linke_2025.pdf": ("Linke", 2025, "https://..."),
    "afd_2025.pdf": ("AfD", 2025, "https://..."),
}

chunks = []
for datei, (partei, jahr, url) in PROGRAMME.items():
    for seite, page in enumerate(PdfReader(f"pdfs/{datei}").pages, start=1):
        woerter = (page.extract_text() or "").split()
        for i in range(0, len(woerter), 150):
            text = " ".join(woerter[i:i + 150])
            if len(text) > 200:
                chunks.append({"partei": partei, "jahr": jahr,
                               "seite": seite, "quelle": url, "text": text})

json.dump(chunks, open("wahlprogramme.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(chunks), "Abschnitte")
