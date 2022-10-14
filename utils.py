import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import json



def add_bg_from_url():
    # from https://levelup.gitconnected.com/how-to-add-a-background-image-to-your-streamlit-app-96001e0377b2
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/3872532.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def connect_firestore():
    # Authenticate to Firestore with the JSON account key.
    # from https://blog.streamlit.io/streamlit-firestore-continued/
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="kfd-poc")
    return db

