from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)


def get_sensor_data():
    level = random.randint(50, 800)
    depth = round((level / 1023) * 55, 1)
    percent = round((level / 1023) * 100, 1)

    if level > 500:
        status = "critical"
        color = "#ef4444"
    elif level > 300:
        status = "warning"
        color = "#f59e0b"
    else:
        status = "normal"
        color = "#10b981"

    return {
        "water_level": level,
        "water_depth": depth,
        "water_percentage": percent,
        "status": status,
        "color": color,
        "last_updated": datetime.now().strftime("%H:%M:%S")
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/sensor-data')
def api_sensor_data():
    return jsonify(get_sensor_data())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # debug=False for production