import json
from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

with open('texts.json', 'r', encoding='utf-8') as f:
    all_texts = json.load(f)

@app.route('/')
def home():
    # Sending data into template
    return render_template('template.html', **all_texts)

if __name__ == '__main__':
    # create livereload server
    server = Server(app.wsgi_app)

    # point files & folders to watch for
    server.watch('templates/')
    server.watch('texts.json')

    # http://127.0.0.1:5500 as default
    server.serve(port=5500, debug=True)