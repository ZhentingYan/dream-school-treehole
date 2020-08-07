from flask import Blueprint, request, g
from auth import login_required
from db import get_collection

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/new', methods=['POST'])
@login_required
def new_post():
    POST = get_collection('post')

    document = {
        'title': request.form['title'],
        'content': request.form['content'],
        'usr': str(g.usr['_id'])
    }
    POST.insert_one(document)

    return 'Success'
