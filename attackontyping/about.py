from colorama import Fore, Back, Style 
import pyfiglet

def logan():
    print('\n\n')
    print("****************************")
    print(Fore.GREEN)
    print(pyfiglet.figlet_format("Logan", 'banner'))
    print(Style.RESET_ALL)
    print("****************************")
    print()
    print("Other stuff about me whatever\nOther stuff about me whatever\nOther stuff about me whatever")

logan()