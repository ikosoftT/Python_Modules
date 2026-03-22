from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.health = health

        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: Dict) -> Dict:
        game_state.items()
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters battlefield"
        }

    def attack(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> Dict:

        self.health -= incoming_damage

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> Dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> Dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
