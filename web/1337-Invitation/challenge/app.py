import pdfkit
from flask import Flask, request, render_template_string, send_file, abort
from io import BytesIO
import os

app = Flask(__name__)

FLAG =  os.getenv("FLAG")

# HTML-Oberfläche für den LAN-Party-Ticket-Generator
INDEX_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>1337 LAN Party Ticket Generator</title>
    <style>
        body { font-family: 'Courier New', Courier, monospace; margin: 40px; background-color: #1a1a1a; color: #00ff00; }
        .container { max-width: 500px; background: #2a2a2a; padding: 20px; border: 2px solid #00ff00; border-radius: 8px; box-shadow: 0 0 15px #00ff00; }
        input, textarea { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #00ff00; background: #111; color: #00ff00; border-radius: 4px; }
        button { background-color: #00ff00; color: black; font-weight: bold; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; width: 100%; }
        button:hover { background-color: #00cc00; }
    </style>
</head>
<body>
    <div class="container">
        <h2>== LAN Party Invite Generator ==</h2>
        <p>Enter your seat details to generate your official PDF entrance ticket.</p>
        <form action="/generate" method="POST">
            <label>Gamer Tag (Name):</label>
            <input type="text" name="gamertag" placeholder="Fatal1ty / xX_NoobSlayer_Xx" required>
            <label>Seat Number (e.g., Table B, Seat 4):</label>
            <input type="text" name="seat" placeholder="Table A, Seat 12" required>
            <label>Extra Gear Notes (HTML allowed for styling):</label>
            <textarea name="notes" placeholder="Bringing a 240Hz monitor and 5-way power strip..." rows="4"></textarea>
            <button type="submit">Generate Ticket (PDF)</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(INDEX_TEMPLATE)

@app.route('/generate', methods=['POST'])
def generate_pdf():
    gamertag = request.form.get('gamertag', '')
    seat = request.form.get('seat', '')
    notes = request.form.get('notes', '')

    # Das HTML-Template für das Ticket mit echtem Browser-Styling-Support
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; background-color: #ffffff; color: #000000; }}
            h1 {{ color: #00aa00; text-align: center; border-bottom: 2px dashed #00aa00; padding-bottom: 10px; }}
            .ticket-box {{ border: 3px solid #00aa00; padding: 20px; }}
            .detail {{ margin-bottom: 10px; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="ticket-box">
            <h1>OFFICIAL LAN PARTY TICKET</h1>
            <div class="detail"><strong>Gamer Tag:</strong> {gamertag}</div>
            <div class="detail"><strong>Allocated Seat:</strong> {seat}</div>
            <div class="detail"><strong>User Notes:</strong> {notes}</div>
        </div>
    </body>
    </html>
    """

    # 'enable-local-file-access' erlaubt wkhtmltopdf das Nachladen von Ressourcen
    options = {
        'enable-local-file-access': None,
        'quiet': ''
    }
    
    try:
        # Generiert das PDF über wkhtmltopdf im RAM
        pdf_bytes = pdfkit.from_string(html_content, False, options=options)
    except Exception as e:
        return f"Error generating PDF: {str(e)}", 500
    
    pdf_buffer = BytesIO(pdf_bytes)
    return send_file(pdf_buffer, mimetype='application/pdf', as_attachment=True, download_name='lan_ticket.pdf')

# Die interne Admin-Schnittstelle, die nur Localhost aufrufen darf
@app.route('/admin/secret-vip-list.txt')
def admin_secret():
    if request.remote_addr != '127.0.0.1':
        return abort(403, "Access Denied: Only the internal LAN-Admin sitting at 127.0.0.1 can view the VIP Flag.")
    return f"GG! You found the internal VIP room. Here is your flag: {FLAG}"

if __name__ == '__main__':
    # threaded=True ist absolut zwingend notwendig für den SSRF-Request!
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)