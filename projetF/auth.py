from flask import request, jsonify, session, g
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

def init_auth_routes(app):
    @app.before_request
    def load_logged_in_user():
        user_id = session.get('etudiant_id')
        if user_id is None:
            g.user = None
        else:
            db = get_db()
            g.user = db.execute(
                'SELECT * FROM etudiant WHERE id = %s', (user_id,)
            ).fetchone()
            db.close()

    @app.route('/auth/register', methods=['POST'])
    def register():
        data = request.json
        required_fields = ['nom', 'prenom', 'cin', 'email', 'classes', 'fields', 'password']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400
        
        nom = data.get('nom')
        prenom = data.get('prenom')
        cin = data.get('cin')
        email = data.get('email')
        classes = data.get('classes')
        fields = data.get('fields')
        password = data.get('password')

        db = get_db()
        try:
            existing_user = db.execute(
                'SELECT * FROM etudiant WHERE email = %s', (email,)
            ).fetchone()
            if existing_user:
                return jsonify({'error': 'User with this email already exists.'}), 400
            db.execute(
                """
                INSERT INTO etudiant (nom, prenom, cin, email, classes, fields, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (nom, prenom, cin, email, classes, fields, generate_password_hash(password)),
            )
            db.commit()
            return jsonify({'message': 'User registered successfully'}), 201
        except Exception as e:
            db.rollback()
            print(f"An error occurred during registration: {str(e)}")
            return jsonify({'error': 'An error occurred during registration.'}), 500
        finally:
            db.close()

    @app.route('/auth/login', methods=['POST'])
    def login():
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        db = get_db()
        try:
            user = db.execute(
                'SELECT * FROM etudiant WHERE email = %s', (email,)
            ).fetchone()

            if user is None:
                return jsonify({'error': 'Incorrect email.'}), 400
            elif not check_password_hash(user['password'], password):
                return jsonify({'error': 'Incorrect password.'}), 400

            session.clear()
            session['etudiant_id'] = user['id']
            return jsonify({'message': 'Login successful'}), 200
        except Exception as e:
            print(f"An error occurred during login: {str(e)}")
            return jsonify({'error': 'An error occurred during login.'}), 500
        finally:
            db.close()

    @app.route('/auth/logout', methods=['POST'])
    def logout():
        session.clear()
        return jsonify({'message': 'Logged out successfully'}), 200
