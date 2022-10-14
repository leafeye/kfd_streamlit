import streamlit as st
import utils

import json
import requests

# background image
utils.add_bg_from_url()

rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

# Streamlit widgets for input text
input_email = st.text_input("Emailaddress")
input_password = st.text_input("Password", type="password")
input_submit_button = st.button("Submit")


def sign_in_with_email_and_password(email: str, password: str, return_secure_token: bool = True):
    # https://betterprogramming.pub/user-management-with-firebase-and-python-749a7a87b2b6

    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(rest_api_url,
                      params={"key": st.secrets["firebase_web_api_key"]},
                      data=payload)

    return r.json()


if input_email and input_password and input_submit_button:
    token = sign_in_with_email_and_password(email=input_email,
                                            password=input_password)

    st.write(token)
