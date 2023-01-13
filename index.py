from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    # return "Hello lalit! "
    return render_template('index.html')


@app.route('/about')
def about():
    name = "lalit"
    return render_template('about.html', name=name)


app.run(debug=True)
