class Point:

    def __init__(self, x, y):
        self.x = x

        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

def Main():
    p1 = Point(1, 2)

    p2 = Point(1, 2)

    print(p1 == p2)

if __name__ == "__main__":
    Main()