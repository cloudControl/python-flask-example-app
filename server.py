import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')

app.debug = True
app.run(host='0.0.0.0', port=int(os.environ['PORT']))
