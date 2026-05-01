import requests
import os

# kolory
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# czerwony banner
banner = f"""{RED}
_       _       _               _            _  __      _____  
           (_)     (_)     | |             | |          | | \ \    / /__ \ 
  _ __ ___  _ _ __  _   ___| |__   ___ _ __| | ___   ___| | _\ \  / /   ) |
 | '_ ` _ \| | '_ \| | / __| '_ \ / _ \ '__| |/ _ \ / __| |/ /\ \/ /   / / 
 | | | | | | | | | | | \__ \ | | |  __/ |  | | (_) | (__|   <  \  /   / /_ 
 |_| |_| |_|_|_| |_|_| |___/_| |_|\___|_|  |_|\___/ \___|_|\_\  \/   |____|
                   ______                                                  
                  |______|
{RESET}
"""

sites = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitter/X": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Twitch": "https://www.twitch.tv/{}",
    "GitLab": "https://gitlab.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Steam": "https://steamcommunity.com/id/{}"
}

def scan(username):
    print("\nSkanowanie...\n")
    found = 0

    for name, url in sites.items():
        full_url = url.format(username)

        try:
            r = requests.get(full_url, timeout=5)

            if r.status_code == 200:
                print(f"{GREEN}[+] {name}: {full_url}{RESET}")
                found += 1
            else:
                print(f"[-] {name}: brak")

        except:
            print(f"[!] {name}: blad")

    print(f"\nZnaleziono: {found}/{len(sites)}")

def credits():
    print("\n=== CREDITS ===")
    print("Tool: Mini Sherlock PRO")
    print("Author: Rybkix")
    print("Language: Python")
    print("================\n")

os.system("cls" if os.name == "nt" else "clear")

print(banner)

while True:
    print("1. Skanuj nick")
    print("2. Credits")
    print("3. Wyjscie")

    choice = input("\nWybierz opcje: ")

    if choice == "1":
        username = input("Podaj nick: ")
        scan(username)

    elif choice == "2":
        credits()

    elif choice == "3":
        break

    else:
        print("Zla opcja")
