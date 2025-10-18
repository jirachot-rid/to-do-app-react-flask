from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origin="*")

@app.route("/api/users", methods=['GET'])
def users():
    return jsonify(
        {
            "users": [
                "Russ",
                "Chin",
                "Toto"
            ]
        }
    )

if __name__ == "__app__":
    app.run(debug=True, port=8080)