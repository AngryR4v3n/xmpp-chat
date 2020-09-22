#client testing.
from handler import *
import getpass
from bullet import VerticalPrompt, SlidePrompt, Bullet, Input, Password, Check
from consolemenu import *
from consolemenu.items import *
from bullet import styles
from bullet import colors
from colorama import Fore,Style
#user = input("Ingrese usuario: ")
#pw = getpass.getpass("Ingrese pw: ")
string = """
███████╗██████╗  █████╗ ███╗   ██╗     ██████╗██╗  ██╗ █████╗ ████████╗
█╔════╝██╔══██╗██╔══██╗████╗  ██║    ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
████╗  ██████╔╝███████║██╔██╗ ██║    ██║     ███████║███████║   ██║   
██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║    ██║     ██╔══██║██╔══██║   ██║   
██║     ██║  ██║██║  ██║██║ ╚████║    ╚██████╗██║  ██║██║  ██║   ██║   
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
"""
print(f'{Fore.BLUE}-----------------------------------------------------------------------{Style.RESET_ALL}')
print(string)
print(f'{Fore.BLUE}-----------------------------------------------------------------------{Style.RESET_ALL}')
print(f'{Fore.BLUE}-----------------------------------------------------------------------{Style.RESET_ALL}')
"""
CLI
Matriz de preguntas (num campo, valor)
valor: [0][1]
"""
cli = VerticalPrompt(
    [
        Input("Ingrese su usario: ",
            default = "fran@redes2020.xyz",
            word_color = colors.foreground["yellow"]),
        Password("Ingrese su contraseña: ", word_color=colors.foreground["yellow"], hidden="*"),
    ]
)

result = cli.launch()
client = Client(result[0][1], result[1][1])

def registrar():
    cli = SlidePrompt([
        Input("Ingrese JID ", default="pruebanding123@redes2020.xyz",
            word_color = colors.foreground["yellow"]),
        Password("Ingrese su contraseña: ", word_color=colors.foreground["yellow"], hidden="*"),
    ])
    results = cli.launch()
    print(results[0][1])
    Screen().input('Press [Enter] to continue')

# Create the root menu
menu = MultiSelectMenu("Fran-Chat_v1", "Escoja una opcion",
                        epilogue_text=("Cliente hecho en Sleek-XMPP"),
                        exit_option_text='❌ Salir de cliente XMPP')  # Customize the exit text

# Add all the items to the root menu
menu.append_item(FunctionItem("✅ Registrar nueva cuenta", registrar))


'''
menu.append_item(FunctionItem("📔 Mis contactos", action, args=['two']))
menu.append_item(FunctionItem("➕ Agregar contacto", action, args=['two']))
menu.append_item(FunctionItem("🔎 Descubrir nuevos usuarios", action, args=['three']))
menu.append_item(FunctionItem("📨 Enviar mensaje", action, args=['four']))
menu.append_item(FunctionItem("🧑‍🤝‍🧑 Nuevo grupo", action, args=['four']))
menu.append_item(FunctionItem("🫂 Unirse a grupo", action, args=['four']))
menu.append_item(FunctionItem("📂 Enviar archivo", action, args=['four']))
'''
# Show the menu
menu.start()
menu.exit()
menu.join()

#client.get_users()