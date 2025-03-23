'''Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F'''

califi= float(input("Por favor digita tu calificacion del 1 al 100: "))

if califi <=100 and califi >=90:
    print("Su calificacion es A, ¡FELCITACIONES :D!")
elif califi <=89 and califi >=80:
    print("Su calificacion es B, ¡FELCITACIONES :)!")
elif califi <=79 and califi >=70:
    print("Su calificacion es C, ¡REGULAR ._.!")
elif califi <=69 and califi >=60:
    print("Su calificacion es D, ¡MUY REGULAR :C!")
else:
    print("Su calificacion es F, ¡NOOOO T_T!")