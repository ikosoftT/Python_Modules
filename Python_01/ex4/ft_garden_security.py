class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print("Invalid operation attempted: ", end='')
            print(f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected", end="\n\n")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Invalid operation attempted: ", end='')
            print(f"Age {age} days [REJECTED]")
            print("Security: Negative age rejected", end="\n\n")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(f"Plant created: {self.name}")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: SecurePlant = SecurePlant("Rose", 1000, -55)
    plant.get_info()
    plant.set_height(55)
    plant.set_age(150)
    print(f"Current plant: {plant.name} ({plant.get_height()}cm, ", end='')
    print(f"{plant.get_age()} days)")
