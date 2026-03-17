from ex0.Card import Card, Rarity
from enum import Enum
from typing import Dict


class SpellEffect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: Rarity, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        game_state.values()
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type.value
        }

    def resolve_effect(self, targets: list) -> Dict:
        return {
            "spell": self.name,
            "targets": targets,
            "effect": self.effect_type.value,
            "resolved": True
        }
