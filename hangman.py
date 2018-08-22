"""
Hangman CLI game written in Python 3
"""

WORD_TO_GUESS = 'mountain'
correct_guesses = []
has_guessed_word = False
attempts = 9


def get_user_input():
    users_guess = input('Type a letter or try to guess the secret word: ')
    return users_guess.lstrip().lower()


def get_displayed_text():
    """
    Creates a string replacing all letters with underscores except letters
    that have been guessed correctly. This is used to indicated the users
    progress.
    """
    return ''.join([l if l in correct_guesses else '_' for l in WORD_TO_GUESS])


if __name__ == '__main__':

    # initialize text to be shown
    displayed_text = ' '.join(l for l in get_displayed_text())
    # print game welcome message
    print('\nWelcome to another game of hangman!\n')

    # main game logic
    while True:
        if has_guessed_word:
            msg = '\nWell done! you have guessed the word {} correctly :)\n'.format(WORD_TO_GUESS)
            print(msg)
            break
        else:
            msg = '\n\nWord to guess: {}'.format(' '.join([l for l in displayed_text]))
            print(msg)
            print('Lives left: {}\n'.format(attempts))
            users_guess = get_user_input()

            if users_guess == WORD_TO_GUESS:
                has_guessed_word = True
            elif users_guess in WORD_TO_GUESS and len(users_guess) == 1:
                correct_guesses.append(users_guess)
                displayed_text = get_displayed_text()
                users_guess = None
                if displayed_text == WORD_TO_GUESS:
                    has_guessed_word = True
            else:
                attempts -= 1
                if attempts < 1:
                    print('\nNo more lives left :( Better luck next time.\n')
                    break
