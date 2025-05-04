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