from alchemy.grimoire import record_spell, validate_ingredients


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")
    test_cases = ["fire air", "dragon scales"]
    test_names = ["Fireball", "Dark Magic"]

    print("Testing ingredient validation:")

    for d in test_cases:
        print(f"validate_ingredients({d}): ", validate_ingredients(d))

    print("\nTesting spell recording with validation:")

    for n, d in zip(test_names, test_cases):
        print(f"record_spell(\"{n}\", \"{d}\"): ", record_spell(n, d))
    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"): ",
          record_spell("Lightning", "air"))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERR:", e)
