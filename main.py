from flask import Flask, request, render_template
import jinja2
import string
import pdb

app = Flask(__name__)

dictionary = { 'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s',
               'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
               'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e',
               's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
               'y':'l', 'z':'m' }

def rot(text):
    rot13 = ''
    for character in text:
        if character.islower():
            rot13 += dictionary.get(character)
        if character.isupper():
            character = letter.lower()
            rot13 += dictionary.get(character).capitalize()
        if character not in dictionary:
            rot13 += character

    return rot13

@app.route('/', methods=['GET', 'POST'])
def main():
    text = request.form.get("text")
    translated_text = text
    if text:
        translated_text = rot(text)

    return render_template("index.html", text = translated_text) 
