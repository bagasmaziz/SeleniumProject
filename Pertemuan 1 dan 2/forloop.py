# FOR LOOP
# Mencetak "Pikachu" sebanyak 5x
n = int(input('Nilai n : '))
for _ in range(n):
    print("Pikachu")
    
print("-----------------------------")

# Mencetak nilai kuadrat 1-10 dengan step=2
for val in range (1, 10, 3): # Menghasilkan nilai 1, 4, 7, 10
    val_kuadrat = val ** 2 # Kalkulasi untuk menghitung kuadrat
    print(f"{val}^2 adalah {val_kuadrat}")
    
print("-----------------------------")

# Iterasi pada list
skills = ["Python", "R", "Julia", "Scala"] 
for skill in skills:
    print(f"Anda menguasai {skill}")
    
print("-----------------------------")

# Iterasi pada list dengan menyertakan indeks (key)
for idx, skill in enumerate(skills): # nilai idx awal adalah 0
    print(f"Skill ke-{idx+1} : {skill}") # setiap looping akan menampilkan idx awal + 1
    