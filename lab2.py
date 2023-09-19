number = int(input("Введите число: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print("Делители числа", number, ":", divisors)
