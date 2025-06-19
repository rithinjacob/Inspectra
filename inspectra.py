from modules.qa import run_qa_check

def main():
    print("\n🔷 Welcome to Inspectra 🔷")
    print("1. QA Button/Link Check")
    print("2. [Coming Soon] Scraper")
    print("3. [Coming Soon] Accessibility Audit")

    choice = input("Choose an option (1–3): ")

    if choice == "1":
        url = input("Enter the full website URL (e.g., https://example.com): ")
        run_qa_check(url)
    else:
        print("🚧 That module isn't built yet.")

if __name__ == "__main__":
    main()
