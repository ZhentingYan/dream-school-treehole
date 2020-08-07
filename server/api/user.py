from flask import Blueprint, request, g, jsonify
from auth import login_required
from db import get_collection

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/info', methods=['GET'])
@login_required
def get_user_information():
    MEMBER = get_collection('member')

    result = MEMBER.find_one({'usr': g.usr['usr']})

    responce = {
        'usr': result['usr'],
        'role': result['role'],
        'name': result['name']
    }

    if result['role'] == 'volunteer':
        responce['number'] = result['number']

    return jsonify(responce)


# @bp.route('/update', methods=['POST'])
# @login_required
# def update_user_information():
#     MEMBER = get_collection('member')

#     result = MEMBER.find_one({'usr': request.form['usr']})

#     if result and request.form['usr'] != g.usr['usr']:
#         return 'Taken'

#     result = request.form['usr']

#     responce = {
#         'usr': result['usr'],
#         'role': result['role'],
#         'name': result['name']
#     }

#     if result['role'] == 'volunteer':
#         responce['number'] = result['number']

#         MEMBER.update_one(result)

#     return jsonify(responce)
