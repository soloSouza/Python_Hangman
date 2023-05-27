import random

# variables:
page_break = """
-----------------------------------------------------------------------------------------------------------------------
"""
game_header = """ 
Welcome to:

|XX|--------------------s
|XX|                    s
|XX|                   sss 
|XX|                   sss        
|XX|                  s   s 
|XX|                 s     s   
|XX|                  s s s    
|XX|
|XX|  TTTTTTT  H     H  EEEEEEE    H     H     A     N     N   GGGGG   M     M     A     N     N
|XX|     T     H     H  E          H     H    A A    NN    N  G     G  MM   MM    A A    NN    N
|XX|     T     H     H  E          H     H   A   A   N N   N  G        M M M M   A   A   N N   N
|XX|     T     HHHHHHH  EEEEE      HHHHHHH  AAAAAAA  N  N  N  G  GGGG  M  M  M  AAAAAAA  N  N  N 
|XX|     T     H     H  E          H     H  A     A  N   N N  G  G  G  M     M  A     A  N   N N
|XX|     T     H     H  E          H     H  A     A  N    NN  G     G  M     M  A     A  N    NN
|XX|     T     H     H  EEEEEEE    H     H  A     A  N     N   GGGGG   M     M  A     A  N     N
|XX|   

\"THE HANGMAN\" is a single player terminal game.
"""
hangman_initial = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   sss
|XX|                   sss
|XX|                  s   s
|XX|                 s     s
|XX|                  s s s
|XX|                    
|XX|               
|XX|               
|XX|               
|XX|                  
|XX|                  
|XX|                  
|XX|                 
|XX|                
|XX|
|XX|
|XX|
"""
hangman_one_miss = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|
|XX|
|XX|
"""
hangman_two_misses = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|            
|XX|            
|XX|            
|XX|
|XX|
|XX|
"""
hangman_three_misses = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|
|XX|                 //|z|
|XX|                // |z|
|XX|               //  |z|
|XX|              '''  |z|
|XX|                   |z|
|XX|               
|XX|               
|XX|               
|XX|
|XX|
|XX|
"""
hangman_four_misses ="""
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|
|XX|                 //|z|
|XX|                // |z|
|XX|               //  |z|
|XX|              '''  |z|
|XX|                   |z|
|XX|                     \\\\
|XX|                      \\\\
|XX|                       \\\\
|XX|                       ''''
|XX|
|XX|
"""
hangman_five_misses = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|\\
|XX|                 //|z|\\\\
|XX|                // |z| \\\\
|XX|               //  |z|  \\\\
|XX|              '''  |z|  '''
|XX|                   |z|
|XX|                     \\\\
|XX|                      \\\\
|XX|                       \\\\
|XX|                       ''''
|XX|
|XX|
"""
hangman_six_misses = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  o o  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|\\
|XX|                 //|z|\\\\
|XX|                // |z| \\\\
|XX|               //  |z|  \\\\
|XX|              '''  |z|  '''
|XX|                   |z|
|XX|                  // \\\\
|XX|                 //   \\\\
|XX|                //     \\\\
|XX|              ''''     ''''
|XX|
|XX|
"""
hangman_seven_misses = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  x x  o
|XX|                o  ...  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|\\
|XX|                 //|z|\\\\
|XX|                // |z| \\\\
|XX|               //  |z|  \\\\
|XX|              '''  |z|  '''
|XX|                   |z|
|XX|                  // \\\\
|XX|                 //   \\\\
|XX|                //     \\\\
|XX|              ''''     ''''
|XX|
|XX|
"""
hangman_game_over = """

|XX|--------------------s        
|XX|                    s        
|XX|                   sss       
|XX|                   sss       
|XX|                  s   s      
|XX|                 s     s     
|XX|                  s s s       
|XX|          
|XX|   GGGGG      A     M     M  EEEEEEE      OOO    V     V  EEEEEEE  RRRRR      !!!  !!!  !!!                         
|XX|  G     G    A A    MM   MM  E          O     O  V     V  E        R     R    !!!  !!!  !!!                  
|XX|  G         A   A   M M M M  E          O     O  V     V  E        R     R    !!!  !!!  !!!                  
|XX|  G  GGGG  AAAAAAA  M  M  M  EEEEE      O     O  V     V  EEEEE    RRRRR      !!!  !!!  !!!                      
|XX|  G  G  G  A     A  M     M  E          O     O   V   V   E        R   R      !!!  !!!  !!!                  
|XX|  G     G  A     A  M     M  E          O     O    V V    E        R    R                        
|XX|   GGGGG   A     A  M     M  EEEEEEE      OOO       V     EEEEEEE  R     R    !!!  !!!  !!!                        
|XX|   

"""
hangman_you_win = """

|XX|--------------------s
|XX|                    s
|XX|                   sss 
|XX|                   sss        
|XX|                  s   s 
|XX|                 s     s   
|XX|                  s s s    
|XX|          
|XX|  Y     Y    OOO    U     U    W     W  IIIIIII  N     N    !!!  !!!  !!!
|XX|   Y   Y   O     O  U     U    W     W     I     NN    N    !!!  !!!  !!!
|XX|    Y Y    O     O  U     U    W     W     I     N N   N    !!!  !!!  !!!
|XX|     Y     0     O  U     U    W  W  W     I     N  N  N    !!!  !!!  !!!
|XX|     Y     O     O  U     U    W W W W     I     N   N N    !!!  !!!  !!!
|XX|     Y     O     O  U     U    WW   WW     I     N    NN  
|XX|     Y       OOO      UUU      W     W  IIIIIII  N     N    !!!  !!!  !!!
|XX|

"""
word_list = []
word_as_list = []
guesses_as_list = []
guesses_as_string = ""
misses_counter = 0
possible_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
past_guesses = []
guess_counter = 0
game_word = ""
games = 0
wins = 0
looses = 0

# Import word list from wordList.txt and store as word_list in the program:
with open("wordList.txt") as wordList_txt:
    for word in wordList_txt:
        word_list.append(word.upper().rstrip())

class Game:
    def __init__(self, word_list, word_as_list, guesses_as_list, guesses_as_string, misses_counter, possible_letters, past_guesses, guess_counter, game_word, games, wins, looses, page_break, game_header, hangman_initial, hangman_one_miss, hangman_two_misses, hangman_three_misses, hangman_four_misses, hangman_five_misses, hangman_six_misses, hangman_seven_misses, hangman_game_over, hangman_you_win):
        self.word_list = word_list
        self.word_as_list = word_as_list
        self.guesses_as_list = guesses_as_list
        self.guesses_as_string = guesses_as_string
        self.misses_counter = misses_counter
        self.possible_letters = possible_letters
        self.past_guesses = past_guesses
        self.guess_counter = guess_counter
        self.game_word = game_word
        self.games = games
        self.wins = wins
        self.looses = looses
        self.page_break = page_break
        self.game_header = game_header
        self.hangman_initial = hangman_initial
        self.hangman_ones_miss = hangman_one_miss
        self.hangman_two_misses = hangman_two_misses
        self.hangman_three_misses = hangman_three_misses
        self.hangman_four_misses = hangman_four_misses
        self.hangman_five_misses = hangman_five_misses
        self.hangman_six_misses = hangman_six_misses
        self.hangman_seven_misses = hangman_seven_misses
        self.hangman_game_over = hangman_game_over
        self.hangman_you_win = hangman_you_win
    
    def update_guess_as_string(self):
        self.guesses_as_string = ""
        for i in range(len(self.word_as_list)):
            if self.guesses_as_list[i] == self.word_as_list[i]:
                self.guesses_as_string += " {value}".format(value = self.guesses_as_list[i])
            else:
                self.guesses_as_string += " _"
        return self.guesses_as_string
    
    def insert_visual_aid(self):
        if self.misses_counter == 0:
            print(self.hangman_initial)
        elif self.misses_counter == 1:
            print(self.hangman_ones_miss)
        elif self.misses_counter == 2:
            print(self.hangman_two_misses)
        elif self.misses_counter == 3:
            print(self.hangman_three_misses)
        elif self.misses_counter == 4:
            print(self.hangman_four_misses)
        elif self.misses_counter == 5:
            print(self.hangman_five_misses)
        elif self.misses_counter == 6:
            print(self.hangman_six_misses)
        elif self.misses_counter == 7:
            print(self.hangman_seven_misses)
        else:
            print("This is an error message")        
    
    def play_game(self):
        while self.word_as_list != self.guesses_as_list and self.misses_counter <= 7:
            if self.guess_counter == 0:
                print(page_break)
                player_guess = input("What is your first guess: ")
            else:
                print(page_break)
                player_guess = input("What is your next guess: ")
            if player_guess.upper() == "EXIT":
                print(page_break)
                print("\nI'm sad to see you leave! Come back at any time.\n")
                quit()
            else:
                if player_guess.upper() in self.possible_letters:
                    if player_guess.upper() not in self.past_guesses:
                        if player_guess.upper() not in self.word_as_list:
                            self.misses_counter += 1
                            self.guess_counter += 1
                            if self.misses_counter == 8:
                                word = ""
                                for i in range(len(self.word_as_list)):
                                    word += self.word_as_list[i]
                                print(page_break)
                                print("Sorry, but my word was {word} and {letter} is not part of it: {string}".format(word = word, letter = player_guess.upper(), string = self.update_guess_as_string()))
                                print(self.hangman_game_over)
                                self.looses += 1
                                break
                            else: 
                                self.past_guesses.append(player_guess.upper())
                                print(page_break)
                                print("Game #{x}".format(x = self.games))
                                print("Games won: {x}".format(x = self.wins))
                                print("Games lost: {x}".format(x = self.looses))
                                self.insert_visual_aid()
                                print("Sorry, but {letter} is not in my word: {string}\n".format(letter = player_guess.upper(), string = self.update_guess_as_string()))
                                self.past_guesses_string = ""
                                for i in self.past_guesses:
                                    self.past_guesses_string += i + " "
                                if self.guess_counter > 1:
                                    print("You have made {number} guesses so far: {letters}".format(number = self.guess_counter, letters = self.past_guesses_string))
                                    print("Wrong guesses: {x}".format(x = self.misses_counter))
                                    print("Correct guesses: {x}".format(x = (self.guess_counter-self.misses_counter)))
                                else:
                                    print("You have made {number} guess so far: {letters}".format(number = self.guess_counter, letters = self.past_guesses_string))
                                    print("Wrong guesses: {x}".format(x = self.misses_counter))
                                    print("Correct guesses: {x}".format(x = (self.guess_counter-self.misses_counter)))
                        if player_guess.upper() in self.word_as_list:
                            self.guess_counter += 1
                            self.past_guesses.append(player_guess.upper())
                            for i in range(len(self.word_as_list)):
                                if self.word_as_list[i] == player_guess.upper():
                                    self.guesses_as_list[i] = player_guess.upper()
                            if self.guesses_as_list == self.word_as_list:
                                word = ""
                                for i in range(len(self.word_as_list)):
                                    word += self.word_as_list[i]
                                print(page_break)
                                print("Good job! My word was {word} and it does contain the letter {letter}: {string}".format(word = word, letter = player_guess.upper(), string = self.update_guess_as_string()))
                                print(self.hangman_you_win)
                                self.wins += 1
                                break
                            else:
                                print(page_break) 
                                print("Game #{x}".format(x = self.games))
                                print("Games won: {x}".format(x = self.wins))
                                print("Games lost: {x}".format(x = self.looses))
                                self.insert_visual_aid()
                                print("Good job! My word does contain the letter {letter}: {string}\n".format(letter = player_guess.upper(), string = self.update_guess_as_string()))
                                self.past_guesses_string = ""
                                for i in self.past_guesses:
                                    self.past_guesses_string += i + " "
                                if self.guess_counter > 1:
                                    print("You have made {number} guesses so far: {letters}".format(number = self.guess_counter, letters = self.past_guesses_string))
                                    print("Wrong guesses: {x}".format(x = self.misses_counter))
                                    print("Correct guesses: {x}".format(x = (self.guess_counter-self.misses_counter)))
                                else:
                                    print("You have made {number} guess so far: {letters}".format(number = self.guess_counter, letters = self.past_guesses_string))
                                    print("Wrong guesses: {x}".format(x = self.misses_counter))
                                    print("Correct guesses: {x}".format(x = (self.guess_counter-self.misses_counter)))
                    elif player_guess.upper() in self.past_guesses:
                        print(page_break)
                        print("Oops, it seems like you already guessed {letter} before, please try again: ".format(letter = player_guess.upper()))
                        continue
                else:
                    print(page_break)
                    print("Oops, it seems like you did not enter a valid letter as your guess, please try again: ")
                    continue

    def start_new_game(self):
        player_input = input("Would you like to start a new game? (Y/N): ")
        if player_input.upper() == "Y" or player_input.upper() == "N":
            if player_input.upper() == "Y":
                self.games += 1
                self.word_as_list = []
                self.guesses_as_list = []
                self.guesses_as_string = ""
                self.misses_counter = 0
                self.past_guesses = []
                self.guess_counter = 0
                word_index = random.randint(1,len(self.word_list))
                self.game_word = self.word_list[word_index]
                self.word_list.remove(self.game_word)
                for letter in self.game_word:
                    self.word_as_list.append(letter)
                for letter in self.game_word:
                    self.guesses_as_list.append(" ")
                print(page_break)
                print("Great, let's play:\n")
                print("You can type \"EXIT\" at any time to quit the game.\n")
                print("Game #{x}".format(x = self.games))
                print("Games won: {x}".format(x = self.wins))
                print("Games lost: {x}".format(x = self.looses))
                print(self.hangman_initial)
                print("I've selected a word of {letter_count} letters for you to try and guess before being hanged: {string}".format(letter_count = len(self.game_word), string = self.update_guess_as_string()))
                self.play_game()
                self.start_new_game()
            else:
                print(page_break)
                print("I'm sad to see you leave! Come back at any time.\n")
                quit()    
        else:
            print(page_break)
            print("Oops, it seems like you did not provide a valid answer, please try again:")
            self.start_new_game()        

    def __repr__(self):
        return """ 
Welcome to:

|XX|--------------------s
|XX|                    s
|XX|                   sss 
|XX|                   sss        
|XX|                  s   s 
|XX|                 s     s   
|XX|                  s s s    
|XX|
|XX|  TTTTTTT  H     H  EEEEEEE    H     H     A     N     N   GGGGG   M     M     A     N     N
|XX|     T     H     H  E          H     H    A A    NN    N  G     G  MM   MM    A A    NN    N
|XX|     T     H     H  E          H     H   A   A   N N   N  G        M M M M   A   A   N N   N
|XX|     T     HHHHHHH  EEEEE      HHHHHHH  AAAAAAA  N  N  N  G  GGGG  M  M  M  AAAAAAA  N  N  N 
|XX|     T     H     H  E          H     H  A     A  N   N N  G  G  G  M     M  A     A  N   N N
|XX|     T     H     H  E          H     H  A     A  N    NN  G     G  M     M  A     A  N    NN
|XX|     T     H     H  EEEEEEE    H     H  A     A  N     N   GGGGG   M     M  A     A  N     N
|XX|   

\"THE HANGMAN\" is a single player terminal game.
"""


hangman_game = Game(word_list, word_as_list, guesses_as_list, guesses_as_string, misses_counter, possible_letters, past_guesses, guess_counter, game_word, games, wins, looses, page_break, game_header, hangman_initial, hangman_one_miss, hangman_two_misses, hangman_three_misses, hangman_four_misses, hangman_five_misses, hangman_six_misses, hangman_seven_misses, hangman_game_over, hangman_you_win)

print(hangman_game)
hangman_game.start_new_game()
