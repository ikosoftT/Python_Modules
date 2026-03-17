class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 typ: str, color: str) -> None:
        super().__init__(name, height, age)
        self.typ: str = typ
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!", end="\n\n")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, typ: str,
                 trunk_diameter: str) -> None:

        super().__init__(name, height, age)
        self.typ: str = typ
        self.trunk: str = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.height * 3} ", end="")
        print("square meters of shade", end="\n\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, typ: str,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.typ: str = typ
        self.season: str = harvest_season
        self.value: str = nutritional_value

    def natural_val(self) -> None:
        print(f"{self.name} is rich in Vitamin {self.value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower: Flower = Flower("Rose", 25, 30, "Flower", "red color")
    flower2: Flower = Flower("lilya", 95, 80, "Flower", "Green color")
    print(f"{flower.name} ({flower.typ}): {flower.height}cm,",
          f"{flower.age} days, {flower.color}")
    print(f"{flower2.name} ({flower2.typ}): {flower2.height}cm,",
          f"{flower2.age} days, {flower2.color}")
    flower.bloom()
    flower2.bloom()
    tree: Tree = Tree("Oak", 500, 1825, "Tree", "50cm diameter")
    tree2: Tree = Tree("Cactus", 580, 2825, "Tree", "99cm diameter")
    print(f"{tree.name} ({tree.typ}): {tree.height},",
          f" {tree.age} days, {tree.trunk}")
    print(f"{tree2.name} ({tree2.typ}): {tree2.height},",
          f" {tree2.age} days, {tree2.trunk}")
    tree.produce_shade()
    tree2.produce_shade()
    vegetable: Vegetable = Vegetable("Tomato", 80, 90, "Vegetable",
                                     "summer harvest", "C")
    vegetable2: Vegetable = Vegetable("Carot", 9, 10, "Vegetable",
                                      "Winter harvest",  "B")
    print(f"{vegetable.name} ({vegetable.typ}): {vegetable.height},",
          f" {vegetable.age} days, {vegetable.season}")
    print(f"{vegetable2.name} ({vegetable2.typ}): {vegetable2.height},",
          f" {vegetable2.age} days, {vegetable2.season}")
    vegetable.natural_val()
    vegetable2.natural_val()
