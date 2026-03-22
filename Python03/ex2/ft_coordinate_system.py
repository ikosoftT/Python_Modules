import math


def calculate_dist(origin: tuple, distance: tuple) -> float:
    x, y, z = origin
    x2, y2, z2 = distance
    return (math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2 + (z2 - z) ** 2))


def parse_data(data: str) -> tuple:
    parts: str = []
    if not data:
        raise ValueError("Cannot Parse None or Empty!")
    try:
        parts = data.split(',')
    except ValueError:
        raise ValueError("Please Enter Valid Coordinates int,int,int")
    i: int = 0
    while i < len(parts):
        try:
            parts[i] = int(parts[i])
        except ValueError as e:
            raise ValueError(e)
        i += 1
    return parts[0], parts[1], parts[2]


def main() -> None:
    print("=== Game Coordinate System ===\n")
    good_position: str = "100, 220, 5"
    position2: str = "3,4,0"
    bad_position: str = "abc,efg,igh"
    origin: tuple = (0, 0, 0)

    try:
        good_position: tuple = parse_data(good_position)
    except ValueError:
        raise ValueError
    dist: float = calculate_dist(origin, good_position)
    print(f"Position created: {good_position}")
    print(f"Distance between {origin} and {good_position}: {dist:.2f}\n")

    print(f"Parsing coordinates: {position2}")
    parsed_coords: tuple = parse_data(position2)
    dist: float = calculate_dist(origin, parsed_coords)
    print(f"Parsed position: {parsed_coords}")
    print(f"Distance between {origin} and {parsed_coords}: {dist:.2f}\n")

    print(f"Parsing invalid coordinates: \"{bad_position}\"")
    try:
        parse_data(bad_position)
    except ValueError as e:
        print("Error:", e)
        print(f"Error details - Type: {e.__class__.__name__}, Args:{e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = good_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
