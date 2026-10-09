
from ctf_toolbox.analyzer import analyze_text


def test_basic_statistics():
    result = analyze_text("Hello World 123")

    assert result["length"] == 15
    assert result["letters"] == 10
    assert result["digits"] == 3
    assert result["spaces"] == 2


def test_unique_letters():
    result = analyze_text("Hello")

    assert result["unique_letters"] == 4


def test_letter_frequencies():
    result = analyze_text("Hello")

    assert result["frequencies"]["L"] == 2
    assert result["frequencies"]["O"] == 1


def test_empty_text():
    result = analyze_text("")

    assert result["length"] == 0
    assert result["letters"] == 0
    assert result["unique_letters"] == 0
    assert result["frequencies"] == {}
