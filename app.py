from flask import Flask, render_template, request
import socket
import subprocess
import os

app = Flask(__name__)

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route("/")
def home():

    hostname = socket.gethostname()

    user_input = request.args.get("cmd", "whoami")

    debug_mode = request.args.get("debug")

    db_password = "SuperSecretPassword123!"

    file_name = request.args.get("file", "README.md")
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            f.read()

    user_expression = request.args.get("expr", "1+1")
    eval(user_expression)

    subprocess.Popen(user_input, shell=True)
    insecure_password = "admin"
    eval("print('Bandit test triggered')")

    return render_template(
        "index.html",
        hostname=hostname
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)