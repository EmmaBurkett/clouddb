class edit_inventory: 

    def add_new_document(self, db):
        #get info from user
        name = input("Item Name: ")
        quote = input("Quote: ")
        speaker = input("Speaker: ")
        #get document from firestore
        result = db.collection("Quotes").document(name).get() #no document = all documents
        #Error solving
        if result.exists:
            print("Item already exists!")
            return
        # initialize data in correct formatting
        data = {"Quote": quote, "Speaker": speaker}
        #set data in the database
        db.collection("Quotes").document(name).set(data)
        #print message to user
        print(f"Added {name} with quote {quote}\n~ by {speaker}")

    def adjust_document_name(self, db):
        #get document name from user and database
        old_Name = input("Document Name: ")
        results = db.collection("Quotes").document(old_Name).get()
        if not results.exists: #error checking!
            print("Document does not exist!")
            return
        #store data from document
        data = results.to_dict()
        quote = data['Quote']
        speaker = data['Speaker']
        #get new name from user
        name = input("New Name: ")
        #sets data from the old document to a new document with the specified name
        db.collection("Quotes").document(name).set(data)
        #This does something important?
        data = {"Quote": quote, "Speaker": speaker}
        #deletes old document
        self.delete_document(db, old_Name)

    def adjust_selected_quote(self, db):
        #get document name and fields
        name = input("Document Name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists: #error check
            print("Item does not exist!")
            return
        data = result.to_dict() #get data in document

        #get new quote
        quote = input("New Quote: ")

        #replaces old quote with a new one and sets it
        self.adjust_quote(db, name, data, quote)
        dataSpeaker = data["Speaker"] #the next like demanded this be declared.
        #is speaker the same speaker?
        new_speaker = input(f"Is {dataSpeaker} the Speaker? (y/n) ")
        if new_speaker == 'n': # if not then get a new speaker and set that.
            speaker = input("Name: ")
            if data["Speaker"] == speaker: #error checking
                print("ERROR: Correct Speaker is already inputted")
                return
            #replaces speaker and sets it in frirestore
            self.adjust_speaker(db, name, speaker, data)
        if new_speaker == 'n':
            return

    def adjust_selected_speaker(self, db):
        #get document
        name = input("Document Name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists: #error check
            print("Item does not exist!")
            return
        data = result.to_dict() #get data from document
        #replace speaker and set
        speaker = input("Speaker: ")
        self.adjust_speaker(db, name, speaker, data)

    def adjust_speaker(self, db, name, speaker, data):
        #overwrites old data and replaces it with new data
        data["Speaker"] = speaker
        db.collection("Quotes").document(name).set(data)
    
    def adjust_quote(self, db, name, data, quote):
        #overwrites old data and replaces it with new data
        data["Quote"] = quote
        db.collection("Quotes").document(name).set(data) #MUHAHAHAHAHAHA NO-ONE CAN STOP ME NOW!!! I got excited about learning how to use set lol

    def delete_selected_document(self, db):
        #get document
        name = input("Document Name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists: #errror checking
            print("Item does not exist!")
            return
        #delete document
        self.delete_document(db, name)
        return name

    def delete_document(self, db, name):
        #deletes document
        db.collection("Quotes").document(name).delete()
