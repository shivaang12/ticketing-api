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
            return jsonify({'message' : 'Token is missing!'}), 401
        
        print ("Before token data ", token)

        try:
            token_data = jwt.decode(token, app.config["SECRET_KEY"])
            print ("got token data ", token_data['UserName'])
            current_user = db.session.query(main_user).filter(main_user.UserName == token_data['UserName']).first()
            print ("Current User name ", current_user.FirstName)
        except:
            return jsonify({'message' : 'Token is in valid!'})
        
        return f(current_user, *args, **kwargs)
    return decorated