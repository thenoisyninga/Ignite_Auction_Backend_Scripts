from Logout_A_Single_Delegation import logout_a_delegation
from Clear_All_Login_History import delete_login_logs
from get_delegation_nums_not_logged_in import get_del_not_login
from Initialize_Biddings import clear_bidding_record
from logout_all_delegations import logout_all
from Populate_db_with_test_user_data import populate_with_test_data
from Set_all_hasbids_to_no import set_has_bids_to_no
from addNewUser import add_backup_user

print("=============ADMIN CONTROLS AUCTION © Sarim Ahmed================")
print("=============ADMIN CONTROLS AUCTION © Sarim Ahmed================")
print("=============ADMIN CONTROLS AUCTION © Sarim Ahmed================")
print("=============ADMIN CONTROLS AUCTION © Sarim Ahmed================")
print("=============ADMIN CONTROLS AUCTION © Sarim Ahmed================")
print("=============ADMIN CONTROLS AUCTION © Sarim Ahmed================")


while True:
    print("[*] Here are your options,")
    print(" [1] Logout A Delegation.")
    print(" [2] Clear All Login History.")
    print(" [3] Get Del Num Not Logged In.")
    print(" [4] Clear All Bidding Placed.")
    print(" [5] Logout All Delegations.")
    print(" [6] Populate DB with Test User Data.")
    print(" [7] Set all 'HasBid's to no.")
    print(" [8] Set things up for new round.")
    print(" [9] Add New Backup User.")
    print(" [99] Quit Program.")

    option = int(input("Enter Option ->"))

    if option == 1:
        delNum = int(input("Enter the delegation number you want to log out"))
        logout_a_delegation(delNum)

    elif option == 2:
        delete_login_logs()

    elif option == 3:
        get_del_not_login()
    elif option ==4:
        clear_bidding_record()
    elif option==5:
        logout_all()
    elif option==6:
        populate_with_test_data()
    elif option==7:
        set_has_bids_to_no()
    elif option==8:
        logout_all()
        delete_login_logs()
        set_has_bids_to_no()
        clear_bidding_record()
    elif option==9:
        add_backup_user()
    elif option ==99:
        break
    else:
        print("Invalid option")


