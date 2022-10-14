import streamlit as st
import utils
import admin_utils

###############
## Streamlit ##
###############

# background image
utils.add_bg_from_url()

st.markdown("# KFD Create User")
#st.sidebar.header("create user")

# Streamlit widgets for input text
# create empty placeholders
placeholder_input_email = st.empty()
placeholder_input_password = st.empty()
placeholder_input_username= st.empty()
placeholder_button = st.empty()

input_username = placeholder_input_username.text_input("username")
input_email = placeholder_input_email.text_input("Emailaddress")
input_password = placeholder_input_password.text_input("Password", type="password")
input_submit_button = placeholder_button.button("Submit")

if input_email and input_username and input_password and input_submit_button:
    # initialize app
    try:
        app = admin_utils.firebase_admin_app()
    except:
        st.write("already connected with app")


    new_user = admin_utils.create_user(email=input_email, 
                                       username=input_username,
                                        password=input_password)
    
    placeholder_input_username.empty()
    placeholder_input_email.empty()
    placeholder_input_password.empty()
    placeholder_button.empty()

    st.write(f"new user created")
    st.write(f"id: {new_user.uid}")
    st.write(f"tokens valid after timestamp: {new_user.tokens_valid_after_timestamp}" )

    new_user_metadata = new_user.user_metadata
    st.write(f"created on : {new_user_metadata.creation_timestamp}")