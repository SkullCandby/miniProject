a, b, c = [int(x) for x in input().split()]
print(a, b, c)
x = (a + c + abs(a-c)) / 2
y = (b + c + abs(b-c)) / 2
z = (a + b + abs(a-b)) / 2
delta = abs(abs(x - y) + abs(x - z) + abs(y - z)) / 2
print((x + y + z + delta) / 3)
print(f'x = {x}, y = {y}, z = {z}')
#hdhaodwoihd