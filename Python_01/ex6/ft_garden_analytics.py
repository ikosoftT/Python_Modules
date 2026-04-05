class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> int:
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1

    def get_description(self) -> str:
        return f"- {self.name}: {self.height}cm"

    def get_type(self) -> str:
        return "regular"

    def get_score(self) -> int:
        return self.height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.blooming: bool = True

    def get_description(self) -> str:
        return (f"- {self.name}: {self.height}cm,{self.color} flowers "
                f"(blooming)")

    def get_type(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points: int = prize_points

    def get_description(self) -> str:
        return (f"- {self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.prize_points}")

    def get_type(self) -> str:
        return "prize"

    def get_score(self) -> int:
        return self.height + self.prize_points


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.total_growth: int = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.total_growth += plant.grow()

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_description())
        print(f"Plants added: {len(self.plants)},", end='')
        print(f" Total growth: {self.total_growth}cm")


class GardenManager:

    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    def add_garden(self, garden) -> None:
        self.gardens += [garden]

    def create_garden_network(cls):
        return cls()
    create_garden_network = classmethod(create_garden_network)

    def validate_height(height: int) -> bool:
        return height >= 0
    validate_height = staticmethod(validate_height)

    class GardenStats:

        def count_by_type(garden: str) -> tuple[int, int, int]:
            regular = flowering = prize = 0
            for plant in garden.plants:
                if plant.get_type() == "regular":
                    regular += 1
                elif plant.get_type() == "flowering":
                    flowering += 1
                elif plant.get_type() == "prize":
                    prize += 1
            return regular, flowering, prize
        count_by_type = staticmethod(count_by_type)

        def calculate_score(garden) -> int:
            total: int = 0
            for plant in garden.plants:
                total += plant.get_score()
            return total
        calculate_score = staticmethod(calculate_score)


if __name__ == "__main__":

    print("=== Garden Management System Demo ===")

    manager: GardenManager = GardenManager.create_garden_network()

    garden: Garden = Garden("Alice")

    p1: Plant = Plant("Oak Tree", 100, 5)
    p2: FloweringPlant = FloweringPlant("Rose", 25, 2, "red")
    p3: PrizeFlower = PrizeFlower("Sunflower", 50, 1, "yellow", 10)

    garden.add_plant(p1)
    garden.add_plant(p2)
    garden.add_plant(p3)

    garden.grow_all()

    manager.add_garden(garden)

    garden.report()

    types = GardenManager.GardenStats.count_by_type(garden)
    print(f"Plant types: {types[0]} regular, {types[1]}", end='')
    print(f" flowering, {types[2]} prize flowers")

    print("Height validation test:",
          GardenManager.validate_height(50))

    score: int = GardenManager.GardenStats.calculate_score(garden)
    print(f"Garden scores - {garden.owner}: {score}")
