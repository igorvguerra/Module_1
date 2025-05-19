# Esse é o meu primeiro comentário
""" comentários com mais de uma linha
    usa se três aspas duplas
"""
name = "Igor" + " Guerra"

idade = 5

if idade < 18: 
    print("underage")
else:
    print("overage")





full_name = "Igor Guerra"
age = 35

    # declarar variável com snake_case e classe com camelCase

number = 4
print("Inter number = ", number)


float_number = 3.14
print("Float number = ", float_number)

# type() retorna o tipo da vaiável

print("Type of the variable number = ", type(number))
print("Type of the variable real number = ", type(float_number))

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


# dicionários em python

person = {"name": "Igor", "age": 35, "city": "Lisbon"}
print(person)

print("Name:", person["name"])
person["last_name"] = "Guerra"

print(person["last_name"])

person["age"] = 40
print(person)

del person["last_name"]
print(person)

keys = person.keys()
print(keys)

list_of_keys = list(keys)
print(list_of_keys[1])

values = person.values()
print(values)


items = list(person.items())
print(items)

print("First Key-value:, %s = %s" % (items[0] [0], items[0] [1]))


# if elif e else

legal_age = int(input("What is your age? "))
if legal_age >= 18:
    print("This person is over 18")
elif legal_age <=12:
    print("This person will pay kids entrance fee")
else:
    print("This person is not over 18")

message = "You can request a drivers license" if legal_age >= 18 else "You can not request a drivers license yet"
print(message)

# for
print("For using list")
new_list = [1,2,3,4,5]
for element in new_list:
    print(element)

print("For using tuple")
my_tuple = (6,7,8,9,10)
for element in my_tuple:
    print(element)


new_product = {"code": "7563", "stock": "43", "description": "New hair product"}
print("for using a dictionary - keys")
for key in new_product.keys():
    print(key)

print("\nfor using a dictionary - values")
for value in new_product.values():
    print(value)

print("\nfor using a dictionary - items")
for key, value in new_product.items():
    print(f"{key}: {value}")

# range(): intervalo numérico.
# [0,1,2,3,4,5,6,7,8,9]
print(list(range(0,10)))

for guy in range(5):
    print("Number:", guy)

print("\n Using range() with len()")
listin = [1,2,3,4,5]
print(listin)
for indice in range(0, len(listin)):
    if indice == 3:
        listin[indice] = 5
print(listin)

#enumarate()

list_enumarate = ["a", "b", "c"]
for indice, value in enumerate(list_enumarate):
    print(f"{indice}: {value}")

#while 

print("Exemple of while")
counter = 0
while counter < 5:
    print("Couting:", counter)
    counter += 1
print("End of counting")


#functions

def salute(individual): 
    print(f"Hello, {individual}!")

print("\nExecuting function salute:")
salute("Alice")
salute("Bob")

question = input("what is yout name?")
salute(question)

def squareroot(target):
    result = target ** 2
    return result

result_of_squareroot = squareroot(5)
print("\nThe squareroot of 5 is: ", result_of_squareroot)


print(squareroot(3))

def addition(number1, number2):
    addition_result = number1 + number2
    return addition_result

number1 = 30
number2 = 45

add_result = addition(number1, number2)

# print("The result of adding %s and %s is %s" % (number1, number2, addition(number1, number2)))
print("The result of adding %s and %s is %s" % (number1, number2, add_result))

# errors

print("example of exceptions")
try:
    target = int(input("Please type a number: "))
    result_target = 10 / target   
except ValueError as e:
    print(f"Value error: {e}")
    raise ValueError("Variables types are not compatibles")
except Exception as e:
    print(f"Error: {e}")
else: 
    print(f"Result: {result_target}")
finally:
    print("End of program")