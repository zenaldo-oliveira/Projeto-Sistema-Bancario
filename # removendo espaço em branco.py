# removendo espaço em branco 
nome = "zenaldo"

print(nome.upper())
print(nome.lower())
print(nome.title())


texto = "  ola mundo!  "


print(texto + ".")
print(texto.strip()  + ".")
print(texto.lstrip() + ".")
print(texto.lstrip() + ".")

menu = "java"

print("###" + menu + "###")
print(menu.center(14))
print(menu.center(10,  "#"))
print("p-y-t-h-o-n")



for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu))