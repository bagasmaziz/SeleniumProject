# While dengan Else
b = 1
while b < 5:
    print("b masih lebih kecil dari 5")
    b = b + 1
else:
    print("b sekarang sama dengan 5") # Print kondisi kalau False
    
# break : menghentikan iterasi total
print("--------- BREAK ------------")

skills = ["Python", "R", "Julia", "Scala"] 
print("start loop")
for val in skills:
    # jika val = "Julia" hentikan iterasi
    if val == "Julia":
        break
    print("Bahasa" , val)
    
# Continue : menghentikan iterasi saat ini
# dan langsung melanjutkan ke iterasi berikutnya
print("--------- CONTINUE ------------")
print("start loop")
a = 0
while a < 5:
    a = a + 1    
    # jika nilai a 2 atau 3 : continue
    if a == 2 or a == 3:    # Kondisi Salah
        continue            # tetap continue walaupun
    print('nilai a = ', a)
    
    print('Nilai dari ID adalah "1206"')
    print("Nilai dari ID adalah '1206'")
    #print('Nilai dari ID adalah '1206'') #salah