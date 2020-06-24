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
        # Parse message
        parse = parsing.ParsingMessage(msg_content)
        print(parse.msg_parsed)
        # Get coordinates
        map_info = google_map.MapInfo(parse.msg_parsed)
        place_info = map_info.get_address_and_coord()
        try:
            coord = place_info['geometry']
            address = place_info['address']
        except TypeError as err:
            print(err)
            return jsonify({'response': 'fail'})
        # Get info of the place
        wiki_info = wiki.WikiInfo(address, coord[0], coord[1])
        summary = wiki_info.get_summary()
        if address and summary:
            return jsonify({'response': 'success',
                            'address': address,
                            'summary': summary
                        })
        else:
            return jsonify({'response': 'fail'})
        