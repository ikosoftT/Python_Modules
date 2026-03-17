from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.SpellCard import SpellCard, SpellEffect
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    creature = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

    spell = SpellCard("Lightning Bolt", 3, Rarity.RARE, SpellEffect.DAMAGE)

    artifact = ArtifactCard(
        "Mana Crystal", 2, Rarity.COMMON, 10, "+1 mana per turn")

    deck = Deck()

    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    print("Deck status:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")

    deck.shuffle()

    game_state = {
        "battlefield": [],
        "artifacts": [],
        "mana": 10
    }
    while True:
        card = deck.drew_card()

        if card is None:
            break
        print(f"Drew: {card.name} ({card.__class__.__name__})")
        if card.is_playable(game_state['mana']):
            result = card.play(game_state)

            print("Play result:", result)

            game_state['mana'] -= 1
        else:
            print("You Can't Play : Not Enough Mana! Sorry :(")
        print()
    print("\nPolymorphism in action: Same interface,",
          " different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
