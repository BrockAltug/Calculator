from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the calculator page
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

# Define a route for the measurement conversion
@app.route('/measurement-conversion')
def measurement_conversion():
    return render_template('measurement_conversion.html')

# Define a route for the weight conversion
@app.route('/weight-conversion')
def weight_conversion():
    return render_template('weight_conversion.html')


if __name__ == '__main__':
    app.run(debug=True)
