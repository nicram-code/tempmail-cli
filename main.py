from src.imports import *
from src.utils import *

CRREATE_TEMP_EMAIL_URL = ""
INBOX_URL =""
SITE_URL=""


colorama.init()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    reset = "\033[0m"
    print(
        "\033[38;2;255;50;50m"   + " /$$$$$$$$                                      /$$      /$$           /$$ /$$        /$$$$$$  /$$ /$$" + "\n" +
        "\033[38;2;255;80;80m"   + "|__  $$__/                                     | $$$    /$$$          |__/| $$       /$$__  $$| $$|__/" + "\n" +
        "\033[38;2;255;110;110m" + "   | $$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$$$  /$$$$  /$$$$$$  /$$| $$      | $$  \__/| $$ /$$" + "\n" +
        "\033[38;2;255;140;140m" + "   | $$ /$$__  $$| $$_  $$_  $$ /$$__  $$      | $$ $$/$$ $$ |____  $$| $$| $$      | $$      | $$| $$" + "\n" +
        "\033[38;2;255;170;170m" + "   | $$| $$$$$$$$| $$ \ $$ \ $$| $$  \ $$      | $$  $$$| $$  /$$$$$$$| $$| $$      | $$      | $$| $$" + "\n" +
        "\033[38;2;255;200;200m" + "   | $$| $$_____/| $$ | $$ | $$| $$  | $$      | $$\  $ | $$ /$$__  $$| $$| $$      | $$    $$| $$| $$" + "\n" +
        "\033[38;2;255;225;225m" + "   | $$|  $$$$$$$| $$ | $$ | $$| $$$$$$$/      | $$ \/  | $$|  $$$$$$$| $$| $$      |  $$$$$$/| $$| $$" + "\n" +
        "\033[38;2;255;240;240m" + "   |__/ \_______/|__/ |__/ |__/| $$____/       |__/     |__/ \_______/|__/|__/       \______/ |__/|__/" + "\n" +
        "\033[38;2;255;248;248m" + "                               | $$                                                                   " + "\n" +
        "\033[38;2;255;252;252m" + "                               | $$                                                                   " + "\n" +
        "\033[38;2;255;255;255m" + "                               |__/                                                                   " + "\n" +
        "\033[38;2;255;255;255m" + "    ───────────────────────────────────────────────────────────────────────────────────────────────" +
        reset + "\n"
    )





def choose_mode():
    print(
        f"\n{Fore.RED}[{Style.RESET_ALL}1{Fore.RED}]{Style.RESET_ALL} Create a new temporary email address\n"
        f"{Fore.RED}[{Style.RESET_ALL}2{Fore.RED}]{Style.RESET_ALL} View existing email addresses\n"
        f"{Fore.RED}[{Style.RESET_ALL}3{Fore.RED}]{Style.RESET_ALL} Help\n"
        f"{Fore.RED}[{Style.RESET_ALL}99{Fore.RED}]{Style.RESET_ALL} Exit"
    )

def create_email():
    pass

def view_emails():
    pass

def open_site():
    webbrowser.open(SITE_URL)


def help_menu():
    banner()
    print(f"\n{Fore.RED}{'─' * 40}{Style.RESET_ALL}")
    print(f"  {Fore.RED}[{Style.RESET_ALL} Help Center {Fore.RED}]{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─' * 40}{Style.RESET_ALL}\n")

    print(f"  {Fore.RED}[{Style.RESET_ALL}1{Fore.RED}]{Style.RESET_ALL} Create new email")
    print(f"      Generate a random temporary email address\n")

    print(f"  {Fore.RED}[{Style.RESET_ALL}2{Fore.RED}]{Style.RESET_ALL} View existing emails")
    print(f"      Check inbox of a previously created address\n")

    print(f"  {Fore.RED}[{Style.RESET_ALL}3{Fore.RED}]{Style.RESET_ALL} Help")
    print(f"      Show this help menu\n")

    print(f"  {Fore.RED}[{Style.RESET_ALL}99{Fore.RED}]{Style.RESET_ALL} Exit")
    print(f"      Quit the program\n")

    print(f"{Fore.RED}{'─' * 40}{Style.RESET_ALL}")
    print(f"  {Fore.RED}[{Style.RESET_ALL}*{Fore.RED}]{Style.RESET_ALL} Powered by 1secmail API")
    print(f"  {Fore.RED}[{Style.RESET_ALL}*{Fore.RED}]{Style.RESET_ALL} Emails expire after ~1-2h")
    print(f"  {Fore.RED}[{Style.RESET_ALL}*{Fore.RED}]{Style.RESET_ALL} No registration required")
    print(f"{Fore.RED}{'─' * 40}{Style.RESET_ALL}\n")
    input(f"{Fore.RED}Press Enter to return to the main menu...{Style.RESET_ALL}")
    clear()
    main()


def main():
    clear()
    banner()
    choose_mode()
    hostname = check_platform()
    while True:
        choice = input(f"\n{Fore.RED}{hostname}@root {Style.RESET_ALL}")
        if choice == "1":
            create_email()
        elif choice == "2":
            view_emails()
        elif choice == "3":
            help_menu()
        elif choice == "99":
            print(f"\n{Fore.RED}Exiting...{Style.RESET_ALL}")
            time.sleep(0.3)
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    
    clear()
    main()