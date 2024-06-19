from flask import Flask, render_template, send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('experience.json') as f:
        experiences = json.load(f)
    return render_template('index.html', experiences=experiences['experiences'])


# Route to serve the resume PDF
@app.route('/resume.pdf')
def serve_pdf():
    return send_from_directory('static/dist/pdf', 'resume.pdf')


if __name__ == '__main__':
    app.run(debug=True)
