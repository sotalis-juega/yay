import random as r, string as s

elements = s.ascii_letters + s.ascii_uppercase + s.digits + s.punctuation
lenght = int(input("cuantos caracteres tendra la contraseña?"))

password = ""

for i in range (lenght):
    password += r.choice(elements)

print (f"🔒 tu contraseña generada 😎👍:, {password}") 