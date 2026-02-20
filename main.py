from entities.user import User
from getpass import getpass

def register_user():
    name = input("Nombre: ")
    curp = input("CURP: ")
    account = input("Cuenta: ")
    password = getpass("Contraseña: ")

    User.insert(name, curp, account, password)

def view_users():
    users = User.get_users()
    for user in users:
        print(f"ID: {user.id}, Nombre: {user.name}, CURP: {user.curp}, Cuenta: {user.account}")

if __name__ == "__main__":
    print("Seleccione una opciond de menu")
    print("1.- Registrar usuario")
    print("2.- Consultar usuario")
    option = int(input())
    if option == 1:
        register_user()
    elif option == 2:
        view_users()
