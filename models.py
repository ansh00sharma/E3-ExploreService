from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from database import db
import uuid

class UserLog(db.Model):

    __tablename__ = 'user_logs'

    uuid = db.Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    ip_address = db.Column(db.String(255))
    user_agent = db.Column(db.String(255))
    time = db.Column(db.String(8),nullable=False)
    date = db.Column(db.String(10),nullable=False)
    day = db.Column(db.String(10),nullable=False)

    def __init__(self, user_id, action, ip_address, user_agent):
        now = datetime.now()
        self.user_id = user_id
        self.action = action
        self.ip_address = ip_address
        self.user_agent = user_agent
        self.time = now.strftime('%H:%M:%S')
        self.date = now.strftime('%d-%m-%Y')
        self.day = now.strftime('%A')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __str__(self):
        return self.name
