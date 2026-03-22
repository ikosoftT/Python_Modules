import sys


def parse_args() -> dict:
    if len(sys.argv) < 2:
        raise ValueError("No Argumants Provided!")
    data: dict = {}
    i: int = 1
    colon: int = 0
    while i < len(sys.argv):
        arg: str = sys.argv[i]
        j: int = 0
        while j < len(arg):
            colon = -1
            if arg[j] == ":":
                colon = j
                break
            j += 1
        if colon == -1:
            raise ValueError("Please Enter valid args key:value")
        key: str = arg[:colon]
        value: str = arg[colon + 1:]
        try:
            value: int = int(value)
        except ValueError as e:
            raise e
        data.update({key: value})
        i += 1
    return data


def current_inventory(data: dict, total: int) -> None:
    print("\n=== Current Inventory ===")
    for key, value in data.items():
        percent: int = 0
        if total == 0:
            percent = 0
        else:
            percent = (value / total) * 100
        print(f"{key}: {value} ({percent:.1f}%)")


def stats_helper(data: dict) -> tuple:
    Max: str = None
    Min: str = None

    for key in data.keys():
        if Max is None or data[key] > data[Max]:
            Max = key
        if Min is None or data[key] < data[Max]:
            Min = key
    return Max, Min


def inventory_stats(data: dict) -> None:
    Most: str = None
    Least: str = None
    print("\n=== Inventory Statistics ===")
    Most, Least = stats_helper(data)
    print(f"Most abundant: {Most} ({data[Most]} units)")
    print(f"Least abundant: {Least} ({data[Least]} unit)")


def item_categories(data: dict) -> None:
    print("\n=== Item Categories ===")
    category: dict = {
        "Moderators": {},
        "Scarce": {}
    }
    for key, value in data.items():
        if value >= 5:
            category['Moderators'].update({key: value})
        else:
            category['Scarce'].update({key: value})
    print(f"Moderate: {category.get('Moderators')}")
    print(f"Scarce: {category.get('Scarce')}")


def suggestions(data: dict) -> None:
    print("\n=== Management Suggestions ===")
    restock: list[str] = []
    for key, val in data.items():
        if val <= 1:
            restock += [key]
    print("Restock needed:", end=' ')
    i = 0
    while i < len(restock):
        if i + 1 < len(restock):
            print(restock[i], end=', ')
        else:
            print(restock[i])
        i += 1


def print_demo(data: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end='')
    print(*data.keys(), sep=', ')
    print("Dictionary values: ", end='')
    print(*data.values(), sep=", ")
    s: bool = False
    if data.get('sword'):
        s = True
    print(f"Sample lookup - 'sword' in inventory: {s}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    data: dict = parse_args()
    total: int = 0
    for v in data.values():
        total += v
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(data)}")
    current_inventory(data, total)
    inventory_stats(data)
    item_categories(data)
    suggestions(data)
    print_demo(data)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
