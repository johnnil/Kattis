import sys

# For use with PyCharm
# lines = iter(sys.argv[1].split())

lines = sys.stdin.readlines()
lines = iter(lines)
nb_years = int(next(lines))
unique_per_year = []
for year in range(nb_years):
    nb_postcards = int(next(lines))
    unique_per_year.append(set())
    for i in range(nb_postcards):
        city_name = next(lines)
        unique_per_year[year].add(city_name)
    print(len(unique_per_year[year]))
