from tgbot.misc.sqlite import Database

db = Database()

def test():
    db.create_table_users()
    users = db.select_all_users()
    print(f"BEFORE: {users}")
    db.add_user(1, "Ilyusha", "gmgm")
    db.add_user(2, "Vasyok")
    db.add_user(3, 3, 4)
    users = db.select_all_users()
    print(f"AFTER: {users}")
    user = db.select_user(id=1)
    print(f"SELECTED USER {user}")
    db.delete_users()
    users = db.select_all_users()
    print(f"AFTER: {users}")

test()