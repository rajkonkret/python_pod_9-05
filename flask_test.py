# flask - framework do aplikacji webowych (backend)

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    # return "Hello, World"
    return render_template('home.html')


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


if __name__ == '__main__':
    app.run(debug=True)
# 11:05
