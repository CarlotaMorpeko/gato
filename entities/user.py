from persistance.db import get_connection
from security.crypto import encrypt, decrypt


class User:
    
    def __init__(self, id: int,name: str, curp: str, account: str, password: str,user_id: int = None, 
                 card_num: str = None, bank: str = None, card_type: str = None):
        self.id = id
        self.name = name
        self.curp = curp
        self.account = account
        self.password = password
        self.card_num = card_num
        self.bank = bank
        self.card_type = card_type

    def insert(name, curp, account, password):
        connection = get_connection()
        cursor = connection.cursor()

        curp_encrypt = encrypt(curp)
        password_encrypt = encrypt(password)


        sql = "INSERT INTO user(name, curp, account, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, curp_encrypt, account, password_encrypt))
        connection.commit()

        cursor.close()
        connection.close()
    
    def get_users():
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT id, name, curp, account, password FROM user"
        
        cursor.execute(sql)
        rows = cursor.fetchall()

        return [
            
            User(id = row["id"],
                 name = row["name"],
                 account = row["account"],
                 curp = decrypt(row["curp"]),
                 password = row["password"]
                 )
            for row in rows
        ]
    
    def check_account_exists(account):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT account FROM user WHERE account = %s"
        
        cursor.execute(sql, (account,))
        row = cursor.fetchone()
        
        return row is not None
          
    def get_user_by_account(account):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT id, name, curp, account, password FROM user WHERE account = %s"
        
        cursor.execute(sql, (account,))
        row = cursor.fetchone()

        if row is None:
            return None
        else:
            return User(id = row["id"],
                        name = row["name"],
                        account = row["account"],
                        curp = decrypt(row["curp"]),
                        password = decrypt(row["password"])
                        )
        
    def card_insert(id, card_num=None, bank=None, card_type=None, id_user=None):
        connection = get_connection()
        cursor = connection.cursor()

        card_num_encrypt = encrypt(card_num)

        sql = "INSERT INTO card(user_id, card_num, bank, card_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_user, card_num_encrypt, bank, card_type))
        connection.commit()

        cursor.close()
        connection.close()

    def get_cards(card_num=None):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT card_num, bank, card_type FROM card"
        
        cursor.execute(sql)
        rows = cursor.fetchall()

        return [
            
            User(
                 user_id = row["user_id"],
                 card_num = decrypt(row["card_num"]),
                 bank = row["bank"],
                 card_type = row["card_type"]
                 )
            for row in rows
        ]
        
            


