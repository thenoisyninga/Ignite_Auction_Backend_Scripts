from db_connection import connect_to_auction_admin_db


def populate_with_test_data():
    db = connect_to_auction_admin_db()

    my_cursor = db.cursor()

    print("> The existing users on the table will be deleted if you proceed.")
    option = input("Proceed? (Y/n): ")

    query = "DELETE FROM `login` WHERE 1"
    my_cursor.execute(query)
    db.commit()

    print("[+] Login table empty. All users deleted")

    print("> How many users are you testing for?")
    num = int(input(": "))

    if option.lower() == 'y':
        for i in range(1, num + 1):
            query = f'''INSERT INTO `login` (`ID`, `Username`, `Password`, `Name`, `School`, `Email`, `Has_Bid`) VALUES({i},'DEL{i}', '1234', 'a_name_without_spaces', 'FPSAL', 'merium.mifta@fps.edu.pk', 'no')'''
            my_cursor.execute(query)
            db.commit()
            print(f"[+] Created {i} test users.")
    print(f"\nCreated {i} new test users, check database.")
