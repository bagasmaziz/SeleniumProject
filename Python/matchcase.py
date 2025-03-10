pokemon = "Pikachu"
match pokemon:
    case "Pikachu":
        print("Anda menangkap Pikachu")
    case "Charmender":
        print("Anda menangkap Charmender")
    case "Bulbasour":
        print("Anda menangkap Bulbasour")
    case _:
        print("Pokemon tidak diketahui")
        print("Maaf sepertinya tangkapan anda bukan Pokemon")