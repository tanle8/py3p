cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = zip(cityNames, populations, states)


class City:

    def __init__(self, n, p, s):
        self.name = n
        self.population = p
        self.state = s

    def __str__(self):
        return '{}, {} (pop: {})'.format(self.name, self.state, self.population)


cities = []

# way 1
# for city_tup in city_tuples:
#     name, pop, state = city_tup
#     city = City(name, pop, state)   # instance of the City class
#     cities.append(city)
#     # print(city)

# way 2
cities = [City(n, p, s) for (n, p, s) in city_tuples]




# Test
# print(city_tuples)
# print(City('Hanoi', 1000000, 'Hanoi'))
print(cities)
