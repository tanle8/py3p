class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x,
                     self.y + otherPoint.y)

    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x,
                     self.y - otherPoint.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        ref_x = self.x
        ref_y = -self.y
        return Point(ref_x, ref_y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy



p1 = Point(3, 4)
p2 = Point(5, 12)
# mid = p1.halfway(p2)

# print(p1)
# print(p1.getX())
# print(p1.getY())

# print(mid)
# print(mid.getX())
# print(mid.getY())

# print(p1 - p2)
# print(p1.reflect_x())
p1.move(1, 2)
print(p1)
