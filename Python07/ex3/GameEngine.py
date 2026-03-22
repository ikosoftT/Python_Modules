from typing import Dict
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:

        hand = [
            self.factory.create_creature(),
            self.factory.create_creature(),
            self.factory.create_spell()
        ]

        battlefield = []
        hand_display = ", ".join(f"{card.name} ({card.cost})" for card in hand)

        print(f"Hand: [{hand_display}]")

        result = self.strategy.excute_turn(hand, battlefield)

        self.turns += 1
        self.total_damage += result["damage_dealt"]
        self.cards_created += len(hand)

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": result,
        }

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
