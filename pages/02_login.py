import streamlit as st
import json
import requests
import utils

###############
## functions ## 
###############

def sign_in_with_email_and_password(email: str, password: str, return_secure_token: bool = True):
    # https://betterprogramming.pub/user-management-with-firebase-and-python-749a7a87b2b6

    rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(rest_api_url,
                      params={"key": st.secrets["firebase_web_api_key"]},
                      data=payload)

    return r.json()

###############
## Streamlit ##
###############

# background image
utils.add_bg_from_url()

#st.set_page_config(page_title="Login")

st.markdown("# KFD Login")
st.sidebar.header("KFD Login")

# Streamlit widgets for input text
# create empty placeholders
placeholder_input_email = st.empty()
placeholder_input_password = st.empty()
placeholder_button = st.empty()

input_email = placeholder_input_email.text_input("Emailaddress")
input_password = placeholder_input_password.text_input("Password", type="password")
input_submit_button = placeholder_button.button("Submit")

if input_email and input_password and input_submit_button:
    token = sign_in_with_email_and_password(email=input_email,
                                            password=input_password)

    placeholder_input_email.empty()
    placeholder_input_password.empty()
    placeholder_button.empty()

    st.write(f"### Welcome {token['displayName']}")
    st.write(token)
