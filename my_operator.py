import sqlite3


def connect_to_db():
    db = "brut_our_media.db"
    try:
        conn = sqlite3.connect(db)
        print("🏠 the database has been created/connexion to the database has been successfull")
        return conn

    except:
        print(f"‼ Failed to connect to the database {db}")




if __name__ == '__main__':
    create_table()
