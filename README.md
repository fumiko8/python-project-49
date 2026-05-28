### Hexlet tests and linter status:
[![Actions Status](https://github.com/fumiko8/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/fumiko8/python-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=fumiko8_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=fumiko8_python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=fumiko8_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fumiko8_python-project-49)

# Brain Games

## Description

A set of five math-based mini-games for the terminal:
- **brain-even** - Determine if a number is even
- **brain-calc** - Calculate the result of arithmetic expressions
- **brain-gcd** - Find the greatest common divisor of two numbers
- **brain-progression** - Find the missing number in arithmetic progression
- **brain-prime** - Determine if a number is prime

## Installation

```bash
uv tool install dist/hexlet_code-0.1.0-py3-none-any.whl
```

## Usage

After installation, run any game:

```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

## Game Rules
- You need to answer 3 questions correctly to win
- One wrong answer ends the game


## Requirements
- Python 3.10 or higher
- uv package manager

## Asciinema Demo
[![asciicast](https://asciinema.org/a/mGqj1U81ocHfuZpy.svg)](https://asciinema.org/a/mGqj1U81ocHfuZpy)

## Project Structure

```
brain_games/
├── cli.py              # User greeting
├── engine.py           # Common game engine
├── games/              # Game logic
│   ├── brain_even.py
│   ├── brain_calc.py
│   ├── brain_gcd.py
│   ├── brain_progression.py
│   └── brain_prime.py
└── scripts/            # Game launchers
    ├── brain_even.py
    ├── brain_calc.py
    ├── brain_gcd.py
    ├── brain_progression.py
    └── brain_prime.py
```

## Code Quality
Ruff - Linter for code style checking

SonarQube - Code quality inspection

GitHub Actions - Automated testing

## Run linter locally:
```bash
uv run ruff check brain_games
```

## Development
```bash
# Setup
uv sync

# Build package
uv build

# Install locally
uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl
```

Created by fumiko8