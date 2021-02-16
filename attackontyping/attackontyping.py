



class Game:
    def __init__(self):
        self.lives = 3
        self.points = 0
        self.difficulty = 'easy'

    def menu_selection(self):
        # Print Welcome ASCII

        user_input = None

        while user_input not in ('r', 'p', 'd', 'e'):
            print('Would you like to (p)lay the game, read the (r)ules, learn about the (d)evs, or (e)xit?')
            
            user_input = input('> ').lower()
            
            if user_input == 'r':
                print('Selected rules')
            if user_input == 'p':
                print('Selected play')
            if user_input == 'd':
                print('Selected devs')
            if user_input == 'e':
                print('Thanks for playing!')
                exit()


    def rules(self):
        pass










    def about_us(self):
        print("[1] Anthony Beaver")
        print("[2] Nick Dorkins")
        print("[3] Logan Jones")
        print("[4] Nebiuy Kifle")
        print("[0] Go to game page")

    about_us(self= None)
    option = int(input("inter index number: "))

    green = '\033[32;1;40m'
    print(green + 'about us')

    while option != 0:
        # green = '\033[32;1;40m'
        # print(green + 'about us')
        if option == 1:
            print("""
            ##################################################################################################################################################################################
                       Anthony Beaver:

            My about me: "Anthony Beaver is a full stack software developer from Seattle Washington.Passionate about problem solving and playing the drums! Looking to change the world one syntax error at a time..

            ##################################################################################################################################################################################
            """) 
        elif option == 2:
            print("""
            ##################################################################################################################################################################################
                       Nick Dorkins:

            Software Developer with a background in Specialized Industrial Safety, and fabrication. Enjoy's traveling and spending time with family and puppies. Favorite things to do outside quarantine are going to Disney parks and playing Magic the Gathering.

            ##################################################################################################################################################################################
            """)
        elif option == 3:
            print("""
            ##################################################################################################################################################################################
                       Logan Jones:

            Logan Jones is a former product manager and current software engineer. She is a skilled problem solver who loves cats, taco bell, and world of warcraft..

            ##################################################################################################################################################################################

            """)
        elif option == 4:
            print("""
            ##################################################################################################################################################################################
                       Nebiuy Kifle:

            Hello My name is Nebiyu kifle. I am a professional and highly motivated software engineer.I have a background on marketing and logistics management for about 6 years back home in Ethiopia. I used to also have my own business.  I have worked on multiple projects and have a broad experience in software development at code fellows. I am passionate about to learn new think in techs industry. I would love the opportunity to put my experience at tech company. I am currently looking for a new role that will utilize my skills and experience and take my career to the next level.

            ##################################################################################################################################################################################
            """)
        else:
            print("lets go to next step")
        print()
        about_us(self=None)
        option = int(input("inter index number you choice: "))



    def play_game(self):
        # easy - extreme rounds in here   
        pass








    def start_easy_round(self):
        pass







    def start_med_round(self):
        pass








    def start_hard_round(self):
        pass









    def start_extreme_round(self):
        pass
































if __name__ == '__main__':
    game = Game()
    game.menu_selection()
    # game.about_us()
    game.about_us()
    

