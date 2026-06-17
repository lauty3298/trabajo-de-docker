from colorama import init, Fore
from rich.console import Console
from rich.panel import Panel

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

console = Console()

def main():
    console.print("\n[bold green]¡Hola desde Docker![/bold green] :rocket:")
    
    console.print(
        Panel.fit(
            "[bold cyan]Rich[/bold cyan] está funcionando correctamente dentro de tu contenedor.",
            title="[bold magenta]Éxito[/bold magenta]",
            border_style="green"
        )
    )
    print("") # Un espacio en blanco al final

if __name__ == "__main__":
    main()