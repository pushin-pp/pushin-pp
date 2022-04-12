from flask import Flask, render_template
from website import create_app

# app = create_app()
app = Flask(__name__)

# new changes
@app.route('/')
def index():
    return render_template("index.html")

# new changes
@app.route('/about')
def about():
    return render_template("about.html")

# new changes
@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    # added use_reloader=True
    app.run(debug=True, use_reloader=True)

