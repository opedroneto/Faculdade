# Determinação da situação em função da pressão arterial

sistolica = int(input("Sistólica: "))
diastolica = int(input("Diastólica: "))

if diastolica >= 120 or sistolica >= 180:
    print("Crise Hipertensiva")
elif 90 <= diastolica <= 120 or 140 <= sistolica <= 180:
    print("Hipertensão Estágio 2")
elif 80 < diastolica < 90 or 130 < sistolica < 140:
    print("Hipertensão Estágio 1")
elif diastolica < 80 and 120 < sistolica < 130:
    print("Elevada")
elif diastolica < 80 and sistolica < 120:
    print("Normal")
