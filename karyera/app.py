from flask import Flask, request, redirect, url_for, flash, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    cv_filename = db.Column(db.String(100), nullable=False)
    cover_letter = db.Column(db.Text, nullable=False)

@app.route('/')
def form():
    return render_template('karyera.html')

@app.route('/submit_application', methods=['POST'])
def submit_application():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    position = request.form['position']
    cv = request.files['cv']
    cover_letter = request.form['coverletter']

    cv_filename = f"uploads/{cv.filename}"
    cv.save(cv_filename)

    application = Application(
        name=name,
        email=email,
        phone=phone,
        position=position,
        cv_filename=cv_filename,
        cover_letter=cover_letter
    )
    db.session.add(application)
    db.session.commit()

    flash('Application submitted successfully!')
    return redirect(url_for('form'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
