# build_index.py - wandelt die Wahlprogramm-PDFs in wahlprogramme.json um
import json
from pathlib import Path
from pypdf import PdfReader

ORDNER = Path(__file__).parent / "pdfs"

# Dateiname: (Partei, Jahr, URL zur Originalquelle)
PROGRAMME = {
    "spd_2025.pdf": ("SPD", 2025, "https://mehr.spd.de/custom-static-assets/documents/Regierungsprogramm.pdf"),
    "cdu_2025.pdf": ("CDU", 2025, "https://www.cdu.de/app/uploads/2025/01/km_btw_2025_wahlprogramm_langfassung_ansicht.pdf"),
    "gruene_2025.pdf": ("Grüne", 2025, "https://cms.gruene.de/uploads/assets/Regierungsprogramm_DIGITAL_DINA5.pdf"),
    "linke_2025.pdf": ("Linke", 2025, "https://www.die-linke.de/fileadmin/user_upload/Wahlprogramm_Langfassung_Linke-BTW25_01.pdf"),
    "afd_2025.pdf": ("AfD", 2025, "https://www.afd.de/wp-content/uploads/2025/02/AfD_Bundestagswahlprogramm2025_web.pdf"),
}

chunks = []
for datei, (partei, jahr, url) in PROGRAMME.items():
    pfad = ORDNER / datei
    if not pfad.exists():
        print(f"WARNUNG: {pfad} fehlt, {partei} wird übersprungen")
        continue
    n_vorher = len(chunks)
    for seite, page in enumerate(PdfReader(pfad).pages, start=1):
        woerter = (page.extract_text() or "").split()
        for i in range(0, len(woerter), 150):
            text = " ".join(woerter[i:i + 150])
            if len(text) > 200:
                chunks.append({"partei": partei, "jahr": jahr,
                               "seite": seite, "quelle": url, "text": text})
    print(f"{partei}: {len(chunks) - n_vorher} Abschnitte")

Path("wahlprogramme.json").write_text(json.dumps(chunks, ensure_ascii=False), encoding="utf-8")
print(len(chunks), "Abschnitte gesamt")
