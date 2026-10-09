
from ctf_toolbox.caesar import encrypt, decrypt, brute_force


def test_encrypt():
    assert encrypt("Hello", 3) == "Khoor"


def test_decrypt():
    assert decrypt("Khoor", 3) == "Hello"


def test_wraparound():
    assert encrypt("XYZ", 3) == "ABC"


def test_preserve_spaces_and_punctuation():
    assert encrypt("Hello, World!", 3) == "Khoor, Zruog!"


def test_brute_force_finds_original():
    candidates = brute_force("Khoor")
    assert (3, "Hello") in candidates
    assert len(candidates) == 26
