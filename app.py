from flask import Flask, request
import logging
import re
import os
import time


    alerts = []
    if len(brute_force_logs) > 5:
        alerts.append("Brute force attack detected")

    if len(mouse_logs) > 0:
        alerts.append("A Mouse is connected")

    if len(sudo_logs) > 0:
        alerts.append("Someone has run a root privilege account")

    if len(keyboard_logs) > 0:
        alerts.append("A new keyboard has been connected")

    if len(alerts) > 0:
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

# Other detection functions    

if __name__ == "__main__":
    app.run(debug=True)
