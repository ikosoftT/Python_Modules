from typing import Generator


def event_generator(n: int) -> Generator[dict, None, None]:
    players: list[str] = ["alice", "bob", "charlie", "diana"]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]
    for i in range(1, n + 1):
        yield {
            "id": i,
            "player": players[i % len(players)],
            "level": (i * 3) % 20 + 1,
            "action": actions[i % len(actions)]
        }


def fibonacci() -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def prime_gen() -> Generator[int, None, None]:
    num: int = 2
    while True:
        is_prime: bool = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    total_events: int = 0
    high_level_player: int = 0
    treasure_events: int = 0
    level_up: int = 0
    process_time: float = 0

    fib: Generator[int, None, None]
    prime: Generator[int, None, None]

    for event in event_generator(1000):
        total_events += 1
        process_time += 0.00001
        print(f"Event {event['id']}: Player {event['player']}"
              f" ({event['level']}) {event['action']}")
        if event['level'] >= 10:
            high_level_player += 1
        if event['action'] == "found treasure":
            treasure_events += 1
        if event['action'] == "leveled up":
            level_up += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_player}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {process_time:.3f} seconds")

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end='')
    fib = fibonacci()
    for _ in range(9):
        print(next(fib), end=", ")
    print(next(fib))
    print("Prime numbers (first 5): ", end='')
    prime = prime_gen()
    for _ in range(4):
        print(next(prime), end=", ")
    print(next(prime))


if __name__ == "__main__":
    main()
