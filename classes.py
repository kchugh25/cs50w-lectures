# definging a class
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# storing 1 value in obj
ax = int(input("A.X: "))
ay = int(input("A.Y: "))

# storing another value in obj
bx = int(input("B.X: "))
by = int(input("B.Y: "))

p = point(ax, ay)
q = point(bx, by)

print(p.x, p.y)
print(q.x, q.y)