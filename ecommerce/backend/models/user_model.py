from backend.database.db import get_db

def create_user(email, password):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO users (email, password) VALUES (%s, %s)",
        (email, password)
    )

    db.commit()
    cursor.close()
    db.close()


def get_user(email):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT id, email, password FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()
    cursor.close()
    db.close()

    if user:
        return {
            "id": user[0],
            "email": user[1],
            "password": user[2]
        }

    return None