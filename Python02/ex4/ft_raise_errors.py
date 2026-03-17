def check_plant_health(plant_name: str,
                       water_level: int, sunlight_hours: int) -> str:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level > 10 or water_level < 1:
        if water_level > 10:
            raise ValueError(
                f"Error: Water level {water_level} too high(max 10)")
        else:
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)")
    elif sunlight_hours > 12 or sunlight_hours < 2:
        if sunlight_hours > 12:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
        else:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    else:
        return f"Plant '{plant_name}' is healthy!\n"


def test_plant_check() -> None:
    print("Testing good values...")
    try:
        msg: str = check_plant_health("tomato", 9, 5)
        print(msg)
    except ValueError as e:
        print(f"{e}")
    print("Testing empty plant name...")
    try:
        check_plant_health("", 9, 5)
    except ValueError as e:
        print(f"{e}")
    print("Testing bad water level...")
    try:
        check_plant_health("test", 19, 5)
    except ValueError as e:
        print(f"{e}")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("test", 10, -55)
    except ValueError as e:
        print(f"{e}")
    finally:
        print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    try:
        test_plant_check()
    except Exception as e:
        print(e)
