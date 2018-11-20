from firebase_admin import auth

def getuser(id_token):
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    return uid