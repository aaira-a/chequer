
from flask import Flask, render_template, request

from chequer import chequer_main

app = Flask(__name__)


@app.route("/")
def index():
    input = request.args.get('number')
    return render_template('index.html', text=chequer_main(input))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
