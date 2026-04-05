import alchemy.elements


from alchemy.potions import healing_potion as heal

from alchemy.potions import strength_potion

from alchemy.elements import create_water, create_earth, create_fire


def main() -> None:
    print("\n=== Import Transmutation Mastery ===\n")
    print("Method 1 - Full module import:")

    print("alchemy.elements.create_fire(): ", end='')
    print(alchemy.elements.create_fire())

    print("\nMethod 2 - Specific function import:")

    print("create_water(): ", end='')
    print(create_water())

    print("\nMethod 3 - Aliased import:")

    print("heal(): ", heal())

    print("\nMethod 4 - Multiple imports:")

    print(f"create_earth(): {create_earth()}\n",
          f"create_fire(): {create_fire()}\n",
          f"Strength_potion(): {strength_potion()}")
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERR:", e)
