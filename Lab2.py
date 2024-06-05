#Tusk1
# Введення довжини та ширини першого прямокутника
length1 = float(input("Введіть довжину першого прямокутника: "))
width1 = float(input("Введіть ширину першого прямокутника: "))

# Обчислення площі першого прямокутника
area1 = length1 * width1
print(f"Площа першого прямокутника: {area1}")

# Введення довжини та ширини другого прямокутника
length2 = float(input("Введіть довжину другого прямокутника: "))
width2 = float(input("Введіть ширину другого прямокутника: "))

# Обчислення площі другого прямокутника
area2 = length2 * width2
print(f"Площа другого прямокутника: {area2}")

# Введення довжини та ширини третього прямокутника
length3 = float(input("Введіть довжину третього прямокутника: "))
width3 = float(input("Введіть ширину третього прямокутника: "))

# Обчислення площі третього прямокутника
area3 = length3 * width3
print(f"Площа третього прямокутника: {area3}")
#Tusk2
# Обчислення гіпотенузи за допомогою формули Піфагора
c = (length1**2 + width1**2) ** 0.5
b = (length2**2 + width2**2) ** 0.5
d = (length3**2 + width3**2) ** 0.5

# Виведення результату
print(f"Гіпотенуза першого прямокутного трикутника: {c}")
print(f"Гіпотенуза другого прямокутного трикутника: {b}")
print(f"Гіпотенуза третього прямокутного трикутника: {d}")

if  c > b:
    print("Гіпотенуза першого трикутника більше.")
elif c < b:
    print("Гіпотенуза другого трикутника більше.")
else:
    print("Гіпотенузи рівні.")
#Tusk3

def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a = float(input("Введіть координату x центра кола: "))
b = float(input("Введіть координату y центра кола: "))
R = float(input("Введіть радіус кола: "))

p1, p2 = map(float, input("Введіть координати точки P (через пробіл): ").split())
f1, f2 = map(float, input("Введіть координати точки F (через пробіл): ").split())
l1, l2 = map(float, input("Введіть координати точки L (через пробіл): ").split())

points = [(p1, p2), (f1, f2), (l1, l2)]
inside_count = 0
for i, (x, y) in enumerate(points, start=1):
    if is_inside_circle(x, y, a, b, R):
        inside_count += 1
        print(f"Точка {chr(80+i-1)} лежить всередині кола.")
print(f"Кількість точок, що лежать всередині кола: {inside_count}")
#Tusk4
def calculate_quadrilateral_area(X, Y, Z, T):
    triangle_area = 0.5 * X * Y
    semi_perimeter = (Z + T + (X**2 + Y**2)**0.5) / 2
    triangle2_area = (semi_perimeter * (semi_perimeter - Z) * (semi_perimeter - T) * (semi_perimeter - (X**2 + Y**2)**0.5)) ** 0.5
    return triangle_area + triangle2_area
X = float(input("Введіть довжину сторони X: "))
Y = float(input("Введіть довжину сторони Y: "))
Z = float(input("Введіть довжину сторони Z: "))
T = float(input("Введіть довжину сторони T: "))
area = calculate_quadrilateral_area(X, Y, Z, T)
print("Площа чотирикутника: {area}")
#Tusk5
def find_numbers(n, nums):
    result = []
    for i in range(1, n+1):
        if all(i % num == 0 for num in nums):
            result.append(i)
    return result
n = int(input("Введіть значення n: "))
nums = list(map(int, input("Введіть числа, через які має ділитися n (через пробіл): ").split()))
result = find_numbers(n, nums)
print(f"Натуральні числа, що не перевищують {n} і діляться на кожне з чисел {nums}: {result}")
