# Variables

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 10
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print('Hola', my_string_variable, 'Tengo', my_int_variable, 'años', 'es', my_bool_variable )


# Algunas Funciones del sistema
print(len(my_string_variable))

# Variables en ua sola línea
name, surname, alias, age = "Jassed", "Martinez", "Mouredev", 23
print(name, surname, alias, age)


# Inputs
'''
name = input('What is your name: ')
age = input('How old are you? ')
print(name)
print(age)
'''


# Forzando el tipo?
# Realmente no lo forzamos, estamos indicando lo que queremos que sea
address: str = "Mi dirección"
address: int = 32
print(address)