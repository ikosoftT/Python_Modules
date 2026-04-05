def garden_operations(err: str) -> None:
    if err == "ValueError":
        int('abc')
    elif err == "ZeroDivisionError":
        10 / 0
    elif err == "FileNotFoundError":
        open('hamid.html', 'r')
    elif err == "KeyError":
        books: dict = {"book1": 10}
        print(books['book100'])
    else:
        return None


def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")
    print("Testing FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")
    print("Testing KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")
    print("Testing multiple errors together...")
    try:
        garden_operations("KeyError")
        garden_operations("ValueError")
    except (ValueError, KeyError):
        print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    try:
        test_error_types()
    except Exception as e:
        print(e)
    print("All error types tested successfully!")
