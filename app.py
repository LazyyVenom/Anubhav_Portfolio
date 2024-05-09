from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/not_in_github")
def not_in_github():
    return render_template("not_in_github.html")

if __name__ == '__main__':
    app.run(debug=True)