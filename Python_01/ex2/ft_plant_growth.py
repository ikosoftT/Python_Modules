class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.Age: int = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.Age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.Age} days old")


if __name__ == "__main__":
    plant: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Fly", 35, 50)
    old_height: int = (plant.height + plant2.height)
    print("=== Day 1 ===")
    plant.get_info()
    plant2.get_info()
    for i in range(6):
        plant.grow()
        plant2.grow()
        plant.age()
        plant2.age()
    print("=== Day 7 ===")
    plant.get_info()
    plant2.get_info()
    full_height: int = (plant2.height + plant.height) - old_height
    print(f"Growth this week: +{full_height}cm")
