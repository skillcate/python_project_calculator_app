from flask import Flask, request, jsonify, render_template

# Create the app object
app = Flask(__name__)


# Define calculator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():


#   a = [float(x) for x in request.form['a'].values()]
#   b = [float(x) for x in request.form['b'].values()]
#   operation = [str(x) for x in request.form['operation'].values()]

    a = float(request.form['a'])
    b = float(request.form['b'])
    operation = str(request.form['operation'])

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "divide":
        result = a / b
    else:
        result = a * b

    return render_template('index.html', prediction_text=str(result))


if __name__ == "__main__":
    app.run(debug=True)
