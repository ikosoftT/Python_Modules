def mage_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int):
    total = initial_power

    def add(power):
        nonlocal total
        total += power
        return total

    return add


def enchantment_factory(enchantment_type: str):
    def enchant(item: str):
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault():
    storage = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}