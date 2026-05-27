"""Brain Calc game."""

import random


RULE = "What is the result of the expression?"


def get_question_and_answer():
    """Generate random math expression and return it with correct answer."""
    operations = [
        ("+", lambda x, y: x + y),
        ("-", lambda x, y: x - y),
        ("*", lambda x, y: x * y),
    ]

    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation_symbol, operation_func = random.choice(operations)

    question = f"{num1} {operation_symbol} {num2}"
    correct_answer = str(operation_func(num1, num2))

    return question, correct_answer