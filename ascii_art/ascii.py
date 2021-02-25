from colorama import Fore, Back, Style
import pyfiglet

def welcome_message():
    return(Fore.GREEN + """  █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗ 
 ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝ 
 ███████║   ██║      ██║   ███████║██║     █████╔╝  
 ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗  
 ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗ 
 ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝""" 
 + Fore.RED + """ 
                 ██████╗ ███╗   ██╗                
                ██╔═══██╗████╗  ██║"""+ Fore.YELLOW +"""                 
 █████╗█████╗"""+ Fore.RED +"""   ██║   ██║██╔██╗ ██║"""+ Fore.YELLOW +"""   █████╗█████╗
 ╚════╝╚════╝""" + Fore.RED + """   ██║   ██║██║╚██╗██║"""+ Fore.YELLOW +"""   ╚════╝╚════╝"""+ Fore.RED +"""
                ╚██████╔╝██║ ╚████║                
                 ╚═════╝ ╚═╝  ╚═══╝""" 
+ Fore.CYAN + """                
 ████████╗██╗   ██╗██████╗ ██╗ ███╗   ██╗ ██████╗    
 ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██║ ████╗  ██║██╔════╝    
    ██║    ╚████╔╝ ██████╔╝██║ ██╔██╗ ██║██║  ███╗   
    ██║     ╚██╔╝  ██╔═══╝ ██║ ██║╚██╗██║██║   ██║   
    ██║      ██║   ██║     ██║ ██║ ╚████║╚██████╔╝   
    ╚═╝      ╚═╝   ╚═╝     ╚═╝ ╚═╝  ╚═══╝ ╚═════╝""" + Fore.WHITE +"""
 __________________________________________________
| __  ___________  ___________     By PySnooper == |
|[_j  L_I_I_I_I_j  L_I_I_I_I_j         Ver. 1.0 == |
|________________________________ _______ ______==_|
|[__I_I_I_I_I_I_I_I_I_I_I_I_I_I_] [__I__] [_I_I_I_]|
|[___I_I_I_I_I_I_I_I_I_I_I_I_]  |    _    [_I_I_I_]|
|[__I_I_I_I_I_I_I_I_I_I_I_I_L___|  _[_]_  [_I_I_I_]|
|[_____I_I_I_I_I_I_I_I_I_I_I____] [_I_I_] [_I_I_T ||
| [__I__I_________________I__L_]  _______ [___I_I_j|
|__________________________________________________|""" + Style.RESET_ALL)

def lives():
    return "♥ "

def easy_ascii():
    return ("*************************** \n" + Fore.GREEN + pyfiglet.figlet_format("EASY") + Style.RESET_ALL + "\n***************************")


def med_ascii():
    return("*************************************\n" + Fore.YELLOW + pyfiglet.figlet_format("MEDIUM") + Style.RESET_ALL + "*************************************") 

def hard_ascii():
    return("****************************\n" + Fore.RED + pyfiglet.figlet_format("HARD") + Style.RESET_ALL + "****************************")

def ext_ascii():
    return("*********************************************************\n" + Fore.MAGENTA + pyfiglet.figlet_format("EXTREME ! !", 'slant') + Style.RESET_ALL + "*********************************************************")

def roger_ascii():
    return("*********************************************************\n" + Fore.MAGENTA + pyfiglet.figlet_format("ROGER ? !", 'slant') + Style.RESET_ALL + "*********************************************************")

def game_over_ascii():
    return(Fore.RED +"""
 ██████╗  █████╗ ███╗   ███╗███████╗  
██╔════╝ ██╔══██╗████╗ ████║██╔════╝  
██║  ███╗███████║██╔████╔██║█████╗    
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝    
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗  
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
 """+ Fore.RED +"""
     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
 """ + Style.RESET_ALL)

def dev_menu_art():
    return("************************\n" + Fore.GREEN + pyfiglet.figlet_format("Devs") + Style.RESET_ALL + "************************\n")
    

def rules_art():
    return("************************\n" + Fore.GREEN + pyfiglet.figlet_format("Rules") + Style.RESET_ALL + "************************\n")

def thanks():
    return(Fore.BLUE + """\
    ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗    
    ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝    
       ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗    
       ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║    
       ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║    
       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    
                                                           
                ███████╗ ██████╗ ██████╗                   
                ██╔════╝██╔═══██╗██╔══██╗                  
                █████╗  ██║   ██║██████╔╝                  
                ██╔══╝  ██║   ██║██╔══██╗                  
                ██║     ╚██████╔╝██║  ██║                  
                ╚═╝      ╚═════╝ ╚═╝  ╚═╝                  
                                                           
██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗ ██╗ 
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝ ██║ 
██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗██║ 
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║╚═╝ 
██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗ 
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝ 
                                                 

    """ + Style.RESET_ALL)

def you_win_ascii():
    return(Fore.YELLOW + """\
          ██╗   ██╗ ██████╗ ██╗   ██╗          
▄ ██╗▄    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ▄ ██╗▄
 ████╗     ╚████╔╝ ██║   ██║██║   ██║     ████╗
▀╚██╔▀      ╚██╔╝  ██║   ██║██║   ██║    ▀╚██╔▀
  ╚═╝        ██║   ╚██████╔╝╚██████╔╝      ╚═╝ 
             ╚═╝    ╚═════╝  ╚═════╝           
                                               
    ██╗    ██╗██╗███╗   ██╗    ██╗    ██╗    ██╗   
    ██║    ██║██║████╗  ██║    ██║    ██║    ██║   
    ██║ █╗ ██║██║██╔██╗ ██║    ██║    ██║    ██║   
    ██║███╗██║██║██║╚██╗██║    ╚═╝    ╚═╝    ╚═╝   
    ╚███╔███╔╝██║██║ ╚████║    ██╗    ██╗    ██╗   
     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝    ╚═╝    ╚═╝   
    """ + Style.RESET_ALL)  