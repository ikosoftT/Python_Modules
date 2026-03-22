import random
from typing import Dict
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name) -> None:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def drew_card(self) -> Card | None:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        t_cost = crt = spl = art = 0
        for card in self.cards:
            n = card.__class__.__name__
            t_cost += card.cost
            if n == "CreatureCard":
                crt += 1
            elif n == "SpellCard":
                spl += 1
            elif n == "ArtifactCard":
                art += 1
        return {
            "total_cards": len(self.cards),
            "creatures": crt,
            "spells": spl,
            "artifacts": art,
            "avg_cost": f"{t_cost / len(self.cards):.1f}"
        }
