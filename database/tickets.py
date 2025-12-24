import json
import os
from config.settings import DB_FILE

def load_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({}, f)
    with open(DB_FILE) as f:
        return json.load(f)

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def get_ticket(uid):
    return load_db().get(str(uid))

def is_open(uid):
    t = get_ticket(uid)
    return t and t["open"]

def create_ticket(uid, thread_id):
    db = load_db()
    db[str(uid)] = {"thread": thread_id, "open": True, "claimed": None}
    save_db(db)

def close_ticket(uid):
    db = load_db()
    if str(uid) in db:
        db[str(uid)]["open"] = False
        save_db(db)

def set_claim(uid, staff_id):
    db = load_db()
    if str(uid) in db:
        db[str(uid)]["claimed"] = staff_id
        save_db(db)

def find_owner(thread_id):
    for uid, data in load_db().items():
        if data["thread"] == thread_id:
            return int(uid)
    return None