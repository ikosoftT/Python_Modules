def help(day, days) -> None:
    if (day > days):
        print("Harvest time!")
        return
    print(f"Day {day}")
    help(day + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    help(1, days)
