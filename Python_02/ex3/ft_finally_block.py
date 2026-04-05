def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for p in plant_list:
            if p is None:
                raise ValueError("Error: Cannot water None - invalid plant!")
            print(f"Watering {p}")
    except ValueError as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    normal_list: list[str] = ["tomato", "lettuce", "carrots"]
    err_list: list[str] = ["tomato", None, "carrots"]
    print("Testing normal watering...")
    water_plants(normal_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(err_list)


if __name__ == "__main__":
    print("=== Garden Watering System ==\n")
    try:
        test_watering_system()
    except Exception as e:
        print(e)
    print("\nCleanup always happens, even with errors!")
