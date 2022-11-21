from db_connection import connect_to_auction_admin_db


def logout_a_delegation(del_num):
    username = f"DEL{int(del_num)}"

    choice = input("Are you sure? (Y/n): ")

    if choice == "Y":
        db = connect_to_auction_admin_db()
        print(f"[+] Setting all {username} logins to inactive...")
        myCursor = db.cursor()
        myCursor.execute(f"UPDATE `login_details` SET `status`='Inactive' WHERE 'name'='{username}'")
        db.commit()
        print(("[+] Done."))
    else:
        print("[+] Program Ended.")