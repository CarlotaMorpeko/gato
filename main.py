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

def login():
    account = input("Cuenta: ")
    password = getpass("Contraseña: ")
    user = User.get_user_by_account(account)
    if user and user.password == password:
        return True
    else:
        return False
    
    #return user and user.password == password


if __name__ == "__main__":
    print("Inicio de sesion")
    if login():
        while True:    
            print("Seleccione una opcion de menu")
            print("1.- Registrar usuario")
            print("2.- Consultar usuario")
            print("3.- Salir")
        
            option = int(input())
            if option == 1:
                register_user()
            elif option == 2:
                view_users()
            elif option == 3:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida")
            
    else:
        print("Usted es invalido")