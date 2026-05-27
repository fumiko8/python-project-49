#!/usr/bin/env python3
"""Brain Progression launcher."""

from brain_games.engine import run_game
from brain_games.games import brain_progression


def main():
    """Run brain progression game."""
    run_game(brain_progression)


if __name__ == "__main__":
    main()