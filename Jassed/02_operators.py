## Operadores Aritméticos

print(3 + 3) ## Suma
print(3 - 3) ## Resta
print(3 * 3) ## Multiplicación
print(3 % 3) ## Resto
print(3 / 3) ## División
print(3 // 3) ## Floor division (para que aproxime a número entero)
print(3 ** 3) ## Calcular exponente
print(3 ** 3 + 3 - 8 / 1 // 2)

print("------------------")

print("Hola " + "Python")
print("Hola " + str(6))
print("Hola " * 6)
print("Hola " * ( 2 ** 2))

my_float = 2.5 * 2 
print("Hola " * int(my_float))

print("------------------")

## Operadores Comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

print("------------------")

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Sola") ## Compara en ordenación Alfabética por ASCII
print(len("aaa") >= len("abaa")) # Cuenta caracteres
print("Hola" == "Hola")
print("Hola" != "Python")

print("------------------")

## Operadores Lógicos

print(3 > 4 and "Hola" > "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or ("Hola" < "Python" and 4 == 4))
print(not(3 > 4)) # El "not" se usa para negar toda la condición
