import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    with open("/var/log/auth.log", "r") as f:
        logs = f.readlines()[-20:]
    
    alerts = check_logs(logs)

    if alerts:
        return render_template("index.html", alerts=alerts, logs=logs)
    else:
        return "<h1>No Alerts</h1>"


def check_logs(logs):
    alerts = []

    brute_force = detect_brute_force(logs)
    if brute_force:
        alerts.append(brute_force)

    mouse = detect_mouse(logs)
    if mouse:
        alerts.append(mouse)

    sudo = detect_sudo(logs)
    if sudo:
        alerts.append(sudo)

    keyboard = detect_keyboard(logs)
    if keyboard:
        alerts.append(keyboard)

    return alerts


def detect_brute_force(logs):
    brute_logs = [log for log in logs if re.search("Failed password", log)]
    if len(brute_logs) > 5:
        return "Brute force attack detected"


def detect_mouse(logs):
    mouse_logs = [log for log in logs if re.search("Mouse", log)]
    if mouse_logs:
        return "Mouse detected"


# Other detection functions    

if __name__ == "__main__":
    app.run(debug=True)
