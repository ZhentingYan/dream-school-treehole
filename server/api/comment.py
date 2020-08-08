from flask import Blueprint, request, g, jsonify
from auth import login_required
from db import get_collection
from datetime import datetime
from bson.objectid import ObjectId

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/new', methods=['POST'])
@login_required
def new_comment():
    COMMENT = get_collection('comment')

    document = {
        'post-id': request.form['post-id'],
        'content': request.form['content'],
        'usr': g.usr['_id'],
        'date': str(datetime.now())
    }
    COMMENT.insert_one(document)

    return 'Success'


@bp.route('/all', methods=['GET'])
def get_all_comment():
    COMMENT = get_collection('comment')
    MEMBER = get_collection('member')
    responce = []

    for document in COMMENT.find({'post-id': request.args.get('id')}, sort=[('date', -1)]):
        result = MEMBER.find_one({'_id': document['usr']})

        responce.append({
            'id': str(document['_id']),
            'content': document['content'],
            'date': document['date'],
            'sender': result['usr']
        })

    return jsonify(responce)
