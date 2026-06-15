from colorama import init, Fore

init(strip=False)

color = input("dame un color (red, green, blue): ").lower()

match color:
    case "red":
        print(Fore.RED + "El color es rojo")
    case "green":
        print(Fore.GREEN + "El color es verde")
    case "blue":
        print(Fore.BLUE + "El color es azul")
    case _:
        print("Color no reconocido")