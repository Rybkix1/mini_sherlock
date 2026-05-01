import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

banner = f"""{RED}
            _       _       _               _            _    
           (_)     (_)     | |             | |          | |   
  _ __ ___  _ _ __  _   ___| |__   ___ _ __| | ___   ___| | __
 | '_ ` _ \| | '_ \| | / __| '_ \ / _ \ '__| |/ _ \ / __| |/ /
 | | | | | | | | | | | \__ \ | | |  __/ |  | | (_) | (__|   < 
 |_| |_| |_|_|_| |_|_| |___/_| |_|\___|_|  |_|\___/ \___|_|\_\
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

headers = {
    "User-Agent": "Mozilla/5.0"
}


def check_site(name, url):
    try:
        r = requests.get(url, headers=headers, timeout=7)

        # redirect check (często fake profile detection)
        final_url = r.url

        if r.status_code in [404, 410]:
            return f"{RED}[-] NOT FOUND {name}{RESET}"

        if final_url == "https://github.com/" or final_url.endswith("/login"):
            return f"{RED}[-] NOT FOUND {name}{RESET}"

        if r.status_code == 200:
            return f"{GREEN}[+] FOUND {name}: {url}{RESET}"

        return f"{YELLOW}[!] BLOCKED/UNKNOWN {name}{RESET}"

    except requests.RequestException:
        return f"{YELLOW}[!] BLOCKED {name}{RESET}"


def scan(username):
    print("\nSkanowanie (FAST MODE)...\n")

    found = 0

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []

        for name, url in sites.items():
            full_url = url.format(username)
            futures.append(executor.submit(check_site, name, full_url))

        for f in as_completed(futures):
            result = f.result()
            print(result)

            if "[+] FOUND" in result:
                found += 1

    print(f"\nZnaleziono: {found}/{len(sites)}")


def credits():
    print("\n=== CREDITS ===")
    print("Tool: Mini Sherlock PRO FAST")
    print("Author: Rybkix")
    print("Version: v2")
    print("================\n")


os.system("cls" if os.name == "nt" else "clear")
print(banner)

while True:
    print("\n1. Skanuj nick")
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