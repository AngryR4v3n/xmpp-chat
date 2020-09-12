#client testing.
from handler import *


user = input("Ingrese usuario: ")
pw = input("Ingrese pw: ")
server_handler = Connection(user)

server_handler.connect(pw)
#server_handler.send_message("test_fran@redes2020.xyz", "hola fran_test")

#server_handler.register(pw)