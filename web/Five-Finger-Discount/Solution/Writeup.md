## Five-Finger-Discount

This challenge is a simple application logic flaw. 

It simulates Webshop with a given amount of money and your task is to buy the golden jacket, which is way more than the users money.

The Flaw: The backend trusts the money send by the frontend and just checks with it, no further checking.

```
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
```

Therefore you just need to change the money amount in the API and thats everything.