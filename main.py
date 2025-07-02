import os
import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Get the absolute path to the experience.json file
        file_path = os.path.join(os.path.dirname(__file__), 'static\dist\json\experience.json')
        with open(file_path) as f:
            experiences = json.load(f)
        return render_template('index.html', experiences=experiences['experiences'])
    except Exception as e:
        app.logger.error(f"Error loading experiences: {e}")
        return "Internal Server Error", 500

# Route to serve the resume PDF
@app.route('/resume.pdf')
def serve_pdf():
    return send_from_directory('static/dist/pdf', 'resume.pdf')

# For development only
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 
