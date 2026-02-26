from entities.user import User
from getpass import getpass

def register_user():
    name = input("Nombre: ")
    curp = input("CURP: ")
    account = input("Cuenta: ")
    if User.check_account_exists(account):
        print("Usuario ya existe")
    else:
        password = getpass("Contraseña: ")
        User.insert(name, curp, account, password)
        print("Usuario registrado exitosamente")
    
def view_users():
    users = User.get_users()
    for user in users:
        print(f"ID: {user.id}, Nombre: {user.name}, CURP: {user.curp}, Cuenta: {user.account}")

def login():
        try:
            account = input("Cuenta: ")
            password = getpass("Contraseña: ")
            user = User.get_user_by_account(account)
            if user and user.password == password:
                return True
            else:
                return False
        except KeyboardInterrupt as e:
            print("\nOperación cancelada por el usuario.")

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
                    print("Saliendo...")
                    break
                else:
                     print("Opcion no valida")
            
    else:
        print("Credenciales incorrectas")