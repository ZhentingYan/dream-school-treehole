from flask import Blueprint, request, g, jsonify
from auth import login_required
from db import get_collection
from datetime import datetime

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/new', methods=['POST'])
@login_required
def new_post():
    POST = get_collection('post')

    document = {
        'title': request.form['title'],
        'content': request.form['content'],
        'usr': g.usr['_id'],
        'date': str(datetime.now())
    }
    POST.insert_one(document)

    return 'Success'


@bp.route('/all', methods=['GET'])
def get_all_post():
    POST = get_collection('post')
    MEMBER = get_collection('member')
    responce = []

    for document in POST.find(sort=[('date', -1)]):
        result = MEMBER.find_one({'_id': document['usr']})

        responce.append({
            'id': str(document['_id']),
            'title': document['title'],
            'content': document['content'],
            'date': document['date'],
            'sender': result['usr']
        })

    return jsonify(responce)
