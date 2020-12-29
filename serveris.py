from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    a = 10
    return "Labrīt!<>$"

@app.route('/sveiki')
def sveiki():
  return 'nav rīc'


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
