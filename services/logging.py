from models import UserLog
from database import db
from sqlalchemy.orm.exc import NoResultFound
from flask import request, jsonify

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
    
def get_user_logs(user_id, page=1, per_page=20):
    try:
        paginated_logs = UserLog.query.filter_by(user_id=user_id).order_by(UserLog.date.desc()).order_by(UserLog.time.desc()).paginate(page=page, per_page=per_page, error_out=False)

        logs_data = [{
            "log_id": log.uuid,
            "action": log.action,
            "ip_address": log.ip_address,
            "user_agent": log.user_agent,
            "time": log.time,
            "date": log.date,
            "day": log.day
        } for log in paginated_logs.items]

        if logs_data:
            return {"message": logs_data, "status":200}
        else:
            return {"message": "No Logs Found", "status":200}
    except NoResultFound:
        return {"message": "No Logs Found", "status":400}
    except Exception as e:
        return {"message": str(e), "status":500}