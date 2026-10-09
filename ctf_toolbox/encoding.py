
import base64


def encode_text(text: str, method: str) -> str:
    """Encode text using a supported encoding method."""
    if method == "base64":
        return base64.b64encode(text.encode("utf-8")).decode("ascii")

    if method == "hex":
        return text.encode("utf-8").hex()

    if method == "binary":
        return " ".join(format(byte, "08b") for byte in text.encode("utf-8"))

    raise ValueError(f"Unsupported encoding method: {method}")


def decode_text(encoded: str, method: str) -> str:
    """Decode text using a supported encoding method."""
    if method == "base64":
        raw = base64.b64decode(encoded, validate=True)
        return raw.decode("utf-8")

    if method == "hex":
        return bytes.fromhex(encoded).decode("utf-8")

    if method == "binary":
        bits = encoded.split()

        if not bits:
            return ""

        if any(len(bit) != 8 or set(bit) - {"0", "1"} for bit in bits):
            raise ValueError("Binary input must contain 8-bit groups.")

        raw = bytes(int(bit, 2) for bit in bits)
        return raw.decode("utf-8")

    raise ValueError(f"Unsupported encoding method: {method}")
