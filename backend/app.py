from flask import Flask, jsonify
import requests
import os  # <-- 1. Import the 'os' library

app = Flask(__name__)

@app.route('/live-score')
def get_live_score():
    url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/h"

    # 2. Get the key securely from the environment
    api_key = os.environ.get('RAPIDAPI_KEY')

    # 3. Add a check in case the key is missing
    if not api_key:
        return jsonify({"error": "API key is missing"}), 500

    headers = {
        "x-rapidapi-key": api_key,  # <-- 4. Use the secure key
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to fetch live score"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)