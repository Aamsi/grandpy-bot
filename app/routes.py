from flask import render_template
from flask import request
from flask import jsonify

from app import app_bot

@app_bot.route('/')
@app_bot.route('/index')
def index():
    return render_template('index.html')

@app_bot.route('/process_msg', methods=['POST'])
def process_message():
    msg_content = request.form['msg_content']
    if msg_content:
        return jsonify({'msg': 'Bonjour'})