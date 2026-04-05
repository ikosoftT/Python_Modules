from ex0.Card import Card, Rarity
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("Durability Must be Positive.")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        artifacts = game_state.setdefault("artifacts", [])
        artifacts.append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> Dict:
        return {
            "artifact": self.name,
            "ability": self.effect,
            "durability": self.durability
        }
