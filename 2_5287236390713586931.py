#dont edit my name!!!!
#by @bahez_sherwany
	

input("  what your name ? : ")

import smtplib
import ssl
import os
from colorama import Fore, Style, init

init(autoreset=True)

def check_smtp(host, port, user, password):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, int(port), context=context, timeout=10) as server:
            server.login(user, password)
        return True
    except:
        return False

def print_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "="*50)
    print(Fore.GREEN + "   [✓]   SMTP CHECKER PRO ")
    print('')
    print(Fore.GREEN + "[✓] Developer  @bahez_sherwany ")
    print(Fore.CYAN + "="*50)
    print(Fore.YELLOW + " Combo Format: " + Fore.WHITE + "host|port|email|password")
    print(Fore.MAGENTA + " Example     : smtp.example.com|465|mail@example.com|pass123")
    print(Fore.CYAN + "="*50 + "\n")

def main():
    print_banner()

    combo_file = input(Fore.YELLOW + "Enter combo filename: " + Fore.WHITE)

    if not os.path.exists(combo_file):
        print(Fore.RED + "File not found.")
        return

    with open(combo_file, "r") as file:
        combos = file.read().splitlines()

    valid_count = 0
    invalid_count = 0

    for line in combos:
        try:
            host, port, user, password = line.strip().split("|")
            print(Fore.BLUE + f"Checking: {user}...", end=" ")
            if check_smtp(host, port, user, password):
                print(Fore.GREEN + "VALID")
                with open("valid_smtps.txt", "a") as valid_file:
                    valid_file.write(f"{host}|{port}|{user}|{password}\n")
                valid_count += 1
            else:
                print(Fore.RED + "INVALID")
                invalid_count += 1
        except:
            print(Fore.RED + "FORMAT ERROR")
            invalid_count += 1

    print(Fore.CYAN + "\nScan Finished.")
    print(Fore.GREEN + f"Total Valid: {valid_count}")
    print(Fore.RED + f"Total Invalid: {invalid_count}")
    print(Fore.CYAN + "Saved to: valid_smtps.txt")

if __name__ == "__main__":
    main()
