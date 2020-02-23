from flask import request, jsonify, make_response

from MandirTicket import app, db, main_user
from MandirTicket.MandirAuth import userauth


@app.route('/api/query', methods=['POST'])
@userauth.token_required
def query(current_user):
    error = None
    try:
        results = db.session.query(main_user).all()
        for r in results:
            print(r.UserName)
        return jsonify({'message': 'Printed!', 'user': current_user.UserName}), 200
    except:
        return jsonify(success=False), 400
    return jsonify(success=False), 400
