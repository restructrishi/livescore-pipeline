from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/live-score')
def get_live_score():
    #
    # --- THIS IS THE ONLY LINE I CHANGED ---
    #
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/live"
    #
    # --------------------------------------
    #

    # Get the key securely from the environment
    api_key = os.environ.get('RAPIDAPI_KEY')

    # Add a check in case the key is missing
    if not api_key:
        return jsonify({"error": "API key is missing"}), 500

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    # You might need to add params here if the API requires them
    # querystring = {"live": "true"}
    # response = requests.get(url, headers=headers, params=querystring)
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        # This is what's happening now:
        # The API returns a 403, so your code returns this 500 error.
        return jsonify({"error": "Failed to fetch live score", "api_status_code": response.status_code}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)