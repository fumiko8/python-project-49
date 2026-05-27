#!/usr/bin/env python3
"""Brain Even game."""

from brain_games.cli import welcome_user


def is_even(number: int) -> bool:
    """Check if number is even."""
    return number % 2 == 0


def main():
    """Run brain even game."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        import random
        number = random.randint(1, 100)

        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        is_correct = (is_even(number) and user_answer == "yes") or \
                     (not is_even(number) and user_answer == "no")

        if is_correct:
            print("Correct!")
            correct_answers += 1
        else:
            correct_answer = "yes" if is_even(number) else "no"
            print(f"'{user_answer}' is wrong answer ;( Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()