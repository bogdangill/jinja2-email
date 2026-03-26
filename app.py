import json
from flask import Flask, render_template

app = Flask(__name__)

with open('texts.json', 'r', encoding='utf-8') as f:
    all_texts = json.load(f)

@app.route('/')
def home():
    # Sending data into template
    return render_template('template.html', **all_texts)

if __name__ == '__main__':
    # Run server locally
    app.run(debug=True)