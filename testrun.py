import telebot
from colorama import *


bot = telebot.TeleBot('8263239418:AAF--j6XK5lrsyLoyyJWB6bHq4dY9Ju1sEU')

ids = [
    1354151664,
    6075185878,
    6465197738,
    5793178716,
    6001251435,
    700757795,
    1366186241,
    5124322209,
    7690702801,
    5927695653,
    7060081455,
]


print(f"{Fore.GREEN}{'ID':^11}|{'Username':^20}|{'First Name':^20}|{'Last Name':^20}|{Style.RESET_ALL}")
print("-" * 72)

i = 1000000000
while i <= 8000000000:
    try:
        user = bot.get_chat(i)
        print(f"{Fore.RED}{i:^11}{Fore.RESET}|"
              f"{Fore.YELLOW}{(user.username or 'N/A'):^20}{Fore.RESET}|"
              f"{Fore.GREEN}{(user.first_name or 'N/A'):^20}{Fore.RESET}|"
              f"{Fore.CYAN}{(user.last_name or 'N/A'):^20}{Fore.RESET}|")
        print('_' * 71)
    except Exception as e:
        print(f"{Fore.RED}{'Could not fetch info for user':^30} {i}: {e}{Fore.RESET}")
    i += 1
