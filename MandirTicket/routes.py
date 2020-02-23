from flask import request, jsonify
from MandirTicket import app, db, main_user

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/query', methods=['POST', 'GET'])
def query():
    error = None
    try:
        results = db.session.query(main_user).all()
        for r in results:
            print (r.UserName)
        return jsonify(success=True), 200
    except:
        return jsonify(success=False), 400
    return jsonify(success=False), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    if not data:
        return jsonify({'message' : 'Data is empty!'}), 400
    
    query_result = db.session.query(main_user).filter(main_user.UserName == data['UserName'], main_user.Password == data['Password']).first()

    if query_result:
        return jsonify(success=True), 200
    
    return jsonify({'message' : 'Username or Password does not match.'}), 400

@app.route('/api/register', methods=['POST'])
def register():
    error = None
    if request.method == 'POST':
        data = request.json

        # If data is empty.
        # Also it might be empty if no json header is not used
        if not data:
            return jsonify({'message' : 'Data is empty!'}), 400
        
        # TODO: Check for unique username and email
        username_query_result = db.session.query(main_user).filter(main_user.UserName == data['UserName']).first()
        if username_query_result:
            return jsonify({'message' : 'Username you entered exist in database. Please enter another!'}), 400
        
        email_query_result = db.session.query(main_user).filter(main_user.EmailAddress == data['EmailAddress']).first()
        if email_query_result:
            return jsonify({'message' : 'Email you entered have already registered. Please enter another or request password change!'}), 400
        # TODO: Admin Athentication for Registration

        user_add = main_user(
            UserName=data['UserName'],
            Password=data['Password'],
            EmailAddress=data['EmailAddress'],
            FirstName=data['FirstName'],
            LastName=data['LastName'],
            PhoneNumber=data['PhoneNumber'],
            RoleID=data['RoleID'],
            Enabled=True,
            CreateUserID=data['CreateUserID'],
            ModifiedUserID=1)
        db.session.add(user_add)
        db.session.commit()
        return jsonify(success=True), 200
    return jsonify(success=False), 400