
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
        'Set': 'Base Set',
        'image': 'img\E-001 - The Will to Protect.png'
   },
   {
        'id': 'M-107',
        'title': 'Laila {Bounds of Partnership}',
        'rarity': 'SR',
        'description':'[1MP] Neither player can send their in-play PARTNER cards to the Discard Pile during this tur>        'type': 'Mamodo',
        'turn': None
        'Set': 'Dawn of the Ancients',
        'image': 'img\M-107 - Laila {Bounds of Partnership}.png'
   },
    {
        'id': 'E-002',
        'title': 'Tina',
        'rarity': 'C',
        'description': 'Both players cannot play any SPELL cards until your opponents next END PHASE',
        'type': 'Event',
        'turn': 2,
        'Set': 'Base Set',
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
def api_id():
        if 'id' in request.args:
                id = request.args['id']
        else:
                return "Error. No id field provided. Please specify an id."

        results = []
        for card in cards:
                if card['id'] == id:
                        results.append(card)

app.run()