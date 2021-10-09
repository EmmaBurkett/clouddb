class edit_inventory: 

    def add_new_document(self, db):
        name = input("Item Name: ")
        quote = input("Quote: ")
        speaker = input("Speaker: ")
        result = db.collection("Quotes").document(name).get() #no document = all documents

        if result.exists:
            print("Item already exists!")
            return

        data = {"Quote": quote, "Speaker": speaker}
        db.collection("Quotes").document(name).set(data)
        print(f"Added {name} with quote {quote}\n~ by {speaker}")

    def adjust_document_name(self, db):
        old_Name = input("Document Name: ")
        results = db.collection("Quotes").document(old_Name).get()
        if not results.exists:
            print("Document does not exist!")
            return
        data = results.to_dict()
        quote = data['Quote']
        speaker = data['Speaker']
        name = input("New Name: ")
        db.collection("Quotes").document(name).set(data)
        data = {"Quote": quote, "Speaker": speaker}
        self.delete_document(db, old_Name)

    def adjust_selected_quote(self, db):
        name = input("Document Name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists:
            print("Item does not exist!")
            return
        data = result.to_dict()
        quote = input("New Quote: ")
        self.adjust_quote(db, name, data, quote)
        dataSpeaker = data["Speaker"]
        new_speaker = input(f"Is {dataSpeaker} the Speaker? (y/n) ")
        if new_speaker == 'n':
            speaker = input("Name: ")
            if data["Speaker"] == speaker:
                print("ERROR: Correct Speaker is already inputted")
                return
            self.adjust_speaker(db, name, speaker, data)
        if new_speaker == 'n':
            return

    def adjust_selected_speaker(self, db):
        name = input("Document Name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists:
            print("Item does not exist!")
            return
        data = result.to_dict()
        speaker = input("Speaker: ")
        self.adjust_speaker(db, name, speaker, data)

    def adjust_speaker(self, db, name, speaker, data):
        data["Speaker"] = speaker
        db.collection("Quotes").document(name).set(data)
    
    def adjust_quote(self, db, name, data, quote):
        data["Quote"] = quote
        db.collection("Quotes").document(name).set(data) #MUHAHAHAHAHAHA NO-ONE CAN STOP ME NOW!!!

    def delete_selected_document(self, db):
        name = input("Document Name: ")
        result = db.collection("Quotes").document(name).get()
        if not result.exists:
            print("Item does not exist!")
            return
        self.delete_document(db, name)
        return name

    def delete_document(self, db, name):
        db.collection("Quotes").document(name).delete()
