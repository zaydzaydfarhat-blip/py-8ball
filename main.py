#!/usr/bin/env python3
"""A tiny terminal Magic 8-Ball game. No third-party packages needed."""

import random

ANSWERS = [
    "Yes, definitely.",
    "It is certain.",
    "Without a doubt.",
    "You can count on it.",
    "Most likely.",
    "The signs point to yes.",
    "Absolutely!",
    "Yes.",
    "Looks good to me.",
    "Ask again later.",
    "Maybe. Time will tell.",
    "I'm not sure yet.",
    "Better not tell you now.",
    "Hard to say right now.",
    "Try asking again.",
    "No.",
    "Probably not.",
    "My answer is no.",
    "Don't count on it.",
    "Very unlikely.",
]


def show_banner():
    print()
    print("  +-------------------+")
    print("  |                   |")
    print("  |        8          |")
    print("  |     MAGIC         |")
    print("  |      BALL         |")
    print("  |                   |")
    print("  +-------------------+")
    print("       PY-8BALL")
    print()


def main():
    show_banner()
    print("Ask a question and let the 8-Ball decide!")
    print("Type q, quit, or exit to stop.\n")

    while True:
        try:
            question = input("Your question > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye! Thanks for playing.")
            break

        if question.lower() in {"q", "quit", "exit"}:
            print("Bye! Thanks for playing.")
            break

        if not question:
            print("Type a question first!\n")
            continue

        answer = random.choice(ANSWERS)
        print("\n  🎱 The 8-Ball says:")
        print(f"  {answer}\n")


if __name__ == "__main__":
    main()
