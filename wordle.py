import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

def generate_secret_word(word_list):
    return random.choice(word_list)

def get_feedback(secret_word, guessed_word):
    feedback = ''
    for i in range(len(secret_word)):
        if guessed_word[i] == secret_word[i]:
            feedback += Fore.GREEN + guessed_word[i]

        elif guessed_word[i] in secret_word:
            feedback += Fore.YELLOW + guessed_word[i]
        
        else:
            feedback += Fore.RED + guessed_word[i]

    return feedback

def play_wordle():
    word_list = ['bed', 'desk', 'matress', 'television', 'book', 'mango', 'grape', 'banana', 'table', 'comedy', 'happy', 'stairs']
    secret_word = generate_secret_word(word_list)
    attempts = 7
    guessed_word = ['_' for i in secret_word]

    print(f"Welcome to Wordle!")
    print(f"You have {attempts} attempts to guess the word.")

    while attempts > 0:
        print(' '.join(guessed_word))
        guess = input("Guess a word: ").lower()
        if guess == secret_word:
            print(Fore.GREEN + f"Congratulations! You've guessed the word correctly.")
            break
        
        if len(guess) != len(secret_word):
            print(Fore.RED + f"Invalid input. The word length is {len(guessed_word)}.")
            if attempts == 1:
                print(f'You have {attempts-1} attempts left left')
                print(Fore.RED + f"Sorry, you've run out of attempts. The secret word was '{secret_word}'.")
                break
            print(f'You have {attempts-1} attempts left left')
            attempts -= 1
            continue

        feedback = get_feedback(secret_word, guess)
        print(feedback)
        print(f'You have {attempts-1} attempts left left')
        attempts -= 1
        if attempts == 0:
            print(Fore.RED + f"Sorry, you've run out of attempts. The secret word was '{secret_word}'.")

if __name__ == "__main__":
    play_wordle()
