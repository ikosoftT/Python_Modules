from ex0.Card import Card, Rarity
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if health <= 0 or attack <= 0:
            raise ValueError("Attack/Health Can'Not Be Empty")
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        battlefield = game_state.setdefault("battlefield", [])
        battlefield.append(self.name)
        game_state['mana'] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "Combat_resolved": True
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()

        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
