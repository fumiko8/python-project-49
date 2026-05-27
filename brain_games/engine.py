"""Game engine."""

from brain_games.cli import welcome_user


def run_game(game):
    """Run generic game logic."""
    name = welcome_user()
    print(game.RULE)

    rounds_to_win = 3
    for _ in range(rounds_to_win):
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;( Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")