from flask import Flask, request, jsonify
from database import db, init_db
from config import Config
from services.logging import log_user_activity

app = Flask(__name__)
app.config.from_object(Config)
init_db(app)

@app.route('/explore/s2/', methods=['POST'])
def audio_to_text():
    return "working"


@app.route('/log/', methods=['POST'])
def log_activity():
    data = request.json

    if not data or 'user_id' not in data or 'action' not in data:
        return jsonify({'error': 'Invalid data', 'status':400})
    
    message, status  = log_user_activity(user_id=data['user_id'],action=data['action'],ip_address=request.remote_addr,user_agent=request.headers.get('User-Agent', ''))
    return jsonify(message,status)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)