from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main():

    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())

    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")

    turn = engine.simulate_turn()

    print("\nTurn execution:")
    print("Strategy:", turn["strategy"])
    print("Actions:", turn["actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
