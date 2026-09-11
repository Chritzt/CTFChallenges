from flask import Flask, request, render_template_string
import subprocess
import urllib.parse

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Secure Admin Ping Tool</title></head>
<body>
    <h2>Admin Internal Ping Tool</h2>
    <form method="GET">
        <input type="text" name="url" placeholder="http://example.com" style="width: 300px;">
        <input type="submit" value="Ping">
    </form>
    {% if result %}
    <h3>Output:</h3>
    <pre>{{ result }}</pre>
    {% endif %}

    <h3>Internal Service Directory (Active Nodes)</h3>
<table style="border-collapse: collapse; width: 100%; max-width: 500px; font-family: sans-serif;">
    <thead>
        <tr style="border-bottom: 2px solid #ddd; text-align: left;">
            <th style="padding: 8px;">Service Name</th>
            <th style="padding: 8px;">Internal Host</th>
            <th style="padding: 8px;">Status</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;">Internal Wiki</td>
            <td style="padding: 8px;"><code>wiki.internal:80</code></td>
            <td style="padding: 8px; color: #ff9800;">● Maintenance</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;">Backup Server</td>
            <td style="padding: 8px;"><code>backup-node.internal:22</code></td>
            <td style="padding: 8px; color: #f44336;">● Offline</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;"><strong>Redis Backend</strong></td>
            <td style="padding: 8px;"><code>gopher-it-redis:6379</code></td>
            <td style="padding: 8px; color: #4caf50;">● Online (Unauthenticated)</td>
        </tr>
    </tbody>
</table>
</body>
</html>
"""

@app.route('/')
def index():
    url = request.args.get('url', '')
    result = ""
    if url:
        try:
            cmd = f"curl -s --max-time 3 {url}"
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        except Exception as e:
            result = str(e)
            
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)