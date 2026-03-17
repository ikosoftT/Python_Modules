def check_temperature(temp_str: str) -> int | None:
    if temp_str is None:
        raise TypeError("Temperature cannot be None\n")
    try:
        conv = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number\n")
    if 0 <= conv <= 40:
        return conv
    elif conv > 40:
        raise ValueError(f"Error: {conv}°C is too hot for plants (max 40°C)\n")
    elif conv < 0:
        raise ValueError(f"Error: {conv}°C is too cold for plants (min 0°C)\n")


def test_temperature_input() -> None:
    tests = ["25", "abc", "100", "-50"]
    for i in tests:
        try:
            print(f"Testing temperature: {i}")
            res = check_temperature(i)
        except (ValueError, TypeError) as e:
            print(e)
        else:
            print(f"Temperature {res}°C is perfect for plants!\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    try:
        test_temperature_input()
    except Exception as e:
        print(e)
