from flask import Flask, render_template_string, request, render_template
import os

app = Flask(__name__)

app.config['FLAG'] = os.getenv("FLAG")



buzzwords = [
    {
        # The IT Classic
        "Have you tried turning it off and on again?": 
            ["black", "stuck", "slow", "dead", "frozen", "not responding"],
        
        # Printer Hatred
        "Printers are spawned from the depths of hell. Go buy a pen and a piece of paper. Ticket closed.": 
            ["printer", "printing", "jam", "ink", "toner", "streaks"],
        
        # Wi-Fi / Internet issues
        "The Wi-Fi works perfectly fine. Your device is just ancient, or you typed the password wrong three times again.": 
            ["wifi", "wi-fi", "internet", "network", "connection", "slow"],
        
        # Liquid damage
        "I can literally see the coffee inside your keyboard. Don't tell me it 'just stopped working out of nowhere'.": 
            ["coffee", "water", "coke", "soda", "keyboard", "sticky", "spill", "liquid"],
        
        # Permissions / Passwords
        "No, you will not get admin rights just to install an illegal copy of Minecraft. Don't ask again.": 
            ["admin", "password", "rights", "install", "blocked", "access", "permission"],
        
        # Windows/System Updates
        "You do NOT start a system update at 11:59 AM right before a major meeting. Now you have to wait.": 
            ["update", "windows", "loading", "updating", "blue screen", "bluescreen"],
            
        # Default fallback for everything else
        "Your ticket has been moved to the trash bin. Please do not bother us again until next week Tuesday. Thanks.": 
            ["help", "problem", "error", "urgent", "important", "boss", "broken"]
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/check-ticket', methods=["POST"])
def check_ticket() : 
    user_input = request.form.get("problem", "").lower()
    selected_response = ""

    for response, keywords in buzzwords[0].items():
        for keyword in keywords:
            if keyword in user_input:
                selected_response = response
                break
        if selected_response:
            break


    if not selected_response:
        selected_response = "Ticket received. We are successfully ignoring it with high priority."

    template = f'''
    <html>
        <head>
            <title>IT Support Ticket Status</title>
        </head>
        <body style="background-color: #f0f0f0; font-family: monospace; padding: 50px;">
            <h2>Automated Response System</h2>
            <hr>
            <p><strong>Status of your request: {user_input} </strong></p>
            <div style="background: white; padding: 20px; border: 1px solid #ccc;">
                {selected_response}
            </div>
            <br>
            <a href="/">Back to submission</a>
        </body>
    </html>
    '''

    return render_template_string(template)


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=False)