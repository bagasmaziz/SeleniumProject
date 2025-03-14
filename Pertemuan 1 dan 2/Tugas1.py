# Fungsi untuk menentukan grade berdasarkan nilai
def hitung_grade(nilai):
    if 90 <= nilai <= 100:
        return 'A'
    elif 80 <= nilai <= 89:
        return 'B'
    elif 70 <= nilai <= 79:
        return 'C'
    elif 60 <= nilai <= 69:
        return 'D'
    else:
        return 'F'

# Fungsi untuk menghitung rata-rata nilai siswa
def hitung_rata_rata(nilai_siswa):
    return sum(nilai_siswa) / len(nilai_siswa)

# Fungsi untuk menjalankan program dengan semua fungsi yang telah dibuat
def allrun():
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    nilai_siswa = []

    for i in range(jumlah_siswa):
        nilai = int(input(f"Masukkan nilai siswa {i+1} (0-100): "))
        nilai_siswa.append(nilai)

    rata_rata = hitung_rata_rata(nilai_siswa)
    grade_kelas = hitung_grade(rata_rata)

    print(f"Rata-rata kelas: {rata_rata:.2f}% - Grade: {grade_kelas}")
    print(f"Nilai tertinggi: {max(nilai_siswa)}% - Grade: {hitung_grade(max(nilai_siswa))}")
    print(f"Nilai terendah: {min(nilai_siswa)}% - Grade: {hitung_grade(min(nilai_siswa))}")

# Menjalankan program dengan memanggil fungsi 
allrun()
