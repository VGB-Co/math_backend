import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("../rft-vgb-ec34f-firebase-adminsdk-tejvo-ee32444d29.json")
firebase_admin.initialize_app(cred)