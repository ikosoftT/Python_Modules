from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def excute_turn(self, hand: List, battlefield: List) -> Dict:
        cards_played = []
        mana_used = 0

        for card in hand:
            if card.cost <= 3:
                cards_played.append(card.name)
                mana_used += card.cost

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8
        }

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def priorotize_targets(self, available_targets: List) -> List:
        return available_targets
