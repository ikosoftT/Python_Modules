import functools
import operator
from typing import Any, Callable, List, Dict

def spell_reducer(spells: List[int], operation: str) -> int:
    if not spells:
        return 0
    
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    
    return functools.reduce(ops[operation], spells)

def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "ice": functools.partial(base_enchantment, 50, "ice"),
        "storm": functools.partial(base_enchantment, 50, "storm")
    }

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

@functools.singledispatch
def spell_dispatcher(spell: Any) -> str:
    return "Unknown spell type"

@spell_dispatcher.register(int)
def _(spell: int) -> str:
    return f"Damage spell: {spell} damage"

@spell_dispatcher.register(str)
def _(spell: str) -> str:
    return f"Enchantment: {spell}"

@spell_dispatcher.register(list)
def _(spell: list) -> str:
    return f"Multi-cast: {len(spell)} spells"

def main():
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    print(spell_dispatcher(42))
    print(spell_dispatcher("fireball"))
    print(spell_dispatcher([1, 2, 3]))
    print(spell_dispatcher(None))

if __name__ == "__main__":
    main()