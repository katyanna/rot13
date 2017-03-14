from flask import Flask, render_template
import jinja2
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")
