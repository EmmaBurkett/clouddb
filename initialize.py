import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
class initialize_firestore:
    def __init__(self):
        self.db = ""


    def initialize_firestore(self):
            # Use a service account
            cred = credentials.Certificate('hello-world-plus-my-files-lol-firebase-adminsdk-vqbze-48919c460d.json')
            firebase_admin.initialize_app(cred, {'projectID': 'hello-world-plus-my-files-lol'})

            self.db = firestore.client()
            return self.db