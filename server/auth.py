import functools
from flask import Blueprint, g, request, session, jsonify
from db import get_collection

# https://flask.palletsprojects.com/en/1.1.x/tutorial/views/

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    MEMBER = get_collection('member')

    result = MEMBER.find_one({'usr': request.form['usr']})
    if result:
        return 'Taken'
    else:
        document = {
            'usr': request.form['usr'],
            'pwd': request.form['pwd'],
            'name': request.form['name'],
            'role': request.form['role'],
        }
        if document['role'] == 'volunteer':
            document['number'] = request.form['number']

        MEMBER.insert_one(document)
        return 'True'


@bp.route('/signin', methods=['POST'])
def sign_in():
    result_filter = {
        'usr': request.form['usr'],
        'pwd': request.form['pwd']
    }
    MEMBER = get_collection('member')

    result = MEMBER.find_one(result_filter)
    if result:
        session.clear()
        session['usr'] = result['usr']
        return jsonify(status=True, role=result['role'])
    else:
        return jsonify(status=False)


@bp.before_app_request
def load_logged_in_user():
    if (request.endpoint != 'auth.logout'):
        usr_id = session.get('usr')

        if usr_id is None:
            g.usr = None
        else:
            MEMBER = get_collection('member')

            result = MEMBER.find_one({'usr': usr_id})
            result.pop('pwd')
            g.usr = result


@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return 'Success'


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.usr is None:
            return 'Invalid User'

        return view(**kwargs)
    return wrapped_view
