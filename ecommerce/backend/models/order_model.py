from backend.database.db import get_db

def create_order(user_id, total):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", (user_id, total))
    db.commit()
    db.close()