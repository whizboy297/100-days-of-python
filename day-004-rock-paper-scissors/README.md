# Day 4 - Rock Paper Scissors

A simple Rock Paper Scissors game built with Python.

## What I Learned

- Python lists
- List indexing
- The `random` module
- `random.randint()`
- Using variables as list indexes
- Nested conditions
- `if`, `elif`, and `else`
- Logical operators with `and`
- Multi-line strings
- ASCII art

## How It Works

The player chooses:

- `0` for Rock
- `1` for Paper
- `2` for Scissors

The computer randomly selects a choice using Python's `random` module.

The program then compares the player's choice with the computer's choice and determines whether the result is:

- A draw
- A win
- A loss

## Concepts Practiced

```python
import random

computer_choice = random.randint(0, 2)