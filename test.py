import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
from bs4 import BeautifulSoup

# Use a service account.
cred = credentials.Certificate('firebase_key.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

var1 = "§ 9500."
var2 = var1.split(".")[0].split(" ")[1]
print(var2)
