a, b, c = input().split()
if "\\" in a:
    a = a.split('\\')
    a = int(a[0]) / int(a[1])
elif "/" in a:
    a = a.split('/')
    a = int(a[0]) / int(a[1])
elif ":" in a:
    a = a.split(':')
    a = int(a[0]) / int(a[1])
else:
    a = int(a)

if "\\" in b:
    b = b.split('\\')
    b = int(b[0]) / int(b[1])
elif "/" in b:
    b = b.split('/')
    b = int(b[0]) / int(b[1])
elif ":" in b:
    b = b.split(':')
    b = int(b[0]) / int(b[1])
else:
    b = int(b)

if "\\" in c:
    c = c.split('\\')
    c = int(c[0]) / int(c[1])
elif "/" in c:
    c = c.split('/')
    c = int(c[0]) / int(c[1])
elif ":" in a:
    c = c.split(':')
    c = int(c[0]) / int(c[1])
else:
    c = int(c)

print(f'({a})*x^2 + ({b})*x + ({c}) = 0 - введенное квадратное уравнение')
d = (b ** 2 - 4 * a * c) ** (1 / 2)
if not (isinstance(d, int) or isinstance(d, float)):
    print('Корней в рациональных числах нет')
elif d > 0:
    x1 = ((b * (-1) + d) / (2 * a))
    x2 = ((b * (-1) - d) / (2 * a))
    print("Корни данного уравнения", x1, x2)
elif d == 0:
    x = ((b * (-1) + d) / (2 * a))
    print("Корень данного уравнения", x)
