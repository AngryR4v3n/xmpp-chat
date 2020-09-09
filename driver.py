#client testing.
from handler import *


user = input("Ingrese usuario: ")
pw = input("Ingrese pw: ")
server_handler = Connection(user)
#server_handler.connect()
print(server_handler.register(pw))