# Day 5 - Password Generator

A Python password generator that creates a random password based on the number of letters, symbols, and numbers requested by the user.

## What I Learned

- `for` loops
- `range()`
- Python lists
- `append()`
- `random.choice()`
- `random.shuffle()`
- String `.join()`
- Combining lists
- Generating random data

## How It Works

The user chooses how many:

- Letters
- Symbols
- Numbers

they want in their password.

The program randomly selects the requested characters, combines them into a list, shuffles their order, and then generates the final password.

## Concepts Practiced

```python
for letter in range(input_letters):
    letter_list.append(random.choice(letters))

random.shuffle(generated_password)