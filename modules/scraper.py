import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_scraper():
    print("\n🌐 Website Scraper Module")
    url = input("Enter a website URL to scrape: ")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        images = [img.get('src') for img in soup.find_all('img')]
        alt_texts = [img.get('alt') for img in soup.find_all('img') if img.get('alt')]

        print(f"\n📝 Headings found: {len(headings)}")
        print(f"📄 Paragraphs found: {len(paragraphs)}")
        print(f"🖼️ Images found: {len(images)}")
        print(f"🔤 Alt text present: {len(alt_texts)}")

        # 🧾 Write results to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"inspectra_scrape_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Inspectra Web Scrape Report - {url}\n\n")
            f.write(f"Headings ({len(headings)}):\n" + "\n".join(headings[:10]) + "\n\n")
            f.write(f"Paragraphs ({len(paragraphs)}):\n" + "\n".join(paragraphs[:5]) + "\n\n")
            f.write(f"Images ({len(images)}):\n" + "\n".join(images[:5]) + "\n\n")
            f.write(f"Alt Texts ({len(alt_texts)}):\n" + "\n".join(alt_texts[:5]) + "\n\n")

        print(f"\n✅ Report saved to `{filename}`\n")

    except Exception as e:
        print(f"❌ Error: {e}")
