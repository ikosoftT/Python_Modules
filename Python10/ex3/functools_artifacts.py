from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment):
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher():

    @singledispatch
    def cast(arg):
        return "Unknown spell"

    @cast.register
    def _(arg: int):
        return f"Damage spell: {arg}"

    @cast.register
    def _(arg: str):
        return f"Enchantment: {arg}"

    @cast.register
    def _(arg: list):
        return f"Multi-cast: {len(arg)} spells"

    return cast