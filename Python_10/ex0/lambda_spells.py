def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact['power'],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtred_ite = filter(lambda m: m['power'] >= min_power, mages)
    return list(filtred_ite)


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_iter = map(lambda s: f"* {s}*", spells)
    return list(transformed_iter)


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))

    if not powers:
        return {
            'max_power': 0,
            'min_power': 0,
            'avg_power': 0,
        }
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
    ]
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']})",
          f" comes before {sorted_arts[1]['name']}",
          f"({sorted_arts[1]['power']})")
    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(*transformed)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
