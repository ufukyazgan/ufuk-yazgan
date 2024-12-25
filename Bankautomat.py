# Müşterinin başlangıç bakiyesi
bakiyesi = float(input("Başlangıç bakiyenizi girin: "))

# Müşterinin yapacağı işlem
islem = input("Yapmak istediğiniz işlemi girin (Einzahlung/Auszahlung): ").strip().lower()

# Müşterinin işlem miktarı
miktar = float(input("Miktarı girin: "))

# İşlemi kontrol et
if islem == "einzahlung":
    # Para yatırma işlemi
    bakiyesi += miktar
elif islem == "auszahlung":
    # Para çekme işlemi
    bakiyesi -= miktar
else:
    # Geçersiz işlem
    print("Geçersiz işlem!")
    # Eğer işlem geçersizse bakiye değişmez
    bakiyesi = bakiyesi

# Bakiye negatifse kullanıcıyı uyar
if bakiyesi < 0:
    print("Negatif bakiye olamaz!")
else:
    print("Son bakiye: {bakiyesi} TL")