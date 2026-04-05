import sys
import site
import os


def main() -> None:
    curr = sys.executable
    path = sys.prefix

    print("\nMATRIX STATUS: ", end='')

    if sys.prefix != sys.base_prefix:

        print("Welcome to the construct\n")

        print(f"Current Python: {curr}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {path}")

        print("\nSUCCESS: You're in an isolated environment!\n",
              "Safe to install packages without affecting",
              "the global system.")

        print("\nPackage installation path:")
        print(path + site.getsitepackages(path)[0])
    else:
        print("You're still plugged in\n")

        print(f"Current Python: {curr}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!\n",
              "The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")

        print("\nThen run this program again.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
