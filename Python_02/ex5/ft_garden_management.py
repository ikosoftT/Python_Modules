class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water() -> None:
    raise WaterError("Not enough water in the tank!")


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        if not plant_name:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        self.plants += [plant_name]
        print(f"Added {plant_name} successfully")

    def water_plant(self) -> None:
        print("Opening watering system...")
        try:
            if not self.plants:
                raise WaterError("Error: No Plant to Water!")
            for p in self.plants:
                if not p:
                    raise WaterError(
                        "Cannot water invalid plant!")
                print(f"Watering {p} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self, plant_name: str, w_lev: int, sun: int) -> str:
        if not plant_name:
            raise ValueError("Error: Plant name cannot be empty!")
        if plant_name not in self.plants:
            raise PlantError(f"Error: {plant_name} is not in the garden!")
        if w_lev > 10 or w_lev < 1:
            if w_lev > 10:
                raise ValueError(
                    f"Water level {w_lev} too high(max 10)")
            else:
                raise ValueError(
                    f"Water level {w_lev} is too low (min 1)")
        elif sun > 12 or sun < 2:
            if sun > 12:
                raise ValueError(
                    f"Sunlight hours {sun} is too high (max 12)")
            else:
                raise ValueError(
                    f"Sunlight hours {sun} is too low (min 2)")
        else:
            return f"{plant_name}: healthy (water: {w_lev}, sun: {sun})"


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    garden: GardenManager = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant(None)
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print(f"{e}\n")
    print("Watering plants...")
    try:
        garden.water_plant()
    except WaterError as e:
        print(f"{e}\n")

    print("Checking plant health...")
    try:
        print(garden.check_plant_health("tomato", 5, 8))
        garden.check_plant_health("lettuce", 15, 8)
    except (ValueError, PlantError) as e:
        print(f"Error checking lettuce: {e}\n")
    print("Testing error recovery...")
    try:
        test_water()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    try:
        test_garden_management()
    except Exception as e:
        print(e)
