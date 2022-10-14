import streamlit as st
import utils
import admin_utils

# background image
utils.add_bg_from_url()

# Streamlit widgets to let a user create a new post
input_email = st.text_input("Emailaddress")
input_username = st.text_input("Username")
input_password = st.text_input("Password", type="password")
input_submit_button = st.button("Submit")

if input_email and input_username and input_submit_button:
    # initialize app
    app = admin_utils.firebase_admin_app()

    new_user = admin_utils.create_user(email=input_email, 
                                       username=input_username,
                                        password=input_password)

    st.write(f"new user created")
    st.write(f"id: {new_user.uid}")
    st.write(f"tokens valid after timestamp: {new_user.tokens_valid_after_timestamp}" )

    new_user_metadata = new_user.user_metadata
    st.write(f"created on : {new_user_metadata.creation_timestamp}")

