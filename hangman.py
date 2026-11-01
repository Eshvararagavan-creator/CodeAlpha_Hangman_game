"""A small text-based Hangman game for the CodeAlpha internship task."""

from random import choice

WORDS = ["python", "github", "program", "keyboard", "function"]
MAX_INCORRECT_GUESSES = 6


def play_game(secret_word=None, input_fn=input, output_fn=print):
    """Run one game and return True for a win, False for a loss."""
    secret_word = (secret_word or choice(WORDS)).lower()
    guessed = set()
    incorrect = 0

    output_fn("Welcome to Hangman!")
    while incorrect < MAX_INCORRECT_GUESSES:
        display = " ".join(letter if letter in guessed else "_" for letter in secret_word)
        output_fn(f"Word: {display}")
        output_fn(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect}")
        guess = input_fn("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            output_fn("Please enter exactly one letter.")
            continue
        if guess in guessed:
            output_fn("You already guessed that letter.")
            continue
        guessed.add(guess)
        if guess in secret_word:
            output_fn("Good guess!")
        else:
            incorrect += 1
            output_fn("That letter is not in the word.")
        if set(secret_word).issubset(guessed):
            output_fn(f"You won! The word was '{secret_word}'.")
            return True
    output_fn(f"Game over! The word was '{secret_word}'.")
    return False


if __name__ == "__main__":
    play_game()
