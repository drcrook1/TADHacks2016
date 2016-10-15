from flask import Blueprint, request, jsonify

confapis = Blueprint('confapis', __name__, url_prefix='/api')

@confapis.route('/values', methods=['GET', 'POST'])
def values():
    if request.method == 'GET':
        return jsonify({'status' : 'success GET'})
    else:
        return jsonify({'status' : 'success POST'})

