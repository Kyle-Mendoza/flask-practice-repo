from flask import Flask 
from flask import render_template, request, redirect, url_for
from constants import USERNAME, PASSWORD
from markupsafe import Markup
from flask import render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None 

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username != USERNAME and password != PASSWORD:
            error = "username or password is error, please try again."
            return redirect(url_for('login', error=error))

        return redirect(url_for('home'))
    
    error = request.args.get("error")
    return render_template("login.html", error=error)
        

@app.route("/register", methods=['GET', 'POST'])
def register():
    pass

@app.route("/markup")
def test_markup():
    content = Markup("<strong>This string used markup</strong>")
    return render_template_string("<p>{{ content }}</p>", content=content)

if __name__ == "__main__":
    app.run(debug=True)