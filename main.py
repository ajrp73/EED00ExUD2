# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("Hello World...")


# Ejercicio 1
L0=[[1,2,3],['A','B','C'], "EED", "DAM"]

#1. Obtener L1 de manera que L1=[[1,2,3,3,2,1],['ABCCBA'], "EEDDAM", "MADDEE"] (2 Ptos.)
L1=[ L0[0]+L0[0][::-1], [''.join(L0[1] + L0[1][::-1]) ], [L0[2]+L0[3]], [''.join(reversed([L0[2]+L0[3]]))] ]

print("L1:",L1)


# Ejercicio 2

"""
2.1.	Cree un diccionario dicc de forma que se asignen las claves ‘a’, ‘e’, ‘i’, ‘o’, ‘u’ a los valores 0, 1, 2, 3 y 4 ( 0,5 Ptos.)
2.2.	Determinar el valor correspondiente a la clave más alta (orden alfabético) (0,5 Ptos.)
2.3.    Solicite al usuario la introducción de una cadena y muestre el resultado de su cifrado. La cadena resultante siempre estará en minúsculas.
        Ejemplo: Si el usuario introduce "Hola", la cadena resultante será "h3l0" (1 Pto.)
"""
# Ejercicio 2.1
dicc = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

# Ejercicio 2.2
valorMaximo = dicc.get(max(dicc.keys()))
print(valorMaximo)

# Ejercicio 2.3
cad = "pepe"

resultado1 = ""
resultado2 = ""
for c in cad.lower():
    try:
        pos = "aeiou".index(c)
        resultado1 += str(dicc.get(c))
    except ValueError:
        resultado1 += c

    if (c in "aeiouAEIOU"):
        c = dicc.get(c)
    resultado2 += str(c)

print(resultado1)
print(resultado2)
