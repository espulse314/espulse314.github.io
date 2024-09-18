from flask import Flask, request, jsonify

app = Flask(__name__)

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