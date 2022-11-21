from db_connection import connect_to_auction_admin_db


def add_backup_user():
    db = connect_to_auction_admin_db()
    my_cursor = db.cursor()
    name = input("Enter Del no having the problem: ")
    del_num = input("Enter Delegation Number to add:- ")
    query = f'''INSERT INTO `login` (`ID`, `Username`, `Password`, `Name`, `School`, `Email`, `Has_Bid`) VALUES({del_num},'DEL{del_num}', '1234', '{name}', 'FPSAL','', 'no')'''

    my_cursor.execute(query)
    db.commit()
    print(f"New User created for delegation {name}")
    print(f"USERNAME: DEL{del_num}")
    print("PASSWORD: 1234")

