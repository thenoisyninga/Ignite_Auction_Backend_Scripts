from db_connection import connect_to_auction_admin_db


def delete_login_logs():
    print("> WARNING!!!!!!!!!!!!!!!!!!\n> YOU ARE ABOUT TO DELETE ALL LOGIN LOGS FROM THE AUCTION DATABASE...")

    choice = input("Are you sure? (Y/n): ")

    if choice == "Y":
        db = connect_to_auction_admin_db()

        print("[+] Connected.")
        my_cursor = db.cursor()
        print(f"[+] Clearing all login logs...")
        my_cursor.execute(f"DELETE FROM `login_details` WHERE 1")
        db.commit()
        print("[+] Logs Deleted.")
    else:
        print("[+] Cancelled.")