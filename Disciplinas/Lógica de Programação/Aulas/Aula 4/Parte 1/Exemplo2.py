'''

Determinar as condições climáticas a partir de medições da 
temperatura e umidade atuais:

- temperatura acima de 30, e clima úmido (mais de 60%)
- temperatura acima de 30, e não úmido (menos de 60%)
- temperatura de 20 a 30
- temperatura de 10 a 20 (não incluindo)
- temperatura inferior a 10

'''

temperatura = float(input("Informe a temperatura: "))

if temperatura > 30:
  umidade = float(input("Informe a umidade: "))
  if umidade > 60:
    print("Quente e úmido")
  else:
     print("Quente")
elif 20 <= temperatura <= 30:
    print("Ameno")
elif 10 <= temperatura <= 20:
   print("Frio")
else:
   print("Muito frio")