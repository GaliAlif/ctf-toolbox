
import pytest

from ctf_toolbox.encoding import encode_text, decode_text


def test_base64_roundtrip():
    text = "Hello World"
    encoded = encode_text(text, "base64")
    assert decode_text(encoded, "base64") == text


def test_hex_roundtrip():
    text = "Hello World"
    encoded = encode_text(text, "hex")
    assert decode_text(encoded, "hex") == text


def test_binary_roundtrip():
    text = "Hello"
    encoded = encode_text(text, "binary")
    assert decode_text(encoded, "binary") == text


def test_unsupported_encoding():
    with pytest.raises(ValueError):
        encode_text("Hello", "unknown")
