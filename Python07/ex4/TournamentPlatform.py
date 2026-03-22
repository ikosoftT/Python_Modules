import random
from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:

        card_id = f"{card.name.lower().replace(' ', '_')}" \
            f"_{len(self.cards)+1:03d}"

        self.cards[card_id] = card

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner = random.choice([card1, card2])
        loser = card2 if winner == card1 else card1

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        winner_id = card1_id if winner == card1 else card2_id
        loser_id = card2_id if winner == card1 else card1_id

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List:

        ranking = []

        for card_id, card in self.cards.items():
            info = card.get_tournament_stats()
            ranking.append(
                (card_id, info["rating"], info["record"],
                 card.name))

        ranking.sort(key=lambda x: x[1], reverse=True)

        return ranking

    def generate_tournament_report(self) -> Dict:

        ratings = [card.calculate_rating() for card in self.cards.values()]

        avg_rating = sum(ratings) // len(ratings) if ratings else 0

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
