from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://lalit:Lalit@33cool@localhost/flaskdataapp'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Contactsform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(20), nullable=False)


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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form['subject']
        message = request.form['message']

        entry = Contactsform(name=name, email=email, subject=subject, message=message)
        db.session.add(entry)
        db.session.commit()
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
