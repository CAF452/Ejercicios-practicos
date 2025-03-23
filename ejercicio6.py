'''Escribe un programa que solicite al usuario tres números y determine
cuál de ellos es el mayor.'''

num1= int(input("Digite el primer numero: "))
num2= int(input("Digite el segundo numero: "))
num3= int(input("Digite el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(f"\nEl numero mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"\nEl numero mayor es: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"\nEl numero mayor es: {num3}")
else:
    print("\nNO HAY NUMERO MAYOR.")

