#Escribe un programa que solicite al usuario dos números y muestre su
#suma, resta, multiplicación, división, división entera y residuo (módulo).
num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa el segundo numero: "))

suma= num1+num2
resta= num1-num2
multi= num1*num2
divi= num1/num2
divisi= num1//num2
residuo= num1%num2

print(f"la suma es: {suma}")
print(f"la resta es: {resta}")
print(f"la multiplicacion es: {multi}")
print(f"la division es: {divi}")
print(f"la division entera es: {divisi}")
print(f"El residuo es: {residuo}")
