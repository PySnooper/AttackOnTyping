from colorama import Fore, Back, Style 
import pyfiglet

LOGAN_TEXT = """\
Logan Jones is a former product manager and current
software engineer. She is a skilled problem solver
who loves cats, taco bell, and world of warcraft.
"""

NEIBYU_TEXT = """\
Hello My name is Nebiyu Kifle. I am a professional
and highly motivated software engineer. I have a
background in marketing and logistics management
for about 6 years back home in Ethiopia. I used to
also have my own business. I have worked on multiple
projects and have a broad experience in software
development at Code Fellows. I am passionate to
learn new things in the tech industry. I would love
the opportunity to put my experience at tech company
I am currently looking for a new role that will 
utilize my skills and experience and take my career
to the next level.
"""

ANTHONY_TEXT = """\
Anthony Beaver is a full stack software developer
from Seattle Washington. Passionate about problem
solving and playing the drums! Looking to change
the world one syntax error at a time.
"""

NICK_TEXT = """\
Nick Dorkins is a Software Developer with a background in Specialized
Industrial Safety, and fabrication. Enjoys traveling
and spending time with family and puppies. Favorite
things to do outside quarantine are going to Disney
parks and playing Magic the Gathering.
"""


def logan():
    print("*******************************")
    print(Fore.GREEN + pyfiglet.figlet_format("Logan") + Style.RESET_ALL)
    print("*******************************")
    print('\n' + LOGAN_TEXT)


def nebiyu():
    print("*********************************")
    print(Fore.RED + pyfiglet.figlet_format("Nebiyu") + Style.RESET_ALL)
    print("*********************************")
    print('\n' + NEIBYU_TEXT)

def anthony():
    print("********************************************")
    print(Fore.CYAN + pyfiglet.figlet_format("Anthony") + Style.RESET_ALL)
    print("********************************************")
    print('\n' + ANTHONY_TEXT)

def nick():
    print("*******************************")
    print(Fore.MAGENTA + pyfiglet.figlet_format("Nick") + Style.RESET_ALL)
    print("*******************************")
    print('\n' + NICK_TEXT)