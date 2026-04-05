import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    if len(sys.argv) > 1:
        print(f"Programme name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        i: int = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
