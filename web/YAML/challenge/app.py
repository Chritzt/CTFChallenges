from flask import Flask, render_template, request, redirect, url_for
import yaml
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "FLAG{local_fallback_flag}")
with open("/flag.txt", "w") as f:
    f.write(FLAG)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/importer", methods=["GET", "POST"])
def importer():
    message = None
    if request.method == "POST":
        if "config_file" not in request.files:
            return redirect(request.url)
        
        file = request.files["config_file"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            try:
                content = file.read()
                parsed_data = yaml.load(content, Loader=yaml.Loader)
                message = f"Success! Config applied to cluster. Server response object: {parsed_data}"
            except Exception as e:
                message = f"Deployment Error: {str(e)}"
                
    return render_template("importer.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)