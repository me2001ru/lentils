from flask import Flask, render_template

# 'app'= flask instance . '__name__' holds name of the current python module.
app = Flask(__name__)

# flask view function


@app.route('/')
def index():
    return render_template('index.html')
