from flask import Flask, request
import os

app = Flask(__name__)

FLAG = os.getenv("FLAG")

@app.route('/api/v1/menu')
def menu():
    return "Standard Cafeteria Menu: Overcooked Pasta with sad tomato sauce."

@app.route('/api/v1/admin/flag')
def admin_flag():
    return f"ACCESS GRANTED. Welcome Admin. Here is your system flag: {FLAG}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)