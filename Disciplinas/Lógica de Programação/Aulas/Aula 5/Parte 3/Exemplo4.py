'''

Comparando strings

'''

texto1 = "texto"
texto2 = "outro texto"

if texto1 < texto2:
    print(f'"{texto1}" vem antes de "{texto2}"')
elif texto2 < texto1:
    print(f'"{texto2}" vem antes de "{texto1}"')
else:
    print(f'"{texto1}" é igual a "{texto2}"')
