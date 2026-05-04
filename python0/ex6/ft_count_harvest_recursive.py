def day_nbr(day :int , total: int):
    if day > total:
        return
    elif day == total:
        print(f"Day {day}")
        print(f"Harvest time!")
    else:
        print(f"Day {day}")
        day_nbr(day+1, total)

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    day_nbr(1, days)

ft_count_harvest_recursive()