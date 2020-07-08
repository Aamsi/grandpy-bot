from flask import render_template
from flask import request
from flask import jsonify


from app import app_bot, parsing, wiki, google_map, settings


@app_bot.route('/')
@app_bot.route('/index')
def index():
    return render_template('index.html')


@app_bot.route('/process_msg', methods=['POST'])
def process_message():
    msg_content = request.form['msg_content']
    if msg_content:
        # Parse message
        parse = parsing.ParsingMessage(msg_content)
        # Get coordinates
        map_info = google_map.MapInfo(parse.msg_parsed)
        place_info = map_info.get_address_and_coord()

        if not place_info:
            return jsonify({'response': 'fail', "error": "placerror"})
        coord = place_info['geometry']
        address = place_info['address']

        # Get info of the place
        wiki_info = wiki.WikiInfo(address, coord[0], coord[1])
        response = wiki_info.get_response()
        page = wiki_info.get_matching_page(response)
        summary = wiki_info.get_summary(page)

        if address and summary:
            return jsonify({
                'response': 'success',
                'address': address,
                'summary': summary,
                'lat': coord[0],
                'long': coord[1],
                'token': settings.MAPBOX_TOKEN
            })
        else:
            return jsonify({'response': 'fail', 'error': 'no address and summary'})
