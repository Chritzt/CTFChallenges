from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <h2>CoreTech Cafeteria Kiosk</h2>
        <form action="/get-menu" method="GET">
            <input type="submit" value="Load Today's Menu">
        </form>
    ''')

@app.route('/get-menu')
def get_menu():
    user_controlled_host = request.headers.get('X-Forwarded-Host', 'internal_api:5000')
    
    internal_url = f"http://{user_controlled_host}/api/v1/menu"
    
    try:
        backend_response = requests.get(internal_url, timeout=3)
        return f"<h3>Backend Response:</h3><pre>{backend_response.text}</pre><br><a href='/'>Back</a>"
    except Exception as e:
        return f"Error connecting to backend asset server at {internal_url}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)