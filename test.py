import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('firebase_key.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# Get the current database name
database_name = db._database_string
# print(database_name)

# Get the users collection documents
users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")