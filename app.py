import os
from flask import jsonify, Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)


@app.route("/", methods=['GET'])
def index():
    return jsonify({"message": "You are logged In!"}), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=PORT)
