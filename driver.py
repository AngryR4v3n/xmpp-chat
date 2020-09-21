#client testing.
from handler import *
import getpass
from bullet import Bullet, SlidePrompt, Check, Input, YesNo, Numbers, Password
from bullet import styles
from bullet import colors
from colorama import Fore,Style
#user = input("Ingrese usuario: ")
#pw = getpass.getpass("Ingrese pw: ")
string = """
███████╗██████╗  █████╗ ███╗   ██╗     ██████╗██╗  ██╗ █████╗ ████████╗
██╔════╝██╔══██╗██╔══██╗████╗  ██║    ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
█████╗  ██████╔╝███████║██╔██╗ ██║    ██║     ███████║███████║   ██║   
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
cli = SlidePrompt(
    [
        Input("Ingrese su usario: ",
            default = "fran@redes2020.xyz",
            word_color = colors.foreground["yellow"]),
        Password("Ingrese su contraseña: ", hidden="*"),
    ]
)

result = cli.launch()
client = Client(result[0][1], result[1][1])
newMenu = SlidePrompt([
    Check("What food do you like? ",
            choices = ["1.  📔 List friends", 
                       "2.  📨 Send message",
                       "3.  🧑‍🤝‍🧑 Join group", 
                       "4.  🆕 Create group", 
                       "5.  🚫 Delete user",
                       "6.  ✍ Write status",
                       "7.  🔎 List all users",
                       "8.  🔌 Disconnect"],
            check = " √",
            margin = 2,
            check_color = colors.bright(colors.foreground["red"]),
            check_on_switch = colors.bright(colors.foreground["red"]),
            background_color = colors.background["black"],
            background_on_switch = colors.background["white"],
            word_color = colors.foreground["white"],
            word_on_switch = colors.foreground["black"]
        ),
])

result2=newMenu.launch()
#client.get_users()