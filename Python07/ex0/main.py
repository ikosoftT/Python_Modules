from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard


def main() -> None:

    print("\n=== DataDeck Card Foundation ===\n")

    print("\nTesting Abstract Base Class Design:\n")

    game_state = {
        "battlefield": [],
        "mana": 6
    }
    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    print(f"CreatureCard Info:\n{dragon.get_card_info()}\n")

    print(f"Playing {dragon.name} with {game_state['mana']} mana available:")
    print(f"Playable: {dragon.is_playable(game_state['mana'])}")

    print(f"Play result: {dragon.play(game_state)}\n")

    att = dragon.attack_target("Goblin Warrior")

    print(f"{att['attacker']} attacks {att['target']}:")
    print(f"Attack result: {att}\n")

    print(f"Testing insufficient mana ({game_state['mana']} available):")
    print(f"Playable: {dragon.is_playable(game_state['mana'])}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
