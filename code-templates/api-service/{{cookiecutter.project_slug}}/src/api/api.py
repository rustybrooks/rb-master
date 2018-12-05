from flask import Flask, jsonify

app = Flask('{{cookiecutter.project_slug}}')

@app.route('/health')
def hello_world():
    return 'so healthy it hurts'

@app.route('{{cookiecutter.role}}/health')
def home():
    return 'so healthy it hurts'