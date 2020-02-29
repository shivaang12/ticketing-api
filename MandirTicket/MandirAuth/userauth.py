from functools import wraps
from flask import request, jsonify
import jwt

from MandirTicket import app, db, main_user


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        print("Before token data ", token)

        try:
            token_data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = db.session.query(main_user).filter(
                main_user.UserName == token_data['UserName']).first()
        except:
            return jsonify({'message': 'Token is in valid!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if not current_user.RoleID == 1:
            return jsonify({'message': 'Unauthorized'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

