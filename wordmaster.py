import random

def welcome():
    print("Welcome to the Prahlad's Word Guessing Game!")
    print("Try to guess the secret country one letter at a time.")

def choose_secret_word():
    """
    Choose a random country as the secret word.
    """
    countries = ["Canada", "Brazil", "Japan", "Australia", "France", "India", "Mexico", "Germany", "Italy", "Spain"]
    return random.choice(countries).upper()

def display_word(word, guessed_letters):
    """
    Display the word with correctly guessed letters revealed.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_user_guess(guessed_letters):
    """
    Get the user's guess and validate it.
    """
    while True:
        guess = input("Enter a letter: ").upper()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            return guess
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        else:
            print("Invalid input. Please enter a single letter.")

def get_hint(secret_word, guessed_letters):
    """
    Provide a hint by revealing a letter in the secret word.
    """
    unrevealed_letters = [letter for letter in secret_word if letter not in guessed_letters]
    hint_letter = random.choice(unrevealed_letters)
    return hint_letter

def calculate_score(difficulty, attempts, hints_used):
    """
    Calculate the player's score based on difficulty, attempts, and hints used.
    """
    base_score = 100
    difficulty_multiplier = {"easy": 1, "medium": 1.5, "hard": 2}
    score = base_score * difficulty_multiplier[difficulty]
    penalty_per_hint = 20

    score -= attempts * 5  # Deduct points for each attempt
    score -= hints_used * penalty_per_hint  # Deduct points for each hint used

    return max(0, round(score))  # Ensure the score is not negative

def play_game():
    """
    Main game loop.
    """
    welcome()
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    secret_word = choose_secret_word()
    guessed_letters = []
    attempts = 0
    max_attempts = 8
    hints_used = 0

    while True:
        display = display_word(secret_word, guessed_letters)
        print("\nCurrent word:", display)
        print("Guessed letters:", ", ".join(guessed_letters))

        if "_" not in display:
            score = calculate_score(difficulty, attempts, hints_used)
            print(f"Congratulations! You guessed the country '{secret_word}' correctly.")
            print(f"Your score: {score}")
            break

        if attempts == max_attempts:
            print(f"Sorry, you've run out of attempts. The correct country was '{secret_word}'.")
            break

        action = input("Enter 'G' to guess a letter, 'H' for a hint: ").upper()

        if action == 'G':
            user_guess = get_user_guess(guessed_letters)
            guessed_letters.append(user_guess)

            if user_guess not in secret_word:
                attempts += 1
                print(f"Wrong guess! You have {max_attempts - attempts} attempts remaining.")
        elif action == 'H':
            if hints_used < 3:  # Allow a maximum of 3 hints
                hint_letter = get_hint(secret_word, guessed_letters)
                print(f"Hint: The secret word contains the letter '{hint_letter}'.")
                hints_used += 1
            else:
                print("You've already used the maximum number of hints.")
        else:
            print("Invalid action. Please enter 'G' to guess a letter or 'H' for a hint.")

def display_credits():
    print("\nDesigned by Prahlad")

play_game()
display_credits()
