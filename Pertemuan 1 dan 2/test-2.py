# Input Pengguna
first_name = input("Nama depan : ")
last_name = input("Nama belakang : ")

full_name = first_name + " " + last_name

print(full_name)

uang = input("Jumlah uang saat ini : ")
belanja = input("Nominal belanja :")

# Harus melakukan konversi ke int atau float
uang_int = int(uang)
belanja_int = int(belanja)

# Menghitung sisa uang
sisa = uang_int - belanja_int

# Penggabungan str dan int dengan f-sring
info = f"{full_name} memiliki sisa uang {sisa}"

print(info)