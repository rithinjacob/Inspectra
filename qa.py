import requests
from bs4 import BeautifulSoup

def run_qa_check(url):
    print(f"\n🔍 Inspectra QA running on: {url}\n")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        print(f"❌ Error fetching the site: {e}")
        return

    # Find all links/buttons (a tags)
    buttons = soup.find_all("a")
    print("🧩 Buttons / Links Found:")
    for i, btn in enumerate(buttons, 1):
        label = btn.text.strip() or "[No Text]"
        href = btn.get("href", "❌ No link")
        print(f"{i}. {label} → {href}")

    if not buttons:
        print("⚠️ No links or buttons found.")

    print("\n✅ QA check complete.\n")
