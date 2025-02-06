import jwt
from datetime import datetime, timedelta
import os
from functools import wraps
from flask import Flask, request, jsonify, g

def token_required(fnc):
    def verify_token(*args, **kwargs):
        token = None
        # Check if token is in the Authorization header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]

        # If no token is found
        if not token:
            return {'message': 'Token is missing!', "status":401}

        try:
            secret_key = os.getenv("SECRET_KEY")
            if not secret_key:
                return {"message": "Server configuration error: SECRET_KEY not set", "status": 500}
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
    
            current_user_uuid = data.get('user_id')
            if not current_user_uuid:
                return {'message': 'Invalid token payload!', "status": 401}

            # Store user ID in Flask's `g` context for use in views
            g.current_user = current_user_uuid
            return fnc(*args, **kwargs)
            
        except jwt.ExpiredSignatureError:
            return {'message': 'Token has expired!', "status":401}
        except jwt.InvalidTokenError:
            return {'message': 'Invalid token!', "status":401}
        except Exception as e:
            return {'message': f'{e}', "status":500}
    
    return verify_token

# def verify_token(request):
#         token = None
#         # Check if token is in the Authorization header
#         if 'Authorization' in request.headers:
#             token = request.headers['Authorization'].split(' ')[1]

#         # If no token is found
#         if not token:
#             return {'message': 'Token is missing!', "status":401}

#         try:
#             secret_key = os.getenv("SECRET_KEY")
#             if not secret_key:
#                 return {"message": "Server configuration error: SECRET_KEY not set", "status": 500}
#             data = jwt.decode(token, secret_key, algorithms=['HS256'])
    
#             current_user_uuid = data.get('user_id')
#             if not current_user_uuid:
#                 return {'message': 'Invalid token payload!', "status": 401}

#             # Store user ID in Flask's `g` context for use in views
#             g.current_user = current_user_uuid
#             return {'message': 'Token verified', "status":200}
#         except jwt.ExpiredSignatureError:
#             return {'message': 'Token has expired!', "status":401}
#         except jwt.InvalidTokenError:
#             return {'message': 'Invalid token!', "status":401}
#         except Exception as e:
#             return {'message': f'{e}', "status":500}