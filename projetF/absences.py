from flask import request, jsonify, g
from .db import get_db
from datetime import time as dt_time
from datetime import datetime

def init_absences_routes(app):
    @app.route('/absences/rfid', methods=['POST','GET'])
    def handle_rfid():
        data = request.json
        if 'uid' not in data or 'timestamp' not in data or 'salle_name' not in data:
            return jsonify({"status": "fail", "message": "Invalid data"}), 400

        uid = data['uid']
        try:
            timestamp = datetime.fromisoformat(data['timestamp'])
        except ValueError:
            return jsonify({"status": "fail", "message": "Invalid timestamp format"}), 400

        salle_name = data.get('salle_name', 'Unknown')

        try:
            db = get_db()
            cur = db.cursor()

            insert_query = """
                INSERT INTO ouvertures_porte (carte_rfid, date_ouverture, salle_id) 
                VALUES (%s, %s, (SELECT id FROM salles WHERE nom = %s))
            """
            cur.execute(insert_query, (uid, timestamp, salle_name))
            db.commit()

            return jsonify({"status": "success"}), 201

        except Exception as e:
            db.rollback()
            return jsonify({"status": "error", "message": str(e)}), 500

        finally:
            cur.close()
            db.close()

    @app.route('/absences', methods=['GET'])
    def get_absences():
        cin = request.args.get('cin')
        if not cin:
            return jsonify({'error': 'CIN is required'}), 400

        db = get_db()
        cur = db.cursor()

        absences = cur.execute(
            '''
            SELECT e.nom AS Nom_Etudiant, e.prenom AS Prenom_Etudiant, e.cin AS CIN,
                   ed.periode AS Periode, ed.matiere AS Matiere, s.nom AS Salle,
                   a.presence AS Presence, a.date_absence AS Date_Absence
            FROM etudiant e
            JOIN absences a ON e.id = a.etudiant_id
            JOIN emplois_du_temps ed ON a.emploi_du_temps_id = ed.id
            JOIN salles s ON a.salle_id = s.id
            WHERE e.cin = %s
            ''', (cin,)
        ).fetchall()
        periods = [
            (dt_time(8, 30), dt_time(8, 40)),
            (dt_time(10, 0), dt_time(10, 5)),
            (dt_time(11, 30), dt_time(14, 0)),
            (dt_time(14, 10), dt_time(15, 30)),
            (dt_time(15, 35), dt_time(15, 40)),
            (dt_time(17, 0), dt_time(17, 5))
        ]

        cur.execute('''
            SELECT date_ouverture
            FROM ouvertures_porte
            WHERE carte_rfid = (
                SELECT carte_rfid
                FROM etudiant
                WHERE cin = %s
            )
        ''', (cin,))
        ouvertures = cur.fetchall()

        for ouverture in ouvertures:
            date_ouverture = ouverture[0].time()
            presence = "absent"

            for start_time, end_time in periods:
                if start_time <= date_ouverture <= end_time:
                    presence = "being processed ..."
                    break

            # Update the presence status
            cur.execute(
                "INSERT INTO absences (presence) VALUES (%s)",
                (presence,)
            )

        db.commit()

        return jsonify({'message': 'Absences processed'}), 200

    @app.route('/absences/profile/<int:etudiant_id>', methods=['GET'])
    def get_profile(etudiant_id):
        db = get_db()
        etudiant = db.execute('SELECT * FROM etudiant WHERE id = %s', (etudiant_id,)).fetchone()
        if etudiant is None:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify({
            'id': etudiant['id'],
            'nom': etudiant['nom'],
            'prenom': etudiant['prenom'],
            'cin': etudiant['cin'],
            'email': etudiant['email'],
            'classes': etudiant['classes'],
            'fields': etudiant['fields']
        }), 200
