import time

import mysql.connector

from db_connection import connect_to_auction_admin_db


def set_has_bids_to_no():
    print("\n\nWARNING!!!\nTHIS PROGRAM IS ABOUT TO ALLOW ALL DELEGATIONS TO BID IN THE AUCTION")
    print("\nDo you proceed???")
    choice = input("Y/n: ")

    if choice == "Y":
        db = connect_to_auction_admin_db()

        print("[+] Setting all 'Has_Bids' to no...")
        my_cursor = db.cursor()
        my_cursor.execute(f"UPDATE `login` SET Has_Bid= 'no' WHERE 1")
        db.commit()
        time.sleep(0.3)
        print("\n[+] All hasbids set to no.")
        my_cursor.close()
        db.close()
    else:
        print("[+] Cancelled.")
