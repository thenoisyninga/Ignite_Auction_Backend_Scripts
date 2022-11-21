from db_connection import connect_to_auction_admin_db


def logout_all():
    print("\n\nWARNING!!!\nYOU ARE ABOUT TO LOG OUT EVERY DELEGATION IN DB RECORDS")
    print("\nDo you proceed???")
    choice = input("Y/n: ")

    if choice == "Y":
        db = connect_to_auction_admin_db()

        print("[+] Setting all logins to inactive...")
        my_cursor = db.cursor()
        my_cursor.execute(f"UPDATE `login_details` SET `status`='Inactive' WHERE 1")
        db.commit()
        print("[+] Logged out all delegations.")
        my_cursor.close()
        db.close()
    else:
        print("[-] Cancelled.")
