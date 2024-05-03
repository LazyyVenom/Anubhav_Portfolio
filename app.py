from flask import Flask

app = Flask()

@app.route("/")
def index():
    return "HEllo World"

if __name__ == '__main__':
    app.run(debug=True)