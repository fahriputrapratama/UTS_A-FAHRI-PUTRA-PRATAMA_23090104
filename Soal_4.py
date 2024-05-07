def rumus_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal"
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

def hitung():
    berat_badan = float(input("Masukkan Berat Badan (Kg) : "))
    tinggi_badan = float(input("Masukkan Tinggi Badan (M) : "))
    print('Berat Badan :',berat_badan)
    print('Tinggi Badan :',tinggi_badan)
    bmi = rumus_bmi(berat_badan, tinggi_badan)
    print("Nilai  BMI Anda :", bmi)
    kategori = kategori_bmi(bmi)
    print("Kategori BMI :", kategori)

hitung()