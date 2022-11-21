from db_connection import connect_to_an_auction_industry_db


def clear_bidding_record():
    print("\n\n> WARNING!!!\n> THIS PROGRAM IS ABOUT TO DELETE ALL EXISTING BIDS ON THE AUCTION DATABASES")
    print("\n> Do you proceed?")

    choice = input("Y/n: ")

    if choice.upper() == "Y":
        for i in range(1, 9):
            db = connect_to_an_auction_industry_db(i)
            print("[+] Deleting bid history...")
            my_cursor = db.cursor()
            my_cursor.execute(f"DELETE FROM `bidding` WHERE 1")
            db.commit()
            print(f"[+] Industry {i} Bid History Deleted.")
            my_cursor.close()
            db.close()
        print("\n\n[+] All Bidding History Deleted.")
    else:
        print("\n[+] Cancelled.")

