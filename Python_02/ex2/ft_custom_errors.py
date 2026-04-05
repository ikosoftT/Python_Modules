class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant() -> None:
    raise PlantError("The tomato plant is wilting!\n")


def test_water() -> None:
    raise WaterError("Not enough water in the tank!\n")


if __name__ == "__main__":
    print("== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        test_plant()
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("Testing WaterError...")
    try:
        test_water()
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("Testing catching all garden errors...")
    try:
        test_plant()
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}", end='')
    try:
        test_water()
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("All custom error types work correctly!")
