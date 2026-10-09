
from collections import Counter
import string


def analyze_text(text: str) -> dict:
    """Return basic statistics about a text."""
    letters = [
        char.upper()
        for char in text
        if char.isascii() and char.isalpha()
    ]

    frequencies = Counter(letters)

    return {
        "length": len(text),
        "letters": len(letters),
        "digits": sum(char.isdigit() for char in text),
        "spaces": sum(char.isspace() for char in text),
        "unique_letters": len(frequencies),
        "frequencies": dict(
            sorted(frequencies.items())
        ),
    }
