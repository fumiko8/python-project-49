#!/usr/bin/env python3
"""Brain GCD launcher."""

from brain_games.engine import run_game
from brain_games.games import brain_gcd


def main():
    """Run brain gcd game."""
    run_game(brain_gcd)


if __name__ == "__main__":
    main()