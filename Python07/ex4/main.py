from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main():

    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 10)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 8)

    id1 = platform.register_card(dragon)
    id2 = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {id1}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print(f"\n{wizard.name} (ID: {id2}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.calculate_rating()}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")

    result = platform.create_match(id1, id2)

    print("Match result:", result)

    print("\nTournament Leaderboard:")

    leaderboard = platform.get_leaderboard()

    for i, (cid, rating, record, name) in enumerate(leaderboard, 1):
        print(f"{i}. {name} - Rating: {rating} ({record})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
