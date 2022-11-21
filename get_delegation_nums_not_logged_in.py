from db_connection import connect_to_auction_admin_db


def get_del_not_login():

    db = connect_to_auction_admin_db()
    my_cursor = db.cursor()

    query = f"SELECT * FROM login WHERE 1;"
    my_cursor.execute(query)

    n = 0
    for x in my_cursor:
        n += 1

    query = f"SELECT name FROM login_details WHERE status = 'Active';"
    my_cursor.execute(query)
    myList = []
    for i in range(1, n + 1):
        myList.append(i)
    num = 0
    for x in my_cursor:
        # print("got here")
        num += 1
        try:
            myList.remove(int(x[0][3:]))
        except ValueError:
            pass
    print(f"\n[+] Total {num} people logged in.")

    input("> Press enter to see not logged in accounts.")

    print("\n[+] These are the account that can be used:")
    for deleg in myList:
        print(f"DEL{deleg}")
