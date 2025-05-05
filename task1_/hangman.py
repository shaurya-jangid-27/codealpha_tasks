import random

def display_instructions():
    print("\nWelcome to Hangman!")
    print("---------------------------")
    print("Instructions:")
    print("1. A random word will be selected by the computer.")
    print("2. You need to guess one letter at a time.")
    print("3. You have 6 chances. Each wrong guess adds one part to the hangman.")
    print("4. If the full hangman appears, you lose.")
    print("5. If you guess the word before that, you win!")
    print("---------------------------\n")

def choose_word():
    words = ['python', 'developer', 'keyboard', 'internet', 'function', 'variable']
    return random.choice(words)

def display_hangman(wrong_guesses):
    stages = [
        """
           ------
           |    |
                |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        ---------
        [FULL HANGMAN]
        """
    ]
    print(stages[wrong_guesses])

def play_game():
    word = choose_word()
    guessed_letters = set()
    correct_letters = set(word)
    display_word = ['_' for _ in word]
    wrong_guesses = 0
    game_result = None

    while wrong_guesses < 6 and '_' in display_word:
        print("\nWord:", ' '.join(display_word))
        print("Guessed Letters:", ' '.join(sorted(guessed_letters)))
        print(f"Wrong guesses left: {6 - wrong_guesses}")
        display_hangman(wrong_guesses)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter only.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print(" Wrong guess!")

    if '_' not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        print("You saved the hangman!")
        game_result = 'win'
    else:
        display_hangman(6)
        print("\n Hangman died... You lose!")
        print("The word was:", word)
        print("Better luck next time!")
        game_result = 'lose'

    return game_result

def main():
    last_result = None
    while True:
        print("\nDo you want to play Hangman? (yes/no)")
        choice = input("> ").lower()
        if choice == 'yes':
            display_instructions()
            last_result = play_game()
        elif choice == 'no':
            if last_result == 'lose':
                print("Take a break champ! You'll do better next time. Keep practicing! 🔁")
            else:
                print("Goodbye! Thanks for playing. ")
            break
        else:
            print("Please enter a valid input: 'yes' or 'no'.")

if __name__ == "__main__":
    main()
