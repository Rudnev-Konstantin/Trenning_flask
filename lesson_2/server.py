from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        )

@app.route('/training/<prof>')
def index():
    return render_template(
        'training.html',
        title="",
        title2 = ""
        )

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
