from flask import Flask, render_template, request
import socket
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():

    hostname = socket.gethostname()

    aws_access_key_id = "AKIAQWERTYUIOPASDFG"
    aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    github_token = "ghp_abcdEFGHijklMNOPqrstUVWXyz1234567890"
    user_input = request.args.get("cmd", "whoami")
    subprocess.Popen(user_input, shell=True)

    user_expression = request.args.get("expr", "1+1")
    eval(user_expression)

    db_password = "SuperSecretPassword123!"

    file_name = request.args.get("file", "README.md")
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            f.read()


    return render_template(
        "index.html",
        hostname=hostname
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)