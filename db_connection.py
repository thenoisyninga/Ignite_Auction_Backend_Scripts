import mysql.connector


def read_password():
    file = open('password.txt', 'r')
    password = file.read().rstrip().lstrip()
    return password


def connect_to_auction_admin_db():
    print("\n[+] Connecting to the auction's admin database...")
    db = mysql.connector.connect(
        host="185.212.70.52",
        user="u168617617_admin",
        passwd=read_password(),
        port="3306",
        database="u168617617_auction_main"
    )
    print("[+] Connected.")
    return db


def connect_to_an_auction_industry_db(industry_index):
    print(f"\n[+] Connecting to Industry {industry_index}'s Database...")
    db = mysql.connector.connect(
        host="185.212.70.52",
        user=f"u168617617_user_ind{industry_index}",
        passwd=read_password(),
        port="3306",
        database=f"u168617617_auction_ind{industry_index}"
    )
    print("[+] Connected.")
    return db
