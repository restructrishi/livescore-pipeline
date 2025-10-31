from flask import Flask, jsonify
import requests
import os 

app = Flask(__name__)

@app.route('/live-score')
def get_live_score():
    
    # This is the correct URL from your testing
    url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/hscard"

    # Get the key securely from the environment
    api_key = os.environ.get('RAPIDAPI_KEY')

    # Add a check in case the key is missing
    if not api_key:
        # This will be returned if you forget the -e flag in docker run
        return jsonify({"error": "API key is missing"}), 500

    headers = {
        "x-rapidapi-key": api_key, 
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    
    # If the API call is successful, send the data
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        # If the API call fails, send an error
        return jsonify({"error": "Failed to fetch live score", "api_status_code": response.status_code}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)