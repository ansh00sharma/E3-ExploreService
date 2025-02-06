from flask import Flask, request, jsonify,g
from database import db, init_db
import jwt
from config import Config
from services.logging import log_user_activity,get_user_logs
from flask_cors import CORS
from services.token import token_required

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
app.config.from_object(Config)
init_db(app)

@app.route('/explore/s2/', methods=['POST'])
def audio_to_text():
    return "working"


@app.route('/log/', methods=['POST'])
def log_activity():
    data = request.json

    if not data or 'user_id' not in data or 'action' not in data:
        return jsonify({'message': 'Invalid data', 'status':400})
    
    message, status  = log_user_activity(user_id=data['user_id'],action=data['action'],ip_address=request.remote_addr,user_agent=request.headers.get('User-Agent', ''))
    return jsonify(message,status)

@app.route('/logs/<int:page>/', methods=['GET'])
@token_required
def fetch_user_logs(page):
    response = get_user_logs(g.current_user, page, 20)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)