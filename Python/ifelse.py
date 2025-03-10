# Praktek IF - ELIF - ELSE
# Menginput nilai a
a = int(input("Masukkan nilai A : "))

# IF Statement
# Jika TRUE -> Menjalankan Blok IF
if a > 0:
    print("Nilai a = ",a)
    print(a, "lebih besar dari 10")
    
print("-----------------------------")

# IF ELSE Statement
# Jika TRUE -> Menjalankan Blok IF
# Jika FALSE -> Menjalankan Blok ELSE

if a % 2 == 0:
    print(f"{a} adalah bilangan genap")
else:
    print(f"{a} adalah bilangan ganjil")
    
print("-----------------------------")

# IF ELIF ELSE Statement
# Cek kondisi sampai terpenuhi pada IF atau ELIF
# Jika FALSE -> Menjalankan Blok ELSE

if a % 4 == 1:
    print(f"{a} dibagi 4, sisa 1")
elif a % 4 == 2:
    print(f"{a} dibagi 4, sisa 2")
elif a % 4 == 3:
    print(f"{a} dibagi 4, sisa 3")
else:
    print(f"{a} adalah kelipatan 4")
    
print("-----------------------------")

# Contoh Grading
# Cara Biasa
nilai = 90
status = None

if nilai >= 80:
    status = "LULUS"
else:
    status = "GAGAL"
    
print(f"Status : {status}")
    
# If Else langsung disimpan ke variabel
nilai = 60
status = "LULUS" if nilai >=80 else "GAGAL"

print(f"Status : {status}")

    