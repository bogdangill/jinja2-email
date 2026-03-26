from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Sending data into template
    return render_template('template.html')

if __name__ == '__main__':
    # Run server locally
    app.run(debug=True)