# Password Strength Checker

A command-line tool written in Python that checks a password against basic rules, asks the user to confirm it, and rates its strength. Built as a Stage 1 project while learning Python.

## Features

- Hides the password while typing (uses `getpass`)
- Reports every missing requirement at once, not just the first
- Asks the user to re-type the password and starts over on a mismatch
- Gives a strength rating: WEAK, MODERATE or STRONG

## Requirements

- Python 3.x
- No external libraries (only `string` and `getpass` from the standard library)

## How to run

Open a terminal, go to the project folder and run:

```
python password_check.py
```

Run it from a real terminal (such as Windows Terminal), not from IDLE. IDLE cannot hide typed input, so the password would be shown on screen.

## Example

```
Enter your password:
- Password must contain at least 8 characters
- Password must contain at least one uppercase letter
- Password must contain at least one digit
- Password must contain at least one special character
Enter your password:
Re-type your password:
Password accepted.
STRONG PASSWORD
```

## Rules a password must meet

- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

## How the strength score works

After the rules are met, the password earns points for extra length (12+ and 16+ characters) and for including digits and special characters. The total score decides the rating.

## Limitations

- It checks character types, not real-world strength. A predictable password like `Password1!` can still pass.
- It does not check against lists of common passwords.
- It does not detect repeated characters or sequences such as `aaaa` or `1234`.
- This is a learning project and should not be used to protect real accounts.

## Possible improvements

- [ ] Reject passwords from a list of common passwords
- [ ] Detect repeated and sequential characters
- [ ] Put more weight on length in the score
- [ ] Add a username check
- [ ] Add tests with pytest

## What I learned

- Writing functions that return values instead of printing
- Looping with `while True`, `break` and `continue`
- Structuring a script with `main()` and `if __name__ == "__main__":`
