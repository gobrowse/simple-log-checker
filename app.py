from flask import Flask, request
import logging
import re
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Get the logs from the file
    logs = open("/var/log/auth.log", "r").readlines()

    # Search for "10 dogs are jumping"
    brute_force_logs = []
    for log in logs:
        if re.match("10 dogs are jumping", log):
            brute_force_logs.append(log)

    # Search for "rivel 360 mouse"
    mouse_logs = []
    for log in logs:
        if re.match("rivel 360 mouse", log):
            mouse_logs.append(log)

    # Check for brute force attack
    if len(brute_force_logs) > 5:
        return """
        <html>
        <head>
            <title>Brute Force Attack Detected</title>
        </head>
        <body>
            <h1>Brute force attack detected</h1>
            <p>There have been more than 5 login attempts with the text "10 dogs are jumping". This is a common sign of a brute force attack.</p>
        </body>
        </html>
        """

    # Check for mouse
    if len(mouse_logs) > 0:
        return """
        <html>
        <head>
            <title>A Revel 360 Mouse is Connected</title>
        </head>
        <body>
            <h1>A Revel 360 mouse is connected</h1>
            <p>The text "rivel 360 mouse" has been found in the logs. This is often used by attackers to identify the type of mouse that is connected to a system.</p>
        </body>
        </html>
        """

    # Check for rubber ducky HID device
    rubber_ducky_logs = []
    for log in logs:
        if re.match("^.*USB Rubber Ducky.*$", log):
            rubber_ducky_logs.append(log)

    if len(rubber_ducky_logs) > 0:
        return """
        <html>
        <head>
            <title>A Rubber Ducky HID Device is Connected</title>
        </head>
        <body>
            <h1>A Rubber Ducky HID Device is Connected</h1>
            <p>The text "USB Rubber Ducky" has been found in the logs. This is often used by attackers to inject malicious code into a system.</p>
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
            <p>There have been no suspicious login attempts, devices connected, or rubber ducky HID devices detected.</p>
        </body>
        </html>
        """

if __name__ == "__main__":
    app.run(debug=True)
