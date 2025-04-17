full_name = "Igor Guerra"
age = 35

    # declarar variável com snake_case e classe com camelCase

number = 4
print("Inter number = ", number)


float_number = 3.14
print("Float number = ", float_number)

# type() retorna o tipo da vaiável

print("Type of the vaiable number = ", type(number))
print("Type of the vaiable real number = ", type(float_number))

# declarar variavel com quebra de linha usar 3 aspas duplas ou simples, melhor dupla

client_name = """Jorge
Fonseca
""" 

print(client_name)

name_another_line = "Igor \
    Guerra"

# concatenação com vírgula ou com + e também com %s e %

print("Client name: %s" % full_name)

print(f"Client's name and age: {full_name}, {age} years old")
print("Client's name and age: {}, {} years old".format(full_name, age))

