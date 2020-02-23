from flask import request, jsonify
from MandirTicket import app, db, db_main_user

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        results = db.session.query(db_main_user).all()
        for r in results:
            print (r)
        resp = jsonify(success=True)
        return resp
    return jsonify(success=False)