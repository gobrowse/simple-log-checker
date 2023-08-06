from flask import Flask, request
import logging
import re
import os
import time

app = Flask(__name__)

@app.route("/")
def index():
    # Get the logs from the file
    logs = open("/var/log/auth.log", "r").readlines()[-20:]

    # Check for brute force attack
    brute_force_logs = []
    for log in logs:
        if re.match("Failed password", log):
            brute_force_logs.append(log)

    # Check for mouse
    mouse_logs = []
    for log in logs:
        if re.match("Mouse", log):
            mouse_logs.append(log)

    # Check for sudo
    sudo_logs = []
    for log in logs:
        if "sudo" in log:
            sudo_logs.append(log)

    # Check for keyboard
    keyboard_names = ["Keyboard","keyboard","KB"]
    keyboard_logs = []
    for log in logs:
        for kb_name in keyboard_names:
            if re.match(kb_name, log):
                keyboard_logs.append(log)

    if len(brute_force_logs) > 5:
        alerts = ["Brute force attack detected"]

    if len(mouse_logs) > 0:
        alerts.append("A Mouse is connected")

    if len(sudo_logs) > 0:
        alerts.append("Someone has run a root privilege account")

    if len(keyboard_logs) > 0:
        alerts.append("A new keyboard has been connected")

    if alerts:
        return """
        <html>
        <head>
            <title>Alerts</title>
        </head>
        <body>
            <h1>Alerts</h1>
            <p>The following alerts have been detected:</p>
            <ul>
                {% for alert in alerts %}
                <li>{{ alert }}</li>
                {% endfor %}
            </ul>
        </body>
        </html>
        """

    return """
        <html>
        <head>
            <title>No Suspicious Activity Detected</title>
        </head>
        <body>
            <h1>No suspicious activity detected</h1>
            <p>There have been no suspicious login attempts, and/or devices connected</p>
        </body>
        </html>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

