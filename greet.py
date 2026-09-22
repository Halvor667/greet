def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    if not name:
        name = "there"
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys

    who = sys.argv[1] if len(sys.argv) > 1 else ""
    print(greet(who))
