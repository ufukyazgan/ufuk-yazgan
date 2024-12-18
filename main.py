N1 = float(input("Birinci sınavın notunu giriniz: "))
N2 = float(input("İkinci sınavın notunu giriniz: "))
WunschDurchschnitt = float(input("İstenilen ortalama: "))
N3 = 3 * WunschDurchschnitt - N1 - N2
print("Üçüncü sınavda alman gereken not: ", round(N3, 2))

