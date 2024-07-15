def hangman():
    import random

    # Function to display the current state of the word
    def display_word(word, guessed_letters):
        return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

    # Function to display the hangman
    def display_hangman(lives):
        stages = [
            """
               ------
               |    |
               |    
               |   
               |    
               |   
               -
            """,
            """
               ------
               |    |
               |    O
               |   
               |    
               |   
               -
            """,
            """
               ------
               |    |
               |    O
               |    |
               |    
               |   
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |    
               |   
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |    
               |   
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / 
               |   
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |   
               -
            """
        ]
        return stages[lives]

    # Setting up the game
    print("Welcome to Hangman Game!")
    word = input("Player 1, enter a word for Player 2 to guess: ").lower()
    guessed_letters = []
    lives = 6
    word_set = set(word)
    
    print("\n" * 50)  # Clear the screen

    # Main game loop
    while lives > 0 and set(guessed_letters) != word_set:
        print(display_hangman(lives))
        print("Word to guess:", display_word(word, guessed_letters))
        print(f"Lives left: {lives}")
        
        guess = input("Player 2, guess a letter: ").lower()
        
        if guess in word_set:
            guessed_letters.append(guess)
            word_set.remove(guess)
        else:
            lives -= 1
        
        print("\n" * 2)  # Space between rounds
    
    # Final game state
    if set(guessed_letters) == set(word):
        print("Congratulations! You guessed the word:", word)
    else:
        print(display_hangman(lives))
        print("Sorry, you've run out of lives. The word was:", word)

# Run the game
hangman()
