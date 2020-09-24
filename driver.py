#client testing.
from handler import *
import getpass
from bullet import VerticalPrompt, SlidePrompt, Bullet, Input, Password, Check
from bullet import styles
from bullet import colors
from colorama import Fore,Style
from tabulate import tabulate
from tkinter import Tk
from tkinter.filedialog import askopenfilename
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
        Input("Ingrese su usuario: ",
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
    Screen().input('Press [Enter] to continue')

def obtener_contactos():
    contactos = client.list_contacts()
    
    print(tabulate(contactos, headers=["JID","Subscripcion", "Estado"]))

def agregar_contacto():
    cli = SlidePrompt([
        Input("Ingrese JID de contacto por agregar.", default="mafprueba@redes2020.xyz",
        word_color= colors.foreground["yellow"])
    ])
    results = cli.launch()
    client.addRoster(results[0][1])

def obtener_usuario():
    res=client.get_users()
    print(tabulate(res, headers=['E-mail','JID', 'Username', 'Name' ]))

def enviar_mensaje():
    cli = SlidePrompt([
        Input("Ingrese JID de contacto a chatear.", default="mafprueba@redes2020.xyz",
        word_color= colors.foreground["yellow"]),

        Input("Ingrese mensaje a enviar.", default="Hola!",
        word_color= colors.foreground["yellow"])
    ])
    result = cli.launch()
    client.send_msg(result[0][1], result[1][1])

def crear_grupo():
    cli = SlidePrompt([
        Input("Ingrese nombre de grupo a crear", default="migrupo@conference.redes2020.xyz",
        word_color=colors.foreground["yellow"]),
        Input("Ingrese su apodo", default="Fran",
        word_color=colors.foreground["yellow"])
    ])
    result = cli.launch()
    client.create_group(result[0][1], result[1][1])

def unirse_grupo():
    cli = SlidePrompt([
        Input("Ingrese nombre de grupo a unirse", default="migrupo@conference.redes2020.xyz",
        word_color=colors.foreground["yellow"]),
        Input("Ingrese su apodo", default="Fran",
        word_color=colors.foreground["yellow"])
    ])
    result = cli.launch()
    client.join_group(result[0][1], result[1][1])

def enviar_imagen():
    cli = SlidePrompt([
        Input("Ingrese JID de contacto a chatear", default="prueba1@redes2020.xyz",
        word_color=colors.foreground["yellow"])
    ]) 
    result = cli.launch()
    Tk().withdraw()
    filename = askopenfilename(filetypes=[("PNG","*.png"),("JPG","*.jpg")])
    if filename:
        with open(filename,"rb") as file_img:
            my_str = base64.b64encode(file_img.read())
        client.send_msg(result[0][1])
    else:
        print("ERROR")
        return 0

def actualizar_estado():
    cli = SlidePrompt([
        Input("Estado nuevo: ", default="Mi nuevo estado",
        word_color=colors.foreground["yellow"])
    ])
    result = cli.launch()
    client.send_pres(result[0][1])
    print("Se ha actualizado tu estado.")

def enviar_grupo():
    cli = SlidePrompt([
        Input("Ingrese grupo a chatear.", default="migrupo@conference.redes2020.xyz",
        word_color= colors.foreground["yellow"]),

        Input("Ingrese mensaje a enviar.", default="Hola! Participantes del mejor grupo del mundo",
        word_color= colors.foreground["yellow"])
    ])
    result = cli.launch()
    client.msg_group(result[0][1], result[1][1])

        
# Create the root menu
x = True
menu = """
    1. ✅ Registrar nueva cuenta
    2. 📔 Mis contactos
    3. ➕ Agregar contacto 
    4. 🔎 Descubrir nuevos usuarios
    5. 📨 Enviar mensaje
    6. 🧑 Nuevo grupo
    7. 🫂 Unirse a grupo
    8. 📂 Enviar archivo
    9. 📃 Actualizar estado
    10. 📨📨 Enviar mensaje a grupo 

"""
while x:
    print(f'{Fore.BLUE}##################################{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}       Menu de opciones{Style.RESET_ALL}')
    print(menu)
    
    print(f'{Fore.BLUE}##################################{Style.RESET_ALL}')
    reply = input("Elija una opcion: ")

    if reply == "1":
        registrar()
    elif reply == "2":
        obtener_contactos()
    elif reply == "3":
        agregar_contacto(jid)
    elif reply == "4":
        get_users()
    elif reply == "5":
        enviar_mensaje()
    elif reply == "6":
        crear_grupo()
    elif reply == "7":
        unirse_grupo()
    elif reply == "8":
        enviar_imagen()
    elif reply == "9":
        actualizar_estado()
    elif reply == "10":
        enviar_grupo()

   