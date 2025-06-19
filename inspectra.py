from modules.qa import run_qa_check
from modules.scraper import run_scraper
from modules.accessibility import run_accessibility_check

def main():
    while True:
        print("\n🔷 Welcome to Inspectra 🔷")
        print("1. QA Button/Link Check")
        print("2. Web Scraper")
        print("3. Accessibility Audit")
        print("q. Quit")

        choice = input("Choose an option (1–3 or q): ").lower()

        if choice == "1":
            url = input("Enter the full website URL (e.g., https://example.com): ")
            run_qa_check(url)
        elif choice == "2":
            run_scraper()
        elif choice == "3":
            run_accessibility_check()
        elif choice == "q":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

