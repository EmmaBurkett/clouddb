from firebase_admin import firestore
class interact():
    
    def update_likes(self, db):
        #get document
        name = input("Document name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists: #error check
            print("Item does not exist!")
            return
        retrieve_data = result.to_dict() # get data in document

        if 'Likes' not in retrieve_data: #if the field Likes does not exist
            self.add_likes(db, retrieve_data, name) #creates a field called likes and puts a one in it
            return
        else: 
            retrieve_data['Likes'] += 1 # adds a like to existing likes
            db.collection("Quotes").document(name).set(retrieve_data) #sets the data
    
    def add_likes(self, db, retrieve_data, name):
        # Stores data
        quote = retrieve_data["Quote"]
        speaker = retrieve_data["Speaker"]
        data = {"Quote": quote, "Speaker": speaker, "Likes": 1}
        #sets data
        db.collection("Quotes").document(name).set(data)

    def comment(self, db, name_on_file):
        #get document and error check
        name = input("Document name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists:
            print("Document does not exist!")
            return

        # get comment from user
        comment_title = input("Comment Title: ")
        comment = input("Comment: ")
        anonymous = input("Comment anonymously? (y/n)")

        # Can comment anonymously or with user_name
        if anonymous == 'y':
            user_name = 'Anonymous'
        else:
            user_name = name_on_file
        
        # includes a time stamp
        timestamp = firestore.SERVER_TIMESTAMP
        #stores data
        data = {"1) Comment Title": comment_title, "2) Comment": comment, "3) Submitted By": user_name, "4) Submitted At": timestamp}
        #sets data
        db.collection("Quotes").document(name).collection("Comments").add(data)

        
        

        