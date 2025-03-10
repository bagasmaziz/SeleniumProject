# Format Fungsi dalam Python
# Contoh 1 : Hello Pikachu
# tanpa parameter
# tanpa nilai balik (return)
def hello_pikachu():
    print("Hello Pikachu")
    
# Memanggil Fungsi tanpa parameter dan return
hello_pikachu()

# Contoh 2 : Pokemon Info
# 3 parameter (name, type dan hp)
# tanpa nilai balik (return)

# set nilai variable untuk parameter fungsi
name = "Pikachu"
tipe = "Tipe"
hp = "12345"

def pokemon_info(name, tipe, hp):
    print(f"Nama : {name}")
    print(f"Type : {tipe}")
    print(f"HP : {hp}")
    
# Memanggil Fungsi dengan parameter dan return

pokemon_info("Pikachu", "Pokemon", "123")

# Contoh 3 : Celcius to Farenheit
# 1 parameter (suhu celcius)
# nilai balik float (suhu fahreinhet)

def celcius_to_fahrenheit(suhu_celcius):
    suhu_fahrenheit = 9 / 5 * suhu_celcius + 32
    return suhu_fahrenheit

# Cara memanggil Fungsi dengan nilai return
celcius = 30
fahrenheit = celcius_to_fahrenheit(celcius)
print(f"{celcius} celcius sama dengan {fahrenheit}")
