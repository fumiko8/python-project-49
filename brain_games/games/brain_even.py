"""Brain Even game."""

import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    """Generate random number and return it with correct answer."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer