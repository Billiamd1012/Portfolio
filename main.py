import os
import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Get the absolute path to the experience.json file
        file_path = os.path.join(os.path.dirname(__file__), 'templates/experience.json')
        with open(file_path) as f:
            experiences = json.load(f)
        # Get the absolute path to the project.json file
        file_path = os.path.join(os.path.dirname(__file__), 'templates/projects.json')
        with open(file_path) as f:
            projects = json.load(f)
        return render_template('index.html', experiences=experiences['experiences'], projects=projects['projects'])
    except Exception as e:
        app.logger.error(f"Error loading experiences: {e}")
        return "Internal Server Error", 500
    
# Route to show project archive
@app.route('/projects')
def projects():
    try:
        # Get the absolute path to the project.json file
        file_path = os.path.join(os.path.dirname(__file__), 'templates/projects.json')
        with open(file_path) as f:
            projects = json.load(f)
        return render_template('projects.html', projects=projects['projects'])
    except Exception as e:
        app.logger.error(f"Error loading experiences: {e}")
        return "Internal Server Error", 500

# Route to serve the resume PDF
@app.route('/resume.pdf')
def serve_pdf():
    return send_from_directory('static/dist/pdf', 'resume.pdf')


if __name__ == '__main__':
    app.run() 
