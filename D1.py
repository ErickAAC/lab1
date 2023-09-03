maximo = int(input("Ingrese el número máximo: "))

if maximo >= 2:
    print(2, end=" ")

if maximo >= 3:
    print(3, end=" ")

for k in range(1, (maximo - 1) // 6 + 1):
    numero1 = 6 * k - 1
    numero2 = 6 * k + 1

    if numero1 <= maximo:
        print(numero1, end=" ")

    if numero2 <= maximo:
        print(numero2, end=" ")