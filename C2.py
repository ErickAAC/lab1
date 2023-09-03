# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True



message = int(input('ingrese el mensaje: '))
e = int(input('Ingrese un exponente: '))
p = int(input("Ingresa un número: "))

if es_primo(p):
    print(f"{p} es un número primo.")
else:
    print(f"{p} no es un número primo, ingrese otro.")
    p = int(input("Ingresa un número: "))

cipher = (int(message) ** int(e)) % int(p)
print (cipher)
