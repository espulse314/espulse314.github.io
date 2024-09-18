from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow cross-origin requests for all routes

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        number = float(request.form['number'])
        result = number * 7
        return jsonify(result=result)
    except ValueError:
        return jsonify(error="Invalid input, please enter a number."), 400

if __name__ == '__main__':
    app.run(debug=True)