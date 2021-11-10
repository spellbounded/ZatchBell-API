
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
        'turn': None,
        'Set': 'Dawn of the Ancients',
        'image': 'img\M-107 - Laila {Bounds of Partnership}'
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
        # check if an ID was provided as part of the URL
        # If ID is provided, assign it to a variable
        # If no ID is proivded, display an error in the browser
        if 'id' in request.args:
                id = request.args['id']
        else:
                return "Error. No id field provided. Please specify an id."

        # Create an empty list for our results
        results = []

        # Loop through the data and match results that fit the requested ID
        # IDs are unique, but other fields might return many results
        for card in cards:
                if card['id'] == id:
                        results.append(card)

app.run()