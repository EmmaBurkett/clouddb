from firebase_admin import firestore
class interact():
    def add_likes(self, db, retrieve_data, name):
        quote = retrieve_data["Quote"]
        speaker = retrieve_data["Speaker"]
        data = {"Quote": quote, "Speaker": speaker, "Likes": 1}
        db.collection("Quotes").document(name).set(data)
    
    def update_likes(self, db):
        name = input("Document name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists:
            print("Item does not exist!")
            return
        retrieve_data = result.to_dict() 

        if 'Likes' not in retrieve_data:
            self.add_likes(db, retrieve_data, name)
            return
        else: 
            retrieve_data['Likes'] += 1
        
        db.collection("Quotes").document(name).set(retrieve_data)

    def comment(self, db, name_on_file):
        name = input("Document name: ")

        result = db.collection("Quotes").document(name).get()
        if not result.exists:
            print("Document does not exist!")
            return

        comment_title = input("Comment Title: ")
        comment = input("Comment: ")
        anonymous = input("Comment anonymously? (y/n)")

        if anonymous == 'y':
            user_name = 'Anonymous'
        else:
            user_name = name_on_file
        
        timestamp = firestore.SERVER_TIMESTAMP
        data = {"1) Comment Title": comment_title, "2) Comment": comment, "3) Submitted By": user_name, "4) Submitted At": timestamp}
        db.collection("Quotes").document(name).collection("Comments").add(data)

        
        

        