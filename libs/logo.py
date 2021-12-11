# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
    _    ____   ____ _   _ ____  ____   _    __  __ 
   / \  |  _ \ / ___| | | / ___||  _ \ / \  |  \/  |
  / _ \ | |_) | |   | |_| \___ \| |_) / _ \ | |\/| |
 / ___ \|  _ <| |___|  _  |___) |  __/ ___ \| |  | |
/_/   \_\_| \_\\____|_| |_|____/|_| /_/   \_\_|  |_|

"""



def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Yapımcı: Archzets"+ Style.RESET_ALL + Style.BRIGHT)
    print("Sorumluluk size aittir.")
