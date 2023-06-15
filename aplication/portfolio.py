from flask import Flask, render_template
from flask_login import LoginManager

app = Flask(__name__)

login_maneger = LoginManager()
login_maneger.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rule')
def rule():
    return render_template('rule.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/start')
def start():
    return render_template('start.html')

if __name__ == '__main__':
    app.run(debug=True)
