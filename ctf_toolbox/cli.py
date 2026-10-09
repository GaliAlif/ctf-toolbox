
import argparse

from ctf_toolbox.encoding import encode_text, decode_text
from ctf_toolbox.caesar import encrypt, decrypt, brute_force
from ctf_toolbox.analyzer import analyze_text


def main():
    parser = argparse.ArgumentParser(
        prog="ctf-toolbox",
        description="A lightweight educational CTF toolkit."
    )
    commands = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Encoding
    for name in ("encode", "decode"):
        sub = commands.add_parser(name)
        sub.add_argument(
            "method",
            choices=["base64", "hex", "binary"]
        )
        sub.add_argument("text")

    # Caesar cipher
    caesar = commands.add_parser("caesar")
    actions = caesar.add_subparsers(
        dest="action",
        required=True
    )

    for name in ("encrypt", "decrypt"):
        sub = actions.add_parser(name)
        sub.add_argument("text")
        sub.add_argument("shift", type=int)

    crack = actions.add_parser("crack")
    crack.add_argument("text")

    # Text analyzer
    analyze = commands.add_parser(
        "analyze",
        help="Analyze text statistics and letter frequencies"
    )
    analyze.add_argument("text")

    args = parser.parse_args()

    try:
        if args.command == "encode":
            print(encode_text(args.text, args.method))

        elif args.command == "decode":
            print(decode_text(args.text, args.method))

        elif args.command == "caesar":
            if args.action == "encrypt":
                print(encrypt(args.text, args.shift))
            elif args.action == "decrypt":
                print(decrypt(args.text, args.shift))
            else:
                for shift, candidate in brute_force(args.text):
                    print(f"Shift {shift:2}: {candidate}")

        elif args.command == "analyze":
            result = analyze_text(args.text)
            print(f"Length: {result['length']}")
            print(f"Letters: {result['letters']}")
            print(f"Digits: {result['digits']}")
            print(f"Spaces: {result['spaces']}")
            print(f"Unique letters: {result['unique_letters']}")
            print("Letter frequencies:")

            for letter, count in result["frequencies"].items():
                print(f"  {letter}: {count}")

    except (ValueError, UnicodeDecodeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
