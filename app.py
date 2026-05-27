from flask import Flask, render_template, request
import socket
import subprocess

app = Flask(__name__)

FAKE_AWS_ACCESS_KEY = "AKIAQWERTYUIOPASDFG"
FAKE_AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY123456789"
GITHUB_TOKEN_TEST = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

@app.route("/")
def home():

    hostname = socket.gethostname()

    user_input = request.args.get("cmd", "whoami")

    subprocess.Popen(user_input, shell=True)
    insecure_password = "admin123"
    eval("print('Bandit test triggered')")

    return render_template(
        "index.html",
        hostname=hostname
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)