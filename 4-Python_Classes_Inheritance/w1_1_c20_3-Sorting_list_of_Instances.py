class Fruit:

    def __init__(self, n, p):
        self.name = n
        self.price = p

    def sort_priority(self):
        return self.price


# Test
fruits = [Fruit('Cherry', 10),
          Fruit('Apple', 5),
          Fruit('Blueberry', 20)]

# Print out the result
# for f in sorted(fruits, key=Fruit.sort_priority):
#     print(f.name)

# Or you can use lambda function, x is every instance which stored in the list fruits
for f in sorted(fruits, key=lambda x: x.sort_priority()):
    print(f.name)
