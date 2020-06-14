from flask import render_template
from flask import request
from flask import jsonify


from app import app_bot, parsing, wiki, google_map


@app_bot.route('/')
@app_bot.route('/index')
def index():
    return render_template('index.html')

@app_bot.route('/process_msg', methods=['POST'])
def process_message():
    msg_content = request.form['msg_content']
    if msg_content:
        # Get coordinates
        coord = google_map.MapInfo(msg_content)
        get_coord = coord.get_coordinates()
        print("Coordinates: ", get_coord)
        # Get info of the place
        summary = wiki.WikiInfo(msg_content)
        get_summary = summary.get_summary()
        print("Summary: ", get_summary)
        return jsonify({'msg': get_summary})
        