import sqlite3
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.secret_key = "super_secret_key"
DB_PATH = '/app/data.db' 
FLAG = os.environ.get('FLAG', 'CLA{DEBUG_FLAG_ONLY}')

def get_db():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, role TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS memos (id INTEGER PRIMARY KEY, owner_id INTEGER, content TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS shares (memo_id INTEGER, user_id INTEGER)')
    
    c.execute('INSERT OR IGNORE INTO users VALUES (1, "admin@company.ctf", "admin")')
    c.execute('INSERT OR IGNORE INTO users VALUES (2, "hacker@test.com", "user")')
    c.execute('INSERT OR IGNORE INTO memos VALUES (2, 2, "Dies ist dein privates Memo.")')
    c.execute('INSERT OR REPLACE INTO memos (id, owner_id, content) VALUES (1, 1, ?)', (FLAG,))
    
    conn.commit()
    conn.close()

init_db()

@app.route('/api/memo/view', methods=['GET'])
def get_memos():
    user_id = 2 
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT m.id, m.content FROM memos m 
                 LEFT JOIN shares s ON m.id = s.memo_id 
                 WHERE m.owner_id = ? OR s.user_id = ?''', (user_id, user_id))
    memos = [{"id": row[0], "content": row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify({"memos": memos})

@app.route('/api/memo/share', methods=['POST'])
def share_memo():
    user_id = 2 
    data = request.json
    memo_id = data.get('memo_id')
    target_email = data.get('email')

    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT id FROM users WHERE email = ?', (target_email,))
    target_user = c.fetchone()
    
    if target_user:
        c.execute('INSERT INTO shares VALUES (?, ?)', (memo_id, target_user[0]))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"})
    
    conn.close()
    return jsonify({"error": "User not found"}), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)