## Strings

my_string = "Mi String"
my_other_string = 'Mi otra String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\nescapado"
print(my_scape_string)

# Formateo

name, surname, age = "Jassed", "Martínez", 23
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desenpaquetado de Caracteres

language = "python"
a, b, c, d ,e, f = language
print(a)
print(b)
print(c)
print(d)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

# Revserse

reverse_language = language[::-1]
print(reverse_language)

# Funciones del sistema

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper()) 
print(language.lower().isupper()) 