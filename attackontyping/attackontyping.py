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
        pass









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