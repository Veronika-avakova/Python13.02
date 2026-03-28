def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


test_year = 2020


result = is_year_leap(test_year)
print(f'год {test_year}: {result}')
