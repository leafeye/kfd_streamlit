

## this was first try, could update users in db


# authenticate and connect to firestore db
db = utils.connect_firestore()

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