from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # return "Hello lalit! "
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/blogdetails')
def blogdetails():
    return render_template('blog-details.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/portfoliodetails')
def portfoliodetails():
    return render_template('portfolio-details.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/team')
def team():
    return render_template('team.html')


app.run(debug=True)
