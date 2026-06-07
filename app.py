from flask import Flask, render_template, request
import socket
import subprocess

app = Flask(__name__)

app_version = "1.0.0"

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route("/")
def home():

    hostname = socket.gethostname()

    user_input = request.args.get("cmd", "whoami")

    subprocess.Popen(user_input, shell=True)
    insecure_password = "admin"
    eval("print('Bandit test triggered')")

    return render_template(
        "index.html",
        hostname=hostname
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)