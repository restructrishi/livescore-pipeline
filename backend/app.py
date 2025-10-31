from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/live-score')
def get_live_score():
    url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/h"
    headers = {
        "x-rapidapi-key": "ca73524eccmsh5e543d079b5a0fep189fb6jsn032f1ae37486",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # You can customize this according to your UI
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to fetch live score"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
