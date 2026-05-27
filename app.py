from flask import Flask, render_template, request
import socket
import subprocess

app = Flask(__name__)

FAKE_AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
FAKE_AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route("/")
def home():

    hostname = socket.gethostname()

    user_input = request.args.get("cmd", "whoami")

    subprocess.Popen(user_input, shell=True)

    return render_template(
        "index.html",
        hostname=hostname
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)