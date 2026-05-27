"""Brain Prime game."""

import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Check if number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    """Generate random number and return it with correct answer."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer