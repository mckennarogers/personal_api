import flask
from flask import request, jsonify

app = flask.Flask(__name__)

app.config['DEBUG'] = True

drivers = [
    {'id': 0,
     'name': 'Lewis Hamilton',
     'born': '1985',
     'team': 'Mercedes AMG Petronas',
     'points': '180'},
    {'id': 1,
     'name': 'Max Verstappen',
     'born': '1997',
     'team': 'Red Bull Racing',
     'points': '366'},
    {'id': 2,
     'name': 'Lando Norris',
     'born': '1999',
     'team': 'McLaren',
     'points': '101'}
]

@app.route("/", methods = ['GET'])

def home():
    return "<h1>F1 Driver info</h1><p>A prototype API for F1 driver infro.<p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/f1/all', methods=['GET'])
def api_all():
      return jsonify(drivers)
      
      
@app.route('/api/v1/resources/f1', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
        
    results: []
    
    for driver in drivers:
        if driver['id'] == id:
            results.append(driver)
    
    return jsonify(results)