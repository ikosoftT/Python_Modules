from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def get_methods(cls):
    return [
        name for name, value in cls.__dict__.items()
        if callable(value) and not name.startswith("_")
    ]


def main():

    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:\n")

    card_methods = get_methods(Card)
    combat_methods = get_methods(Combatable)
    magic_methods = get_methods(Magical)

    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Epic",
        attack=5,
        health=10,
        mana=4
    )

    print(f"\nPlaying Arcane Warrior ({elite.__class__.__name__}):")

    print("\nCombat phase:")
    attack_result = elite.attack("Enemy")
    print("Attack result:", attack_result)

    defense_result = elite.defend(5)
    print("Defense result:", defense_result)

    print("\nMagic phase:")
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell_result)

    mana_result = elite.channel_mana(3)
    print("Mana channel:", mana_result)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
