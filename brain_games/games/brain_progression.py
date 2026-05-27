"""Brain Progression game."""

import random


RULE = "What number is missing in the progression?"


def generate_progression():
    """Generate arithmetic progression with one missing element."""
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 10)

    # Generate full progression
    progression = [start + i * step for i in range(length)]

    # Choose random position to hide (0-indexed)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    # Replace hidden element with '..'
    progression[hidden_index] = ".."

    # Convert to string
    question = " ".join(str(x) for x in progression)

    return question, correct_answer


def get_question_and_answer():
    """Return question and correct answer for brain progression game."""
    return generate_progression()