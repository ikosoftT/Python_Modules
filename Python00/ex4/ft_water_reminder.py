def ft_water_reminder() -> None:
    current_day: int = int(input("Days Since last watering: "))
    if current_day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
