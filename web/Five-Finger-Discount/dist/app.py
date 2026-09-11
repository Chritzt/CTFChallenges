from flask import Flask, render_template, request
import os

app = Flask(__name__)

articles = [
    {"id": 1, "name": "Shoes", "price": 49.99},
    {"id": 2, "name": "T-Shirt", "price": 20.99}, 
    {"id": 3, "name": "Golden Jacket", "price": 100000000.00}
]

FLAG = os.environ.get("FLAG", "FLAG{flag_flag_flag}")

@app.route('/', methods=['GET'])
def getAll(): 
    return render_template('shop.html', articles=articles)

@app.route('/buy', methods=['POST'])
def buy(): 
    article_id = request.form.get('id')
    try:
        user_money = float(request.form.get('money'))
    except (TypeError, ValueError):
        return "Not enough money", 400

    chosen_article = None
    for a in articles:
        if str(a['id']) == str(article_id):
            chosen_article = a
            break

    if not chosen_article:
        return "Article not found", 404

    
    if user_money >= chosen_article['price']:
        if chosen_article['id'] == 3:
            return "Have your flag: " + FLAG
        else:
            return f"Success {chosen_article['name']} bought!"
    else:
        return f"Not enough money", 400

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=False)