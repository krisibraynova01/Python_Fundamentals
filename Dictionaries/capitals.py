country_of_names = input().split(", ")
capital_of_cities = input().split(", ")

country_by_capital = {}

for index in range(len(country_of_names)):
    country = country_of_names[index]
    capital = capital_of_cities[index]
    country_by_capital[country] = capital

for country, capital in country_by_capital.items():
    print(f"{country} -> {capital}")