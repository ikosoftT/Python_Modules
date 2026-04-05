from collections.abc import Callable
from typing import Tuple, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> List[str]:
        return [s(target, power) for s in spells]
    return sequence_spell


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 10)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")

    def simple_spell(target: str, power: int) -> str:
        return f"Power: {power}"

    amplified = power_amplifier(simple_spell, 3)
    print(f"Original: 10, Amplified: {amplified('Target', 10).split(': ')[1]}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Err:", e)
