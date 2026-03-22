import random
from typing import Dict
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None):
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(self, name_or_power=None):
        return ArtifactCard("Mana Ring", 2, "Uncommon", 5, "+1 mana")

    def create_themed_deck(self, size: int) -> Dict:

        deck = []

        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])

            if card_type == "creature":
                deck.append(self.create_creature())

            elif card_type == "spell":
                deck.append(self.create_spell())

            else:
                deck.append(self.create_artifact())

        return {"deck_size": len(deck), "cards": deck}

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
