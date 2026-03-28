def month_to_season(month):
    if not isinstance(month, int) or month < 1 or month > 12:
        return "Неверный ввод. Укажите число от 1 до 12."

    seasons = {
        (12, 1, 2): 'Зима',
        (3, 4, 5): 'Весна',
        (6, 7, 8): 'Лето',
        (9, 10, 11): 'Осень'
    }

    for months, season in seasons.items():
        if month in months:
            return season


print(month_to_season(3))
