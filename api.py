
# Zatch Bell CCG API

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data to be used for our api

cards = [
   {
        'id': 'E-001',
        'title': 'The Will to Protect is GAYYYYYY',
        'rarity': 'C',
        'description':'Add 3000 Power to 1 of your MAMODO cards of your choice during your opponents next turn.',
        'type': 'Event',
        'turn': '3',
        'set': 'Base Set',
        'image': 'img\E-001 - The Will to Protect.png'
   },
   {
        'id': 'M-107',
        'title': 'Laila {Bounds of Partnership}',
        'rarity': 'SR',
        'description':'[1MP] Neither player can send their in-play PARTNER cards to the Discard Pile during this tur>        'type': 'Mamodo',
        'turn': None
        'set': 'Dawn of the Ancients',
        'image': 'img\M-107 - Laila {Bounds of Partnership}.png'
   },
    {
        'id': 'E-002',
        'title': 'Tina',
        'rarity': 'C',
        'description': 'Both players cannot play any SPELL cards until your opponents next END PHASE',
        'type': 'Event',
        'turn': 2,
        'set': 'Base Set',
        'image': 'img\E-002 - Tina.png'
    }
]



@app.route('/', methods=['GET'])
def home():
    return "<h1>Zatch Bell API Homepage</h1><p>Hopefully this will be full one day....</p>"

@app.route('/api/v1/resources/cards/all', methods=['GET'])
def api_all():
        return  jsonify(cards)

@app.route('/api/v1/resources/cards', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    title = query_parameters.get('title')
    rarity = query_parameters.get('rarity')
    description = query_parameters.get('description')
    type= query_parameters.get('type')
    turn = query_parameters.get('turn')
    set = query_parameters.get('set')
    author = query_parameters.get('author')
    image= query_parameters.get('image')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if title:
        query += ' title=? AND'
        to_filter.append(title)
    if rarity:
        query += ' rarity=? AND'
        to_filter.append(rarity)
    if description:
        query += ' description=? AND'
        to_filter.append(description)
    if type:
        query += ' type=? AND'
        to_filter.append(type)
    if turn:
        query += ' turn=? AND'
        to_filter.append(turn)
    if set:
        query += ' set=? AND'
        to_filter.append(set)
    if image:
        query += ' image=? AND'
        to_filter.append(image)
    if not (id or title or rarity or description or type or turn or set or image):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


app.run()