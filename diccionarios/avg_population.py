# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:
    avg_data = {}
    total_population = sum(pdata.values())
    for city in pdata:
        city_percent = pdata[city] * 100 / total_population
        avg_data[city] = round(city_percent, 3)

    return avg_data


if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})
