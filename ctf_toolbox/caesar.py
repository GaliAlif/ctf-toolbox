
def encrypt(text: str, shift: int) -> str:
    """Encrypt text using the Caesar cipher."""
    result = []

    for char in text:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)

    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text using the Caesar cipher."""
    return encrypt(text, -shift)


def brute_force(text: str) -> list[tuple[int, str]]:
    """Return all 26 possible Caesar cipher shifts."""
    return [
        (shift, decrypt(text, shift))
        for shift in range(26)
    ]
