import streamlit as st
import json
from google.cloud import firestore
from google.oauth2 import service_account

from helper_functions import add_bg_from_url

# background image
add_bg_from_url()

# Authenticate to Firestore with the JSON account key.
# from https://blog.streamlit.io/streamlit-firestore-continued/
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="kfd-poc")


# Streamlit widgets to let a user create a new post
naam = st.text_input("Naam")
jaar = st.text_input("Jaar")
submit = st.button("Submit new post")

# Once the user has submitted, upload it to the database
if naam and jaar and submit:
	doc_ref = db.collection("users").document(naam)
	doc_ref.set({
		"first": naam,
		"born": jaar
	})


# And then render each user, using some light Markdown
users_ref = db.collection("users")
for doc in users_ref.stream():
	user = doc.to_dict()
	naam = user["first"]
	jaar = user["born"]

	st.subheader(f"User: {naam}")
	st.write(f"jaar: {jaar}")

