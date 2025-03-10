# Contoh Variabel Penamaan Valid
nama = "Maya" #tipe data str double quote
namaBelakang = 'Maulani' #tipe data str single quote
umur = 24 #tipe data int
berat = 33.3 #tipe data float
sudahMenikah = True #tipe data boolean
sertifikat = None #tipe data None Type
nomorHP = 1 + 2j #tipe data complex

# Contoh Variabel Penamaan Invalid
# 4umur = 25 #dimulai dengan angka
# nama pengguna #mengandung spasi
# in = "Maya" #menggunakan kata kunci python

# Menampilkan Output pada Layar
print("Nama = ", nama)
print("Nama Belakang = ", namaBelakang)
print("Umur = ", umur)
print("Berat = ", berat)
print("Sudah Menikah = ", sudahMenikah)
print("Sertifikat = ", sertifikat)
print("Nomor HP = ", nomorHP)

# Menampilkan Tipe Data pada Layar
print(type(nama))
print(type(namaBelakang))
print(type(umur))
print(type(sudahMenikah))
print(type(sertifikat))
print(type(nomorHP))
print(type(berat))

# Menampilkan Output String + Variable
print("Nama ", nama, "umur ", umur, "berat ", berat)

# Contoh List
list = [1,2,3] #Datanya bisa berubah

# Contoh Tuple
tuple = [1,2,3] #Datanya tidak bisa berubah

# Contoh Dictionary
nilai = {
    "nama" : "Maya",
    "umur" : 24
}

# Contoh Set
nilaiSet = {1,2,3}

print(list)
print(tuple)
print(nilai)
print(nilaiSet)

# Konversi Tipe Data
numb = 50

int_str = str(100)          # int ke str    : 100       -> "100"
float_str = str(100.5)      # float ke str  : 100.5     -> "100,5"
bool_str = str(True)        # bool ke str   : True      -> "True"

str_int = int("100")        # str ke int    : "100"     -> 100
float_int = int(10.5)     # float ke int  : 100.5     -> 100
bool_int = int(False)       # bool ke int   : False     -> 0

str_float = float("10.5")   # str ke float  : "10.5"    -> 10.5
int_float = float(100)      # int ke float  : 100       -> 100.0
bool_float = float(True)    # bool ke float : True      -> 1.0

str_bool = bool("pokemon")  # str ke bool   : "pokemon" -> True
int_bool = bool(0)          # int ke bool   : 0         -> False
float_bool = bool(0.5)      # float ke bool : 0.5       -> True

numb_str = str(numb) #konversi dari value dalam variable

# Print Konversi Tipe Data
print(int_str)
print(float_str)
print(bool_str)

print(str_int)
print(float_int)
print(bool_int)

print(str_float)
print(int_float)
print(bool_float)

print(str_bool)
print(int_bool)
print(float_bool)

# Print Tipe Data Setelah Konversi Tipe Data
print(type(int_str))
print(type(bool_str))

# Menggabunngkan String dan Tipe Data Lainnya
# Format menggunakan % -> %s : string, %d : decimal
text_info_1 = "Nama: %s %s, Umur: %d tahun" % (nama, namaBelakang, umur)
text_info_2 = "Nama: {} {}, Umur: {} tahun".format(nama, namaBelakang, umur)
text_info_3 = f"Nama: {nama} {namaBelakang}, Umur: {umur} tahun"

print(text_info_1)
print(text_info_2)
print(text_info_3)

# Praktek Memformat Bilangan Decimal
# Format Decimal
pi = 3.141592653

formatted_pi = f"Pi in 4 digits is {pi:.4f}"
print(formatted_pi)

# Format Scientific
speed_of_light = 299792458234575471234

# Format dengan notasi ilmiah biasa (huruf e)
formatted_1 = f"Kecepatan Cahaya = {speed_of_light:.2e} km/s"
print(formatted_1)

# Format dengan notasi ilmiah besar (huruf E)
formatted_2 = f"Kecepatan Cahaya = {speed_of_light:.4E} km/s"
print(formatted_2)