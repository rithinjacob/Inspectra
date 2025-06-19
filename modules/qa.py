import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_qa_check(url):
    print(f"\n🔎 Inspectra QA running on: {url}\n")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        print(f"❌ Error fetching the site: {e}")
        return

    buttons = soup.find_all("a")
    print(f"🔗 Buttons / Links found: {len(buttons)}")

    results = []

    for i, btn in enumerate(buttons, 1):
        label = btn.text.strip() or "[No Text]"
        href = btn.get("href", "❌ No link")
        line = f"{i}. {label} → {href}"
        results.append(line)
        print(line)

    if not buttons:
        print("▲ No links or buttons found.")

    # 🔽 Save to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"inspectra_qa_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Inspectra QA Report – {url}\n\n")
        if not buttons:
            f.write("▲ No links or buttons found.\n")
        else:
            f.write("\n".join(results))

    print(f"\n✅ QA report saved to `{filename}`\n")
