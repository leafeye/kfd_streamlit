import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin.auth import UserRecord
#from firebase_admin import firestore

# https://betterprogramming.pub/user-management-with-firebase-and-python-749a7a87b2b6


def firebase_admin_app():
    key_dict = json.loads(st.secrets["textkey"])
    creds = credentials.Certificate(key_dict)
    app = firebase_admin.initialize_app(creds)
    return app


## Create new user ##
def create_user(email: str, username: str, password: str) -> UserRecord:
    # return auth.create_user(email=email, uid=user_id) if user_id else auth.create_user(email=email)
    new_user = auth.create_user(email=email, display_name=username, password=password)
    return new_user

