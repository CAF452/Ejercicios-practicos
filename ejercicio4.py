numero = int(input("Por favor, ingresa un número entero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"El número {numero} es divisible por 3 y por 5.")
else:
    print(f"El número {numero} no es divisible por 3 y por 5.")