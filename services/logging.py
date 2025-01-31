from models import UserLog
from database import db

def log_user_activity(user_id, action, ip_address, user_agent):
    try:
        log_entry = UserLog(
            user_id=user_id,
            action=action,
            ip_address=ip_address,
            user_agent=user_agent
        )
        db.session.add(log_entry)
        db.session.commit()
        return {"message": "Log saved successfully", "status":201}
    
    except Exception as e:
        db.session.rollback()
        return {"error": str(e),"status":500}