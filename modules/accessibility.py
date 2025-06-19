import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_accessibility_check():
    print("\n🦽 Accessibility Audit Module")
    url = input("Enter a website URL to audit: ")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        missing_alt = []
        form_issues = []

        for img in soup.find_all('img'):
            if not img.get('alt'):
                missing_alt.append(str(img.get('src')))

        for form in soup.find_all('form'):
            inputs = form.find_all(['input', 'textarea', 'select'])
            for i in inputs:
                if not i.get('aria-label') and not i.get('alt') and not i.get('name'):
                    form_issues.append(str(i))

        print(f"\n🔍 Images missing alt text: {len(missing_alt)}")
        print(f"📝 Form elements missing labels: {len(form_issues)}")

        # Export to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"inspectra_accessibility_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Inspectra Accessibility Report – {url}\n\n")
            f.write(f"Images missing alt text ({len(missing_alt)}):\n" + "\n".join(missing_alt[:10]) + "\n\n")
            f.write(f"Form inputs missing labels ({len(form_issues)}):\n" + "\n".join(form_issues[:10]) + "\n\n")

        print(f"\n✅ Report saved to `{filename}`\n")

    except Exception as e:
        print(f"❌ Error: {e}")
