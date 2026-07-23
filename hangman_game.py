import random

def play_hangman():

    words = ["python", "algorithm", "developer", "software", "network"]
    secret_word = random.choice(words)
    guessed_letters = []  
    incorrect_guesses = 0
    max_incorrect = 6     
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect:

        display_word = ""
        for char in secret_word:
            if char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "
                
        print(f"\nWord: {display_word.strip()}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly!")
            break
    
        guess = input("Guess a letter: ").lower()
       
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter! Try a different one.")
            continue
       
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            incorrect_guesses += 1
            
    if incorrect_guesses == max_incorrect:
        print(f"\nGame Over! You ran out of guesses. The secret word was '{secret_word}'.")

if __name__ == "__main__":
    play_hangman()

    