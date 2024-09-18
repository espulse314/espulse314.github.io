from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        # Get the number from the form and convert to float
        number = float(request.form['number'])
        result = number * 7
        return render_template('index.html', result=result)
    except ValueError:
        return render_template('index.html', result="Invalid input, please enter a number.")

if __name__ == '__main__':
    app.run(debug=True)